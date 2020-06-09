#Project - Password Generator
Author - Mitesh Madaan
Contact:-
    Email Id: miteshmadaan1@gmail.com
    Github profile: https://github.com/miteshmadaan
    LinkedIn profile: https://www.linkedin.com/in/mitesh-madaan-35603217a/
    Facebook profile: https://www.facebook.com/mitesh.madaan
Description- This program asks for user's name, id no and date of birth and generates a strongest password using letters and digits from input information. The generated password is mailed to user.
Disclaimer:
    1. Please read How to use clearly before running the program in your console/interpreter.
    2. The author is not responsible for any loss of login details or any act of breaching or hacking caused due to any negligence on the part of user itself.
    3. The author is not responsible for any loss of data or privacy caused by user giving access to less secure third party apps for user's google account.
How to use:-
    1. The main driver code calls for subsidiary modules for specific operations. Before your run the driver code on your system, make sure you have downloaded driver program code and subsidiary modules too. Also make sure you have downloaded them in same folder for better functioning of program.
    2. The program in 'sendMAIL.py' requires permission for sending mails through your email-ID. Make sure you have given access for less secure third party apps for your google account otherwise it will give an error. You can change the permissions by logging in your google account settings. You can turn it off later as it's generally not recommended to do so.
    3. Remember to enter your email address and password for the same before running for logging in through program. Use only google account for the same. Don't show the code with your login details to anyone else. The author is not responsible for loss of login details or any attempt of breaching.
Working:-
	1.Generation of Password:- 
		1.1 All white spaces are removed from user's name.
		1.2 Length of password is determined according to length of user's name.
		1.3 Letters and digits are separated from input data.
		1.4 Letters and digits are separately randomised and no. of characters equal to desired length of password are randomly selected.
		1.5 Output from each are joined and again randomised and no. of characters equal to desired length of password are randomly selected.
		1.5 During password Generation output of previous step and special characters from string module are mixed and randomised to get password of desired length.
		1.6 Strength of password is determined. If strength of newly generated password is greater than that of previous one, then password is updated with the recently generated password and strength too. The process is repeated 10000 times for maximum randomisation thus increasing security.
	2. Calculation of strength:- 
		2.1 The temporarily generated password is  passed to strength calculator which checks it for various parameters and returns the strength for the same.
	3. Sending of mail:-
		3.1 The generated password is passed to mail generator and an appropriate message is drafted for the same.
		3.2 The generated message is sent to user's email. A thank you note is displayed on the prompt screen.
