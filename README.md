<div align="center">
  <img src="https://raw.githubusercontent.com/MatthewJakubowski/Universal-Lab-Converter/main/going_dark_cover.jpg" width="100%" alt="System Status: Going Dark. Deep Work Protocol.">
</div>

# ✅ Lab Result Verifier (Bulk Auto-Validation)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Automation](https://img.shields.io/badge/Automation-CSV_Processing-orange?style=for-the-badge)
![Healthcare](https://img.shields.io/badge/Healthcare-Clinical_Validation-red?style=for-the-badge)

> **High-performance tool for automated validation of laboratory results.**
> Processes bulk data exports (CSV), applies conditional logic based on medical reference ranges, and prioritizes critical "Panic Values" for immediate action.

---

## 🏥 Problem
In high-throughput laboratories, reviewing thousands of results manually creates a bottleneck and increases the risk of missing a **Critical Value** (e.g., HGB < 7.0 g/dL).
Modern LIS (Laboratory Information Systems) use "Auto-Validation" rules to filter healthy patients. This tool replicates that logic in Python.

## ⚙️ How It Works
The script acts as a filter between the Analyzer and the Medical Laboratory Scientist.

1.  **Ingest:** Reads raw CSV data (simulated LIS export).
2.  **Analyze:** Compares each result against a **Configuration Dictionary** containing:
    * Reference Ranges (Min/Max)
    * Critical Limits (Panic Values)
3.  **Prioritize:** Assigns a priority flag to each patient:
    * 🚨 **PRIORITY 1 (CRITICAL):** Immediate notification required.
    * ⚠️ **PRIORITY 2 (PATHOLOGY):** Requires manual review.
    * ✅ **PRIORITY 3 (NORMAL):** Auto-validated.

---

## 🛠️ Configuration (Medical Logic)
The validation rules are stored in a flexible Python Dictionary, making it easy to update reference ranges without changing the core code.

```python
NORMY = {
    "HGB": {"min": 12.0, "max": 16.0, "crit_min": 7.0, "crit_max": 20.0},
    "PLT": {"min": 150,  "max": 400,  "crit_min": 30,  "crit_max": 1000},
    # Add new parameters here...
}

---
```
## 🚀 Usage
​1. Run the Tool
​The script automatically generates a simulated dataset (dane_z_analizatora.csv) containing 100 random patients and processes it.
```
python main.py
```
## 2. Check the Console
​Critical values are displayed immediately for rapid response:
```
🚨 ALARM: P-045 | HGB 6.57 | CRITICAL LOW
🚨 ALARM: P-099 | PLT 12.0 | CRITICAL LOW
```
## 3. Review the Report (RAPORT_FINALNY.csv)
​A structured file is generated for import into Excel/LIS:
```
PRIORYTET,FLAGA,PACJENT_ID,BADANIE,WYNIK,KOMENTARZ
1,!!!,P-045,HGB,6.57,CRITICAL LOW
2,H,P-021,GLU,105,High
3,N,P-001,TSH,2.5,Normal
```
---
## 👨‍🔬 About the Author

**Mateusz Jakubowski**
*Medical Analyst (15y exp) ➡️ Aspiring AI Engineer & Python Developer.*

I am building tools that bridge the gap between Medical Diagnostics and IT. This project was developed entirely on a mobile environment (**Samsung DeX** + **Pydroid 3**).

* **Connect with me:** [LinkedIn](https://www.linkedin.com/in/mateuszjakubowski)
* **Portfolio:** #FromPipetteToPython

---
### ⚠️ Disclaimer & Legal Notice

* **Educational Purpose Only:** This software is developed as part of a programming portfolio (#FromPipetteToPython) and is intended for demonstration purposes only.
* **Not a Medical Device:** This tool is **not** a validated Laboratory Information System (LIS) or a medical device under MDR/FDA regulations. It has not undergone formal validation for use in a clinical diagnostic setting.
* **Synthetic Data:** All data used in examples (including `dane_z_analizatora.csv`) is entirely synthetic (randomly generated) and does not represent real patients.
* **No Warranty:** The software is provided "as is", without warranty of any kind. The author is not liable for any errors in result interpretation or misuse of this code in a production environment.
