from core import *
from openedFiles import *
import sys

# information = [instrument,quantity, full price, rent price]
information = [["acoustic-guitars", "10", "439.99", "57.20"],
               ["trumpets", "10", "2438.99", "317.07"],
               ["clarinets", "10", "1171.99", "152.36"],
               ["pianos", "10", "1700.99", "221.13"],
               ["violins", "10", "699.99", "91.00"],
               ["saxophones", "10", "3153.99", "410.02"],
               ["electric-guitars", "10", "899.99", "117.00"],
               ["drums", "10", "910.00", "118.30"],
               ["banjos", "10", "439.00", "62.27"],
               ["congas", "10", "269.99", "35.10"]]


def valid_email():
    '''Takes user's email if it's valid or not. '''

    if "@" in userEmail and ".com" in userEmail:
        if userEmail in emails:
            #adds email to user's info
            userInfo_lst.append(userEmail)
            add_date()
            return ("Previous user")
        else:
            print("New user")
            #writes the user's email to the email file
            with open("emails.txt", "a") as emailFile:
                emailFile.write(userEmail + '\n')
            userInfo_lst.append(userEmail)
            add_date()
            return ("Valid email")
    elif userEmail == "q":
        print(cancel_it())
    else:
        print("Invalid email")
        sys.exit()


def customer_search():
    '''Asks for keywords to search and return results if any.'''
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
    '''Return transaction history from file. '''
    print("Transactions:\n")
    all_history = ""
    for line in trans_file:
        all_history += ("\n" + line + "\n")
    return all_history


def buy_item(whatInstrument):
    '''Returns total to buy instrument if the input is correct. Returns "Invalid answer." if input isn't correct.'''
    add_item(whatInstrument)
    for line in information:
        if whatInstrument in line[0]:
            item = line[0]
            cost = float(line[2])
            total = add_tax(cost)
            print(get_buy_total(total))
            if int(dict[item]) <= 0:
                print("Item is out of stock.")
                sys.exit()
            else:
                dict[item] = int(dict[item]) - 1
                return (confirm_trans())
    if whatInstrument not in information:
        return ("Invalid answer.")


def return_item(returnWhat):
    '''Lets the user return the item if input is valid then it updates inventory and transaction file. If input isn't valid it returns "Invalid answer." '''
    for line in information:
        if returnWhat in line[0]:
            item = line[0]
            if int(dict[item]) >= 10:
                print("All of those items are now in stock.")
                sys.exit()
            else:
                dict[item] = int(dict[item]) + 1

                with open("inventory.txt", 'w') as inventoryFile:
                    return_output = ''
                    for d in dict:
                        return_output += d + " " + str(dict[d]) + "\n"
                    inventoryFile.write(return_output)
                update_return_date(userEmail, returnWhat)
                return ("Thanks for returning the " + returnWhat + "!")
    if returnWhat not in information:
        return ("Invalid answer.")


def rent_item(whatInstrument):
    ''' Returns total to rent instrument if the input is correct. Returns "Invalid answer." if input isn't correct.'''
    add_item(whatInstrument)
    for line in information:
        if whatInstrument in line[0]:
            item = line[0]
            cost = float(line[3])
            total = add_tax(cost)
            if int(dict[item]) <= 0:
                print("Item is out of stock.")
                sys.exit()
            else:
                dict[item] = int(dict[item]) - 1
                print("Price to rent (per week): " + '\033[1m' + str(total) +
                      '\033[0m')
                print(get_customer_total(how_many_weeks(), total))
                return (confirm_trans())
    if whatInstrument not in information:
        return ("Invalid answer.")


if __name__ == '__main__':
    print("Hello! Welcome to Instru-Rent!")
    user = input("Customer or Employee?").lower().strip()
    if user == "customer":
        print("\nEnter Q to quit\n")
        userEmail = input("Enter your email address: ")
        userEmail = userEmail.lower().replace(" ", "")
        print(valid_email())
        print(
            "\n(R)= rent| (B)= buy| (RT)= return| (S)= search| (H)= all history")
        customerChoice = input("What would you like to do?").lower().strip()

        if customerChoice == "b" or customerChoice == "r":
            add_action(customerChoice)
            print(show_inventory())
            whatInstrument = input("What instrument?  ").lower().strip()
            whatInstrument = whatInstrument.replace(" ", "-")
            print(item_info(whatInstrument))

            if whatInstrument == "q":
                print(cancel_it())

            if customerChoice == "b":
                print(buy_item(whatInstrument))

            elif customerChoice == "r":
                print(rent_item(whatInstrument))

        elif customerChoice == "rt":
            returnWhat = input("Which item are you returning? ").lower().strip(
            )
            returnWhat = returnWhat.replace(" ", "-")
            print(return_item(returnWhat))
            if update_return_date(
                    userEmail,
                    returnWhat) != "Item has already been returned." and update_return_date(
                        userEmail,
                        returnWhat) != "You haven't rented that instrument out.":
                return_item(returnWhat)

        elif customerChoice == "s":
            print("To search a date: m-da-year\nExample: 8-10-1998")
            print(customer_search())

        elif customerChoice == "h":
            print("Here's our history log:\n")
            print(history())

        elif customerChoice == "q":
            print(cancel_it())

        else:
            print("Invalid Answer.")
            sys.exit()

    elif user == "employee":
        print(history())
        print("Revenue:", format_total(revenue))

    else:
        print("Invalid. Try again.")
        sys.exit()
