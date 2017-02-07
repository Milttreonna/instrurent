from openedFiles import *
import sys
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
    '''Takes user's email and checks to see if it's valid or not'''
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
    '''Takes the instrument's price and gets 13 percent of it'''
    rent = round(price * .13, 2)
    return rent


def add_tax(rent):
    ''' Adds 7% sales tax to rent'''
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
    ''' Takes inventory file, splits it into two lists (one for instrument name
     and the other for how many there are) and returns the formatted version'''
    show = ''
    instruments = inventory[::2]
    quantity = inventory[1::2]
    for i, q in zip(instruments, quantity):
        show += ('\033[1m' + i + "s: " + q + '\033[0m' + "\n")
    return (show)


def description():
    '''returns the complete total and description of the instrument the user wants to rent '''
    # print("\nDescription:")
    if whichInstrument == "clarinet":
        return (get_customer_total(how_many_weeks(), clarinet_info()))
        # return (clarinet_info())
    elif whichInstrument == "piano":
        return get_customer_total(how_many_weeks(), piano_info())
    elif whichInstrument == "violin":
        return get_customer_total(how_many_weeks(), violin_info())
    elif whichInstrument == "electric guitar":
        return get_customer_total(how_many_weeks(), eguitar_info())
    elif whichInstrument == "acoustic guitar":
        return get_customer_total(how_many_weeks(), aguitar_info())
    elif whichInstrument == "banjo":
        return get_customer_total(how_many_weeks(), banjo_info())
    elif whichInstrument == "trumpet":
        return get_customer_total(how_many_weeks(), trumpet_info())
    elif whichInstrument == "saxophone":
        return get_customer_total(how_many_weeks(), sax_info())
    elif "conga" in whichInstrument:
        return get_customer_total(how_many_weeks(), conga_info())
    elif "drum" in whichInstrument:
        return get_customer_total(how_many_weeks(), drum_info())
    else:
        return ("Invalid answer.")


def clarinet_info():
    ''' returns information about the clarinets'''
    customerTotal = ""
    customerTotal += str(rent_price(clarinetCost))

    print('\033[1m' + clarinet + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + str(rent_price(
              clarinetCost)) + '\033[0m')
    return float(customerTotal)


def piano_info():
    ''' returns information about the pianos'''
    customerTotal = ""
    customerTotal += str(rent_price(pianoCost))
    print('\033[1m' + piano + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + str(rent_price(
              pianoCost)) + '\033[0m')
    return float(customerTotal)


def violin_info():
    ''' returns information about the violins'''
    customerTotal = ""
    customerTotal += str(rent_price(violinCost))
    print('\033[1m' + violin + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + str(rent_price(
              violinCost)) + '\033[0m')
    return float(customerTotal)


def eguitar_info():
    '''returns information about the electric guitars '''
    customerTotal = ""
    customerTotal += str(rent_price(eguitarCost))
    print('\033[1m' + eguitar + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + str(rent_price(
              eguitarCost)) + '\033[0m')
    return float(customerTotal)


def aguitar_info():
    '''returns information about the acoustic guitars '''
    customerTotal = ""
    customerTotal += str(rent_price(aguitarCost))
    print('\033[1m' + aguitar + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + str(rent_price(
              aguitarCost)) + '\033[0m')
    return float(customerTotal)


def banjo_info():
    '''returns information about the banjos '''
    customerTotal = ""
    customerTotal += str(rent_price(banjoCost))
    print('\033[1m' + banjo + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + str(rent_price(
              banjoCost)) + '\033[0m')
    return float(customerTotal)


def trumpet_info():
    ''' returns information about the trumpets'''
    customerTotal = ""
    customerTotal += str(rent_price(trumpetCost))
    print('\033[1m' + trumpet + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + str(rent_price(
              trumpetCost)) + '\033[0m')
    return float(customerTotal)


def sax_info():
    ''' returns information about the saxophones'''
    customerTotal = ""
    customerTotal += str(rent_price(saxCost))
    print('\033[1m' + sax + '\033[0m' + "\nPrice to rent (tax not included): "
          + '\033[1m' + str(rent_price(saxCost)) + '\033[0m')
    return float(customerTotal)


def conga_info():
    ''' returns information about the conga sets'''
    customerTotal = ""
    customerTotal += str(rent_price(congaCost))
    print('\033[1m' + conga + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + str(rent_price(
              congaCost)) + '\033[0m')
    return float(customerTotal)


def drum_info():
    '''returns information about the drum sets '''
    customerTotal = ""
    customerTotal += str(rent_price(drumCost))
    print('\033[1m' + drums + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + str(rent_price(
              drumCost)) + '\033[0m')
    return float(customerTotal)


def how_many_weeks():
    '''asks the user how many weeks they would like to rent out the instrument
    and returns it '''
    weeks = ""
    for l in (range(4)):
        rentTime = int(input(
            "How many weeks would you like to rent it?(1-3 only)\n"))
        weeks += str(rentTime)
        if rentTime <= 3:
            break
    return int(weeks)


def get_customer_total(weeks, item):
    '''takes the price to rent the instrument, adds tax to it and multiplies it
    by the number of weeks the user would like to rent it out '''
    item = add_tax(item)
    total = item * weeks
    print("You're complete total will be:")
    return (format_total(total))

#
# def confirm():
#     if confirm =="confirm":
#
#     elif confirm=="cancel":

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
        print(description())
        confirm = input("Confirm or cancel?")

    elif user == "employee":
        print("Not Done")
    else:
        print("Invalid. Try again.")
