#Project Name: Password Generator
#Author: Mitesh Madaan
#Description: This project generates strongest possible password using letters and digits from name, id no. and dob of the user
#The generated password is sent as mail to user
#                                         *****************************START******************************
#imporitng necessary module for generating passwords, checking password strength, sending mail
import secrets
import pswdstrength_github
import sendMAIL_github
import string
#Getting user information
name = str(input("please enter your complete name:\t"))#input prompt for user's name
id_no = str(input("please enter your complete ID NO.:\t"))#input prompt for user's id no
dob = str(input("please enter your date of birth in format ddmmyyyy:\t"))#input prompt for user's dob
email_id =  str(input("please enter your email id:\t"))#input prompt for user's email id
#request to wait until password is generated and mailed
print("\nWait for few seconds until password is generated.\n")
#converting input data into usable data for program.
data1 = name.replace(" ","")# removing all whitespaces
data2 = id_no
data3 = dob
#calculating length of password on the basis of length of user's name
if len(name) <= 15: length = len(data1)
else: length = 15 + 15//len(data1)
#combining data for separating letters and digits.
data = ''.join(i for i in data1+data2+data3 if  i.isalpha())
digit = ''.join(i for i in data1+data2+data3 if i.isdigit())
#randoming the data for security reasons
data = ''.join(secrets.choice(data) for i in range(length))# level 1 randomization
digit = ''.join(secrets.choice(digit) for i in range(length))
data =''.join(secrets.choice(data+digit) for i in range(length))# level 2 randomization
#declarating variables to store password and strength
password = ""
strength = 0
#loop for searching for strongest password.
for i in range(10000):
    pwd = ''.join(secrets.choice(data+string.punctuation) for k in range(length)) # Generation of password and level 3 randomization
    if pwd == "":
        continue
    if pswdstrength_github.strength_calculator(pwd) > strength:#if strength of new password is greater than previous one...
            password = pwd#replace previous one with new one
            strength = pswdstrength_github.strength_calculator(pwd)#update new strength
#sending password and email to mail generator to send mail
sendMAIL_github.send_mail(password,email_id)
#thankyou note for user
print("Your Generated password has been sent to your email.\nThank You for being a part of my project\n")
#                                         *****************************END******************************
