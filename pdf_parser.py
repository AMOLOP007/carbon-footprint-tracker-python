# pdf_parser.py
# A real-world heuristic parser for Aetherra B2B sustainability reports.
# Implements 3-layer extraction (Structural, Table, Narrative) without artificial markers.

import re

DOMAIN_KEYWORDS = {
    "construction": ["construction", "excavator", "crane", "concrete", "site", "haul", "civil", "excavation", "equipment"],
    "manufacturing": ["manufacturing", "machine", "factory", "cycles", "production", "assembly", "industrial", "machinery", "output"],
    "technology": ["technology", "server", "uptime", "node", "cluster", "data center", "cloud", "it infrastructure", "load"],
    "logistics": ["logistics", "truck", "fleet", "freight", "shipment", "warehouse", "van", "transport", "cargo"]
}


def detect_domain(text):
    """Detect the industry domain based on keywords in text."""
    text_lower = text.lower()
    scores = {domain: 0 for domain in DOMAIN_KEYWORDS}
    
    for domain, keywords in DOMAIN_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                scores[domain] += 1
                
    # Return domain with highest score, or None if no keywords found
    if not scores: return None
    detected = max(scores, key=scores.get)
    return detected if scores[detected] > 0 else None

def parse_pdf_offline(text, user_domain):
    """
    Offline fallback parser with 70-80% accuracy requirement.
    1. Detect Domain
    2. Layer 3: Narrative NLP (Regex)
    3. Layer 2: Table Parsing
    """
    detected_domain = detect_domain(text)
    
    # Normalize domain names (handle UI variations)
    norm_detected = detected_domain.replace("_and_IT", "").replace("_and_Transport", "").lower() if detected_domain else None
    norm_user = user_domain.replace("_and_IT", "").replace("_and_Transport", "").lower() if user_domain else ""

    # Domain Mismatch logic
    if norm_detected and norm_user and norm_detected != norm_user:
        return {
            "success": False,
            "error": "Domain mismatch",
            "detected_domain": detected_domain,
            "message": f"This report belongs to the {detected_domain.replace('_', ' ').title()} industry."
        }

    result = {
        "success": True,
        "domain": detected_domain or user_domain,
        "reporting_period": "Unknown",
        "warehouse_kwh": 0.0,
        "total_freight_weight": 0.0,
        "trucks_km": 0.0,
        "cars_km": 0.0,
        "office_kwh": 0.0,
        "factory_kwh": 0.0,
        "fleet_km": 0.0,
        "shipment_kg": 0.0,
        "server_kwh": 0.0,
        "commute_km": 0.0,
        "flights": 0,
        "assets": [],
        "total_emissions": 0.0
    }

    # --- LAYER 1: STRUCTURAL (Reporting Period) ---
    period_match = re.search(r"(?:Period|Cycle|Date|Month):\s*([A-Za-z]+\s+\d{4})", text, re.I)
    if period_match:
        result["reporting_period"] = period_match.group(1).strip()

    # --- LAYER 3: NARRATIVE NLP (Regex) ---
    # Supports both "42716 kWh" and "Energy: 42716 kWh" or "Flights count: 12"
    # Logic: Look for keyword, then optional separator (: or space), then number OR number followed by keyword.
    
    # Energy (kWh)
    kwh_match = (re.search(r"(\d+(?:,\d+)?(?:\.\d+)?)\s*(?:kWh|kw|units)", text, re.I) or 
                 re.search(r"(?:Energy|Electricity|Load|Consumption)[^0-9]*(\d+(?:,\d+)?(?:\.\d+)?)\s*(?:kWh|kw|units)?", text, re.I))
    if kwh_match:
        result["server_kwh"] = float(kwh_match.group(1).replace(',', ''))

    # Distance (km)
    km_match = (re.search(r"(\d+(?:,\d+)?(?:\.\d+)?)\s*(?:km|kilometers|distance)", text, re.I) or 
                re.search(r"(?:Commute|Distance|Travel)[^0-9]*(\d+(?:,\d+)?(?:\.\d+)?)\s*(?:km|kilometers)?", text, re.I))
    if km_match:
        result["commute_km"] = float(km_match.group(1).replace(',', ''))

    # Flights
    flights_match = (re.search(r"(\d+)\s*(?:flights|air trips|flights count)", text, re.I) or 
                     re.search(r"(?:Flights|Air Trips)[^0-9]*(\d+)", text, re.I))
    if flights_match:
        result["flights"] = int(flights_match.group(1))

    # Logistics
    wh_match = re.search(r"(?:warehouse.*|warehouse_kwh.*|energy.*)\s*(\d+(?:,\d+)?(?:\.\d+)?)\s*(?:kWh)", text, re.I)
    if wh_match: result["warehouse_kwh"] = float(wh_match.group(1).replace(',', ''))
    
    fr_match = re.search(r"(?:freight_weight.*|freight.*|weight.*)\s*(\d+(?:,\d+)?(?:\.\d+)?)\s*(?:kg)", text, re.I)
    if fr_match: result["total_freight_weight"] = float(fr_match.group(1).replace(',', ''))
    
    # Construction
    of_match = re.search(r"(?:office_kwh.*|office.*|site.*power)\s*(\d+(?:,\d+)?(?:\.\d+)?)\s*(?:kWh)", text, re.I)
    if of_match: result["office_kwh"] = float(of_match.group(1).replace(',', ''))
    
    trk_match = re.search(r"(?:trucks_km.*|material hauling.*|trucks.*)\s*(\d+(?:,\d+)?(?:\.\d+)?)\s*(?:km)", text, re.I)
    if trk_match: result["trucks_km"] = float(trk_match.group(1).replace(',', ''))

    car_match = re.search(r"(?:cars_km.*|staff vehicles.*|cars.*)\s*(\d+(?:,\d+)?(?:\.\d+)?)\s*(?:km)", text, re.I)
    if car_match: result["cars_km"] = float(car_match.group(1).replace(',', ''))

    # Manufacturing
    fac_match = re.search(r"(?:factory_kwh.*|factory.*|grid.*)\s*(\d+(?:,\d+)?(?:\.\d+)?)\s*(?:kWh)", text, re.I)
    if fac_match: result["factory_kwh"] = float(fac_match.group(1).replace(',', ''))

    fl_match = re.search(r"(?:fleet_km.*|internal fleet.*)\s*(\d+(?:,\d+)?(?:\.\d+)?)\s*(?:km)", text, re.I)
    if fl_match: result["fleet_km"] = float(fl_match.group(1).replace(',', ''))

    shp_match = re.search(r"(?:shipment_kg.*|shipments.*|outbound.*)\s*(\d+(?:,\d+)?(?:\.\d+)?)\s*(?:kg)", text, re.I)
    if shp_match: result["shipment_kg"] = float(shp_match.group(1).replace(',', ''))


    # --- LAYER 2: TABLE PARSING (Refined 3-Column) ---
    # Targets: [Component / Asset Name] [Monthly Usage] [Sector Classification]
    rows = []
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    start_index = -1
    for i, line in enumerate(lines):
        if "Component / Asset Name" in line or "Monthly Usage" in line:
            start_index = i + 1
            break
            
    start_index = -1
    for i, line in enumerate(lines):
        if "Component / Asset Name" in line or "Monthly Usage" in line:
            start_index = i + 1
            break
            
    if start_index != -1:
        # Regex to split: [Name] [Value + Unit] [Sector]
        # Example: "Server Room A 3556 kWh Server Infrastructure"
        row_regex = r"(.+?)[\s\xa0]+(\d+(?:,\d+)?(?:\.\d+)?)(?:[\s\xa0]*(?:kWh|L|km|kg|units|litres))?[\s\xa0]+(.+)"
 
        for line in lines[start_index:start_index + 12]:
            # Stop if we hit a new section
            if re.match(r"^\d+\.", line) or "Verification" in line:
                break
                
            match = re.search(row_regex, line, re.I)
            if match:
                name = match.group(1).strip()
                usage_val = float(match.group(2).replace(',', ''))
                sector = match.group(3).strip()
                
                # Simple offline emission estimation
                # Factors: kWh=0.82, Petrol/Diesel=2.68, KM=0.21
                factor = 0.82 if "kWh" in line else 2.68 if "L" in line else 0.21
                emissions = round((usage_val * factor) / 1000, 4)
                
                asset_obj = {
                    "name": name,
                    "type": sector,
                    "emissions_tCO2e": emissions
                }
                
                # Add domain-specific keys for UI pre-fill
                if "kWh" in line: asset_obj["kwh"] = usage_val
                elif "L" in line: asset_obj["fuel_litres"] = usage_val
                elif "km" in line: asset_obj["distance_km"] = usage_val
                
                rows.append(asset_obj)

    result["assets"] = rows[:10]

    
    # Calculate total from assets
    asset_total = sum(a["emissions_tCO2e"] for a in result["assets"])
    
    # Check for global total in narrative
    total_match = re.search(r"(?:Total Emissions|Carbon Footprint|Total|Footprint):?\s*(\d+(?:,\d+)?(?:\.\d+)?)\s*(?:tCO2e|tons)", text, re.I)
    if total_match:
        result["total_emissions"] = float(total_match.group(1).replace(',', ''))
    else:
        result["total_emissions"] = round(asset_total, 2)

    return result

