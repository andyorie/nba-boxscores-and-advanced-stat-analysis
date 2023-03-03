''' Asking for the user to enter the string for the path to change the working directory'''

import os

while True:
    print(80*'-')
    print('The Current Working Directory is:', os.getcwd())
    user_confirm_path = input('Is this the correct directory (Y/ N)? ')
    if user_confirm_path.upper() == 'Y':
        print('Great!, Let us proceed')
        break
    else:
        new_path = input("Please enter the path: ")
        os.chdir(new_path)
        print()
        print(80*'-')
        print('Files in Working Driectory:', os.listdir(os.getcwd()))
