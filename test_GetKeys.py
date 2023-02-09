import json
import io
import sys

def GetKeys():
    # Open JSON file
    try:
        with open('Employee.json', 'r') as f:
            # Load JSON data from file
            employee_data = json.load(f)

        # Print the keys
        for employee in employee_data['employee']:
            print("Keys:", employee.keys())
            print("---")
    except FileNotFoundError:
        print("File not found")


def test_GetKeys_file_found():
    with open('Employee.json', 'w') as f:
        employee_data = {
            "employee": [
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
                }
            ]
        }
        json.dump(employee_data, f)

    captured_output = io.StringIO()
    sys.stdout = captured_output

    GetKeys()
    sys.stdout = sys.__stdout__

    result = captured_output.getvalue()
    expected_output = ("Keys: dict_keys(['PS.No.', 'Employee Name', 'DOB', 'DOJ', 'DOR', 'Email', ""'Contact', 'Designation', 'Business Unit', 'Base Location', 'LTTS Grade'])\n"'---\n'"Keys: dict_keys(['PS.No.', 'Employee Name', 'DOB', 'DOJ', 'DOR', 'Email', ""'Contact', 'Designation', 'Business Unit', 'Base Location', 'LTTS Grade'])\n"'---\n')
    assert result == expected_output


