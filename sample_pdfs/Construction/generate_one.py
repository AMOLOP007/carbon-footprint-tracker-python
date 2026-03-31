import os
import random
import uuid
import datetime
from fpdf import FPDF

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

COMPANY_POOL = [
    "BuildTech Solutions", "Apex Builders", "Titan Constructors", "Skyline Developments",
    "Prime Infrastructure", "Vertex Construction", "Pioneer Structural", "Crestwood Builders",
    "Monolith Engineering", "IronClad Erectors"
]

def make_pdf(company):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    period = f"{random.choice(months)} 2026"
    
    office_kwh = random.randint(5000, 20000)
    trucks_km = random.randint(10000, 50000)
    cars_km = random.randint(2000, 10000)
    total_emissions = random.uniform(50, 600)

    # --- PAGE 1: TITLE PAGE ---
    pdf.add_page()
    pdf.set_fill_color(44, 62, 80) # Dark Concrete
    pdf.rect(0, 0, 210, 297, 'F')
    
    pdf.set_text_color(241, 196, 15) # Construction Yellow
    pdf.set_font("Arial", "B", 26)
    pdf.ln(90)
    pdf.cell(0, 15, "CONSTRUCTION PORTFOLIO", ln=1, align="C")
    pdf.cell(0, 15, "ENVIRONMENTAL IMPACT REPORT", ln=1, align="C")
    
    pdf.set_font("Arial", "", 16)
    pdf.set_text_color(255, 255, 255)
    pdf.ln(10)
    pdf.cell(0, 10, f"Prepared by: {company} EPC Division", ln=1, align="C")
    
    pdf.set_text_color(200, 200, 200)
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
    pdf.cell(0, 10, "Letter from the Lead Project Engineer", ln=1)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, (
        f"At {company}, we build the skyline of tomorrow with the environment of today in mind. Heavy construction "
        "is inherently resource-intensive, but through modular building techniques, electric heavy plant investments, "
        "and strict idling controls, we are aggressively lowering our carbon footprint per square meter completed. "
        "This report aggregates the temporary power pull, logistical hauling, and on-site generator usage across all "
        "active commercial and residential sites."
    ))
    pdf.ln(15)
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "Table of Contents", ln=1)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "1. Executive Summary .............................................................. Page 3", ln=1)
    pdf.cell(0, 8, "2. Scope 1 On-Site Analytics ...................................................... Page 4", ln=1)
    pdf.cell(0, 8, "3. Detailed Asset Inventory ....................................................... Page 5", ln=1)
    pdf.cell(0, 8, "4. Verification & GHG Standards ................................................... Page 6", ln=1)

    # --- PAGE 3: EXECUTIVE SUMMARY & NLP METRICS ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(243, 156, 18)
    pdf.cell(0, 10, "1. Executive Summary", ln=1)
    pdf.set_text_color(0, 0, 0)
    
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "Below is the aggregated telemetry representing all active sites, including excavation, structural steel erection, and finishing stages.")
    pdf.ln(5)
    
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Narrative Summary", ln=1)
    pdf.set_font("Arial", "", 12)
    nar = (
        f"During this operational period, site infrastructure and temporary office facilities utilized {office_kwh} kWh "
        f"of electrical power. Logistics for material hauling and debris removal spanned {trucks_km} km. "
        f"Additionally, personnel transport and crew vehicles covered {cars_km} km across all sites."
    )
    pdf.multi_cell(0, 8, nar)

    # --- PAGE 4: SITE CONSUMPTION CHARTS ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(243, 156, 18)
    pdf.cell(0, 10, "2. Scope 1 On-Site Analytics", ln=1)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "Diesel generators and heavy plant equipment are tracked meticulously. Below is the fuel consumption breakdown by construction phase.")
    pdf.ln(10)
    
    # Draw mock Bar Chart
    pdf.set_font("Arial", "B", 10)
    pdf.cell(0, 5, "Fuel Burn vs Construction Phase", ln=1)
    phases = ["Demolition/Excavation", "Foundation/Piling", "Structural Steel", "MEP Installation", "Interior Finishing"]
    fuel_burn = [random.randint(100, 600) for _ in range(5)]
    
    start_x = 20
    start_y = pdf.get_y() + 5
    for i, val in enumerate(fuel_burn):
        pdf.set_fill_color(241, 196, 15) # Yellow
        pdf.rect(start_x, start_y + (i*12), val/6, 8, 'F')
        pdf.set_xy(start_x + (val/6) + 5, start_y + (i*12))
        pdf.cell(30, 8, f"{phases[i]} ({val} units)")
        
    pdf.set_xy(10, start_y + 70)
    pdf.multi_cell(0, 6, "As anticipated, the Demolition and Foundation phases represent the highest concentration of heavy plant exhaust. The adoption of hybrid excavators on 2 major sites has reduced this by 8% against historical baselines.")

    # --- PAGE 5: DETAILED ASSET TABLE ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(243, 156, 18)
    pdf.cell(0, 10, "3. Detailed Asset Inventory", ln=1)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "Fuel dispensing logs and equipment hour-meters tabulated for our heaviest contributors to Scope 1 emissions.")
    pdf.ln(5)

    pdf.set_fill_color(230, 230, 230)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(45, 10, "Name", 1, 0, 'C', True)
    pdf.cell(35, 10, "Type", 1, 0, 'C', True)
    pdf.cell(30, 10, "Fuel (liters)", 1, 0, 'C', True)
    pdf.cell(35, 10, "Distance(km)", 1, 0, 'C', True)
    pdf.cell(30, 10, "Hours", 1, 1, 'C', True)

    pdf.set_font("Arial", "", 10)
    for i in range(1, 11):
        name = f"Excavator X{i}" if i % 2 == 0 else f"Crane C{i}"
        typ = "excavator" if i % 2 == 0 else "crane"
        fuel = str(random.randint(50, 400))
        dist = str(random.randint(5, 50))
        hrs = str(random.randint(20, 150))

        pdf.cell(45, 8, name, 1, 0, 'C')
        pdf.cell(35, 8, typ, 1, 0, 'C')
        pdf.cell(30, 8, fuel, 1, 0, 'C')
        pdf.cell(35, 8, dist, 1, 0, 'C')
        pdf.cell(30, 8, hrs, 1, 1, 'C')

    # --- PAGE 6: VERIFICATION ---
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(243, 156, 18)
    pdf.cell(0, 10, "4. Verification & GHG Standards", ln=1)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "Calculations leverage BREEAM and LEED conversion metrics. Fuel receipts were audited cross-referenced against mechanical hour meters by a 3rd party surveyor.")
    pdf.ln(15)
    
    # Total Emissions removed
    pdf.ln(20)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "I", 12)
    pdf.cell(0, 10, "Certified by:", ln=1)
    pdf.set_font("Arial", "U", 12)
    pdf.cell(0, 10, f"Mark Stevenson, Lead Auditor - {company}", ln=1)

    path = f"{company}.pdf"
    pdf.output(path)
    print(f"Generated: {path}")

if __name__ == "__main__":
    for c in COMPANY_POOL[:10]:
        make_pdf(c)
