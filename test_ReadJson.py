import json
import pytest

def test_ReadJson():
    try:
        # Open JSON file
        with open('Employee.json', 'r') as f:
            # Load JSON data from file
            employee_data = json.load(f)

        # Access the employee data
        for employee in employee_data['employee']:
            assert 'PS.No.' in employee
            assert 'Employee Name' in employee
            assert 'DOB' in employee
            assert 'DOJ' in employee
            assert 'DOR' in employee
            assert 'Email' in employee
            assert 'Contact' in employee
            assert 'Designation' in employee
            assert 'Business Unit' in employee
            assert 'Base Location' in employee
            assert 'LTTS Grade' in employee
    except FileNotFoundError:

        pytest.fail("File not found")


