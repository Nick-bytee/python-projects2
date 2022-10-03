import re
from email_validator import validate_email, EmailNotValidError

e_mail = input("Enter Your E-mail Address: ")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def checkemail(email):
    if(re.fullmatch(regex, email)):
        print('Valid Email')
    else:
        print('Invalid Email')

#checkemail(e_mail)


#email validation using module

def check_mail_module(email):
    
    try:
        validate_email(email)
        print("Valid E-mail")
    except EmailNotValidError as e:
        print(str(e))

check_mail_module(e_mail)