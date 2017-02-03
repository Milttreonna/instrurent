from instrurent import *


def test_validEmail():
    '''tests for validEmail() '''
    assert validEmail("person123@email.com") == "Valid email"
    assert validEmail("person") == "Invalid email"
    assert validEmail("person123@email.com") != "Invalid email"


def test_validEmail_uppercase():
    ''' tests'''
    assert validEmail("PERSON123@EMAIL.COM") == "Valid email"


def test_validEmail_spaces():
    ''' tests'''
    assert validEmail("person123 @email .com") == "Valid email"


def test_rent_price():
    assert rent_price(100) == 13.0
    # assert rent_price(drums) == 118.3


def test_rent_price_decimal():
    assert rent_price(1342.30) == 174.5


def test_add_tax():
    ''''''


def test_rent_total():
    ''' tests for rent_total '''


def test_full_total():
    ''' '''


def rounded_total():
    ''' '''


def test_formatted_total():
    ''' '''
