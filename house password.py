def checkio(password: str)-> bool:
    status = False
    if len(password) >= 10 and password.isascii():
        for i in password:
            if i.isdigit():
                status = True
                break
        for i in password:
            if i.isupper():
                status1 = True
                break
        for i in password:
            if i.islower():
                status2 = True
                break
        if status and status1 and status2:
            return True
        else:
            return False
    else:
        return False

# du naprogramovat to krajsie
