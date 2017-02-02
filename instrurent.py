def validEmail(n):
    '''takes valid email address'''
    n = n.lower().replace(" ", "")
    if "@" and ".com" in n:
        return n
    else:
        return ("Invalid")


def test_validEmail():
    assert validEmail("onna@gmail.com") == "onna@gmail.com"
    assert validEmail("onna") == "Invalid"
    assert validEmail("onna@gmail.com") != "Invalid"


def test_validEmail_uppercase():
    assert validEmail("ONNA@GMAIL.COM") == "onna@gmail.com"


if __name__ == '__main__':
    # user = input("Customer or Employee?").lower().strip()
    userEmail = input("Enter your email address: ")
    print(validEmail(userEmail))
