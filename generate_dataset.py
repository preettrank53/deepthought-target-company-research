import pandas as pd

# Create the data structure matching the exact DeepThought rubric
data = [
    {
        "Company Name": "Paragon Fine and Speciality Chemical Ltd",
        "Website": "https://www.paragonind.com",
        "City": "Ahmedabad",
        "Segment": "Basket A — Custom synthesis & specialty chemicals",
        "What They Make": "Pharma intermediates, agro intermediates, cosmetics intermediates via complex differentiated chemistry",
        "Revenue Band": "Rs.100-300Cr",
        "Decision Maker": "Pravinchandra J. Vasolia (MD & CEO)",
        "E1: Producer": "PASS — Production capacity of 650 MTPA expanding to 850 MTPA.",
        "E2: Accessible": "PASS — Operations and corporate headquarters located in Ahmedabad.",
        "C3 Score": "Strong", "C3 Evidence": "DSIR-certified R&D unit, One Star Export House status, and full ISO/SA8000 credentials.",
        "C4 Score": "Strong", "C4 Evidence": "Promoter-led with a professionalized layer including a hired CFO and independent directors.",
        "C5 Score": "Strong", "C5 Evidence": "Pharma intermediates market heavily benefiting from China+1 supply chain diversification.",
        "C6 Score": "Strong", "C6 Evidence": "Acquired new land near Viramgam for a warehouse and invested ₹23.3M in new machinery for FY25.",
        "C7 Score": "Moderate", "C7 Evidence": "Advanced ISO 45001/SA8000 infrastructure indicates formal operational data systems.",
        "C8 Score": "Strong", "C8 Evidence": "Robust board configuration with 3 active independent directors and generational continuity.",
        "Overall Federer Score": 88, "Score Band": "A — Strong Federer", "Verdict": "Strong Pass",
        "Personalization Hook": "Congratulations on the Viramgam land acquisition and your push to hit 850 MTPA capacity by June 2025."
    },
    {
        "Company Name": "Prima Chemicals",
        "Website": "https://www.primachemicals.com",
        "City": "Ahmedabad",
        "Segment": "Basket C — Technical textiles & specialty yarns / Dyes",
        "What They Make": "Pyrazolones and polymer-soluble specialty dyes for plastics and printing inks",
        "Revenue Band": "Rs.100-300Cr",
        "Decision Maker": "Kamlesh Modi (Founder) / Apurv Modi (Gen-2 Director)",
        "E1: Producer": "PASS — Active manufacturing plants in Odhav and a dedicated Unit-II in Vatva GIDC.",
        "E2: Accessible": "PASS — Fully operational within the Ahmedabad manufacturing corridor.",
        "C3 Score": "Strong", "C3 Evidence": "Single largest pyrazolone derivatives manufacturer globally with a deep process capability moat.",
        "C4 Score": "Strong", "C4 Evidence": "Founder is an MSc Organic Chemist (ex-Cadila); Gen-2 Director holds an MS in Organic Chemistry from the US.",
        "C5 Score": "Moderate", "C5 Evidence": "Specialty dyes sector is stable, experiencing steady but niche technical compounding growth.",
        "C6 Score": "Moderate", "C6 Evidence": "Established a secondary operational facility (Unit-II) in Vatva to handle scaling output.",
        "C7 Score": "Moderate", "C7 Evidence": "Latest ISO 45001:2018 operational standard confirmed across automated production lines.",
        "C8 Score": "Strong", "C8 Evidence": "Flawless technical succession with a US-educated Gen-2 organic chemist taking full operational charge.",
        "Overall Federer Score": 82, "Score Band": "A — Strong Federer", "Verdict": "Strong Pass",
        "Personalization Hook": "Seeing Prima Chemicals evolve into the world's largest pyrazolone manufacturer while seamlessly passing the technical baton to US-educated Gen-2 leadership is inspiring."
    },
    {
        "Company Name": "Elixir Pharma",
        "Website": "https://www.elixirpharma.in",
        "City": "Ahmedabad",
        "Segment": "Basket B — Complex APIs & regulated pharma",
        "What They Make": "Active Pharmaceutical Ingredients (Pregabalin, Glibenclamide BP) and GLP-compliant chemistry services",
        "Revenue Band": "Rs.30-100Cr",
        "Decision Maker": "Daleep Malhotra / Jignesh Patel (Techno-commercial Promoters)",
        "E1: Producer": "PASS — Operates in-house WHO-GMP certified manufacturing facilities.",
        "E2: Accessible": "PASS — Based natively out of the Ahmedabad pharma industrial cluster.",
        "C3 Score": "Strong", "C3 Evidence": "Fully WHO-GMP certified production units alongside GLP-compliant research laboratories.",
        "C4 Score": "Strong", "C4 Evidence": "Founded and actively steered by a collective team of seasoned techno-commercial professionals.",
        "C5 Score": "Strong", "C5 Evidence": "High-barrier API sector directly riding the wave of India's domestic self-reliance and export tailwinds.",
        "C6 Score": "Moderate", "C6 Evidence": "15+ years of active market expansion with a steadily widening global contract research portfolio.",
        "C7 Score": "Moderate", "C7 Evidence": "Tight compliance systems required for maintaining concurrent ISO 14001, 18001, and GLP standards.",
        "C8 Score": "Moderate", "C8 Evidence": "Distributed professional corporate structure, though family-level succession metrics are opaque.",
        "Overall Federer Score": 75, "Score Band": "B — Probable Federer", "Verdict": "Pass",
        "Personalization Hook": "Your combination of WHO-GMP manufacturing plants alongside GLP-compliant development labs offers a fantastic blueprint for global scale."
    },
    {
        "Company Name": "Kronox Lab Sciences Ltd",
        "Website": "https://www.kronoxlabsciences.com",
        "City": "Vadodara",
        "Segment": "Basket A — Custom synthesis & specialty chemicals",
        "What They Make": "High-purity specialty chemicals, titanium dioxide pigments, and fine lab reagents",
        "Revenue Band": "Rs.100-300Cr",
        "Decision Maker": "Joginder Singh Jaswal / Ketan Ramani",
        "E1: Producer": "PASS — In-house advanced pigment and ultra-pure chemical manufacturing infrastructure in Padra.",
        "E2: Accessible": "PASS — Plant and core leadership based out of the Padra industrial belt in Vadodara.",
        "C3 Score": "Strong", "C3 Evidence": "Specializes in ultra-high purity materials with rigorous technical testing limits exceeding standard industry metrics.",
        "C4 Score": "Moderate", "C4 Evidence": "Technically adept executive management with decades of deep chemical engineering execution.",
        "C5 Score": "Strong", "C5 Evidence": "High-purity reagents and advanced inputs are booming due to aggressive domestic semiconductor and specialized testing growth.",
        "C6 Score": "Moderate", "C6 Evidence": "Maintained market momentum through a successful initial public listing and capacity upgrades.",
        "C7 Score": "Moderate", "C7 Evidence": "Strict internal process controls and modern analytical testing infrastructure are active across all units.",
        "C8 Score": "Weak", "C8 Evidence": "Highly centralized management structure with minimal public visibility of an independent second-generation transition.",
        "Overall Federer Score": 72, "Score Band": "B — Probable Federer", "Verdict": "Pass",
        "Personalization Hook": "Your precision focus on ultra-high purity chemical manufacturing out of Padra sets a tremendous standard for import substitution in India."
    },
    {
        "Company Name": "Paushak Ltd",
        "Website": "https://www.paushak.com",
        "City": "Vadodara",
        "Segment": "Basket A — Custom synthesis & specialty chemicals",
        "What They Make": "Carbonyl chloride (phosgene) specialty derivatives, specialized isocyanates, and pharma intermediates",
        "Revenue Band": "Rs.100-300Cr",
        "Decision Maker": "Chirayu Amin (Chairman)",
        "E1: Producer": "PASS — Highly specialized in-house hazchem processing plant located in Vadodara.",
        "E2: Accessible": "PASS — Primary operations anchored firmly in Vadodara, Gujarat.",
        "C3 Score": "Strong", "C3 Evidence": "Extremely high barrier to entry; one of the few licensed manufacturers capable of handling phosgene chemistry in India.",
        "C4 Score": "Moderate", "C4 Evidence": "Part of the Alembic group ecosystem; professionalized corporate direction but high promoter centralization.",
        "C5 Score": "Strong", "C5 Evidence": "Phosgene derivatives are critical building blocks for scaling agrochemical and complex pharmaceutical intermediaries.",
        "C6 Score": "Moderate", "C6 Evidence": "Steady capital deployment into process optimization and advanced safety infrastructure containment units.",
        "C7 Score": "Strong", "C7 Evidence": "Advanced safety automation and integrated control loops are mandatory for operations due to the hazardous nature of inputs.",
        "C8 Score": "Weak", "C8 Evidence": "Heavy structural reliance on the overarching parent group's leadership frameworks.",
        "Overall Federer Score": 70, "Score Band": "B — Probable Federer", "Verdict": "Pass",
        "Personalization Hook": "The specialized phosgene-based chemistry moat you have built at Paushak represents one of the strongest technical processing barriers in Gujarat."
    },
    {
        "Company Name": "Palam Pharma Pvt. Ltd.",
        "Website": "Private/No active site",
        "City": "Ahmedabad",
        "Segment": "Basket B — Complex APIs & regulated pharma",
        "What They Make": "Bulk drugs and older API compounds like Fluoxetine HCl and Dicyclomine HCl",
        "Revenue Band": "Rs.30-100Cr",
        "Decision Maker": "Tarun Patel (Director)",
        "E1: Producer": "PASS — Maintains an aging physical manufacturing presence inside Vatva GIDC.",
        "E2: Accessible": "PASS — Located operationally within the Vatva Phase-I industrial estate.",
        "C3 Score": "Weak", "C3 Evidence": "Maintains localized state-level GMP (S-GMP) without holding high-barrier global regulatory clearances (USFDA/WHO-GMP).",
        "C4 Score": "Weak", "C4 Evidence": "Traditional promoter mindset; no visible markers of structured process engineering or technical research investments.",
        "C5 Score": "Strong", "C5 Evidence": "API manufacturing as a sector remains strong, but commodity tracking erodes advantage without specialization.",
        "C6 Score": "Weak", "C6 Evidence": "Stagnant operational trajectory since 1997 with zero evidence of recent physical or capital expansions.",
        "C7 Score": "Weak", "C7 Evidence": "Relies entirely on legacy paper-based record metrics; clear structural deficit in digital workflow management.",
        "C8 Score": "Weak", "C8 Evidence": "Highly siloed single-director control mechanism with no external managerial layer present.",
        "Overall Federer Score": 45, "Score Band": "D — Not ICP", "Verdict": "Fail",
        "Personalization Hook": "Your structural longevity in Vatva since 1997 offers an established base, though scaling to international WHO-GMP standards could open massive avenues."
    }
]

df = pd.DataFrame(data)
print("DataFrame created successfully", flush=True)
try:
    df.to_csv("target_companies.csv", index=False)
    print("Successfully generated target_companies.csv with clear pass/fail configurations!", flush=True)
except Exception as e:
    print(f"Error saving CSV: {e}", flush=True)