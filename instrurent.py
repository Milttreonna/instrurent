with open("emails.csv", "r") as emailFile:
    emails = emailFile.read().split()
with open("inventory.csv", 'r') as inventoryFile:
    inventory = inventoryFile.read().split()


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
        if e in emails:
            print("Previous user")
        else:
            with open("emails.csv", "a") as emailFile:
                emailFile.write(e)
        return ("Valid email")
    else:
        return ("Invalid email")


def rent_price(price):
    '''(str)->int

    Takes the instrument's price and gets 13 percent of it
     '''
    rent = round(price * .13, 2)
    return rent


def add_tax(rent):
    ''' '''
    tax = rent * .07
    rent += tax
    total = round(rent, 2)
    return total


def format_total(total):
    return "${0:.2f}".format(total)


# make dict from inventory
def inventory_dict():
    ''' '''


if __name__ == '__main__':
    user = input("Customer or Employee?").lower().strip()
    if user == "customer":
        userEmail = input("Enter your email address: ")
        print(validEmail(userEmail))
        whichInstrument = input("What instrument would you like to rent?")
