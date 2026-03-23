# api_guard.py
# Centralized API usage tracking and rate limiting
# Prevents accidental overuse of external API keys
# Each API has a daily call limit - once hit, requests gracefully fall back to local data

import os
import json
from datetime import datetime, date
from threading import Lock

# file-based counter to persist across server restarts
COUNTER_FILE = os.path.join(os.path.dirname(__file__), '.api_usage.json')
_lock = Lock()

# ---------- DAILY LIMITS (set conservatively below free tier caps) ----------
# These are YOUR safety limits, not the provider's limits
DAILY_LIMITS = {
    "openai":           30,    # OpenAI: keep well under spending limits
    "climatiq":         25,    # Climatiq free tier: 1000/month (~33/day, we cap at 25)
    "carbon_interface": 8,     # Carbon Interface free: 200/month (~6.6/day, we cap at 8)
    "google_maps":      15,    # Google Maps: $200 free credit, but cap anyway
    "sendgrid":         20,    # SendGrid free: 100/day
    "gemini":           30,    # Gemini API free tier limits
}


def _load_counters():
    """Load today's counters from disk."""
    try:
        with open(COUNTER_FILE, 'r') as f:
            data = json.load(f)
        # reset if it's a new day
        if data.get('date') != str(date.today()):
            return {'date': str(date.today()), 'counts': {}}
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {'date': str(date.today()), 'counts': {}}


def _save_counters(data):
    """Save counters to disk."""
    try:
        with open(COUNTER_FILE, 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Warning: could not save API counters: {e}")


def can_call(api_name):
    """
    Check if we're allowed to make another call to this API today.
    Returns True if under the daily limit, False if limit reached.
    """
    api_name = api_name.lower()
    limit = DAILY_LIMITS.get(api_name, 10)  # default 10 if unknown
    
    with _lock:
        data = _load_counters()
        current = data['counts'].get(api_name, 0)
        return current < limit


def record_call(api_name):
    """Record that we made one API call. Returns the new count."""
    api_name = api_name.lower()
    
    with _lock:
        data = _load_counters()
        current = data['counts'].get(api_name, 0)
        data['counts'][api_name] = current + 1
        _save_counters(data)
        return current + 1


def get_usage_summary():
    """Return a dict showing current usage vs limits for all APIs."""
    with _lock:
        data = _load_counters()
    
    summary = {}
    for api_name, limit in DAILY_LIMITS.items():
        used = data['counts'].get(api_name, 0)
        summary[api_name] = {
            'used': used,
            'limit': limit,
            'remaining': max(0, limit - used),
            'exhausted': used >= limit
        }
    return summary


def safe_api_call(api_name, call_fn, fallback_fn=None):
    """
    Safely execute an API call with automatic limit checking and fallback.
    
    Args:
        api_name: string identifier for the API (e.g. 'openai', 'climatiq')
        call_fn: callable that makes the actual API request. Should return the result.
        fallback_fn: callable that returns fallback data if API is unavailable or limit hit.
    
    Returns:
        Result from call_fn if successful, or from fallback_fn if limit hit or error.
    """
    if not can_call(api_name):
        print(f"API GUARD: Daily limit reached for {api_name} ({DAILY_LIMITS.get(api_name, '?')} calls). Using fallback.")
        if fallback_fn:
            return fallback_fn()
        return None
    
    try:
        result = call_fn()
        record_call(api_name)
        return result
    except Exception as e:
        print(f"API GUARD: {api_name} call failed ({e}). Using fallback.")
        if fallback_fn:
            return fallback_fn()
        return None
