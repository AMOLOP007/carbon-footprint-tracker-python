import os
import random
import glob
from fpdf import FPDF

for f in glob.glob("*.pdf"):
    os.remove(f)

COMPANIES = [
    "SteelWorks Inc", "Apex Manufacturing", "Pioneer Factories", "Prime Industrial", "Core Makers",
    "Nexus Fabrication", "Forge Dynamics", "Quantum Assembly", "Vanguard CNC", "Synapse Production"
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
    pdf.cell(190, 10, txt="Reporting Period: August 2026", border=0, ln=1, align='L')
    
    factory_kwh = random.randint(50000, 200000)
    fleet_km = random.randint(2000, 10000)
    shipment_kg = random.randint(10000, 50000)
    
    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(190, 10, txt="Narrative Summary", border=0, ln=1)
    pdf.set_font("Arial", "", 12)
    
    nar = (f"Primary grid energy draw for our factory installations reached {factory_kwh} kWh this month. "
           f"Our internal logistics fleet traversed {fleet_km} km in support of production. "
           f"Furthermore, total outbound shipments of finished goods amassed {shipment_kg} kg.")
    pdf.multi_cell(0, 8, txt=nar)
    pdf.ln(10)
    
    pdf.set_font("Arial", "B", 14)
    pdf.cell(190, 10, txt="Detailed Asset Inventory", border=0, ln=1)
    
    pdf.set_font("Arial", "B", 10)
    pdf.cell(45, 10, "Name", 1)
    pdf.cell(35, 10, "Type", 1)
    pdf.cell(30, 10, "Energy (kWh)", 1)
    pdf.cell(35, 10, "Output (units)", 1)
    pdf.cell(30, 10, "Hours", 1, ln=1)
    
    pdf.set_font("Arial", "", 10)
    
    for i in range(1, 11):
        name = f"CNC Machine {i}" if i % 2 == 0 else f"Assembly Line {i}"
        typ = "machinery" if i % 2 == 0 else "line"
        kwh = str(random.randint(500, 3000))
        out = str(random.randint(1000, 5000))
        hrs = str(random.randint(100, 500))
        
        pdf.cell(45, 8, name, 1)
        pdf.cell(35, 8, typ, 1)
        pdf.cell(30, 8, kwh, 1)
        pdf.cell(35, 8, out, 1)
        pdf.cell(30, 8, hrs, 1, ln=1)
        
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(190, 10, txt=f"Total Emissions: {random.uniform(400, 1200):.2f} tCO2e", border=0, ln=1, align='R')
    
    path = f"{company}.pdf"
    pdf.output(path)

for i in range(1, 11):
    make_pdf(i)
