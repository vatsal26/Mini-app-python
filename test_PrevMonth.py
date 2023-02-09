import datetime
import json
import pytest
from datetime import timedelta

def test_PrevMonth():
    try:
        with open('Employee.json', 'r') as f:
            # Load JSON data from file
            employee_data = json.load(f)

        # Get the current date and the date of one month ago
        now = datetime.datetime.now()
        previous_month = now - timedelta(days=30)

        # Initialize a list to store the details of employees who joined in the previous month
        employees = []

        # Loop through the employee data
        for employee in employee_data['employee']:
            # Get the date of joining of the current employee
            doj = datetime.datetime.strptime(employee['DOJ'], '%Y-%m-%d')

            # Check if the date of joining is in the previous month
            if doj >= previous_month and doj < now:
                employees.append(employee)

        # Check if any employee joined in the previous month
        assert len(employees) > 0, "NULL"
    except FileNotFoundError:
        assert False, "File not found"


if __name__ == "__main__":
    pytest.main()
