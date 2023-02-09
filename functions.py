"""imports json package"""
import json
from datetime import datetime, timedelta

def ReadJson():
    """Pylint: Missing function or method docstring"""
    try:
        # Open JSON file
        with open('Employee.json', 'r',encoding="utf-8") as f:
            # Load JSON data from file
            employee_data = json.load(f)

        # Access the employee data
        for employee in employee_data['employee']:
            print("PS.No.:", employee['PS.No.'])
            print("Employee Name:", employee['Employee Name'])
            print("DOB:", employee['DOB'])
            print("DOJ:", employee['DOJ'])
            print("DOR:", employee['DOR'])
            print("Email:", employee['Email'])
            print("Contact:", employee['Contact'])
            print("Designation:", employee['Designation'])
            print("Business Unit:", employee['Business Unit'])
            print("Base Location:", employee['Base Location'])
            print("LTTS Grade:", employee['LTTS Grade'])
            print("---")
    except FileNotFoundError:
        print("File not found")

def GetKeys():
    """Function to get all the keys"""
    # Open JSON file
    try:
        with open('Employee.json', 'r',encoding="utf-8") as f:
            # Load JSON data from file
            employee_data = json.load(f)

        # Print the keys
        for employee in employee_data['employee']:
            print("Keys:", employee.keys())
            print("---")
    except FileNotFoundError:
        print("File not found")

def GetValues():
    """Function to get  all the values"""
    try:
        with open('Employee.json', 'r',encoding="utf-8") as f:
            # Load JSON data from file
            employee_data = json.load(f)

            # Print the values
        for employee in employee_data['employee']:
            print("Values:", employee.values())
            print("---")
    except FileNotFoundError:
        print("File not found")

def JsonToDict():
    """Function to convert Json data to dictionary"""
    # Open JSON file
    try:
        with open('Employee.json', 'r',encoding="utf-8") as f:
            # Load JSON data from file
            employee_data = json.load(f)

        # Convert JSON data to dictionary
        employee_dict = dict(employee_data)

        # Print the dictionary
        print(employee_dict)
    except FileNotFoundError:
        print("File not found")

def MaxMinAge():
    """Function to get max and min age from all the employees"""
    try:
        # Open JSON file
        with open('Employee.json', 'r',encoding="utf-8") as f:
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

        # Print the employees with maximum and minimum age
        print("Employee with maximum age:")
        print("Employee Name:", max_age_employee['Employee Name'])
        print("DOB:", max_age_employee['DOB'])
        print("Age:", max_age)
        print("---")
        print("Employee with minimum age:")
        print("Employee Name:", min_age_employee['Employee Name'])
        print("DOB:", min_age_employee['DOB'])
        print("Age:", min_age)
    except FileNotFoundError:
        print("File not found")

def PrevMonth():
    """Function to check for the employee who joined previous month"""
    try:
        with open('Employee.json', 'r',encoding="utf-8") as f:
            # Load JSON data from file
            employee_data = json.load(f)

        # Get the current date and the date of one month ago
        now = datetime.now()
        previous_month = now - timedelta(days=30)

        # Initialize a list to store the details of employees who joined in the previous month
        employees = []

        # Loop through the employee data
        for employee in employee_data['employee']:
            # Get the date of joining of the current employee
            doj = datetime.strptime(employee['DOJ'], '%Y-%m-%d')

            # Check if the date of joining is in the previous month
            if previous_month <= doj < now:
                employees.append(employee)

        # Check if any employee joined in the previous month
        if len(employees) > 0:
            # Print the details of employees who joined in the previous month
            print("Details of employees who joined in the previous month:")
            for employee in employees:
                print("Employee Name:", employee['Employee Name'])
                print("DOJ:", employee['DOJ'])
                print("Base Location:", employee['Base Location'])
                print("-----------------------------")
        else:
            print("NULL")
    except FileNotFoundError:
        print("File not found")

# Function to check Employees who location is "Baroda"

def BarodaLocation():
    """Function to look for employees whose location is in Baroda"""
    try:
        with open('Employee.json', 'r',encoding="utf-8") as f:

            employee_data = json.load(f)

        # Find the employees who belong to the "Baroda" location
        baroda_employees = []

        for employee in employee_data['employee']:
            if employee['Base Location'] == 'Baroda':
                baroda_employees.append(employee)

        # Print the employees who belong to the "Baroda" location
        print("Employees who belong to the Baroda location:")
        for employee in baroda_employees:
            print("Employee Name:", employee['Employee Name'])
            print("Base Location:", employee['Base Location'])
            print("---")
    except FileNotFoundError:
        print("File not found")

def DelEmpChen():
    """Function to delete an employee whose location is in Chennai"""
    try:
        # Open JSON file
        with open('Employee.json', 'r',encoding="utf-8") as f:
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
            with open('Employee.json', 'w',encoding="utf-8") as f:
                json.dump(employee_data, f)

            print("The record of the employee has been deleted.")
        else:
            print("No employee with location 'Chennai' was found.")
    except FileNotFoundError:
        print("File not found")
