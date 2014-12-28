def checkio(data):
    if len(data) < 10:
        return False
    elif data.isalpha():
        return False
    elif data.isalnum():
        return False
    elif data.isdigit():
        return False
    elif data.islower():
        return False
    elif data.isupper():
        return False
    else:
        for x in data:
            if x.isalnum() == False:
                return True

    #replace this for solution
    return True or False

#Some hints
#Just check all conditions
