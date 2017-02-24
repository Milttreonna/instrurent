from openedFiles import *
from instrurent import *
import sys


def show_inventory():
    ''' Returns the formatted inventory in a different color'''
    show = ''
    for i in (inventory):
        show += ('\033[1m' + i + '\033[0m' + "\n")
    return (show)


def add_tax(p):
    ''' Adds 7% sales tax to rent and returns the total'''
    tax = p * .07
    p += tax
    total = round(p, 2)
    return total


def format_total(total):
    '''Returns formatted total '''
    return "${0:.2f}".format(total)


def add_weeks_rented(rentTime):
    '''adds weeks rented to dictionary of user's info '''
    week_dict["Weeks rented"] = rentTime
    userInfo_lst.append(week_dict)


def how_many_weeks():
    '''asks the user how many weeks they would like to rent out the instrument
    and returns it '''
    weeks = ""

    rentTime = int(input(
        "How many weeks would you like to rent it?(1-3 only)\n"))
    weeks += str(rentTime)
    if rentTime > 3 or rentTime <= 0:
        print("Must be between 1-3")
        sys.exit()
    add_weeks_rented(rentTime)

    return int(weeks)


def get_customer_total(weeks, item):
    '''takes the price to rent the instrument, adds tax to it and multiplies it
    by the number of weeks the user would like to rent it out '''
    total = item * weeks

    total_dict["Total"] = (format_total(total))
    userInfo_lst.append(total_dict)
    revenueString = ""
    revenueString += str(add_tax(total))
    newRevenue = revenue + (float(revenueString))
    newRevenue = round(newRevenue, 2)
    with open("revenue.txt", "w") as revenueFile:
        revenueFile.write(str(newRevenue))
    print("Total to rent:")
    return format_total(total)


def confirm_trans():
    '''Writes to transactions and inventory if the user confirms transaction'''
    add_not_returned()
    confirm = input("Confirm or cancel?").lower().strip()
    if confirm == "confirm":
        with open("transactions.txt", "a") as transactionFile:
            transactionFile.write(str(userInfo_lst) + '\n')
        with open("inventory.txt", 'w') as inventoryFile:
            output = ''
            for d in dict:
                output += d + " " + str(dict[d]) + "\n"
            inventoryFile.write(output)
        print("Confirmed")
        return (customer_receipt())
    elif confirm == "cancel":
        print(cancel_it())
    else:
        print("Invalid.")
        sys.exit()


def customer_receipt():
    '''returns the customer receipt '''
    art1 = "                  "
    print("\n¸♬·¯·♩¸¸♪·¯·♫¸¸Here's your receipt!¸¸♬·¯·♩¸¸♪·¯·♫¸¸\n")
    receipt = ""
    for line in userInfo_lst:
        receipt += (art1 + str(line) + "\n")
    return receipt.replace("{", "").replace("}", "").replace("'", "")


def add_item(whatInstrument):
    '''adds what item the user is buying/ renting to the dictionary of user's info '''
    item_dict["Item"] = whatInstrument
    userInfo_lst.append(item_dict)


def item_info(whatInstrument):
    '''Takes the instrument that the user wants to rent or buy and gives a description of that item '''
    print("\n\033[1mDescription: \033[0m\n")
    if "clarinet" in whatInstrument:
        return ('\033[1m' + clarinet + '\033[0m')
    elif "piano" in whatInstrument:
        return ('\033[1m' + piano + '\033[0m')
    elif "violin" in whatInstrument:
        return ('\033[1m' + violin + '\033[0m')
    elif "electric" in whatInstrument or whatInstrument == "electricguitar":
        return ('\033[1m' + electricguitar + '\033[0m')
    elif "acoustic" in whatInstrument or whatInstrument == "acousticguitar":
        return ('\033[1m' + acousticguitar + '\033[0m')
    elif "banjo" in whatInstrument:
        return ('\033[1m' + banjo + '\033[0m')
    elif "trumpet" in whatInstrument:
        return ('\033[1m' + trumpet + '\033[0m')
    elif "saxophone" in whatInstrument:
        return ('\033[1m' + sax + '\033[0m')
    elif "conga" in whatInstrument:
        return ('\033[1m' + conga + '\033[0m')
    elif "drum" in whatInstrument:
        return ('\033[1m' + drums + '\033[0m')
    else:
        print("Invalid answer.")
        sys.exit()


def update_return_date(userEmail, returnWhat):
    '''Takes the users email and and item the user wants to return and updates the return date'''
    transactionString = ""
    for line in trans_file:
        if userEmail in line and "not returned" in line and returnWhat in line and "{'Action': 'b'}" not in line:
            newLine = line.replace("not returned", (
                str(now.month) + "-" + str(now.day) + "-" + str(now.year)))
            transactionString += "{0}".format(newLine)

        elif returnWhat == "q":
            print("Canceling. . .")
            sys.exit()
        elif userEmail in line and returnWhat in line and "not returned" not in line and "{'Action': 'b'}" not in line:
            return ("Item has already been returned.")
        else:
            transactionString += "{0}".format(line)

    with open("transactions.txt", "w") as transactionFile:
        transactionFile.write(transactionString)
    return ("Done")


def cancel_it():
    print("Canceling. . .")
    sys.exit()


def add_not_returned():
    '''adds return date key to dictionary of user's info '''
    return_dict["Return date"] = "not returned"
    userInfo_lst.append(return_dict)


def add_action(customerChoice):
    '''adds what the user is doing to dictionary of user's info '''
    option_dict["Action"] = customerChoice
    userInfo_lst.append(option_dict)


def get_buy_total(total):
    ''' '''
    total_dict["Total"] = (format_total(total))
    userInfo_lst.append(total_dict)
    revenueString = ""
    revenueString += str(total)
    newRevenue = revenue + (float(revenueString))
    newRevenue = round(newRevenue, 2)
    with open("revenue.txt", "w") as revenueFile:
        revenueFile.write(str(newRevenue))
    return "\nTotal: " + str(total)
