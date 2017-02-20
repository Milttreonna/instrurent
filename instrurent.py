from openedFiles import *
# from core import (function names)
import sys

#this would be core


def validEmail():
    '''Takes user's email and checks to see if it's valid or not'''

    if "@" and ".com" in userEmail:
        if userEmail in emails:
            #adds email to user's info
            userInfo_lst.append(userEmail)
            #adds date to user's info
            date_dict["Date"] = (
                str(now.month) + "-" + str(now.day) + "-" + str(now.year))
            userInfo_lst.append(date_dict)
            return ("Previous user")

        else:
            print("New user")
            #writes the user's email to the email file
            with open("emails.txt", "a") as emailFile:
                emailFile.write(userEmail + '\n')
            userInfo_lst.append(userEmail)
            date_dict["Date"] = (
                str(now.month) + "-" + str(now.day) + "-" + str(now.year))
            userInfo_lst.append(date_dict)
            return ("Valid email")
    elif userEmail == "q":
        print("Canceling. . . ")
        sys.exit()
    else:
        print("Invalid email")
        sys.exit()


def show_inventory():
    ''' Returns the formatted inventory in a different color'''
    show = ''
    for i, q in zip(instruments, quantity):
        show += ('\033[1m' + i + "s: " + q + '\033[0m' + "\n")
    return (show)


def customer_search():
    searchWhat = input("Enter keyword:  ").lower().replace(" ", "")
    results = ""
    results += "Results: "
    for line in trans_file:
        if searchWhat in line:
            results += ("\n" + line + "\n")
    if results == "Results: ":
        return ("No results found.")
    else:
        return (results)


def history():
    all_history = ""
    for line in trans_file:
        all_history += ("\n" + line + "\n")
    return all_history


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

    week_dict["Weeks rented"] = rentTime
    userInfo_lst.append(week_dict)
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
    newRevenue= round(newRevenue,2)
    with open("employee.txt", "w") as revenueFile:
        revenueFile.write(str(newRevenue))
    print("Total to rent:")
    return ('\033[1m' + format_total(total) + '\033[0m')


