import os
import random
import glob
from fpdf import FPDF

for f in glob.glob("*.pdf"):
    os.remove(f)

COMPANIES = [
    "Swift Freight", "Global Logistics", "Express Movers", "Cargo Kings", "Transit Pros",
    "OmniRoute Logistics", "Falcon Delivery Systems", "Quantum Supply Chain", "Nautical Shipping", "Metro Transit"
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
    pdf.cell(190, 10, txt="Reporting Period: June 2026", border=0, ln=1, align='L')
    
    warehouse_kwh = random.randint(10000, 50000)
    freight = random.randint(5000, 20000)
    
    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(190, 10, txt="Narrative Summary", border=0, ln=1)
    pdf.set_font("Arial", "", 12)
    
    nar = (f"Operations across all central warehouses accounted for an electrical consumption of {warehouse_kwh} kWh. "
           f"Over the course of the month, our distribution network successfully delivered {freight} kg of total freight weight.")
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
        name = f"Truck T{i}" if i % 2 == 0 else f"Van V{i}"
        typ = "truck" if i % 2 == 0 else "delivery_van"
        fuel = str(random.randint(100, 800))
        dist = str(random.randint(1000, 5000))
        hrs = str(random.randint(50, 200))
        
        pdf.cell(45, 8, name, 1)
        pdf.cell(35, 8, typ, 1)
        pdf.cell(30, 8, fuel, 1)
        pdf.cell(35, 8, dist, 1)
        pdf.cell(30, 8, hrs, 1, ln=1)
        
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(190, 10, txt=f"Total Emissions: {random.uniform(100, 800):.2f} tCO2e", border=0, ln=1, align='R')
    
    path = f"{company}.pdf"
    pdf.output(path)

for i in range(1, 11):
    make_pdf(i)
