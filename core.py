from openedFiles import *
from instrurent import *
import sys


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
