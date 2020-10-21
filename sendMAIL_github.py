#Mail generator
import smtplib
def send_mail(password,email_id):#getting input for password and receiver's email id
    s = smtplib.SMTP('smtp.gmail.com', 587)#setting of server id
    s.starttls()#generating of secure login pathway
    s.login("sender's email ID", "sender's Email ID password")#login details
    message = "\n\nHello Buddy. I am <sender's name>.\nAs a part of my project Password Generator which uses letters and digits from" \
                   " your name, id no. and date of birth and generates a strongest possible password.\n" \
                   "your generated password is '" + password + "'\n" \
                   "I hope you like it.\n\nThank You\n\n"#message to be sent
    s.sendmail("sender's email ID", email_id, message)#sending the mail
    s.quit()#logging out of mail id



