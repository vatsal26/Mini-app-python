"""for regex module"""
import re
"""Loads all the functions from the function file"""
from functions import *
"""Imports Employee class"""
from Employeeclass import *
"""imports all the function files"""
from mailCheck import mailCheck

class Error(Exception):
    """Raises error if the file is not present"""
    pass
class MailError(Exception):
    """Raises error if the main.id is not in proper format"""
    pass
class PhoneError(Exception):
    """Raises error if phone number is of less than 10 digits"""
    pass
while True:
    print("Press 1 to view Employees : ")
    print("Press 2 to view all the keys of json file : ")
    print("Press 3 to view all the values of json file : ")
    print("Press 4 convert json data to dictionary : ")
    print("Press 5 to get employee with minimum and maximum age : ")
    print("Press 6 to view employees who joined previous month : ")
    print("Press 7 to view employees who are in Baroda : ")
    print("Press 8 to delete the details of employee who belongs to Chennai : ")
    print("Press 9 to add new employee : ")
    print("Press 0 to exit : ")
    try:
        choice = int(input())
        if choice == 1:
            ReadJson()
        elif choice == 2:
            GetKeys()
        elif choice == 3:
            GetValues()
        elif choice == 4:
            JsonToDict()
        elif choice == 5:
            MaxMinAge()
        elif choice == 6:
            PrevMonth()
        elif choice == 7:
            BarodaLocation()
        elif choice == 8:
            DelEmpChen()
        elif choice == 9:
            try:
                with open('Employee.json', 'r',encoding="utf-8") as f:
                    # Load JSON data from file
                    employee_data = json.load(f)
                a = input("Enter eight digit P.S. number of the new Employee : ")
                pattern = re.compile(r'\s+')
                finalps = re.sub(pattern, '', a)

                try:
                    if len(finalps) != 8:
                        raise Error
                    else:
                        b = input("Enter name of new Employee : ")
                        c = input("Date of birth in YYYY-MM-DD format only : ")
                        d = input("Date of joining in YYYY-MM-DD format only : ")
                        e = input("Date of Regignation in YYYY-MM-DD format only : ")
                        f = input("Email.id : ")
                        try:
                            mailCheck(f)
                            if(mailCheck(f)==False):
                                raise MailError
                            else:
                                g = input("Cell number")
                                pattern = re.compile(r'\s+')
                                finalph = re.sub(pattern, '', g)
                                try:
                                    if len(finalph)!=10:
                                        raise PhoneError
                                    else:
                                        h = input("Designation : ")
                                        i = input("Business Unit : ")
                                        j = input("Base location : ")
                                        k = input("Grade")
                                        try:
                                            integer = int(k)  # Try to convert the input to an integer
                                            if integer != int(integer):
                                                raise ValueError
                                            else:
                                                new_employee = Employee(finalps, b, c, d, e, f, finalph, h, i, j,integer)

                                                # Add the new employee data to the existing employee data
                                                employee_data['employee'].append(new_employee.to_dict())

                                                # Save the updated JSON data to the file
                                                with open('Employee.json', 'w',encoding="utf-8") as f:
                                                    json.dump(employee_data, f)
                                                print("The details of the new employee have been added to the file.")
                                        except ValueError:
                                            print("----------Grade should be in integer format only----------")
                                except PhoneError:
                                    print("----------Phone number should be of 10 digits only----------")
                        except MailError:
                            print("----------Mail id is not in proper format----------")
                except Error:
                    print("----------P.S number should be equal to 8----------")
            except FileNotFoundError:
                print("File Not Found")
        elif choice == 0:
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Enter a valid input------------------")
