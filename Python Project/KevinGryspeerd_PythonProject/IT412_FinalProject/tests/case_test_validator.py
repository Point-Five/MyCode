import unittest
from classes.validator import *

class CaseTestValidator(unittest.TestCase):

    def setUp(self):
        """Initalizes an instance of the validator class."""
        self.test_validator = Validator()

    def test_getAddressLine_success(self):
        """Case Test to validate the parameter checking of an address line with success."""
        value_list = ["123 Main St.", "3838 Liverhois Rd."]
        for value in value_list:
            self.assertTrue(self.test_validator.validateAddressLine(value))

    def test_getAddressLine_failure(self):
        """Case test to validate that it will fail an address check if it does not meet the criteria."""
        value_list = ["  s ", "This is a really really really long address line that will not pass the test.", "This has bad characters <?"]
        for value in value_list:
            self.assertFalse(self.test_validator.validateAddressLine(value))

    def test_getCity_success(self):
        """Case tests the ability to parameter check a city name"""
        value_list = ["Algonac", "Clay", "Troy", "New Baltimore", "Chesterfield"]
        for value in value_list:
            self.assertTrue(self.test_validator.validateCityName(value))

    def test_getCity_failure(self):
        """Case tests the ability to detect incorrect city data."""
        value_list = ["a    3", "This is a really really really long city that will not pass the test", "city with ) special characters", "   f"]
        for value in value_list:
            self.assertFalse(self.test_validator.validateCityName(value))

    def test_getCompanyName_success(self):
        """Case tests the ability to parameter check the length of a company name."""
        value_list = ["asdasdasdasd ", " ads33' asda", "Kevin's awesome company"]
        for value in value_list:
            self.assertTrue(self.test_validator.validateCompanyName(value))

    def test_getCompanyName_failure(self):
        """Case tests the ability to paramter check teh lenght of a company name."""
        value = "This is a really really really long name for a company that will not meet the length requirements."
        self.assertFalse(self.test_validator.validateCompanyName(value))

    def test_getEmailAddress_success(self):
        """Case tests the ability to parameter check an email address successfully."""
        value_list = ["kevin@outlook.com", "kevin@walshcollege.edu", "testaccount@yahoo.com"]
        for value in value_list:
            self.assertTrue(self.test_validator.validateEmailAddress(value))

    def test_getEmailAddress_failure(self):
        """Case tests the ability to parameter check an email address and reject a failure."""
        value_list = ["kevin", "this is bad characters", "asdasdawdasdasasdasddasdawdawdadasdasdawdawdasdasdasdawawdawdasdasdasd@gmail.com"]
        for value in value_list:
            self.assertFalse(self.test_validator.validateEmailAddress(value))

    def test_getPersonsName_success(self):
        """Case tests the ability to parameter check a person's name successfully."""
        value_list = ["Kevin Gryspeerd", "kevin-test", "kev's test"]
        for value in value_list:
            self.assertTrue(self.test_validator.validatePersonsName(value))

    def test_getPersonsName_failure(self):
        """Case tests the ability to parameter check a person's name and reject failures."""
        value_list = ["21e", "   s", "kev&"]
        for value in value_list:
            self.assertFalse(self.test_validator.validatePersonsName(value))

    def test_getPhoneNumber_success(self):
        """Case tests the ability to parameter check a phone number successfully."""
        value_list = ["123-456-7890", "555-555-5555", "000-000-9999"]
        for value in value_list:
            self.assertTrue(self.test_validator.validatePhoneNumber(value))

    def test_getPhoneNumber_failure(self):
        """Case tests the ability to parameter check a phone number and reject incorrect syntax."""
        value_list = ["132--332-3333", "as3-333-3333", "7897897898", "1"]
        for value in value_list:
            self.assertFalse(self.test_validator.validatePhoneNumber(value))

    def test_getStateAbbreviation_success(self):
        """Case tests the ability to get a state successfully"""
        value_list = ["Mi", "sd", "ri", "dC"]
        for value in value_list:
            self.assertTrue(self.test_validator.validateStateAbbreviation(value))

    def test_getStateAbbreviation_failure(self):
        """Case tests the ability to ensure that values that should fail, fail."""
        value_list = ["asdas", "1", "ss", "22", "fs"]
        for value in value_list:
            self.assertFalse(self.test_validator.validateStateAbbreviation(value))

    def test_getZipCode_success(self):
        """Case tests the ability to get a 4 or 5 digit zip code."""
        value_list = ["1234", "2222", "12345", "00000"]
        for value in value_list:
            self.assertTrue(self.test_validator.validateZipCode(value))

    def test_getZipCode_failure(self):
        """Case tests the ability to error check the parameters of a zip code input"""
        value_list = ["aaaa", "ab12", "8asd", " "]
        for value in value_list:
            self.assertFalse(self.test_validator.validateZipCode(value))