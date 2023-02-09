import json
import pytest

def JsonToDict():
    # Open JSON file
    try:
        with open('Employee.json', 'r') as f:
            # Load JSON data from file
            employee_data = json.load(f)

        # Convert JSON data to dictionary
        employee_dict = dict(employee_data)

        # Return the dictionary
        return employee_dict
    except FileNotFoundError:
        return "File not found"

def test_JsonToDict():
    # Prepare test data
    employee_data = {
        "employee": [
            {"PS.NO": "3456789", "Employee Name": "ShivaPradeep", "DOB": "2001-01-01", "DOJ":"2023-01-26", "DOR":"NA", "Email":"ShivaP@gmail.com", "Contact":"5555555555", "Designation":"Associate Engineer", "Bussiness Unit":"DMS", "Base Location": "Chennai", "LTTS Grade": "2"},
            {"PS.NO": "123456", "Employee Name": "Vatsal Shah", "DOB": "2000-07-26", "DOJ":"2022-12-26", "DOR":"NA", "Email":"vatsal@gmail.com" , "Contact":"9999999999", "Designation":"Associate Engineer", "Bussiness Unit":"DMS", "Base Location": "Baroda", "LTTS Grade": "2"},
            {"PS.NO": "234567", "Employee Name": "Shubham Patil", "DOB": "2000-07-25", "DOJ":"2022-12-26", "DOR":"NA", "Email":"Shubham@gmail.com", "Contact":"7777777777", "Designation":"Associate Engineer", "Bussiness Unit":"DMS", "Base Location": "Chennai", "LTTS Grade": "2"}
        ]
    }

    # Save the test data to a file
    with open('Employee.json', 'w') as f:
        json.dump(employee_data, f)

    # Call the function to be tested
    employee_dict = JsonToDict()

    # Verify the result
    expected_dict = {'employee': [{"PS.NO": "3456789", "Employee Name": "ShivaPradeep", "DOB": "2001-01-01", "DOJ":"2023-01-26", "DOR":"NA", "Email":"ShivaP@gmail.com", "Contact":"5555555555", "Designation":"Associate Engineer", "Bussiness Unit":"DMS", "Base Location": "Chennai", "LTTS Grade": "2"},
            {"PS.NO": "123456", "Employee Name": "Vatsal Shah", "DOB": "2000-07-26", "DOJ":"2022-12-26", "DOR":"NA", "Email":"vatsal@gmail.com" , "Contact":"9999999999", "Designation":"Associate Engineer", "Bussiness Unit":"DMS", "Base Location": "Baroda", "LTTS Grade": "2"},
            {"PS.NO": "234567", "Employee Name": "Shubham Patil", "DOB": "2000-07-25", "DOJ":"2022-12-26", "DOR":"NA", "Email":"Shubham@gmail.com", "Contact":"7777777777", "Designation":"Associate Engineer", "Bussiness Unit":"DMS", "Base Location": "Chennai", "LTTS Grade": "2"}]}
    assert employee_dict == expected_dict
if __name__ == "__JsonToDict__":
    pytest.JsonToDict()