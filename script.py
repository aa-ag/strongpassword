###--- IMPORTS ---###
import re


###--- FUNCTIONS ---###
def check_strenght():
    '''
      password must have: 
      - 8 or more characters, less than or exactly 20.
      - at least 1 digit.
      - at least 1 lowercase character
      - at least 1 uppercase character
      - at least 1 special character
    '''
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
