from openedFiles import *

clarinetCost = 1171.99
drumCost = 910.00
pianoCost = 1700.99
violinCost = 699.99
eguitarCost = 899.99
aguitarCost = 439.99
banjoCost = 479.00
saxCost = 3153.99
trumpetCost = 2438.99
congaCost = 269.99


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
            return ("Previous user")
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


def description():
    '''returns price without tax and description of instrument the user wants to rent '''
    if whichInstrument == "clarinet":
        return ('\033[1m' + clarinet + '\033[0m' + "\nPrice to rent: " +
                '\033[1m' + str(rent_price(clarinetCost)) + '\033[0m')

    elif whichInstrument == "piano":
        return ('\033[1m' + piano + '\033[0m')
    elif whichInstrument == "violin":
        return ('\033[1m' + violin + '\033[0m')
    elif whichInstrument == "electric guitar":
        return ('\033[1m' + eguitar + '\033[0m')
    elif whichInstrument == "acoustic guitar":
        return ('\033[1m' + aguitar + '\033[0m')
    elif whichInstrument == "banjo":
        return ('\033[1m' + banjo + '\033[0m')
    elif whichInstrument == "trumpet":
        return ('\033[1m' + trumpet + '\033[0m')
    elif whichInstrument == "saxophone":
        return ('\033[1m' + sax + '\033[0m')
    elif "conga" in whichInstrument:
        return ('\033[1m' + conga + '\033[0m')
    elif "drum" in whichInstrument:
        return ('\033[1m' + drums + '\033[0m')
    else:
        return ("Invalid answer.")


if __name__ == '__main__':
    user = input("Customer or Employee?").lower().strip()
    # print(inventory_dict(inventory))
    if user == "customer":
        userEmail = input("Enter your email address: ")
        print(validEmail(userEmail))
        print("\nHere's our inventory:")
        print(show_inventory(inventory))
        whichInstrument = input(
            "What instrument would you like to rent?\n").lower().strip()

        print("\nDescription:")
        print(description())

    elif user == "employee":
        print("Not Done")
    else:
        print("Invalid. Try again.")
