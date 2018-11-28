"""
Author: Darian Osahar Nwankwo
Date: November 15, 2018
Description: Represents a patient in the RxStore system
"""
import datetime


class Name:
    """Serves as a container for an entity's first, middle, and last name."""


    def __init__(self, first, last, middle=""):
        """Sets the object's first, middle, and last name

        Args:
            first_name (str): The patient's first name
            mid_name (str): The patient's middle name
            last_name (str): The patient's last name
        """
        self.first, self.middle, self.last = first, middle, last


    def __str__(self):
        """Returns the object's full name."""
        return "%s %s %s" % (self.first, self.middle, self.last)

class Contact:
    """Serves as a container for an entity's contact information."""


    def __init__(self, street_address, state, city, zip_code, country, email, phone_number):
        """Sets the object's street address, city, zip, country, email, phone number

        Args:
            street_address (:obj:`list` of :obj:`str`):  The patient's street address(es)
            state (str):  The patient's state of residence
            city (str):  The patient's city of residence
            zip_code (str):  The patient's zip code of residence
            country (str):  The patient's country of residence
            email (str):  The patient's email address
            phone_number (str): The patient's phone number
        """
        self.street_address, self.state, self.city, self.zip_code = street_address, state, city, zip_code
        self.country, self.email, self.phone_number =  country, email, phone_number


    def __str__(self):
        """Returns an easy to read representation of the contact information."""
        addresses = "\n".join(self.street_address)
        return "{}\n{}, {}, {}, {}\n{}\n{}".format(
            addresses, self.city, self.state, self.country, self.zip_code, self.phone_number, self.email
            )


class Date:
    """Simply stores a month, day, and year."""

    def __init__(self, month, day, year):
        """Sets the object's month, day, and year

        Args:
            month (str): The object's month
            day (str): The object's day
            year (str): The object's year
        """
        self.month, self.day, self.year = month, day, year




class Patient:
    """Stores relevant information about patients."""


    def __init__(self, name, birthdate, gender, contact, insurance_contact, conditions):
        """Sets the patient's information

        Args:
            name (:obj:`Name`): An object holding the patient's name
            birthdate (:obj:`Date`):  The patient's date of birth
            gender (str): The patient's gender
            contact (:obj:`Contact`): An object holding the patient's contact information
            insurance_contact (:obj:`Contact`): An object holding the patient's insurance company's contact information
            conditions (:obj:`list` of :obj:`str`): The patient's conditions
        """
        self.name = name
        self.birthdate, self.gender  = birthdate, gender
        self.contact, self.insurance_contact = contact, insurance_contact
        self.conditions = conditions

    
    def __str__(self):
        return self.name.__str__() + "\n" + self.contact.__str__()



if __name__ == "__main__":
    from hashlib import sha1
    gender = "male"
    name = Name("Darian", "Osahar", "Nwankwo")
    contact = Contact(["291 East Mangle Road"], "Georgia", "Atlanta", "30314", "USA", "email@gmail.com", "404-291-2099")
    birthdate = Date("June", "14", "1985")
    insurance_contact = contact
    conditions = ["Asthma", "Seizures", "Sickle Cell Disease"]
    darian = Patient(name, birthdate, gender, contact, insurance_contact, conditions)

    print(sha1(bytes(darian.__str__(), "ascii")).hexdigest())
    # print("Hashed Value of Darian (Patient Object): {}".format(hash(darian)))
