# insights.py
# domain-specific sustainability insights engine
# primary: uses openai api key for dynamic AI-generated insights
# fallback: prebaked tips (15 per category per domain) when api is unavailable

import random
import json
import os

# ========== prebaked insights (fallback) ==========
# structured as DOMAIN_INSIGHTS[domain][category] = [list of 15 tips]

DOMAIN_INSIGHTS = {

    # ----- TECHNOLOGY / IT -----
    "technology": {
        "transportation": [
            "Encourage remote work policies to cut employee commute emissions by up to 40% (IEA 2023).",
            "Subsidize public transit passes for employees to reduce Scope 3 emissions (WRI 2022).",
            "Replace company cars with electric vehicles to lower direct fleet impact (Carbon Trust).",
            "Use video conferencing instead of flying to meetings -- saves ~1.1 tonnes CO2 per round trip (ICAO).",
            "Offer bike-to-work incentives with secure parking and shower facilities (Sustrans).",
            "Implement a carpooling app for employees to optimize vehicle occupancy (WEF 2021).",
            "Track employee commute data monthly to identify high-emission patterns (GHG Protocol).",
            "Use e-bikes or scooters for short-distance inter-office travel (EPA 2023).",
            "Schedule team activities to reduce the number of individual commute days (IEA).",
            "Offset remaining travel emissions with verified carbon credits (Gold Standard).",
            "Negotiate with airlines for sustainable aviation fuel on corporate bookings (IATA).",
            "Set a per-employee annual flight budget to discourage unnecessary travel (UNEP).",
            "Use train travel for domestic trips under 500km -- significantly lower CO2 than flying (EEA).",
            "Install EV charging stations at the office to incentivize electric car adoption (IEA).",
            "Consolidate office locations to reduce average commute distance (Urban Land Institute).",
        ],
        "electricity": [
            "Migrate on-premise servers to green cloud providers (AWS, Azure, GCP have carbon-neutral data centers) (Google/Microsoft 2023).",
            "Monitor per-room kWh usage to identify energy waste in underused office zones (ISO 50001).",
            "Upgrade server room cooling with hot/cold aisle containment to save 20-30% power (Uptime Institute).",
            "Use smart power strips that cut phantom loads from monitors and peripherals (Energy Star).",
            "Schedule non-urgent batch processing during off-peak (cleaner grid) hours (IEA).",
            "Install occupancy sensors in meeting rooms to auto-switch lights and HVAC (BREEAM).",
            "Replace fluorescent lights with LED panels -- saves 50-75% lighting energy (DOE 2022).",
            "Set server room temperature to 27C instead of 20C (ASHRAE TC 9.9 recommends up to 27C).",
            "Virtualize servers to consolidate workloads and cut physical machine count (VMWare Research).",
            "Purchase renewable energy certificates (RECs) to offset grid electricity (RE100).",
            "Deploy serverless architectures to minimize idle resource consumption (AWS Lambda Whitepaper).",
            "Review and decommission unused cloud instances weekly to avoid waste (RightScale).",
            "Use laptop docking stations instead of desktops -- laptops use 70% less energy (Energy Star).",
            "Install solar panels on office rooftops for partial self-generation (IEA 2023).",
            "Run energy audits quarterly to track electricity reduction progress (ISO 14001).",
        ],
        "logistics": [
            "Digital delivery eliminates physical shipping emissions entirely (World Bank).",
            "Use carbon-neutral shipping providers for hardware deliveries (DHL GOGREEN).",
            "Consolidate hardware orders into larger shipments to reduce packaging (EPA SmartWay).",
            "Source hardware locally where possible to minimize international shipping (IPCC 2022).",
            "Implement digital signatures and paperless documentation to reduce courier needs (UNEP).",
            "Use recycled packaging for all outgoing shipments (SCS Global).",
            "Partner with logistics providers who use electric delivery vans (IEA).",
            "Track per-shipment carbon footprint to identify high-emission routes (GHG Protocol).",
            "Return and recycle old hardware through certified e-waste programs (Basel Convention).",
            "Use palletized shipping for bulk orders to maximize truck utilization (ITF).",
            "Switch from air freight to ground shipping for non-urgent hardware (Carbon Trust).",
            "Negotiate with carriers for route-optimized delivery schedules (UPS ORION).",
            "Maintain a digital asset inventory to avoid unnecessary physical purchases (ISO 55001).",
            "Use shared warehousing to reduce individual facility overhead (Llamasoft).",
            "Implement a buy-back program for old devices to extend product lifecycles (WCEF).",
        ],
        "manufacturing": [
            "Require suppliers to report their carbon emissions data annually (CDP).",
            "Prefer manufacturers powered by renewable energy for hardware sourcing (RE100).",
            "Audit contract manufacturers for energy efficiency in assembly lines (ISO 50001).",
            "Push for right-to-repair design to reduce manufacturing cycles (EEB 2023).",
            "Spec recycled aluminum and plastics in product designs (Ellen MacArthur Foundation).",
            "Reduce product packaging by 20-30% without compromising protection (Sustainable Packaging Coalition).",
            "Design modular products so individual components can be replaced (Circular Economy Action Plan).",
            "Set supplier sustainability targets as part of procurement contracts (UN Global Compact).",
            "Use lifecycle assessment (LCA) tools to compare production methods (ISO 14040).",
            "Invest in suppliers who use water recycling systems in their processes (CDP Water).",
            "Audit the entire supply chain once a year and publish a transparency report (GRI Standards).",
            "Work with suppliers on reducing waste at the component sourcing stage (Lean Manufacturing).",
            "Choose low-emission materials for printed packaging materials (FSC).",
            "Refurbish and resell returned products instead of scrapping them (WCEF).",
        ],
    },

    # ----- LOGISTICS & TRANSPORT -----
    "logistics": {
        "transportation": [
            "Install GPS tracking on every vehicle to identify inefficient routes in real time (EPA SmartWay).",
            "Regularly service engines -- a well-tuned engine uses 4-10% less fuel (Department of Energy).",
            "Replace older diesel trucks with CNG or electric models over the next 3 years (ICCT 2022).",
            "Use predictive analytics to optimize route planning and reduce empty miles (GHG Protocol).",
            "Enforce a speed limit policy for fleet vehicles -- speed over 90km/h tanks fuel efficiency (Carbon Trust).",
            "Install aerodynamic kits (cab fairings, side skirts) on heavy trucks to save 5-8% fuel (NACFE).",
            "Monitor individual driver fuel efficiency and reward the best performers (ISO 14001).",
            "Use telematics to cut excessive idling time across the fleet (EPA 2023).",
            "Transition last-mile delivery to electric vans or cargo e-bikes (IEA 2023).",
            "Consolidate partial-load shipments into full truckloads before dispatch (CSMP).",
            "Implement dynamic routing software that adapts to live traffic and weather (MIT CTL).",
            "Track fuel consumption per vehicle per month to spot anomalies early (Energy Star).",
            "Use tire pressure monitoring systems (TPMS) -- correct pressure saves 3% fuel (Department of Transportation).",
            "Schedule preventive maintenance to avoid breakdowns that cause detour emissions (FTA).",
            "Pilot hydrogen fuel cell trucks for long-haul routes as they become available (Hydrogen Council).",
        ],
        "electricity": [
            "Upgrade warehouse lighting to LED with motion sensors -- saves 60% lighting costs (IEA).",
            "Install rooftop solar on warehouse facilities for partial self-generation (SEIA).",
            "Use smart climate controls in warehouses to avoid over-cooling (ASHRAE).",
            "Switch to energy-efficient refrigeration units for cold chain operations (Energy Star).",
            "Install power factor correction equipment to reduce wasted electrical energy (IEEE).",
            "Monitor warehouse electricity per zone to find high-consumption areas (ISO 50001).",
            "Turn off conveyor belts and sorting machines during off-hours automatically (Lean Logistics).",
            "Use natural ventilation designs in new warehouse builds to cut HVAC needs (LEED).",
            "Install insulation on warehouse walls and roofs to reduce thermal loss (Carbon Trust).",
            "Purchase green energy tariffs for all warehouse and office facilities (RE100).",
            "Deploy smart meters on all electrical circuits for real-time monitoring (DOE).",
            "Run annual energy audits on every warehouse and distribution center (ISO 14001).",
            "Use battery storage systems to capture solar energy for night operations (IEA 2023).",
            "Replace old loading dock equipment with energy-efficient electric models (MHI).",
            "Implement building management systems (BMS) for centralized energy control (BOMA).",
        ],
        "logistics": [
            "Consolidate shipments to improve truck load utilization above 85% (World Economic Forum).",
            "Use intermodal transport (truck + rail) for shipments over 500km (Association of American Railroads).",
            "Ship by sea instead of air for international non-urgent deliveries (IMO 2023).",
            "Set up regional distribution hubs to shorten last-mile distances (DHL Trends).",
            "Use returnable and reusable packaging to cut waste (Ellen MacArthur Foundation).",
            "Track per-shipment CO2 and display it on shipping labels (GHG Protocol).",
            "Negotiate with carriers for carbon-neutral delivery options (GLEC Framework).",
            "Implement cross-docking to reduce warehousing and double-handling (CSCMP).",
            "Use AI to predict demand so you can pre-position stock and reduce rush shipments (Gartner).",
            "Reduce packaging weight by 15% through material engineering (Sustainable Packaging Coalition).",
            "Share delivery routes with partner companies to improve vehicle capacity (WEF).",
            "Set maximum delivery attempt limits to reduce failed delivery emissions (PostNord).",
            "Use lightweight pallets (plastic or composite) instead of heavy wood ones (FEPE).",
            "Digitize proof-of-delivery to eliminate paper-based return trips (UNEP).",
            "Audit your top 10 shipping lanes annually for optimization opportunities (ISO 14064).",
        ],
        "manufacturing": [
            "Audit packaging suppliers for sustainable material sourcing practices (FSC/PEFC).",
            "Use corrugated cardboard made from 80%+ recycled content (FEFCO).",
            "Reduce over-packaging by right-sizing boxes to product dimensions (Sustainable Packaging Coalition).",
            "Source biodegradable void fill instead of polystyrene peanuts (SCS Global).",
            "Partner with packaging suppliers who use renewable energy in production (RE100).",
            "Design packaging for disassembly so materials can be easily recycled (GreenBlue).",
            "Run waste audits at distribution centers to identify reduction opportunities (TRUE Zero Waste).",
            "Implement a loop system for pallet repair and reuse instead of disposal (CHEP).",
            "Use water-based inks and adhesives on all printed packaging (EPA 2022).",
            "Track packaging waste as a KPI alongside delivery performance metrics (GRI Standards).",
            "Invest in automated packaging machines that reduce material waste (PMMI).",
            "Require environmental certifications (FSC, PEFC) for all paper suppliers (WWF).",
            "Use compostable mailers for lightweight last-mile shipments (BPI Certified).",
            "Set annual targets for reducing single-use plastic in shipping (New Plastics Economy).",
            "Switch to digital packing slips and invoices to eliminate paper (UNEP).",
        ],
    },

    # ----- CONSTRUCTION -----
    "construction": {
        "transportation": [
            "Use on-site fuel management systems to track individual truck consumption (RICS 2022).",
            "Replace older haul trucks with Tier 4 or electric models for 30% emission cuts (EPA 2023).",
            "Schedule crew carpooling to reduce the number of personal vehicles on site (GHG Protocol).",
            "Use electric crew transport vans for moving workers between site locations (IEA).",
            "Track fuel usage per trip for material hauling to identify waste (ISO 14064).",
            "Install GPS on all site vehicles to prevent unauthorized or inefficient usage (Fleet Management).",
            "Procure locally sourced materials to reduce transport distances by up to 50% (LEED v4).",
            "Use conveyor systems on large sites instead of trucking material internally (Mineral Products Association).",
            "Implement anti-idling policies for all site vehicles -- save 3-5% fuel daily (Carbon Trust).",
            "Hire a logistics coordinator to consolidate material deliveries into fewer trips (CSCMP).",
            "Switch to biodiesel blends (B20) for diesel equipment to cut emissions by 15% (Department of Energy).",
            "Provide on-site accommodation for remote projects to eliminate daily commutes (UNEP 2022).",
            "Use barges for waterside projects instead of road transport for heavy materials (IMO).",
            "Negotiate with suppliers for delivery window consolidation to reduce trips (Lean Construction).",
            "Deploy electric forklifts on site instead of propane-powered models (NIOSH).",
        ],
        "electricity": [
            "Use solar-powered temporary lighting on construction sites (SEIA).",
            "Deploy battery energy storage systems instead of diesel generators for small loads (IEA).",
            "Use smart timers on temporary electrical installations to prevent overnight waste (IEEE).",
            "Connect to grid power as early as possible instead of running diesel generators (Carbon Trust).",
            "Install LED tower lights instead of halogen -- 80% less energy (DOE 2022).",
            "Use variable speed drives on pumps and compressors to reduce electrical waste (ISO 50001).",
            "Monitor generator fuel consumption daily and right-size equipment (Uptime Institute).",
            "Install temporary solar panels on site offices and break rooms (Solar Power Europe).",
            "Use energy-efficient HVAC in temporary site buildings (ASHRAE 90.1).",
            "Track per-phase electricity usage to identify inefficient site zones (Energy Star).",
            "Deploy hybrid generators that switch to battery mode during low-load periods (NACFE).",
            "Use electric welding machines instead of gas-powered models where feasible (AWS).",
            "Install motion sensors on site office lights and common areas (BREEAM).",
            "Run site-wide energy awareness training for foremen and subcontractors (ISO 14001).",
            "Use reflective roofing on temporary buildings to reduce cooling needs (CRRC).",
        ],
        "logistics": [
            "Pre-fabricate components off-site to reduce on-site waste and transport (RICS).",
            "Use modular construction methods to minimize material deliveries (Modular Building Institute).",
            "Order materials in reusable containers that get returned to suppliers (Ellen MacArthur).",
            "Implement just-in-time delivery to reduce material stored on site (Lean Construction).",
            "Track material waste per delivery to identify over-ordering patterns (BRE).",
            "Use digital takeoff tools to precisely estimate material needs (RICS).",
            "Stockpile excavated soil on-site for reuse instead of trucking it away (DEFRA).",
            "Source aggregates from local quarries within 50km when possible (Mineral Products Association).",
            "Reuse formwork and scaffolding across projects to reduce new material (BREEAM).",
            "Return unused materials to suppliers instead of disposing of them (ISO 14001).",
            "Use lightweight composite materials that reduce transport weight (Carbon Trust).",
            "Coordinate deliveries with subcontractors to avoid duplicate shipments (CSCMP).",
            "Use waste segregation on-site to enable recycling of concrete and metal (TRUE Zero Waste).",
            "Rent equipment locally instead of transporting owned machines (ERA).",
            "Implement a materials passport system to enable reuse across projects (Circular Economy).",
        ],
        "manufacturing": [
            "Switch to low-carbon concrete mixes (slag or fly ash blends) for 30-50% reduction (CDBB).",
            "Use sustainably sourced timber (FSC certified) for structural elements (WWF).",
            "Use recycled steel which produces 75% less CO2 than virgin steel (WorldSteel).",
            "Specify energy-efficient glass (low-e, triple glazed) to reduce building emissions (Passive House).",
            "Install equipment fuel flow meters to monitor real-time consumption (ISO 50001).",
            "Service heavy machinery monthly to maintain peak fuel efficiency (NAEC).",
            "Use electrically powered mini excavators for smaller tasks instead of diesel (CECE).",
            "Replace old crane engines with Tier 4 emission compliant models (EPA).",
            "Deploy automated machine control (GPS grading) to reduce passes and fuel (Trimble Research).",
            "Track idle time per piece of equipment and set targets for reduction (Carbon Trust).",
            "Use concrete batching plants on-site to reduce mixer truck trips (RICS).",
            "Switch to electric concrete vibrators and power tools where possible (OSHA).",
            "Implement a machine sharing platform between projects to improve utilization (CE100).",
            "Use bio-lubricants in hydraulic systems to reduce environmental impact (EPA).",
            "Conduct emissions benchmarking between similar projects for improvement (GRESB).",
        ],
    },

    # ----- MANUFACTURING -----
    "manufacturing": {
        "transportation": [
            "Optimize delivery schedules to consolidate outbound shipments (Lean Manufacturing).",
            "Use electric forklifts and warehouse vehicles instead of propane (NIOSH).",
            "Implement route optimization for raw material inbound logistics (GHG Protocol).",
            "Locate new facilities closer to key suppliers to minimize transport (World Bank).",
            "Use rail siding connections at factories for bulk material delivery (AAR).",
            "Track emissions per delivery mile and set annual reduction targets (ISO 14001).",
            "Use CNG trucks for inter-plant material transfers (Department of Energy).",
            "Consolidate vendor deliveries through a milk-run scheduling system (Toyota Lean).",
            "Install EV charging infrastructure for employee and visitor vehicles (IEA 2023).",
            "Negotiate with logistics partners for carbon-neutral shipping options (Carbon Trust).",
            "Use digital twins to simulate and optimize supply chain transport flows (Gartner).",
            "Replace company fleet with hybrid vehicles for sales and service (Energy Star).",
            "Partner with local last-mile delivery services using electric vans (DHL Trends).",
            "Measure and report outbound freight emissions as a key operations metric (GRI).",
            "Explore autonomous electric vehicles for internal site logistics (Tesla/Waymo Research).",
        ],
        "electricity": [
            "Install sub-meters on every major machine to identify energy hogs (ISO 50001).",
            "Use variable frequency drives (VFDs) on motors to match load (Energy Star).",
            "Deploy combined heat and power (CHP) systems for efficiency (IEA).",
            "Upgrade compressed air systems -- leaks waste 20-30% energy (DOE).",
            "Install skylight roof panels in factories for natural daylight harvesting (LEED).",
            "Use waste heat recovery systems to preheat water or raw materials (Carbon Trust).",
            "Switch to high-efficiency electric motors (IE4/IE5 class) (IEC Standards).",
            "Implement a building management system (BMS) for centralized monitoring (ISO 50001).",
            "Schedule energy-intensive processes during off-peak grid hours (GridPoint Research).",
            "Install rooftop solar to offset daytime production electricity (SEIA).",
            "Use power factor correction capacitors to avoid reactive energy (IEEE).",
            "Run annual thermal imaging audits to find insulation gaps (ISO 14001).",
            "Replace hydraulic presses with servo-electric presses for 50% savings (Lean Mfg).",
            "Use regenerative braking on conveyor systems to recover energy (DOE).",
            "Publish monthly energy consumption dashboards for production teams (GRI).",
        ],
        "logistics": [
            "Implement warehouse management systems (WMS) to reduce movement waste (CSCMP).",
            "Use automated guided vehicles (AGVs) to reduce energy waste (MHI).",
            "Install dock levelers with insulated doors to prevent climate losses (ASHRAE).",
            "Practice lean inventory management to reduce warehousing space (Toyota Lean).",
            "Use reusable totes and bins instead of cardboard containers (Ellen MacArthur).",
            "Consolidate raw material deliveries using just-in-time scheduling (Lean Mfg).",
            "Track packaging waste as a percentage of product weight (Sustainable Packaging Coalition).",
            "Ship finished goods in bulk palletized loads instead of parcels (UPU).",
            "Use regional distribution centers to reduce long-haul trips (Logistics Management).",
            "Implement reverse logistics for component recovery (Circular Economy Action Plan).",
            "Use sustainable packaging (recycled, biodegradable) (SCS Global).",
            "Design packaging to be stackable and space-efficient (ISO 14000).",
            "Digitize quality certificates and shipping documents to reduce paper (UNEP).",
            "Set supplier delivery windows to coordinate inbound traffic (CSCMP).",
            "Measure logistics emissions per unit manufactured monthly (GHG Protocol).",
        ],
        "manufacturing": [
            "Install energy monitoring on each production line (ISO 50001).",
            "Use predictive maintenance to avoid energy spikes (Predictive Maintenance Institute).",
            "Switch from gas-fired furnaces to electric induction heating (IEA).",
            "Implement closed-loop water cooling to reduce treatment energy (CDP Water).",
            "Use automation to reduce scrap rates and wasted energy (Lean Six Sigma).",
            "Design for manufacturability to reduce processing steps (DFM/DFA Society).",
            "Track CO2 per unit produced (carbon intensity) as a key KPI (GRI Standards).",
            "Use 3D printing for prototyping to cut material waste (ASTM International).",
            "Switch to water-based paints to reduce VOC treatment energy (EPA).",
            "Deploy robotic welding for consistent quality and lower energy (AWS).",
            "Use recycled raw materials wherever quality standards permit (Circular Economy).",
            "Install air curtains on factory doors to prevent air escape (ASHRAE).",
            "Use lean manufacturing (5S, Kaizen) to eliminate waste (Toyota).",
            "Set annual machine energy reduction targets by line (ISO 14001).",
            "Benchmark against industry peers using sustainability indices (DJSI).",
        ],
    },
}

