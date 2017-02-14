from openedFiles import *
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
            with open("emails.csv", "a") as emailFile:
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
        print("Canceling . . .")
        sys.exit()
    else:
        print("Invalid.")
        sys.exit()


def customer_search():
    searchWhat = input("Enter keyword:  ").lower().replace(" ", "")
    results = ""
    results += "Results: "
    for line in transactionline:
        if searchWhat in line:
            results += ("\n" + line + "\n")
    if results == "Results: ":
        return ("No results found.")
    else:
        return (results)


def history():
    all_history = ""
    print("Here's our history log:\n")
    for line in transactionline:
        all_history += ("\n" + line + "\n")
    return all_history


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

    

# def customer_receipt():
#

if __name__ == '__main__':
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
            print(confirm_trans())
        elif customerChoice == "rt":
            for line in transactionline:
                seperate = line.split(",")
                if userEmail in line:
                    if "Return date" not in line:
                        if "{'Action': 'b'}" not in line:
                            print("Here's what you have out:")
                            print(seperate[0][2:-1], seperate[1], seperate[3])
                            returnWhat = input(
                                "Which item are you returning? ").lower(
                                ).strip()
                            if returnWhat in seperate[3]:
                                return_to_inventory()
                                print("Thank you for returning!")

        elif customerChoice == "s":
            print("To search a date: m-da-year\nExample: 8-10-1998")
            print(customer_search())
        elif customerChoice == "h":
            print(history())
        elif customerChoice == "q":
            print("Canceling . . .")
            sys.exit()
        else:
            print("Invalid Answer.")
            sys.exit()

    elif user == "employee":
        print("nothing")
    else:
        print("Invalid. Try again.")
        sys.exit()
