import os
import random
import uuid
import datetime
from fpdf import FPDF

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

COMPANY_POOL = [
    "Swift Freight", "Global Logistics", "Express Movers", "Cargo Kings", "Transit Pros",
    "OmniRoute Logistics", "Falcon Delivery Systems", "Quantum Supply Chain", "Nautical Shipping",
    "Metro Transit"
]

def make_pdf(company):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    period = f"{random.choice(months)} 2026"
    
    warehouse_kwh = random.randint(10000, 50000)
    freight = random.randint(5000, 20000)
    total_emissions = random.uniform(100, 800)

    # --- PAGE 1: TITLE PAGE ---
    pdf.add_page()
    pdf.set_fill_color(243, 156, 18) # Logistics Orange
    pdf.rect(0, 0, 210, 297, 'F')
    
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", "B", 26)
    pdf.ln(90)
    pdf.cell(0, 15, "GLOBAL FLEET & SUPPLY CHAIN", ln=1, align="C")
    pdf.cell(0, 15, "ENVIRONMENTAL REPORT", ln=1, align="C")
    
    pdf.set_font("Arial", "", 16)
    pdf.set_text_color(253, 235, 208)
    pdf.ln(10)
    pdf.cell(0, 10, f"Prepared by: {company} Logistics Division", ln=1, align="C")
    
    pdf.set_text_color(255, 255, 255)
    pdf.ln(50)
    pdf.set_font("Arial", "I", 14)
    pdf.cell(0, 10, f"Reporting Period: {period}", ln=1, align="C")
    pdf.cell(0, 10, f"Issued Date: {datetime.date.today().strftime('%B %d, %Y')}", ln=1, align="C")
    
    # --- PAGE 2: DIRECTOR'S OVERVIEW ---
    pdf.add_page()
    pdf.set_fill_color(255, 255, 255)
    pdf.rect(0, 0, 210, 297, 'F')
    pdf.set_text_color(0, 0, 0)
    
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "Global Transport Overview", ln=1)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, (
        f"{company} remains dedicated to reducing the carbon footprint of global trade. The logistics sector "
        "is a massive contributor to global CO2. Through route optimization algorithms, empty-mile reduction "
        "strategies, and our phased transition to EV delivery vans, we are committed to net-zero logistics. "
        "This report details the fuel consumption of heavy trucks, warehouse power usage, and the total freight "
        "mass transported."
    ))
    pdf.ln(15)
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "Table of Contents", ln=1)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "1. Executive Summary .............................................................. Page 3", ln=1)
    pdf.cell(0, 8, "2. Scope 1 Fleet Analytics ........................................................ Page 4", ln=1)
    pdf.cell(0, 8, "3. Detailed Asset Inventory ....................................................... Page 5", ln=1)
    pdf.cell(0, 8, "4. Independent Audit & Assurance .................................................. Page 6", ln=1)

    # --- PAGE 3: EXECUTIVE SUMMARY & NLP METRICS ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(211, 84, 0)
    pdf.cell(0, 10, "1. Executive Summary", ln=1)
    pdf.set_text_color(0, 0, 0)
    
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "Below is the high-level aggregation of operational outputs spanning marine transit, last-mile delivery, and centralized sorting facilities.")
    pdf.ln(5)
    
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Narrative Summary", ln=1)
    pdf.set_font("Arial", "", 12)
    nar = (
        f"Operations across all central warehouses accounted for an electrical consumption of {warehouse_kwh} kWh "
        f"during this reporting cycle. Over the course of the month, our distribution network successfully delivered "
        f"{freight} kg of total freight weight across domestic and international borders. Fuel consumption remains "
        "our biggest priority area."
    )
    pdf.multi_cell(0, 8, nar)

    # --- PAGE 4: ROUTE DENSITY CHART ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(211, 84, 0)
    pdf.cell(0, 10, "2. Scope 1 Fleet Analytics", ln=1)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "Regional lane density impacts our Scope 1 diesel emissions heavily. By observing bottleneck lanes, we can schedule multi-modal rails for long hauls.")
    pdf.ln(10)
    
    # Draw mock Bar Chart
    pdf.set_font("Arial", "B", 10)
    pdf.cell(0, 5, "Lane Congestion Metrics (Idling Hours)", ln=1)
    lanes = ["North-South Corridor", "Eastern Seaboard", "Midwest Hub", "Euro-Link", "Pacific Rim"]
    idle_hours = [random.randint(100, 500) for _ in range(5)]
    
    start_x = 20
    start_y = pdf.get_y() + 5
    for i, val in enumerate(idle_hours):
        pdf.set_fill_color(231, 76, 60) # Red
        pdf.rect(start_x, start_y + (i*12), val/5, 8, 'F')
        pdf.set_xy(start_x + (val/5) + 5, start_y + (i*12))
        pdf.cell(30, 8, f"{lanes[i]} ({val} hrs)")
        
    pdf.set_xy(10, start_y + 70)
    pdf.multi_cell(0, 6, "Excessive idling on the North-South corridor is being mitigated with our new dynamic rerouting AI. Expected reduction next cycle: 15%.")

    # --- PAGE 5: DETAILED ASSET TABLE ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(211, 84, 0)
    pdf.cell(0, 10, "3. Detailed Asset Inventory", ln=1)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "Telemetry captured directly from ELD (Electronic Logging Devices) across active heavy and light goods vehicles.")
    pdf.ln(5)

    pdf.set_fill_color(240, 240, 240)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(45, 10, "Name", 1, 0, 'C', True)
    pdf.cell(35, 10, "Type", 1, 0, 'C', True)
    pdf.cell(30, 10, "Fuel (liters)", 1, 0, 'C', True)
    pdf.cell(35, 10, "Distance(km)", 1, 0, 'C', True)
    pdf.cell(30, 10, "Hours", 1, 1, 'C', True)

    pdf.set_font("Arial", "", 10)
    for i in range(1, 11):
        name = f"Truck TL-{i}00" if i % 2 == 0 else f"Van VM-{i}2"
        typ = "truck" if i % 2 == 0 else "delivery_van"
        fuel = str(random.randint(100, 800))
        dist = str(random.randint(1000, 5000))
        hrs = str(random.randint(50, 200))

        pdf.cell(45, 8, name, 1, 0, 'C')
        pdf.cell(35, 8, typ, 1, 0, 'C')
        pdf.cell(30, 8, fuel, 1, 0, 'C')
        pdf.cell(35, 8, dist, 1, 0, 'C')
        pdf.cell(30, 8, hrs, 1, 1, 'C')

    # --- PAGE 6: VERIFICATION ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(211, 84, 0)
    pdf.cell(0, 10, "4. Verification & Audit", ln=1)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "Audited in accordance with ISO 14064-1 by external environmental logistics consultants. The fleet telemetry system accuracy is verified to within 98.5%.")
    pdf.ln(15)
    
    # Total Emissions removed
    pdf.ln(20)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "I", 12)
    pdf.cell(0, 10, "Fleet Command Signature:", ln=1)
    pdf.set_font("Arial", "U", 12)
    pdf.cell(0, 10, f"/s/ Richard Miles, {company}", ln=1)

    path = f"{company}.pdf"
    pdf.output(path)
    print(f"Generated: {path}")

if __name__ == "__main__":
    for c in COMPANY_POOL[:10]:
        make_pdf(c)
