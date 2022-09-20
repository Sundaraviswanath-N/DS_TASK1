'''
Data Science Task 1
Name : Sundaraviswanath N
Batch : D43
Module : registration 
'''


import re

file_name = 'user_data.txt'

def check_email(email_name):
    '''
    Function that returns 'True' if email is a valid email else returns 'False'.
    '''
    #Checks if length of email is non zero
    if len(email_name) == 0:
        return False
    #Checks the starting character of the email
    x = re.search("^[0-9!#$%^&*+-/={|}_~@\.]",email_name)
    if x != None:
        return False
    #Checks for the presence of a single '@' symbol
    x = re.split("@",email_name)
    if len(x) !=2:
        return False
    else:
        #If only a single '@' is present, checks the length of the name and the domain
        if len(x[0]) == 0 or len(x[1]) == 0:
            return False
    #Chcecks the presence of '.' symbol after the '@' symbol
    x = re.split("\.",x[1])
    if len(x) !=2:
        return False
    else:
        if len(x[0]) == 0 or len(x[1]) == 0:
            return False
    #If valid email, retrun True
    return True


def check_password(password):
    '''
    Function that returns 'True' if password is a
    valid password else returns 'False'.
    '''
    #Checks the length of the password, must be 5 < len(pwd) < 16
    if len(password) <= 5 or len(password) >= 16:
        return False
    #Checks if there is at least 1 DIGIT in the password
    x = re.findall('[0-9]',password)
    if len(x) == 0:
        return False
    #Checks if there is at least 1 LOWERCASE alphabet in the password
    x = re.findall('[a-z]',password)
    if len(x) == 0:
        return False
    #Checks if there is at least 1 UPPERCASE alphabet in the password
    x = re.findall('[A-Z]',password)
    if len(x) == 0:
        return False
    #Checks if there is at least 1 SYMBOL in the password
    x = re.findall('[~!@#$%^\]\[\(\)\{\}]',password)
    if len(x) == 0:
        return False
    return True

def check_email_in_file(email_entered):
    '''
    Check if the email used to register is already present in the file.
    '''
    file_handle = open(file_name,'r')
    for line in file_handle:
        email = re.split("\s",line)[0]
        if email == email_entered:      #Checking if the email is already present in the file.
            file_handle.close()
            return True
    file_handle.close()
    return False

def upload_to_file(email,password):
    '''
    Writing the valid username and password to the file.
    '''
    file_handle = open(file_name,'a')
    string_to_be_written = email + ' ' + password + '\n'
    file_handle.write(string_to_be_written)
    file_handle.close()

def password_requirements():
    '''
    Password Requirements.
    '''
    print("\nThe password must contains.")
    print("1. Atleast 1 digit.")
    print("2. Atleast 1 uppercase .")
    print("3. Atleast 1 lowercase .")
    print("4. Atleast 1 special character.")
    print("5. Length of the password must more than 5 characters.\n")


def register():
    print("\nREGISTRATION PAGE.")                
    print("Choose (B) to go back to Main Menu.\n")
    
    while(True):
        #Accepting user email as input.
        user_email = input("Enter the email id : ")
        if user_email.upper() == 'B':
            print("\nMAIN MENU.\n")
            return
        
        if (check_email(user_email)==True): #Checking if the user email is a valid email.
            if check_email_in_file(user_email) == False: #If the email is valid, checking if it is already present in the file.
                break
            else:
                print("This email address is already registered in the portal.")
                print("Loading MAIN MENU.\n")
                return
        else:
            print("Please enter a valid email address!")
    print("Email address",user_email,"validated.")
    
    while(True):
        #Accepting the user password as input.
        password_requirements()
        user_password = input("Enter the password : ")
        if user_password.upper() == 'B':
            print("\nMAIN MENU.\n")
            return;
        if (check_password(user_password)==True):   #Checking is password satisfies the requirements.
            break
        else:
            print("Please enter a valid password!")
            password_requirements()       # If the password is invalid, display the password rules.
            
    #Uploading the valid credentials to the file.
    upload_to_file(user_email,user_password)
    
    print()
    print(user_email,"succesfully registered in the portal.\n")
    print("Login using the registered credentials.\n")
