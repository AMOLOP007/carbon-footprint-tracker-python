import os
import random
import uuid
import datetime
from fpdf import FPDF

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

COMPANY_POOL = [
    "SteelWorks Inc", "Apex Manufacturing", "Pioneer Factories", "Prime Industrial", "Core Makers",
    "Nexus Fabrication", "Forge Dynamics", "Quantum Assembly", "Vanguard CNC", "Synapse Production",
    "TitanForge Industries", "IronPeak Manufacturing"
]

def make_pdf(company):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    period = f"{random.choice(months)} 2026"
    
    factory_kwh = random.randint(50000, 200000)
    fleet_km = random.randint(2000, 10000)
    shipment_kg = random.randint(10000, 50000)
    total_emissions = random.uniform(400, 1200)

    # --- PAGE 1: TITLE PAGE ---
    pdf.add_page()
    pdf.set_fill_color(39, 55, 70) # Dark Industrial Blue
    pdf.rect(0, 0, 210, 297, 'F')
    
    pdf.set_text_color(229, 152, 102) # Bronze/Copper
    pdf.set_font("Arial", "B", 26)
    pdf.ln(90)
    pdf.cell(0, 15, "GLOBAL MANUFACTURING", ln=1, align="C")
    pdf.cell(0, 15, "ENVIRONMENTAL DISCLOSURE", ln=1, align="C")
    
    pdf.set_font("Arial", "", 16)
    pdf.set_text_color(255, 255, 255)
    pdf.ln(10)
    pdf.cell(0, 10, f"Facility Operations: {company}", ln=1, align="C")
    
    pdf.set_text_color(170, 170, 170)
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
    pdf.cell(0, 10, "Message from the VP of Production", ln=1)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, (
        f"At {company}, we are forging a new path in heavy industry. Historically, manufacturing has "
        "been synonymous with high carbon intensity. We are aggressively challenging this paradigm. "
        "Our latest facility upgrades include transitioning to electric heavy-duty forklifts, implementing "
        "closed-loop cooling systems, and integrating AI to minimize CNC machine idle times. This operational "
        "report breaks down the power consumption of our factory floors and the outbound product logistics."
    ))
    pdf.ln(15)
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "Table of Contents", ln=1)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "1. Executive Summary .............................................................. Page 3", ln=1)
    pdf.cell(0, 8, "2. Facility Energy Profile ........................................................ Page 4", ln=1)
    pdf.cell(0, 8, "3. Equipment Telemetry Inventory .................................................. Page 5", ln=1)
    pdf.cell(0, 8, "4. Compliance & Verification ...................................................... Page 6", ln=1)

    # --- PAGE 3: EXECUTIVE SUMMARY & NLP METRICS ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(211, 84, 0)
    pdf.cell(0, 10, "1. Executive Summary", ln=1)
    pdf.set_text_color(0, 0, 0)
    
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "Below is the aggregated operational data capturing grid energy demands alongside domestic and international shipment tonnages.")
    pdf.ln(5)
    
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Narrative Summary", ln=1)
    pdf.set_font("Arial", "", 12)
    nar = (
        f"Primary grid energy draw for our factory installations reached {factory_kwh} kWh this month. "
        f"Our internal logistics fleet traversed {fleet_km} km in support of production. "
        f"Furthermore, total outbound shipments of finished goods amassed {shipment_kg} kg."
    )
    pdf.multi_cell(0, 8, nar)

    # --- PAGE 4: SITE CONSUMPTION CHARTS ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(211, 84, 0)
    pdf.cell(0, 10, "2. Facility Energy Profile", ln=1)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "Energy intensive processes like smelting, forging, and continuous CNC milling represent over 80% of our Scope 2 footprint. Baseline vs target efficiencies are listed below.")
    pdf.ln(10)
    
    # Draw mock Bar Chart
    pdf.set_font("Arial", "B", 10)
    pdf.cell(0, 5, "Energy Intensity Indicator (kWh per Tonne produced)", ln=1)
    processes = ["Die Casting", "CNC Machining", "Heat Treatment", "Assembly lines", "Facility HVAC"]
    baselines = [random.randint(200, 800) for _ in range(5)]
    
    start_x = 20
    start_y = pdf.get_y() + 5
    for i, val in enumerate(baselines):
        pdf.set_fill_color(229, 152, 102) # Copper/Bronze
        pdf.rect(start_x, start_y + (i*12), val/8, 8, 'F')
        pdf.set_xy(start_x + (val/8) + 5, start_y + (i*12))
        pdf.cell(30, 8, f"{processes[i]} ({val} idx)")
        
    pdf.set_xy(10, start_y + 70)
    pdf.multi_cell(0, 6, "Heat treatment remains the single largest thermal draw. A feasibility study for recovering waste heat and redirecting it to Facility HVAC is currently in Phase 2.")

    # --- PAGE 5: DETAILED ASSET TABLE ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(211, 84, 0)
    pdf.cell(0, 10, "3. Equipment Telemetry Inventory", ln=1)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "IoT meters connected securely to all active PLCs on the manufacturing floor provide real-time visibility into machine-level electricity draws.")
    pdf.ln(5)

    pdf.set_fill_color(230, 230, 230)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(45, 10, "Name", 1, 0, 'C', True)
    pdf.cell(35, 10, "Type", 1, 0, 'C', True)
    pdf.cell(30, 10, "Energy (kWh)", 1, 0, 'C', True)
    pdf.cell(35, 10, "Output (units)", 1, 0, 'C', True)
    pdf.cell(30, 10, "Hours", 1, 1, 'C', True)

    pdf.set_font("Arial", "", 10)
    for i in range(1, 11):
        name = f"CNC Machine {i}" if i % 2 == 0 else f"Assembly Line {i}"
        typ = "machinery" if i % 2 == 0 else "line"
        kwh = str(random.randint(500, 3000))
        out = str(random.randint(1000, 5000))
        hrs = str(random.randint(100, 500))

        pdf.cell(45, 8, name, 1, 0, 'C')
        pdf.cell(35, 8, typ, 1, 0, 'C')
        pdf.cell(30, 8, kwh, 1, 0, 'C')
        pdf.cell(35, 8, out, 1, 0, 'C')
        pdf.cell(30, 8, hrs, 1, 1, 'C')

    # --- PAGE 6: VERIFICATION ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(211, 84, 0)
    pdf.cell(0, 10, "4. Compliance & Verification", ln=1)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "Calculations leverage regional grid emission factors (EPA eGRID metrics). Metering is verified internally using utility sub-meters calibrated annually against ISO standards.")
    pdf.ln(15)
    
    # Total Emissions removed
    pdf.ln(20)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "I", 12)
    pdf.cell(0, 10, "Report Authenticated by:", ln=1)
    pdf.set_font("Arial", "U", 12)
    pdf.cell(0, 10, f"/s/ Dr. Elena Rostova, Director of Environmental Ops", ln=1)

    path = f"{company}.pdf"
    pdf.output(path)
    print(f"Generated: {path}")

if __name__ == "__main__":
    for c in COMPANY_POOL[:10]:
        make_pdf(c)
