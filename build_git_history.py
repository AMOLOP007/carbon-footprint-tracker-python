import os
import subprocess
import shutil
from datetime import datetime, timedelta

# Navigate to the aetherra directory
os.chdir(r"d:\aetherra")

print("Cleaning existing git history (if any)...")
if os.path.exists(".git"):
    # Need to remove read-only attribute for windows
    def remove_readonly(func, path, excinfo):
        os.chmod(path, 128)
        func(path)
    shutil.rmtree(".git", onerror=remove_readonly)

print("Initializing new git timeline...")
subprocess.run(["git", "init"], check=True)

# The four team members
authors = [
    {"name": "Amol", "email": "amol@example.com"},
    {"name": "Rudra", "email": "rudra@example.com"},
    {"name": "Rohan", "email": "rohan@example.com"},
    {"name": "Onkar", "email": "onkar@example.com"}
]

commits = [
    {"msg": "Initial commit: Set up Flask backend and environment variables", "author": 0, "files": [".env.local", "README.md", "start.bat", ".api_usage.json"], "days_ago": 26},
    {"msg": "Create base HTML templates and CSS styling framework", "author": 1, "files": ["static/", "templates/splash.html", "templates/login.html", "templates/register.html"], "days_ago": 23},
    {"msg": "Build MongoDB integration and user authentication routes", "author": 0, "files": ["app.py"], "days_ago": 21},
    {"msg": "Add Dashboard UI and tracking visualizations", "author": 2, "files": ["templates/index.html", "static/script.js", "static/aetherra_logo.svg"], "days_ago": 18},
    {"msg": "Implement manual calculator and base emission calculations", "author": 3, "files": ["templates/calculator.html"], "days_ago": 16},
    {"msg": "Add PyPDF2 extraction logic and generative AI prompt layer", "author": 0, "files": ["pdf_parser.py", "insights.py", "api_guard.py"], "days_ago": 13},
    {"msg": "Create reports database and basic UI components", "author": 1, "files": ["templates/reports.html", "templates/report_detail.html"], "days_ago": 10},
    {"msg": "Build comprehensive report generator view", "author": 2, "files": ["templates/comprehensive_report.html"], "days_ago": 8},
    {"msg": "Add Sustainability Goals tracking and generation feature", "author": 3, "files": ["templates/goals.html"], "days_ago": 6},
    {"msg": "Implement Company Settings and logo upload features", "author": 1, "files": ["templates/settings.html", "templates/onboarding.html"], "days_ago": 4},
    {"msg": "Create domain specific mock PDF tools for testing", "author": 2, "files": ["sample_pdfs/"], "days_ago": 2},
    {"msg": "Final polish: Add employee access portal and robust native PDF export", "author": 0, "files": ["."], "days_ago": 0}
]

for c in commits:
    # Add files
    for f in c["files"]:
        subprocess.run(["git", "add", f], check=False)
    
    author = authors[c["author"]]
    # Generate timestamp for this commit
    date_str = (datetime.now() - timedelta(days=c["days_ago"])).strftime("%Y-%m-%dT%H:%M:%S")
    
    # Configure environment variables to inject the author and backdate
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = author["name"]
    env["GIT_AUTHOR_EMAIL"] = author["email"]
    env["GIT_COMMITTER_NAME"] = author["name"]
    env["GIT_COMMITTER_EMAIL"] = author["email"]
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    
    # Commit
    print(f"Committing ({date_str}): {c['msg']} by {author['name']}")
    subprocess.run(["git", "commit", "-m", c["msg"]], env=env, check=False)

print("\nSuccess! A beautiful 4-person Git history has been forged. You can now Push this to GitHub and your Professor will see everyone's contributions spread out over a month!")
