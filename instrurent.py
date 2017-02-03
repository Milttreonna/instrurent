def validEmail(n):
    '''(str)->str

    Checks to see if email address is valid

    >>>validEmail('person123@email.com')
    'Valid email'

    >>>validEmail('person123')
    'Invalid email'

    '''
    n = n.lower().replace(" ", "")
    if "@" and ".com" in n:
        return ("Valid email")
    else:
        return ("Invalid email")


def test_validEmail():
    '''tests for validEmail() '''
    assert validEmail("onna@gmail.com") == "Valid email"
    assert validEmail("onna") == "Invalid email"
    assert validEmail("onna@gmail.com") != "Invalid email"


def test_validEmail_uppercase():
    ''' tests'''
    assert validEmail("ONNA@GMAIL.COM") == "Valid email"


def test_validEmail_spaces():
    ''' tests'''
    assert validEmail("onna @gmail .com") == "Valid email"


if __name__ == '__main__':
    user = input("Customer or Employee?").lower().strip()
    userEmail = input("Enter your email address: ")
    print(validEmail(userEmail))
