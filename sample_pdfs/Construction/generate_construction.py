import os
import random
import glob
from fpdf import FPDF
import uuid

for f in glob.glob("*.pdf"):
    os.remove(f)

COMPANIES = [
    "BuildTech Solutions", "Apex Builders", "Titan Constructors", "Skyline Developments", "Prime Infrastructure",
    "Vertex Construction", "Pioneer Structural", "Crestwood Builders", "Monolith Engineering", "IronClad Erectors"
]
random.shuffle(COMPANIES)

def make_pdf(index):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    company = COMPANIES[index-1]
    
    pdf.cell(190, 10, txt=f"{company} ESG Report", border=0, ln=1, align='C')
    
    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    
    period = f"May 2026"
    pdf.cell(190, 10, txt=f"Reporting Period: {period}", border=0, ln=1, align='L')
    
    office_kwh = random.randint(5000, 20000)
    trucks_km = random.randint(10000, 50000)
    cars_km = random.randint(2000, 10000)
    
    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(190, 10, txt="Narrative Summary", border=0, ln=1)
    pdf.set_font("Arial", "", 12)
    
    nar = (f"During this operational period, site infrastructure and temporary office facilities utilized {office_kwh} kWh of electrical power. "
           f"Logistics for material hauling spanned {trucks_km} km. "
           f"Additionally, personnel transport and crew vehicles covered {cars_km} km across all sites.")
    pdf.multi_cell(0, 8, txt=nar)
    pdf.ln(10)
    
    pdf.set_font("Arial", "B", 14)
    pdf.cell(190, 10, txt="Detailed Asset Inventory", border=0, ln=1)
    
    pdf.set_font("Arial", "B", 10)
    pdf.cell(45, 10, "Name", 1)
    pdf.cell(35, 10, "Type", 1)
    pdf.cell(30, 10, "Fuel (liters)", 1)
    pdf.cell(35, 10, "Distance(km)", 1)
    pdf.cell(30, 10, "Hours", 1, ln=1)
    
    pdf.set_font("Arial", "", 10)
    
    for i in range(1, 11):
        name = f"Excavator X{i}" if i % 2 == 0 else f"Crane C{i}"
        typ = "excavator" if i % 2 == 0 else "crane"
        fuel = str(random.randint(50, 400))
        dist = str(random.randint(5, 50))
        hrs = str(random.randint(20, 150))
        
        pdf.cell(45, 8, name, 1)
        pdf.cell(35, 8, typ, 1)
        pdf.cell(30, 8, fuel, 1)
        pdf.cell(35, 8, dist, 1)
        pdf.cell(30, 8, hrs, 1, ln=1)
        
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(190, 10, txt=f"Total Emissions: {random.uniform(50, 600):.2f} tCO2e", border=0, ln=1, align='R')
    
    path = f"{company}.pdf"
    pdf.output(path)

for i in range(1, 11):
    make_pdf(i)