def itemInfo():
    whatInstrument = input("What instrument?  ").lower().strip()

    if "clarinet" in whatInstrument:
        print('\033[1m' + clarinet + '\033[0m')
        rent_total = add_tax(rent_price(clarinetCost))
        buy_total = add_tax(clarinetCost)
        if int(dict["Clarinet"]) <= 0:
            print("Item is out of stock.")
            sys.exit()
        else:
            dict['Clarinet'] = int(dict["Clarinet"]) - 1

    elif "piano" in whatInstrument:
        print('\033[1m' + piano + '\033[0m')
        rent_total = add_tax(rent_price(pianoCost))
        buy_total = add_tax(pianoCost)
        if int(dict["Piano"]) <= 0:
            print("Item is out of stock.")
            sys.exit()
        else:
            dict['Piano'] = int(dict["Piano"]) - 1

    elif "violin" in whatInstrument:
        print('\033[1m' + violin + '\033[0m')
        rent_total = add_tax(rent_price(violinCost))
        buy_total = add_tax(violinCost)
        if int(dict["Violin"]) <= 0:
            print("Item is out of stock.")
            sys.exit()
        else:
            dict['Violin'] = int(dict["Violin"]) - 1

    elif "electric" in whatInstrument or whatInstrument == "electricguitar":
        print('\033[1m' + electricguitar + '\033[0m')
        rent_total = add_tax(rent_price(eguitarCost))
        buy_total = add_tax(eguitarCost)
        if int(dict["Electric-guitar"]) <= 0:
            print("Item is out of stock.")
            sys.exit()
        else:
            dict['Electric-guitar'] = int(dict["Electric-guitar"]) - 1

    elif "acoustic" in whatInstrument or whatInstrument == "acousticguitar":
        print('\033[1m' + acousticguitar + '\033[0m')
        rent_total = add_tax(rent_price(aguitarCost))
        buy_total = add_tax(aguitarCost)
        if int(dict["Acoustic-guitar"]) <= 0:
            print("Item is out of stock.")
            sys.exit()
        else:
            dict['Acoustic-guitar'] = int(dict["Acoustic-guitar"]) - 1

    elif "banjo" in whatInstrument:
        print('\033[1m' + banjo + '\033[0m')
        rent_total = add_tax(rent_price(banjoCost))
        buy_total = add_tax(banjoCost)
        if int(dict["Banjo"]) <= 0:
            print("Item is out of stock.")
            sys.exit()
        else:
            dict['Banjo'] = int(dict["Banjo"]) - 1

    elif "trumpet" in whatInstrument:
        print('\033[1m' + trumpet + '\033[0m')
        rent_total = add_tax(rent_price(trumpetCost))
        buy_total = add_tax(trumpetCost)
        if int(dict["Trumpet"]) <= 0:
            print("Item is out of stock.")
            sys.exit()
        else:
            dict['Trumpet'] = int(dict["Trumpet"]) - 1

    elif "saxophone" in whatInstrument:
        print('\033[1m' + sax + '\033[0m')
        rent_total = add_tax(rent_price(saxCost))
        buy_total = add_tax(saxCost)
        if int(dict["Saxophone"]) <= 0:
            print("Item is out of stock.")
            sys.exit()
        else:
            dict['Saxophone'] = int(dict["Saxophone"]) - 1

    elif "conga" in whatInstrument:
        print('\033[1m' + conga + '\033[0m')
        rent_total = add_tax(rent_price(congaCost))
        buy_total = add_tax(congaCost)
        if int(dict["Conga-set"]) <= 0:
            print("Item is out of stock.")
            sys.exit()
        else:
            dict['Conga-set'] = int(dict["Conga-set"]) - 1

    elif "drum" in whatInstrument:
        print('\033[1m' + drums + '\033[0m')
        rent_total = add_tax(rent_price(drumCost))
        buy_total = add_tax(drumCost)
        if int(dict["Drum-set"]) <= 0:
            print("Item is out of stock.")
            sys.exit()
        else:
            dict['Drum-set'] = int(dict["Drum-set"]) - 1

    elif whatInstrument == "q":
        print("Canceling. . .")
        sys.exit()
    else:
        print("Invalid answer")
        return itemInfo()

    if customerChoice == "b":
        item_dict["Item"] = whatInstrument
        userInfo_lst.append(item_dict)
        total_dict["Total"] = (format_total(buy_total))
        userInfo_lst.append(total_dict)
        revenueString = ""
        revenueString += str(add_tax(buy_total))
        newRevenue = revenue + (float(revenueString))
        newRevenue= round(newRevenue, 2)
        with open("employee.txt", "w") as revenueFile:
            revenueFile.write(str(newRevenue))
        return ("\nTotal to buy: " + '\033[1m' + str(buy_total) + '\033[0m')

    elif customerChoice == "r":
        item_dict["Item"] = whatInstrument
        userInfo_lst.append(item_dict)
        print("\nPrice to rent (per week): " + '\033[1m' + str(rent_total) +
              '\033[0m')
    return (get_customer_total(how_many_weeks(), rent_total))


def confirm_trans():
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
        # return(customer_receipt())
    elif confirm == "cancel":
        print("Canceling . . .")
        sys.exit()
    else:
        print("Invalid.")
        sys.exit()


