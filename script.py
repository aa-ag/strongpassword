###--- IMPORTS ---###
import re


###--- FUNCTIONS ---###
def check_strenght():
    user_input = str(input("Enter the password:\n"))

    if(len(user_input) >= 8):
        if(bool(re.match(r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,20})', user_input)) == True):
            print("strong")
        elif(bool(re.match(r'((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,20})', user_input)) == True):
            print("weak")
    else:
        print("invalid")


###--- DRIVER CODE ---###
if __name__ == "__main__":
    check_strenght()
