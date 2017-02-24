from instrurent import *
from core import *
from openedFiles import *
import sys


def test_get_customer_total():
    assert get_customer_total(2, 269.99) == "$539.98"
    assert get_customer_total(3, 269.99) == "$809.97"


def test_add_tax():
    assert add_tax(4.00) == 4.28


def test_add_tax_large():
    assert add_tax(534.99) == 572.44


def test_format_total_with_decimal():
    assert format_total(810.98) == "$810.98"


def test_format_total_without_decimal():
    ''' '''
    assert format_total(5040) == "$5040.00"
