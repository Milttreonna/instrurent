from instrurent import *
from core import *
from openedFiles import *

import sys


# def test_validEmail():
#     '''tests for validEmail() '''
#     assert validEmail("person123@email.com") == "Valid email"
#     assert validEmail("person") == "Invalid email"
#     assert validEmail("person123@email.com") != "Invalid email"
#
#
# def test_validEmail_uppercase():
#     ''' tests'''
#     assert validEmail("PERSON123@EMAIL.COM") == "Valid email"
#
#
# def test_validEmail_spaces():
#     ''' tests'''
#     assert validEmail("person123 @email .com") == "Valid email"
#
#
# def test_rent_price():
#     assert rent_price(100) == 13.0
#
#
# def test_rent_price_decimal():
#     assert rent_price(1342.30) == 174.5
def test_get_customer_total():
    assert get_customer_total(2, 269.99) == "$539.98"
    assert get_customer_total(-1, 269.99) == " "


def test_add_tax():
    assert add_tax(4.00) == 4.28


def test_add_tax_large():
    assert add_tax(534.99) == 572.44


def test_format_total_with_decimal():
    assert format_total(810.98) == "$810.98"


def test_format_total_without_decimal():
    ''' '''
    assert format_total(5040) == "$5040.00"
