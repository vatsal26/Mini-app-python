"""for abstract class"""
from abc import ABC

# Employee class
class Emp(ABC):
    """Employee class for static method"""
    @staticmethod
    def to_dict():
        """Static method"""
        pass

class Employee(Emp):
    """Employee class which inherits Emp"""
    def __init__(self, ps_no, name, dob, doj, dor, email, contact, designation, business_unit, base_location, ltts_grade):
        self.ps_no = ps_no
        self.name = name
        self.dob = dob
        self.doj = doj
        self.dor = dor
        self.email = email
        self.contact = contact
        self.designation = designation
        self.business_unit = business_unit
        self.base_location = base_location
        self.ltts_grade = ltts_grade

    def to_dict(self):
        return {
            "PS.No.": self.ps_no,
            "Employee Name": self.name,
            "DOB": self.dob,
            "DOJ": self.doj,
            "DOR": self.dor,
            "Email": self.email,
            "Contact": self.contact,
            "Designation": self.designation,
            "Business Unit": self.business_unit,
            "Base Location": self.base_location,
            "LTTS Grade": self.ltts_grade
        }

