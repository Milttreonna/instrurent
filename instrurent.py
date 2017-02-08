from openedFiles import *
import sys
import datetime
import pickle
now = datetime.datetime.now()

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
userInfo_lst = []

# email = input("What's your email?")
# userInfo_lst.append(email)
#
# whatwant = input("What do you want?")
#
# sq_dict = {}
#
# sq_dict["instrument"] = whatwant
# userInfo_lst.append(sq_dict)
# print(userInfo_lst)
#
# print(dict)
#
# print(dict.keys())
# print(dict.values())
# if "Clarinet" in dict:
#     dict['Clarinet'] = int(dict["Clarinet"]) - 1
# print(dict)


def validEmail(e):
    '''Takes user's email and checks to see if it's valid or not'''
    e = e.lower().replace(" ", "")
    date_dict = {}
    if "@" and ".com" in e:

        if e in emails:
            userInfo_lst.append(e)
            date_dict["Date"] = (
                str(now.month) + "-" + str(now.day) + "-" + str(now.year))
            userInfo_lst.append(date_dict)
            return ("Previous user")

        else:
            print("New user")
            with open("emails.csv", "a") as emailFile:
                emailFile.write(e + '\n')
            userInfo_lst.append(e)
            date_dict["Date"] = (
                str(now.month) + "-" + str(now.day) + "-" + str(now.year))
            userInfo_lst.append(date_dict)
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


def show_inventory():
    ''' Returns the formatted version of the inventory'''
    show = ''
    for i, q in zip(instruments, quantity):
        show += ('\033[1m' + i + q + '\033[0m' + "\n")
    return (show)


def description():
    '''returns the complete total and description of the instrument the user wants to rent '''
    # print("\nDescription:")
    if whichInstrument == "clarinet":
        dict['Clarinet'] = int(dict["Clarinet"]) - 1
        return (get_customer_total(how_many_weeks(), clarinet_info()))

    elif whichInstrument == "piano":
        dict['Piano'] = int(dict["Piano"]) - 1
        return get_customer_total(how_many_weeks(), piano_info())

    elif whichInstrument == "violin":
        dict['Violin'] = int(dict["Violin"]) - 1
        return get_customer_total(how_many_weeks(), violin_info())

    elif whichInstrument == "electric guitar":
        dict['ElectricGuitar'] = int(dict["ElectricGuitar"]) - 1
        return get_customer_total(how_many_weeks(), eguitar_info())

    elif whichInstrument == "acoustic guitar":
        dict['AcousticGuitar'] = int(dict["AcousticGuitar"]) - 1
        return get_customer_total(how_many_weeks(), aguitar_info())

    elif whichInstrument == "banjo":
        dict['Banjo'] = int(dict["Banjo"]) - 1
        return get_customer_total(how_many_weeks(), banjo_info())

    elif whichInstrument == "trumpet":
        dict['Trumpet'] = int(dict["Trumpet"]) - 1
        return get_customer_total(how_many_weeks(), trumpet_info())

    elif whichInstrument == "saxophone":
        dict['Saxophone'] = int(dict["Saxophone"]) - 1
        return get_customer_total(how_many_weeks(), sax_info())

    elif "conga" in whichInstrument:
        dict['CongaSet'] = int(dict["CongaSet"]) - 1
        return get_customer_total(how_many_weeks(), conga_info())

    elif "drum" in whichInstrument:
        dict['DrumSet'] = int(dict["DrumSet"]) - 1
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
    week_dict = {}
    week_dict["Weeks rented"] = rentTime
    userInfo_lst.append(week_dict)
    return int(weeks)


def get_customer_total(weeks, item):
    '''takes the price to rent the instrument, adds tax to it and multiplies it
    by the number of weeks the user would like to rent it out '''
    item = add_tax(item)
    total = item * weeks
    total_dict = {}
    total_dict["Total"] = (format_total(total))
    userInfo_lst.append(total_dict)
    print("You're complete total will be:")
    return (format_total(total))

# def write_to_inventory(dictionary):
#     '''writes new info to inventory '''
#

if __name__ == '__main__':
    print(inventory)
    user = input("Customer or Employee?").lower().strip()
    if user == "customer":
        userEmail = input("Enter your email address: ")
        print(validEmail(userEmail))
        print("\nHere's our inventory:")
        print(show_inventory())
        whichInstrument = input(
            "What instrument would you like to rent?\n").lower().strip()
        print(description())
        confirm = input("Confirm or cancel?").lower().strip()
        if confirm == "confirm":
            with open("transactions.txt", "a") as transactionFile:
                transactionFile.write(str(userInfo_lst))
            # with open("inventory.csv", 'w') as inventoryFile:
            #     inventoryFile.write(str(dict))
            print("Confirmed")
        elif confirm == "cancel":
            print("Canceling . . .")
            sys.exit()
    elif user == "employee":
        print("nothing")
    else:
        print("Invalid. Try again.")
        sys.exit()
