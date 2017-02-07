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
            print("New user")
            with open("emails.csv", "a") as emailFile:
                emailFile.write(e + '\n')
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


def inventory_dict(inventory):
    '''Takes inventory file and returns a dictionary '''
    dict = {inventory[line]: inventory[line + 1]
            for line in range(0, len(inventory), 2)}
    return dict


def show_inventory(inventory):
    ''' Takes inventory file, splits it into two lists
    (one for instrument name and the other for how many there are)
    and returns the formatted version'''
    show = ''
    instruments = inventory[::2]
    quantity = inventory[1::2]
    for i, q in zip(instruments, quantity):
        show += ('\033[1m' + i + "s: " + q + '\033[0m' + "\n")
    return (show)


if __name__ == '__main__':
    user = input("Customer or Employee?").lower().strip()
    # print(inventory_dict(inventory))
    if user == "customer":
        userEmail = input("Enter your email address: ")
        print(validEmail(userEmail))
        print("Here's our inventory:")
        print(show_inventory(inventory))
        whichInstrument = input("What instrument would you like to rent?")
