# Aetherra - Corporate Sustainability Intelligence Platform

Welcome to Aetherra! This is a modern, AI-powered web application designed to help businesses track, analyze, and reduce their carbon footprint through automated PDF extraction and grid intensity analysis.

## 📋 Section 1 — Required Installations
Before you start, make sure you have the following installed:

**Python (3.9+)**
- Download and install from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- *During installation on Windows, make sure to check "Add python.exe to PATH".*

**MongoDB (Community Server)**
- Download and install from: [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)
- This is the local database where your companies and emission reports will be saved.

**VS Code (Visual Studio Code)**
- Download from: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- This is the code editor we recommend.

## 🚀 Section 2 — How to Download Project from GitHub
Install Git (if you haven't already):
- Download from: [https://git-scm.com/downloads](https://git-scm.com/downloads)

Open VS Code.
1. **Open the Terminal**: Go to the top menu: `Terminal -> New Terminal`.
2. **Download the Code**: Type the following command and press Enter:
   ```bash
   git clone https://github.com/AMOLOP007/carbon-footprint-tracker-python.git
   ```
3. **Navigate into the Project**:
   ```bash
   cd aetherra
   ```

## 📦 Section 3 — Install Dependencies
Install all the Python software libraries required by the project by running this command:

```bash
pip install -r requirements.txt
```
*(This might take a minute or two as it downloads Flask, PyMongo, AI sdks, etc.)*

## 🔐 Section 4 — Create Env File
You need to create a special configuration file for your secret passwords and API keys.

1. Create a new file in the main folder named: `.env.local`
2. Open `.env.local` and paste the following template:

```ini
# Database Connection
MONGODB_URI=mongodb://127.0.0.1:27017/aetherra

# External API Integrations
GEMINI_API_KEY=your_gemini_key_here
OPENAI_API_KEY=your_openai_key_here
CLIMATIQ_API_KEY=your_climatiq_key_here
CARBON_INTERFACE_API_KEY=your_carbon_interface_key_here

# Google OAuth (Required for "Sign in with Google")
# Get these from: https://console.cloud.google.com/
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```
*Note: The platform features offline fallbacks, but supplying actual API keys unlocks the AI-powered PDF extraction.*

## ▶️ Section 5 — Run Project
To start the application, run:

```bash
python app.py
```
Once it says "Aetherra running at http://127.0.0.1:5000", open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🛠 Section 6 — Troubleshooting

- **Error:** `pymongo.errors.ServerSelectionTimeoutError: localhost:27017: [WinError 10061]`
  - **Fix:** Your MongoDB is not running. Search for "MongoDB Compass" or "MongoDB Service" on your computer and start it.

- **Error:** `ModuleNotFoundError: No module named 'flask'`
  - **Fix:** You haven't installed the dependencies. Run `pip install -r requirements.txt`.

- **Google Login Error:** `redirect_uri_mismatch`
  - **Fix:** In your Google Cloud Console, make sure "Authorized redirect URIs" includes: `http://127.0.0.1:5000/auth/google/callback`.

Happy Coding! 🌍🌱
