def validEmail(n):
    '''takes valid email address'''
    n = n.lower().replace(" ", "")
    if "@" and ".com" in n:
        return n
    else:
        return ("Invalid")


if __name__ == '__main__':
    # user = input("Customer or Employee?").lower().strip()
    userEmail = input("Enter your email address: ")
    print(validEmail(userEmail))
