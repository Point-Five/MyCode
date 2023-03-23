class Validator():
    """A class that allows for data validation."""

    def __init__(self):
        """The constructor for intializing the validator class."""

    def listOfUsaStates(self):
        """Returns a dictionary list of all 50 states and their abbreviations"""
        usa_states = [{'state': "Alabama", 'abbreviation': "AL"},
                      {'state': "Alaska", 'abbreviation': "AK"},
                      {'state': "Arizona", 'abbreviation': "AZ"},
                      {'state': "Arkansas", 'abbreviation': "AR"},
                      {'state': "California", 'abbreviation': "CA"},
                      {'state': "Colorado", 'abbreviation': "CO"},
                      {'state': "Connecticut", 'abbreviation': "CT"},
                      {'state': "Delaware", 'abbreviation': "DE"},
                      {'state': "Florida", 'abbreviation': "FL"},
                      {'state': "Georgia", 'abbreviation': "GA"},
                      {'state': "Hawaii", 'abbreviation': "HI"},
                      {'state': "Idaho", 'abbreviation': "ID"},
                      {'state': "Illinois", 'abbreviation': "IL"},
                      {'state': "Indiana", 'abbreviation': "IN"},
                      {'state': "Iowa", 'abbreviation': "IA"},
                      {'state': "Kansas", 'abbreviation': "KS"},
                      {'state': "Kentucky", 'abbreviation': "KY"},
                      {'state': "Louisiana", 'abbreviation': "LA"},
                      {'state': "Maine", 'abbreviation': "ME"},
                      {'state': "Maryland", 'abbreviation': "MD"},
                      {'state': "Massachusetts", 'abbreviation': "MA"},
                      {'state': "Michigan", 'abbreviation': "MI"},
                      {'state': "Minnesota", 'abbreviation': "MN"},
                      {'state': "Mississippi", 'abbreviation': "MS"},
                      {'state': "Missouri", 'abbreviation': "MO"},
                      {'state': "Montana", 'abbreviation': "MT"},
                      {'state': "Nebraska", 'abbreviation': "NE"},
                      {'state': "Nevada", 'abbreviation': "NV"},
                      {'state': "New Hampshire", 'abbreviation': "NH"},
                      {'state': "New Jersey", 'abbreviation': "NJ"},
                      {'state': "New Mexico", 'abbreviation': "NM"},
                      {'state': "New York", 'abbreviation': "NY"},
                      {'state': "North Carolina", 'abbreviation': "NC"},
                      {'state': "North Dakota", 'abbreviation': "ND"},
                      {'state': "Ohio", 'abbreviation': "OH"},
                      {'state': "Oklahoma", 'abbreviation': "OK"},
                      {'state': "Oregon", 'abbreviation': "OR"},
                      {'state': "Pennsylvania", 'abbreviation': "PA"},
                      {'state': "Rhode Island", 'abbreviation': "RI"},
                      {'state': "South Carolina", 'abbreviation': "SC"},
                      {'state': "South Dakota", 'abbreviation': "SD"},
                      {'state': "Tennessee", 'abbreviation': "TN"},
                      {'state': "Texas", 'abbreviation': "TX"},
                      {'state': "Utah", 'abbreviation': "UT"},
                      {'state': "Vermont", 'abbreviation': "VT"},
                      {'state': "Virginia", 'abbreviation': "VA"},
                      {'state': "Washington", 'abbreviation': "WA"},
                      {'state': "West Virginia", 'abbreviation': "WV"},
                      {'state': "Wisconsin", 'abbreviation': "WI"},
                      {'state': "Wyoming", 'abbreviation': "WY"},
                      {'state': "District of Columbia", 'abbreviation': "DC"}]
        return usa_states

    def validateAddressLine(self, passed_value):
        """Validates that the passed value meets the parameters for inserting an address.
        Arguments:
            The variable to be tested as the address line.
        Returns:
            True or False Boolean"""
        if len(passed_value) <= 50:
            counter = 0
            bad_char = ["!", "\"", "\'", "@", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", ";", "[", "]", "{", "}"]
            for character in passed_value:
                if character not in bad_char:
                    if character.isalnum():
                        counter = counter + 1
                else:
                    print("The address contained a bad character.")
                    return False
            test_alnum = len(passed_value) // 2
            if counter > test_alnum:
                return True
            else:
                print("The address must primarily contain alphanumeric characters.")
                return False
        else:
            print("The length of the address line was longer than 46 characters.")
            return False

    def validateCityName(self, passed_value):
        """Validates the value of a city.
        Arguments:
            The variable that will have a city name validated.
        Returns:
            True or False Boolean"""
        # USPS has a city value max length of 50 characters so we will use this for length checking.
        if len(passed_value) <= 50:
            counter = 0
            for character in passed_value:
                if character.isalpha():
                    counter = counter + 1
                elif character == " " or character == "'":
                    continue
                else:
                    print("The city name contained a variable that was not alphanumeric, a space character, or a single quote.")
                    return False
            test_alpha = len(passed_value) // 2
            if counter > test_alpha:
                return True
            else:
                print("The city name must primarily be made up of upper case and lower case letters.")
                return False
        else:
            print("The length of the city is longer than 50 characters.")
            return False

    def validateCompanyName(self, passed_value):
        """Validates the name is of correct length and characters
        Arguments:
            The passed company name to check.
        Returns:
            True or False Boolean"""
        if len(passed_value) <= 50:
            return True
        else:
            print("Length Error: The length of the company name is greater than 50 characters.")
            return False

    def validateEmailAddress(self, passed_value):
        """Validates that the passed value is a valid email address.
        Arguments:
            An email address that will be parameter checked.
        Returns:
            True or False Boolean"""
        # Length parameters are based on RFC3696 Errata ID 1690.
        if len(passed_value) <= 254:
            bad_char = ["!", "\"", "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]
            # Limit the split to two strings.
            email = passed_value.split("@")
            if len(email) != 2:
                print("Email syntax is invalid")
                return False
            # Validate the local part of the email.
            local_part = email[0]
            if len(local_part) <= 64:
                for character in local_part:
                    if character not in bad_char:
                        continue
                    else:
                        print("Email contained a bad character.")
                        return False
            else:
                print("The email contains too many characters.")
                return False
            # Validate the domain part of the email.
            domain_part = email[1]
            for character in domain_part:
                if character not in bad_char:
                    continue
                else:
                    print("Email domain contained a bad character.")
                    return False
        else:
            print("The email contains too many characters.")
            return False
        return True

    def validatePersonsName(self, passed_value):
        """Validates that the passed name is of valid characters
        Arguments:
            A variable that is passed and checked for alphabetic letters, single quotations, or hyphens.
        Returns:
            True or False Boolean"""
        if len(passed_value) <= 50:
            counter = 0
            for character in passed_value:
                if character.isalpha():
                    counter = counter + 1
                elif character == "'" or character == "-" or character == " ":
                    continue
                else:
                    print("You entered %s in the name which is an invalid character.", character)
                    return False
            test_alpha = len(passed_value) // 2
            if counter > test_alpha:
                return True
            else:
                print("The name must primarily be made up of upper case characters.")
                return False
        else:
            print("Length error: name is longer than 50 characters.")
            return False

    def validatePhoneNumber(self, passed_value):
        """Validates that the passed value is of the correct parameters for a phone number.
        Arguments:
            The phone number being checked.
        Returns:
            True or False Boolean"""
        if len(passed_value) == 12:
            for character in passed_value:
                if character.isdigit() or character == "-":
                    continue
                else:
                    print("Phone number contains an invalid character.")
            phone_number = passed_value.split("-")
            if len(phone_number) != 3:
                print("Phone number must have a syntax of xxx-xxx-xxxx")
                return False
            if len(phone_number[0]) != 3 or not phone_number[0].isdigit():
                return False
            if len(phone_number[1]) != 3 or not phone_number[1].isdigit():
                return False
            if len(phone_number[2]) != 4 or not phone_number[2].isdigit():
                return False
        else:
            print("Phone number is not of correct length. The phone number must be entered in the following format: xxx-xxx-xxxx")
            return False
        return True

    def validateStateAbbreviation(self, passed_value):
        """Validates that the passed abbreviation is one of the United States two character codes.
        Arguments:
            A variable that passes a value to be checked for one of the two letter codes of a United State's State.
        Returns:
            True or False Boolean"""
        if len(passed_value) == 2:
            states = self.listOfUsaStates()
            for state in states:
                if state['abbreviation'] == passed_value.upper():
                    return True
            return False
        else:
            return False

    def validateZipCode(self, passed_value):
        """Validates that value passsed is a whole number that is either 4 or 5 digits long
        Returns:
            True or False Boolean"""
        if passed_value.isdigit():
            if len(passed_value) == 4 or len(passed_value) == 5:
                return True
            else:
                return False
        else:
            return False