# legacy flat fallback (used by older routes that reference INSIGHTS[category])
INSIGHTS = {
    "transportation": DOMAIN_INSIGHTS["technology"]["transportation"],
    "electricity": DOMAIN_INSIGHTS["technology"]["electricity"],
    "logistics": DOMAIN_INSIGHTS["technology"]["logistics"],
    "manufacturing": DOMAIN_INSIGHTS["technology"]["manufacturing"],
}


def get_random_insight(category, domain=None):
    """Get a random prebaked insight for dashboard display."""
    category = category.lower()
    if domain and domain in DOMAIN_INSIGHTS:
        pool = DOMAIN_INSIGHTS[domain]
    else:
        pool = INSIGHTS
    
    if category not in pool:
        category = "transportation"
    return random.choice(pool[category])


def get_ai_insights(domain, high_cats, openai_client):
    """
    Primary path: use OpenAI to generate domain-aware sustainability tips.
    Falls back to prebaked insights if the API call fails or daily limit is reached.
    """
    from api_guard import safe_api_call
    
    def _call_openai():
        prompt = (
            f"You are a sustainability expert. A {domain} company has high emissions "
            f"in these categories: {', '.join(high_cats)}. "
            f"For each category, provide 3 specific, actionable sustainability tips "
            f"tailored to the {domain} industry. "
            f"Return ONLY raw JSON with category names as keys and arrays of 3 tip strings as values."
        )
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return json.loads(response.choices[0].message.content)
    
    def _fallback():
        result = {}
        pool = DOMAIN_INSIGHTS.get(domain, DOMAIN_INSIGHTS["technology"])
        for cat in high_cats:
            cat_key = cat.lower()
            if cat_key in pool:
                result[cat] = random.sample(pool[cat_key], min(3, len(pool[cat_key])))
            else:
                result[cat] = ["Review your operations in this category for improvement opportunities."]
        return result
    
    if openai_client:
        ai_result = safe_api_call("openai", _call_openai, _fallback)
        if ai_result:
            return ai_result
    
    return _fallback()


def get_insights_for_report(cats, domain=None):
    """Legacy helper for basic insight retrieval."""
    result = {}
    for cat in cats:
        result[cat] = get_random_insight(cat, domain)
    return result
