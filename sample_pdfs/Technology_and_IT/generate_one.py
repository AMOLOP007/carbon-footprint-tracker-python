import os
import random
import uuid
import datetime
from fpdf import FPDF

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

COMPANY_POOL = [
    "NovaTech Systems", "CloudSphere Data", "CyberNet Solutions", "Apex Server Hosting",
    "Quantum IT Group", "Nexus Computing", "Vanguard Technologies", "Synapse Data Centers",
    "Zenith Network Ops", "Pinnacle Cloud Services"
]

def make_pdf(company):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month = random.choice(months)
    year = "2026"
    period = f"{month} {year}"
    
    server_kwh = random.randint(50000, 200000)
    commute_km = random.randint(10000, 50000)
    flights = random.randint(2, 25)
    total_emissions = random.uniform(500, 2000)

    # --- PAGE 1: TITLE PAGE ---
    pdf.add_page()
    pdf.set_fill_color(33, 47, 61)
    pdf.rect(0, 0, 210, 297, 'F')
    
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", "B", 28)
    pdf.ln(80)
    pdf.cell(0, 15, "SUSTAINABILITY & ESG", ln=1, align="C")
    pdf.cell(0, 15, "PERFORMANCE REPORT", ln=1, align="C")
    
    pdf.set_font("Arial", "", 16)
    pdf.set_text_color(171, 235, 198)
    pdf.ln(10)
    pdf.cell(0, 10, f"{company} Global Infrastructure", ln=1, align="C")
    
    pdf.set_text_color(200, 200, 200)
    pdf.ln(60)
    pdf.set_font("Arial", "I", 14)
    pdf.cell(0, 10, f"Reporting Period: {period}", ln=1, align="C")
    pdf.cell(0, 10, f"Issued Date: {datetime.date.today().strftime('%B %d, %Y')}", ln=1, align="C")
    pdf.cell(0, 10, "Document Confidence: STRICT & CONFIDENTIAL", ln=1, align="C")
    
    # --- PAGE 2: CEO MESSAGE & TOC ---
    pdf.add_page()
    pdf.set_fill_color(255, 255, 255)
    pdf.rect(0, 0, 210, 297, 'F')
    pdf.set_text_color(0, 0, 0)
    
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "Letter from the Chief Sustainability Officer", ln=1)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, (
        f"At {company}, we view sustainability not as a regulatory burden, but as a core pillar of our technological "
        "advancement. The digital economy requires immense energy, and we recognize our responsibility to decouple "
        "cloud infrastructure growth from carbon emissions. This document outlines our performance metrics across all "
        "data center zones, corporate offices, and employee travel habits. We are actively exploring immersive liquid "
        "cooling technologies and signing Power Purchase Agreements (PPAs) to guarantee 100% renewable energy for our "
        "tier-4 data centers by 2030."
    ))
    pdf.ln(10)
    
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "Table of Contents", ln=1)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "1. Executive Summary............................................................... Page 3", ln=1)
    pdf.cell(0, 8, "2. Scope 1 & 2: Data Center Footprint....................................... Page 4", ln=1)
    pdf.cell(0, 8, "3. Detailed Asset Inventory........................................................ Page 5", ln=1)
    pdf.cell(0, 8, "4. Compliance & Verification...................................................... Page 6", ln=1)

    # --- PAGE 3: EXECUTIVE SUMMARY & NLP METRICS ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(41, 128, 185)
    pdf.cell(0, 10, "1. Executive Summary", ln=1)
    pdf.set_text_color(0, 0, 0)
    
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, (
        f"This section encapsulates the macro-level view of our corporate emissions profile. Unlike traditional industries, "
        f"{company}'s primary output is digital logic, meaning our Scope 2 purchased electricity completely dominates our footprint. "
        "We are actively monitoring our Power Usage Effectiveness (PUE) across 15 regional zones. The following metrics are "
        "extracted by our internal monitoring APIs and smart meters across all global locations."
    ))
    pdf.ln(5)
    
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "High-Level Narrative", ln=1)
    pdf.set_font("Arial", "", 12)
    
    # NLP parser relies on these exact string formats:
    nar = (
        f"During this fiscal cycle, our data center base load reached peak utilization, resulting in a total energy draw "
        f"of {server_kwh} kWh tracked through our primary metering endpoints. Alongside structural operations, our "
        f"workforce dynamics contributed to Scope 3 metrics. Employee commuting collectively accounted for {commute_km} km "
        f"driven due to our temporary return-to-office policy iteration. Furthermore, crucial international business expansion "
        f"mandated {flights} flights count recorded globally."
    )
    pdf.multi_cell(0, 8, nar)

    # --- PAGE 4: DETAILED GRAPHS & SCOPE ANALYSIS ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(41, 128, 185)
    pdf.cell(0, 10, "2. Scope 1 & 2: Data Center Footprint", ln=1)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "Our server clusters operate on variable workloads. The chart below illustrates the simulated consumption distribution across our core environments.")
    pdf.ln(10)
    
    # Draw mock Bar Chart using fpdf rects
    pdf.set_font("Arial", "B", 10)
    pdf.cell(0, 5, "Relative Consumption Index", ln=1)
    labels = ["US-East", "EU-West", "AP-South", "US-West", "Edge Nodes"]
    values = [random.randint(40, 90) for _ in range(5)]
    
    start_x = 20
    start_y = pdf.get_y() + 5
    for i, val in enumerate(values):
        # Draw bar
        pdf.set_fill_color(46, 204, 113) # Green
        pdf.rect(start_x, start_y + (i*12), val, 8, 'F')
        # Draw label
        pdf.set_xy(start_x + val + 5, start_y + (i*12))
        pdf.cell(30, 8, f"{labels[i]} (Idx: {val})")
        
    pdf.set_xy(10, start_y + 70)
    pdf.multi_cell(0, 6, "As shown above, AP-South currently accounts for the least efficient PUE due to legacy cooling infrastructure. Upgrades slated for Q4 aim to rectify this thermal imbalance.")

    # --- PAGE 5: DETAILED ASSET INVENTORY (THE TABLE) ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(41, 128, 185)
    pdf.cell(0, 10, "3. Detailed Asset Inventory", ln=1)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "The table below provides granular telemetric data captured directly from PDU sensors and facility meters. This raw data is verified internally before third-party auditing.")
    pdf.ln(5)

    # 3 COLUMNS for Technology (matching parser)
    pdf.set_fill_color(220, 220, 220)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(70, 10, "Component / Asset Name", 1, 0, 'C', True)
    pdf.cell(60, 10, "Monthly Usage", 1, 0, 'C', True)
    pdf.cell(60, 10, "Sector Classification", 1, 1, 'C', True)

    pdf.set_font("Arial", "", 10)
    for i in range(1, 11):
        name = f"Compute Node {i}" if i % 2 == 0 else f"Chiller Bank {i}"
        val = f"{random.randint(5000, 40000)} kWh"
        sec = "IT Infrastructure" if i % 2 == 0 else "Facilities"
        pdf.cell(70, 8, name, 1)
        pdf.cell(60, 8, val, 1, 0, 'C')
        pdf.cell(60, 8, sec, 1, 1, 'C')

    # --- PAGE 6: VERIFICATION ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(41, 128, 185)
    pdf.cell(0, 10, "4. Compliance & Verification", ln=1)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "This report has been curated in strict alignment with the GHG Protocol Corporate Accounting and Reporting Standard. Data normalization algorithms have resolved standard deviations and anomalous meter readings.")
    pdf.ln(15)
    # NLP parser previously looked for total emissions here, removed per user request.
    pdf.ln(20)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "I", 12)
    pdf.cell(0, 10, "Authorized by:", ln=1)
    pdf.cell(0, 10, "Johnathan Doe", ln=1)
    pdf.cell(0, 10, f"VP of Global Operations, {company}", ln=1)

    path = f"{company}.pdf"
    pdf.output(path)
    print(f"Generated: {path}")

if __name__ == "__main__":
    for c in COMPANY_POOL[:10]:
        make_pdf(c)

