import os
import random
import glob
from fpdf import FPDF

# Delete existing
for f in glob.glob("*.pdf"):
    os.remove(f)

COMPANIES = [
    "NovaTech Systems", "CloudSphere Data", "CyberNet Solutions", "Apex Server Hosting", "Quantum IT Group",
    "Nexus Computing", "Vanguard Technologies", "Synapse Data Centers", "Zenith Network Ops", "Pinnacle Cloud Services"
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
    
    period = f"December 2026"
    pdf.cell(190, 10, txt=f"Reporting Period: {period}", border=0, ln=1, align='L')
    
    server_kwh = random.randint(50000, 200000)
    commute_km = random.randint(10000, 50000)
    flights = random.randint(2, 25)
    
    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(190, 10, txt="Narrative Summary", border=0, ln=1)
    pdf.set_font("Arial", "", 12)
    
    nar = (f"During this fiscal cycle, our data center infrastructure recorded a total energy draw of {server_kwh} kWh. "
           f"Employee commuting collectively amounted to {commute_km} km driven. "
           f"Business operations also accounted for {flights} business flights globally.")
    pdf.multi_cell(0, 8, txt=nar)
    pdf.ln(10)
    
    pdf.set_font("Arial", "B", 14)
    pdf.cell(190, 10, txt="Detailed Asset Inventory", border=0, ln=1)
    
    # 3 COLUMNS for Technology 
    pdf.set_font("Arial", "B", 10)
    pdf.cell(70, 10, "Component / Asset Name", 1)
    pdf.cell(60, 10, "Monthly Usage", 1)
    pdf.cell(60, 10, "Sector Classification", 1, ln=1)
    
    pdf.set_font("Arial", "", 10)
    
    for i in range(1, 11):
        name = f"Server Rack {i}" if i % 2 == 0 else f"Cooling Unit {i}"
        val = f"{random.randint(5000, 40000)} kWh" 
        sec = "IT Infrastructure" if i % 2 == 0 else "Facilities"
        
        pdf.cell(70, 8, name, 1)
        pdf.cell(60, 8, val, 1)
        pdf.cell(60, 8, sec, 1, ln=1)
        
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(190, 10, txt=f"Total Emissions: {random.uniform(500, 2000):.2f} tCO2e", border=0, ln=1, align='R')
    
    path = f"{company}.pdf"
    pdf.output(path)

for i in range(1, 11):
    make_pdf(i)
