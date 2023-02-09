import json

# Employee data

# Define employee data
employee_data = [
    {
        "PS.No.": "12345678",
        "Employee Name": "Vatsal Shah",
        "DOB": "2000-07-26",
        "DOJ": "2022-12-26",
        "DOR": "NA",
        "Email": "vatsal@ltts.com",
        "Contact": "9999999999",
        "Designation": "Associate Engineer",
        "Business Unit": "DMS",
        "Base Location": "Baroda",
        "LTTS Grade": "2"
    },
    {
        "PS.No.": "23456789",
        "Employee Name": "Shubham Patil",
        "DOB": "2000-07-25",
        "DOJ": "2022-12-26",
        "DOR": "NA",
        "Email": "Shubham@ltts.com",
        "Contact": "12312312",
        "Designation": "Associate Engineer",
        "Business Unit": "DMS",
        "Base Location": "Baroda",
        "LTTS Grade": "2"
    },
{
        "PS.No.": "36547896",
        "Employee Name": "ShivaPradeep",
        "DOB": "2001-01-01",
        "DOJ": "2023-01-26",
        "DOR": "NA",
        "Email": "ShivaP@ltts.com",
        "Contact": "8978458795",
        "Designation": "Associate Engineer",
        "Business Unit": "DMS",
        "Base Location": "Chennai",
        "LTTS Grade": "2"
    }
]

# Create JSON file
with open('Employee.json', 'w') as f:
    json.dump({"employee": employee_data}, f)
