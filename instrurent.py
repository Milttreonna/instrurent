def validEmail(e):
    '''(str)->str

    Takes user's email and checks to see if it's valid

    >>>validEmail('person123@email.com')
    'Valid email'
    >>>validEmail('person123')
    'Invalid email'
    '''
    e = e.lower().replace(" ", "")
    if "@" and ".com" in e:
        return ("Valid email")
    else:
        return ("Invalid email")


def show_inventory(i):
    with open('inventory.txt', 'r') as file:
        inventory = file.read().split()


def rent_price(price):
    '''(str)->int

    Takes the instrument's price and gets 13 percent of it
     '''
    rent = round(price * .13, 2)
    return rent


def add_tax():
    ''' '''
    rent = rent_price(price)
    tax = rent * .07
    rent += tax
    total = round(rent, 2)
    return total


if __name__ == '__main__':
    # user = input("Customer or Employee?").lower().strip()
    userEmail = input("Enter your email address: ")
    print(validEmail(userEmail))
    userRent = input("What instrument would you like to rent?")
    print(rent_price(userRent))
    # print(rent_price(userRent))
