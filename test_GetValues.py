import json
import pytest


def GetValues():
    # Open JSON file
    try:
        with open('Employee.json', 'r') as f:
            # Load JSON data from file
            employee_data = json.load(f)

            # Print the values
        for employee in employee_data['employee']:
            print("Values:", employee.values())
            print("---")
    except FileNotFoundError:
        print("File not found")


def test_GetValues():
    GetValues()
    assert True
if __name__ == '__main__':
     pytest.main()
