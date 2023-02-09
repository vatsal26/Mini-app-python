import json
import sys
import pytest
from io import StringIO

def ReadJson():
    try:
        # Open JSON file
        with open('Employee.json', 'r') as f:
            # Load JSON data from file
            employee_data = json.load(f)
        # Print the employee data
        for employee in employee_data['employee']:
            print("PS.No.:", employee["PS.No."])
            print("Employee Name:", employee["Employee Name"])
            print("DOB:", employee["DOB"])
            print("DOJ:", employee["DOJ"])
            print("DOR:", employee["DOR"])
            print("Email:", employee["Email"])
            print("Contact:", employee["Contact"])
            print("Designation:", employee["Designation"])
            print("Business Unit:", employee["Business Unit"])
            print("Base Location:", employee["Base Location"])
            print("LTTS Grade:", employee["LTTS Grade"])
            print("---")
    except Exception as e:
        print("Error:", e)

def test_ReadJson():
    # Test when the file is found
    with open('Employee.json', 'w',encoding="utf-8") as f:
        f.write(
            '{"employee": [{"PS.No.": "1", "Employee Name": "John Doe", "DOB": "01-01-1990", "DOJ": "01-01-2010", "DOR": "", "Email": "johndoe@example.com", "Contact": "1234567890", "Designation": "Manager", "Business Unit": "Unit 1", "Base Location": "Location 1", "LTTS Grade": "L1"}]}')

    expected_output = "PS.No.: 1\nEmployee Name: John Doe\nDOB: 01-01-1990\nDOJ: 01-01-2010\nDOR: \nEmail: johndoe@example.com\nContact: 1234567890\nDesignation: Manager\nBusiness Unit: Unit 1\nBase Location: Location 1\nLTTS Grade: L1\n---\n"

    captured_output = StringIO()
    sys.stdout = captured_output

    try:
        ReadJson()
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")

    sys.stdout = sys.__stdout__

    assert captured_output.getvalue() == expected_output

    # Test when the file is not found
    try:
        ReadJson()
    except Exception as e:
        assert str(e) == "Error: [Errno 2] No such file or directory: 'Employee.json'"
