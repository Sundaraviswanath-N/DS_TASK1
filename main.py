'''
Data Science Task 1
Name : Sundaraviswanath N
Batch : D43
Module : Main 
'''

#importing necessary libraries
import registration
import login

#Welcome message of the portal

print(" WELCOME ")

 
while(True):
    #List of features provided by the portal
    print("What do you want to do?")
    print("Press (R) to Register.")
    print("Press (L) to login .")
    print("Press (Q) to Exit.\n")
    
    #Accepting the functionality option as input from the user
    user_input = input("Enter your input R/L/Q : ")

    #Checking the user input
    if (user_input.upper() == 'Q'):         #Quitting the PORTAL
        print("\nThank you for using the Portal.")  
        break 
    elif (user_input.upper() == 'L'):       #Login Page
        login.login()
    elif (user_input.upper() == 'R'):       #Registration Page
        registration.register();
    else:
        print("\nInvalid command, please enter R/L/Q.\n")