from openedFiles import *
import sys

# import datetime


def validEmail(e):
    '''Takes user's email and checks to see if it's valid or not'''
    e = e.lower().replace(" ", "")
    date_dict = {}
    if "@" and ".com" in e:

        if e in emails:
            #adds email to user's info
            userInfo_lst.append(e)
            #adds date to user's info
            date_dict["Date"] = (
                str(now.month) + "-" + str(now.day) + "-" + str(now.year))
            userInfo_lst.append(date_dict)
            return ("Previous user")

        else:
            print("New user")
            #writes the user's email to the email file
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


def add_tax(p):
    ''' Adds 7% sales tax to rent and returns the total'''
    tax = p * .07
    p += tax
    total = round(p, 2)
    return total


def format_total(total):
    '''Returns formatted total '''
    return "${0:.2f}".format(total)


def show_inventory():
    ''' Returns the formatted inventory in a different color'''
    show = ''
    for i, q in zip(instruments, quantity):
        show += ('\033[1m' + i + "s: " + q + '\033[0m' + "\n")
    return (show)


def description():
    '''returns the complete total and description of the instrument the user wants to rent '''
    item_dict = {}
    if whichInstrument == "clarinet":

        #subtracts one of the Clarinets from the inventory dictionary, but
        #doesn't write to the inventory file
        dict['Clarinet'] = int(dict["Clarinet"]) - 1

        # writes what item the user is renting/buying to their info
        item_dict["Item"] = "Clarinet"
        userInfo_lst.append(item_dict)

        return (get_customer_total(how_many_weeks(), clarinet_info()))

    elif whichInstrument == "piano":
        item_dict["Item"] = "Piano"
        userInfo_lst.append(item_dict)
        dict['Piano'] = int(dict["Piano"]) - 1
        return get_customer_total(how_many_weeks(), piano_info())

    elif whichInstrument == "violin":
        item_dict["Item"] = "Violin"
        userInfo_lst.append(item_dict)
        dict['Violin'] = int(dict["Violin"]) - 1
        return get_customer_total(how_many_weeks(), violin_info())

    elif whichInstrument == "electric guitar":
        item_dict["Item"] = "Electric guitar"
        userInfo_lst.append(item_dict)
        dict['ElectricGuitar'] = int(dict["ElectricGuitar"]) - 1
        return get_customer_total(how_many_weeks(), eguitar_info())

    elif whichInstrument == "acoustic guitar":
        item_dict["Item"] = "Acoustic Guitar"
        userInfo_lst.append(item_dict)
        dict['AcousticGuitar'] = int(dict["AcousticGuitar"]) - 1
        return get_customer_total(how_many_weeks(), aguitar_info())

    elif whichInstrument == "banjo":
        item_dict["Item"] = "Banjo"
        userInfo_lst.append(item_dict)
        dict['Banjo'] = int(dict["Banjo"]) - 1
        return get_customer_total(how_many_weeks(), banjo_info())

    elif whichInstrument == "trumpet":
        item_dict["Item"] = "Trumpet"
        userInfo_lst.append(item_dict)
        dict['Trumpet'] = int(dict["Trumpet"]) - 1
        return get_customer_total(how_many_weeks(), trumpet_info())

    elif whichInstrument == "saxophone":
        item_dict["Item"] = "Saxophone"
        userInfo_lst.append(item_dict)
        dict['Saxophone'] = int(dict["Saxophone"]) - 1
        return get_customer_total(how_many_weeks(), sax_info())

    elif "conga" in whichInstrument:
        item_dict["Item"] = "Conga Set"
        userInfo_lst.append(item_dict)
        dict['CongaSet'] = int(dict["CongaSet"]) - 1
        return get_customer_total(how_many_weeks(), conga_info())

    elif "drum" in whichInstrument:
        item_dict["Item"] = "Drum set"
        userInfo_lst.append(item_dict)
        dict['DrumSet'] = int(dict["DrumSet"]) - 1
        return get_customer_total(how_many_weeks(), drum_info())
    else:
        return ("Invalid answer")


def clarinet_info():
    ''' returns rent price of item w/o tax'''
    customerTotal = str(rent_price(clarinetCost))
    #prints info about the item
    print('\033[1m' + clarinet + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + customerTotal +
          '\033[0m')
    return float(customerTotal)


def piano_info():
    ''' returns rent price of item w/o tax'''
    customerTotal = str(rent_price(pianoCost))
    print('\033[1m' + piano + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + customerTotal +
          '\033[0m')
    return float(customerTotal)


def violin_info():
    ''' returns rent price of item w/o tax'''
    customerTotal = str(rent_price(violinCost))
    print('\033[1m' + violin + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + customerTotal +
          '\033[0m')
    return float(customerTotal)


def eguitar_info():
    ''' returns rent price of item w/o tax'''
    customerTotal = str(rent_price(eguitarCost))
    print('\033[1m' + eguitar + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + customerTotal +
          '\033[0m')
    return float(customerTotal)


def aguitar_info():
    ''' returns rent price of item w/o tax'''
    customerTotal = str(rent_price(aguitarCost))
    print('\033[1m' + aguitar + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + customerTotal +
          '\033[0m')
    return float(customerTotal)


def banjo_info():
    ''' returns rent price of item w/o tax'''
    customerTotal = str(rent_price(banjoCost))
    print('\033[1m' + banjo + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + customerTotal +
          '\033[0m')
    return float(customerTotal)


def trumpet_info():
    ''' returns rent price of item w/o tax'''
    customerTotal = str(rent_price(trumpetCost))
    print('\033[1m' + trumpet + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + customerTotal +
          '\033[0m')
    return float(customerTotal)


def sax_info():
    ''' returns rent price of item w/o tax'''
    customerTotal = str(rent_price(saxCost))
    print('\033[1m' + sax + '\033[0m' + "\nPrice to rent (tax not included): "
          + '\033[1m' + customerTotal + '\033[0m')
    return float(customerTotal)


def conga_info():
    ''' returns rent price of item w/o tax'''
    customerTotal = str(rent_price(congaCost))
    print('\033[1m' + conga + '\033[0m' +
          "\nPrice to rent (tax not included): " + '\033[1m' + customerTotal +
          '\033[0m')
    return float(customerTotal)


def drum_info():
    ''' returns rent price of item w/o tax'''
    customerTotal = str(rent_price(drumCost))
    print('\033[1m' + drums + '\033[0m' +
          "\nPrice to rent (per week, tax not included): " + '\033[1m' +
          customerTotal + '\033[0m')
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


def confirm_trans():
    confirm = input("Confirm or cancel?").lower().strip()
    if confirm == "confirm":
        with open("transactions.csv", "a") as transactionFile:
            transactionFile.write(str(userInfo_lst) + '\n')
        with open("inventory.csv", 'w') as inventoryFile:
            output = ''
            for d in dict:
                output += d + " " + str(dict[d]) + "\n"
            inventoryFile.write(output)
        return ("Confirmed")
    elif confirm == "cancel":
        return ("Canceling . . .")
    else:
        return ("Invalid.")


if __name__ == '__main__':
    user = input("Customer or Employee?").lower().strip()
    if user == "customer":
        userEmail = input("Enter your email address: ")
        print(validEmail(userEmail))
        print("\nHere's our inventory:")
        print(show_inventory())
        whichInstrument = input(
            "What instrument would you like to rent?\n").lower().strip()
        print(description())
        print(confirm_trans())
    elif user == "employee":
        print("nothing")
    else:
        print("Invalid. Try again.")
        sys.exit()
