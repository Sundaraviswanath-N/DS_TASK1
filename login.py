'''
Data Science Task 1
Name : Sundaraviswanath N
Batch : D43
Module : Login 
'''

import re
import registration

file_name = 'user_data.txt'


def authenticate(email,password):
    
    '''
    Authentication function, that returns true if authenticated 
    and false if the credentials do not match the data in file.
    '''
    
    file_handle = open(file_name,'r')
    for line in file_handle:
        data = re.split("\s",line)
        if data[0] == email:
            if data[1] == password:
                file_handle.close()
                return True
            else:
                file_handle.close()
                return False
            

def retrieve_password(email):
    '''
    Function that retrieves the old password 
    from the file for the user.
    '''
    
    file_handle = open(file_name,'r')
    for line in file_handle:
        data = re.split("\s",line)
        if data[0] == email:
            print("The retrieved password is :", data[1])
            return


def change_password(email):
    '''
    Function allows the user to change 
    his old password to a new password.
    '''
    
    file_content = []    #Creating a empty list to store the contents of the file.
    file_handle = open(file_name,'r')
    for line in file_handle:
        data = re.split("\s",line)
        if data[0] == email:        #Store all the data except the data which needs modification.
            continue
        else:
            file_content.append(line)
    while(True):
        new_password = input("Enter the new password : ")      #Accept new password from user.
        if new_password.upper() == 'B':
            file_handle.close()
            return
        
        if registration.check_password(new_password) == True:    #Check the validity of the password.
            break
        else:
            print("\nEnter a valid password.")
            registration.password_requirements()   #Display the password requirements, if password is invalid.
            
    changed_data = email + " " + new_password + "\n"  
    file_content.append(changed_data)         #Append the changed data(email + password) to the list.
    file_handle.close()
    
    file_handle = open(file_name,'w')      #Overwrite the existing file with the contents of the List.
    for i in file_content:
        file_handle.write(i)
    file_handle.close()
    print("\nPassword successfully changed.")
        
    

def login():
    print("\nLOGIN PAGE.")                         
    print("Choose (B) to go back to Main Menu.\n")
    
    while(True):
        #Accepting user email as input.
        user_email = input("Enter the registered email address : ")
        if user_email.upper() == 'B':
            print("\nMAIN MENU.\n")
            return
        

        if (registration.check_email(user_email)==True):         #Checking if the user email is a valid email address.
            if registration.check_email_in_file(user_email) == True: #Checking if the email entered is present in the file.
                break
            else:
                print("\nEmail address not registered, please register before login.")
                print("\nMAIN MENU.\n")
                return
        else:
            print("Please enter a valid email address!")

    while(True):
        #Accepting the user password as input.
        user_password = input("Enter the password : ")
        if user_password.upper() == 'B':
            print("\nMAIN MENU.\n")
            return
        #Password Reset Feature
        if user_password.upper() == 'F':
            while(True):
                option = input("Do you want to retrieve the old password (O) or change the password (N)? : ")
                if option.upper() == 'O':
                    retrieve_password(user_email)  #Function that retrieves the old password.
                    return
                elif option.upper() == 'N':
                    change_password(user_email)    #Function that changes old password to a new user defined password.
                    return
                elif option.upper() == 'B':
                    print("\nMAIN MENU.\n")
                    return
                else:
                    print("\n Invalid option entered. Please re-enter a valid option.")

        #Authenticating the user email and password.                
        if authenticate(user_email,user_password) == True:
            print("\nLOGIN SUCCESSFUL.\n")
            break
        else:
            print("\nAuthentication Error! Re-enter the password.")
            print("In case you have forgotten your password choose (F).\n")