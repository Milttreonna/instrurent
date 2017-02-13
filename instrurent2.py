from openedFiles import *
import sys


def validEmail():
    '''Takes user's email and checks to see if it's valid or not'''
    print("Enter Q to quit\n")
    userEmail = input("Enter your email address: ")
    userEmail = userEmail.lower().replace(" ", "")

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


if __name__ == '__main__':
    user = input("Customer or Employee?").lower().strip()
    if user == "customer":
        print(validEmail())
