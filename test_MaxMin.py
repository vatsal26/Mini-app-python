import json
import pytest
from datetime import datetime, timedelta

def test_MaxMinAge():
    # Open JSON file
    with open('Employee.json', 'r') as f:
        # Load JSON data from file
        employee_data = json.load(f)

    # Calculate the age of each employee
    max_age = None
    max_age_employee = None
    min_age = None
    min_age_employee = None

    for employee in employee_data['employee']:
        dob = datetime.strptime(employee['DOB'], '%Y-%m-%d')
        today = datetime.today()
        age = (today - dob) / timedelta(days=365.2425)

        if max_age is None or age > max_age:
            max_age = age
            max_age_employee = employee
        if min_age is None or age < min_age:
            min_age = age
            min_age_employee = employee

    # Assert that the employees with maximum and minimum age are as expected
    assert max_age_employee['Employee Name'] == "Shubham Patil"
    assert min_age_employee['Employee Name'] == "ShivaPradeep"
if __name__ == "__MaxMin__":
    pytest.MaxMin()