import json
import pytest

def BarodaLocation():
    with open('Employee.json', 'r') as f:
        employee_data = json.load(f)

    baroda_employees = []
    for employee in employee_data:
        if employee['Base Location'] == 'Baroda':
            baroda_employees.append({'Base Location': employee['Base Location'], 'Employee Name': employee['Employee Name']})

    return baroda_employees

def test_BarodaLocation():
    employee_data = [
        {
            "PS.No.": "123456",
            "Employee Name": "Vatsal Shah",
            "DOB": "2000-07-26",
            "DOJ": "2022-12-26",
            "DOR": "NA",
            "Email": "vatsal@gmail.com",
            "Contact": "9999999999",
            "Designation": "Associate Engineer",
            "Business Unit": "DMS",
            "Base Location": "Baroda",
            "LTTS Grade": "2"
        },
        {
            "PS.No.": "234567",
            "Employee Name": "Shubham Patil",
            "DOB": "2000-07-25",
            "DOJ": "2022-12-26",
            "DOR": "NA",
            "Email": "Shubham@gmail.com",
            "Contact": "7777777777",
            "Designation": "Associate Engineer",
            "Business Unit": "DMS",
            "Base Location": "Baroda",
            "LTTS Grade": "2"
        },
        {
            "PS.No.": "3456789",
            "Employee Name": "ShivaPradeep",
            "DOB": "2001-01-01",
            "DOJ": "2023-01-26",
            "DOR": "NA",
            "Email": "ShivaP@gmail.com",
            "Contact": "5555555555",
            "Designation": "Associate Engineer",
            "Business Unit": "DMS",
            "Base Location": "Chennai",
            "LTTS Grade": "2"
        }
    ]

    with open("Employee.json", "w") as f:
        f.write(json.dumps(employee_data))

    expected_output = [{'Base Location': 'Baroda', 'Employee Name': 'Vatsal Shah',}, {'Base Location': 'Baroda', 'Employee Name': 'Shubham Patil'}]
    assert BarodaLocation() == expected_output

if __name__ == "__BarodaLocation__":
    pytest.BarodaLocation()
