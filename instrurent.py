def validEmail(n):
    '''takes valid email address'''
    n = n.lower().replace(" ", "")
    if "@" and ".com" in n:
        return n
    else:
        return ("Invalid")
