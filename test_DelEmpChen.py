import json


def DelEmpChen():
    try:
        # Open JSON file
        with open('Employee.json', 'r') as f:
            # Load JSON data from file
            employee_data = json.load(f)

        # Find the index of the employee whose location is "Chennai"
        delete_index = None
        for i, employee in enumerate(employee_data['employee']):
            if employee['Base Location'] == 'Chennai':
                delete_index = i
                break

        # Delete the record of the employee
        if delete_index is not None:
            del employee_data['employee'][delete_index]

            # Save the updated JSON data to the file
            with open('Employee.json', 'w') as f:
                json.dump(employee_data, f)

            print("The record of the employee has been deleted.")
        else:
            print("No employee with location 'Chennai' was found.")
    except FileNotFoundError:
        print("File not found")


def test_DelEmpChen_file_found():
    # create a sample Employee.json file
    with open('Employee.json', 'w') as f:
        employee_data = {
            "employee": [
                {
                    "firstName": "John",
                    "lastName": "Doe",
                    "Base Location": "Chennai"
                },
                {
                    "firstName": "Anna",
                    "lastName": "Smith",
                    "Base Location": "Delhi"
                }
            ]
        }
        json.dump(employee_data, f)

    DelEmpChen()

    # check if the employee record has been deleted
    with open('Employee.json', 'r') as f:
        employee_data = json.load(f)
    assert len(employee_data['employee']) == 1
    assert employee_data['employee'][0]['Base Location'] == 'Delhi'


def test_DelEmpChen_file_not_found():
    result = DelEmpChen()
    assert result == "File not found"


def test_DelEmpChen_employee_not_found():
    # create a sample Employee.json file
    with open('Employee.json', 'w') as f:
        employee_data = {
            "employee": [
                {
                    "firstName": "John",
                    "lastName": "Doe",
                    "Base Location": "Delhi"
                },
                {
                    "firstName": "Anna",
                    "lastName": "Smith",
                    "Base Location": "Bangalore"
                }
            ]
        }
        json.dump(employee_data, f)

    DelEmpChen()

    # check if the employee record has been deleted
    with open('Employee.json', 'r') as f:
        employee_data = json.load(f)
    assert len(employee_data['employee']) == 2
