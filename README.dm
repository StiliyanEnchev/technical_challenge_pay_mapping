# Payroll Data Validator

Automated Python tests to ensure payroll data consistency and integrity across multiple sources.

---

## PROJECT OVERVIEW

This project validates payroll data between three sources:

- **GTN file** – Payroll input file  
- **Payrun file** – Processed payroll output  
- **mapping.json** – Defines how GTN pay elements map to Payrun columns  

The goal is to guarantee data integrity, accurate mappings, and reliable payroll calculations before further processing.

---

## FEATURES & CHECKS

Automated Python unit tests verify:

### 1. GTN File Validity
- Required headers exist and are in the correct order  
- No unexpected empty rows  

### 2. Mapping Accuracy
- All GTN pay elements are properly mapped  
- All Payrun pay elements have corresponding GTN mappings  

### 3. Data Integrity
- All pay element values are numeric  

---

## TECH STACK

- Python 3.x  
- `pandas` for Excel processing  
- `unittest` for automated tests  

---

## GOAL

Ensure payroll data is consistent, correctly mapped, and fully validated before processing, reducing errors and increasing reliability.
