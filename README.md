# **Payroll Data Validator**

**Description**:  
- This project validates payroll data consistency between three sources:  
  - **GTN file** – payroll input file  
  - **Payrun file** – processed payroll output  
  - **mapping.json** – configuration file defining how GTN pay elements map to Payrun columns  

- The system uses automated Python unit tests to verify:  
  - The GTN file is a valid Excel file with required headers in the correct order  
  - No unexpected empty rows exist  
  - All GTN pay elements are properly mapped  
  - All Payrun pay elements have corresponding GTN mappings  
  - Pay element values are numeric  

- The goal of the project is to ensure data integrity, mapping accuracy, and payroll calculation reliability before further processing.

---

## **Tech Stack**

- Python 3.x  
- `pandas` for Excel processing  
- `unittest` for automated tests  

---

## **Goal**

- Ensure payroll data is consistent, correctly mapped, and fully validated before processing, reducing errors and increasing reliability.
