###--- IMPORTS ---###
import re


###--- FUNCTIONS ---###
def check_strenght():
    user_input = input('Enter your password:\n')
    if len(user_input) >= 8:
        print('ok')
    else:
        print('not ok')


###--- DRIVER CODE ---###
if __name__ == "__main__":
    check_strenght()
