from openedFiles import *
from core import *
import sys

#this would be main


def customer_search():
    searchWhat = input("Enter keyword:  ").lower().replace(" ", "")
    results = ""
    results += "Results: "
    for line in transactionline:
        if searchWhat in line:
            results += ("\n" + line + "\n")
    if results == "Results: ":
        print("No results found.")
        return (customer_search)
    else:
        return (results)


def history():
    all_history = ""
    print("Here's our history log:\n")
    for line in transactionline:
        all_history += ("\n" + line + "\n")
    return all_history


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
        return ("Confirmed")
    elif confirm == "cancel":
        print("Canceling . . .")
        sys.exit()
    else:
        print("Invalid.")
        sys.exit()


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


def update_return_date():
    transactionString = ""
    for line in trans_file:
        if userEmail in line and "not returned" in line and returnWhat in line and "{'Action': 'b'}" not in line:
            newLine = line.replace("not returned", (
                str(now.month) + "-" + str(now.day) + "-" + str(now.year)))
            transactionString += "{0}".format(newLine)
            return ("Thank you")
        elif returnWhat == "q":
            print("Canceling. . .")
            sys.exit()
        elif returnWhat not in line:
            return "try again"
        elif userEmail in line and "not returned" not in line and returnWhat in line and "{'Action': 'b'}" not in line:
            return ("Item has already been returned.")
        else:
            transactionString += "{0}".format(line)
    with open("transactions.txt", "w") as transactionFile:
        transactionFile.write(transactionString)


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
            return_dict["Return date"] = "not returned"
            userInfo_lst.append(return_dict)
            print(confirm_trans())

        elif customerChoice == "rt":
            returnWhat = input("Which item are you returning? ").lower().strip(
            )
            update_return_date()
            if update_return_date() == "Thank you":
                return_to_inventory()
            # while update_return_date == "try again":
            #     input(returnWhat)

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
