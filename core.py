from openedFiles import *
from instrurent import *
import sys


def show_inventory():
    ''' Returns the formatted inventory in a different color'''
    show = ''
    for i, q in zip(instruments, quantity):
        show += ('\033[1m' + i + "s: " + q + '\033[0m' + "\n")
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


def rent_price(price):
    '''Takes the instrument's price and gets 13 percent of it'''
    rent = round(price * .13, 2)
    return rent


def get_customer_total(weeks, item):
    '''takes the price to rent the instrument, adds tax to it and multiplies it
    by the number of weeks the user would like to rent it out '''
    total = item * weeks

    total_dict["Total"] = (format_total(total))
    userInfo_lst.append(total_dict)

    print("Total to rent:")
    return ('\033[1m' + format_total(total) + '\033[0m')


def itemInfo():
    whatInstrument = input("What instrument?  ").lower().strip()
    item_dict["Item"] = whatInstrument
    userInfo_lst.append(item_dict)

    if "clarinet" in whatInstrument:
        print('\033[1m' + clarinet + '\033[0m')
        rent_total = add_tax(rent_price(clarinetCost))
        buy_total = add_tax(clarinetCost)
        dict['Clarinet'] = int(dict["Clarinet"]) - 1

    elif "piano" in whatInstrument:
        print('\033[1m' + piano + '\033[0m')
        rent_total = add_tax(rent_price(pianoCost))
        buy_total = add_tax(pianoCost)
        dict['Piano'] = int(dict["Piano"]) - 1

    elif "violin" in whatInstrument:
        print('\033[1m' + violin + '\033[0m')
        rent_total = add_tax(rent_price(violinCost))
        buy_total = add_tax(violinCost)
        dict['Violin'] = int(dict["Violin"]) - 1

    elif "electric" in whatInstrument or whatInstrument == "electricguitar":
        print('\033[1m' + electricguitar + '\033[1m')
        rent_total = add_tax(rent_price(eguitarCost))
        buy_total = add_tax(eguitarCost)
        dict['Electric-guitar'] = int(dict["Electric-guitar"]) - 1

    elif "acoustic" in whatInstrument or whatInstrument == "acousticguitar":
        print('\033[1m' + acousticguitar + '\033[1m')
        rent_total = add_tax(rent_price(aguitarCost))
        buy_total = add_tax(aguitarCost)
        dict['Acoustic-guitar'] = int(dict["Acoustic-guitar"]) - 1

    elif "banjo" in whatInstrument:
        print('\033[1m' + banjo + '\033[1m')
        rent_total = add_tax(rent_price(banjoCost))
        buy_total = add_tax(banjoCost)
        dict['Banjo'] = int(dict["Banjo"]) - 1

    elif "trumpet" in whatInstrument:
        print('\033[1m' + trumpet + '\033[1m')
        rent_total = add_tax(rent_price(trumpetCost))
        buy_total = add_tax(trumpetCost)
        dict['Trumpet'] = int(dict["Trumpet"]) - 1

    elif "saxophone" in whatInstrument:
        print('\033[1m' + sax + '\033[1m')
        rent_total = add_tax(rent_price(saxCost))
        buy_total = add_tax(saxCost)
        dict['Saxophone'] = int(dict["Saxophone"]) - 1

    elif "conga" in whatInstrument:
        print('\033[1m' + conga + '\033[1m')
        rent_total = add_tax(rent_price(congaCost))
        buy_total = add_tax(congaCost)
        dict['Conga-set'] = int(dict["Conga-set"]) - 1

    elif "drum" in whatInstrument:
        print('\033[1m' + drums + '\033[1m')
        rent_total = add_tax(rent_price(drumCost))
        buy_total = add_tax(drumCost)
        dict['Drum-set'] = int(dict["Drum-set"]) - 1

    elif whatInstrument == "q":
        print("Canceling. . .")
        sys.exit()
    else:
        print("Invalid answer")
        return itemInfo()

    if customerChoice == "b":
        total_dict["Total"] = (format_total(buy_total))
        userInfo_lst.append(total_dict)
        return ("\nTotal to buy: " + '\033[1m' + str(buy_total) + '\033[0m')

    elif customerChoice == "r":
        print("\nPrice to rent (per week): " + '\033[1m' + str(rent_total) +
              '\033[0m')
        return (get_customer_total(how_many_weeks(), rent_total))


def return_to_inventory():
    if "clarinet" in returnWhat:
        dict['Clarinet'] = int(dict["Clarinet"]) + 1

    elif "piano" in returnWhat:
        dict['Piano'] = int(dict["Piano"]) + 1

    elif "violin" in returnWhat:
        dict['Violin'] = int(dict["Violin"]) + 1

    elif "electric" in returnWhat or returnWhat == "electricguitar":
        dict['Electric-guitar'] = int(dict["Electric-guitar"]) + 1

    elif "acoustic" in returnWhat or returnWhat == "acousticguitar":
        dict['Acoustic-guitar'] = int(dict["Acoustic-guitar"]) + 1

    elif "banjo" in returnWhat:
        dict['Banjo'] = int(dict["Banjo"]) + 1

    elif "trumpet" in returnWhat:
        dict['Trumpet'] = int(dict["Trumpet"]) + 1

    elif "saxophone" in returnWhat:
        dict['Saxophone'] = int(dict["Saxophone"]) + 1

    elif "conga" in returnWhat:
        dict['Conga-set'] = int(dict["Conga-set"]) + 1

    elif "drum" in returnWhat:
        dict['Drum-set'] = int(dict["Drum-set"]) + 1
    else:
        return ("Not valid.")
    with open("inventory.txt", 'w') as inventoryFile:
        return_output = ''
        for d in dict:
            return_output += d + " " + str(dict[d]) + "\n"
        inventoryFile.write(return_output)
    return ("Thanks for returning the" + returnWhat + "!")
