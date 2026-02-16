This project validates payroll data consistency between three sources:

GTN file - payroll input file
Payrun file - processed payroll output
mapping.json - configuration file defining how GTN pay elements map to Payrun columns

The system uses automated Python unit tests to verify:

The GTN file is a valid Excel file:

Required headers exist and are in correct order
No unexpected empty rows exist
All GTN pay elements are properly mapped
All Payrun pay elements have corresponding GTN mappings
Pay element values are numeric
The goal of the project is to ensure data integrity, mapping accuracy, and payroll calculation reliability before further processing.