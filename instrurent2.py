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
        return validEmail()


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


# def rent_noTax():
def rent_price(price):
    '''Takes the instrument's price and gets 13 percent of it'''
    rent = round(price * .13, 2)
    return rent


def itemInfo():
    if whatInstrument == "clarinet":
        print(clarinet)
        rent_total = add_tax(rent_price(clarinetCost))
        buy_total = add_tax(clarinetCost)
    elif whatInstrument == "piano":
        print(piano)
        rent_total = add_tax(rent_price(pianoCost))
        buy_total = add_tax(pianoCost)
    elif whatInstrument == "violin":
        print(violin)
        rent_total = add_tax(rent_price(violinCost))
        buy_total = add_tax(violinCost)
    elif whatInstrument == "electricguitar":
        print(electricguitar)
        rent_total = add_tax(rent_price(eguitarCost))
        buy_total = add_tax(eguitarCost)
    elif whatInstrument == "acousticguitar":
        print(acousticguitar)
        rent_total = add_tax(rent_price(aguitarCost))
        buy_total = add_tax(aguitarCost)
    elif whatInstrument == "banjo":
        print(banjo)
        rent_total = add_tax(rent_price(banjoCost))
        buy_total = add_tax(banjoCost)
    elif whatInstrument == "trumpet":
        print(trumpet)
        rent_total = add_tax(rent_price(trumpetCost))
        buy_total = add_tax(trumpetCost)
    elif whatInstrument == "saxophone":
        print(saxophone)
        rent_total = add_tax(rent_price(saxCost))
        buy_total = add_tax(saxCost)
    elif "conga" in whatInstrument:
        print(conga)
        rent_total = add_tax(rent_price(congaCost))
        buy_total = add_tax(congaCost)
    elif "drum" in whatInstrument:
        print(drums)
        rent_total = add_tax(rent_price(drumCost))
        buy_total = add_tax(drumCost)
    else:
        print("Invalid")

    if customerChoice == "b":
        total_dict["Total"] = (format_total(buy_total))
        userInfo_lst.append(total_dict)
        return ("\nPrice to buy: " + '\033[1m' + str(buy_total) + '\033[0m')

    elif customerChoice == "r":

        return ("\nPrice to rent (per week): " + '\033[1m' + str(rent_total) +
                '\033[0m')


if __name__ == '__main__':
    user = input("Customer or Employee?").lower().strip()
    if user == "customer":
        print("Enter Q to quit\n")
        userEmail = input("Enter your email address: ")
        userEmail = userEmail.lower().replace(" ", "")

        print(validEmail())
        print(
            "\n(R)= rent| (B)= buy| (RT)= return| (S)= search| (H)= user history")
        customerChoice = input("What would you like to do?").lower().strip()
        if customerChoice == "b":
            print(show_inventory())
            whatInstrument = input("What item would you like to buy?")

            print(itemInfo())
        elif customerChoice == "r":
            print(show_inventory())
            whatInstrument = input("What item would you like to rent?")
            print(itemInfo())
