def validEmail(e):
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


def rent_price(price):
    ''' '''


if __name__ == '__main__':
    user = input("Customer or Employee?").lower().strip()
    userEmail = input("Enter your email address: ")
    print(validEmail(userEmail))
