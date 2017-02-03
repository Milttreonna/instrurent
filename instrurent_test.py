from instrurent import *


def test_validEmail():
    '''tests for validEmail() '''
    assert validEmail("person123@email.com") == "Valid email"
    assert validEmail("person") == "Invalid email"
    assert validEmail("person123@email.com") != "Invalid email"


def test_validEmail_uppercase():
    ''' tests'''
    assert validEmail("PERSON123@GMAIL.COM") == "Valid email"


def test_validEmail_spaces():
    ''' tests'''
    assert validEmail("person123 @email .com") == "Valid email"


if __name__ == '__main__':
    user = input("Customer or Employee?").lower().strip()
    userEmail = input("Enter your email address: ")
    print(validEmail(userEmail))