def return_to_inventory():
    if "clarinet" in returnWhat:
        if int(dict["Clarinet"]) >= 10:
            print("All items are in stock.")
            sys.exit()
        else:
            dict['Clarinet'] = int(dict["Clarinet"]) + 1

    elif "piano" in returnWhat:
        if int(dict["Piano"]) >= 10:
            print("All items are in stock.")
            sys.exit()
        else:
            dict['Piano'] = int(dict["Piano"]) + 1

    elif "violin" in returnWhat:
        if int(dict["Violin"]) >= 10:
            print("All items are in stock.")
            sys.exit()
        else:
            dict['Violin'] = int(dict["Violin"]) + 1

    elif "electric" in returnWhat or returnWhat == "electricguitar":
        if int(dict["Electric-guitar"]) >= 10:
            print("All items are in stock.")
            sys.exit()
        else:
            dict['Electric-guitar'] = int(dict["Electric-guitar"]) + 1

    elif "acoustic" in returnWhat or returnWhat == "acousticguitar":
        if int(dict["Acoustic-guitar"]) >= 10:
            print("All items are in stock.")
            sys.exit()
        else:
            dict['Acoustic-guitar'] = int(dict["Acoustic-guitar"]) + 1

    elif "banjo" in returnWhat:
        if int(dict["Banjo"]) >= 10:
            print("All items are in stock.")
            sys.exit()
        else:
            dict['Banjo'] = int(dict["Banjo"]) + 1

    elif "trumpet" in returnWhat:
        if int(dict["Trumpet"]) >= 10:
            print("All items are in stock.")
            sys.exit()
        else:
            dict['Trumpet'] = int(dict["Trumpet"]) + 1

    elif "saxophone" in returnWhat:
        if int(dict["Saxophone"]) >= 10:
            print("All items are in stock.")
            sys.exit()
        else:
            dict['Saxophone'] = int(dict["Saxophone"]) + 1

    elif "conga" in returnWhat:
        if int(dict["Conga-set"]) >= 10:
            print("All items are in stock.")
            sys.exit()
        else:
            dict['Conga-set'] = int(dict["Conga-set"]) + 1

    elif "drum" in returnWhat:
        if int(dict["Drum-set"]) >= 10:
            print("All items are in stock.")
            sys.exit()
        else:
            dict['Drum-set'] = int(dict["Drum-set"]) + 1
    else:
        return ("Not valid.")
    with open("inventory.txt", 'w') as inventoryFile:
        return_output = ''
        for d in dict:
            return_output += d + " " + str(dict[d]) + "\n"
        inventoryFile.write(return_output)


def update_return_date():
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

def customer_receipt():
    return("Receipt")

if __name__ == '__main__':
    print("Hello! Welcome to Instru-Rent!")
    user = input("Customer or Employee?").lower().strip()
    if user == "customer":
        print("Enter Q to quit\n")
        userEmail = input("Enter your email address: ")
        userEmail = userEmail.lower().replace(" ", "")
        print(validEmail())
        print(
            "\n(R)= rent| (B)= buy| (RT)= return| (S)= search| (H)= all history")

        customerChoice = input("What would you like to do?").lower().strip()
        option_dict["Action"] = customerChoice
        userInfo_lst.append(option_dict)
        if customerChoice == "b" or customerChoice == "r":
            print(show_inventory())
            print(itemInfo())
            return_dict["Return date"] = "not returned"
            userInfo_lst.append(return_dict)
            print(confirm_trans())

        elif customerChoice == "rt":
            returnWhat = input("Which item are you returning? ").lower().strip(
            )

            print(update_return_date())
            if update_return_date(
            ) != "Item has already been returned." and update_return_date(
            ) != "You haven't rented that instrument out.":
                return_to_inventory()
                print("Thanks for returning the " + returnWhat + "!")

        elif customerChoice == "s":
            print("To search a date: m-da-year\nExample: 8-10-1998")
            print(customer_search())
        elif customerChoice == "h":
            print("Here's our history log:\n")
            print(history())
        elif customerChoice == "q":
            print("Canceling . . .")
            sys.exit()
        else:
            print("Invalid Answer.")
            sys.exit()

    elif user == "employee":
        print("Transactions:\n")
        print(history())

        print("Revenue:", format_total(revenue))
        # revenue += float(int(revenueString))

    else:
        print("Invalid. Try again.")
        sys.exit()
