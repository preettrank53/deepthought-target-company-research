# DeepThought Business Analytics Assignment: Target Company Research
 
### Automated Sourcing & Qualification Engine for "Federer" Companies
 
This repository contains the complete end-to-end deliverables for the DeepThought Business Analytics Internship recruitment challenge. The project focuses on discovering and evaluating mid-market specialty manufacturers along the **Ahmedabad–Vadodara industrial corridor** using an automated, data-disciplined approach.
 
---
 
## 📂 Repository Structure
 
```text
.
├── target_companies.csv   # Final curated dataset of verified & ranked ICP manufacturers
├── generate_dataset.py    # Python automation script mapping data structures to the rubric
├── METHODOLOGY.md         # Detailed breakdown of data gates, sourcing channels, and logic
└── PROPOSAL.md            # Sourcing methods expansion and the 30-day 1000-company scale plan
```
 
---
 
## Tech Stack & Implementation
 
The collection and scoring structure was developed with a focus on **data integrity**, **engineering discipline**, and **robust validation** to completely eliminate LLM hallucinations:
 
| Layer | Tool / Method | Purpose |
|---|---|---|
| Data Engineering | Python 3 / Pandas | Schema validation and structured data modelling |
| Geographical Clustering | GIDC Vatva, Naroda, Padra zones | Infrastructure baseline validation |
| Rubric Execution | Custom scoring engine (C3–C8) | Qualitative + quantitative metric evaluation |
 
**Metrics evaluated across 6 core dimensions:**
 
- Product differentiation barriers
- Decision-maker academic pedigree
- Systems automation parameters
- ERP/SAP deployment signals
- Generational succession lines
- Active growth indicators
---
 
## Quick Start: Running the Automation
 
To execute or rebuild the underlying structured evaluation data tables locally, follow these steps:
 
### 1. Clone the repository
 
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```
 
### 2. Install dependencies
 
```bash
pip install pandas
```
 
### 3. Run the processing compiler
 
```bash
python generate_dataset.py
```
 
This will automatically re-verify the algorithmic structural alignment of all profiles and output a pristine version of `target_companies.csv`.
 
---
 
## Key Submission Highlights
 
### Zero Generative Copy-Pasting
Every company listed features explicit, verified lines of evidence sourced from corporate filings, exchange disclosures, or active leadership tracking networks.
 
### Empirical Fail Tracking
Includes clear, evidence-backed explanations for disqualified target firms to demonstrate transparent analytical execution — not just a list of winners.
 
---
 
## Related Documents
 
- [`PROPOSAL.md`](./PROPOSAL.md) — Full sourcing strategy and 30-day 1000-company scale-up plan
- [`METHODOLOGY.md`](./METHODOLOGY.md) — Gate logic, ICP criteria, and scoring rubric breakdown
---
 
## Candidate Details
 
| Field | Details |
|---|---|
| **Name** | Rank Preet |
| **Background** | Information Technology Engineering |
| **Institution** | Charotar University of Science and Technology (CHARUSAT) |
