# Paswoord-Generator
Project - Password Generator
Author - Mitesh Madaan

Descripton- This program asks for user's name, id no and dob and generates a strongest password using letters and digits from input information. The generated password is mailed to user. 
Procedure:- 
	1.Generation of Password:- 
		1.1 All white spaces are removed from user's name.
		1.2 Length of password is determined according to legth of user's name. 
		1.3 Letters and digits sre seperated from input data.
		1.4 Letters and digits are seperately randomised.
		1.5 Output from each are joined and again randomised. 
		1.5 During password Generation output of previous step and special characters from strimg module are mixed and randomised to get password of predetermined length.
		1.6 Strength of password is determined. If password of newly generated is greater than previous one then password is updated with new strength. The process is repeated 10000 times for maximum randomisation thus increasing security.
	2. Calculation of strength:- 
		2.1 The temporarily generated password is  passed to strength calculator which checks it for various parameters and returns the strength for the same.
	3. Sending of mail:-
		3.1 The generated password is passed to mail genrator and appropraite message is drafted for the same.
		3.2 The generated message is sent to user's email. A thankyou note is displayed on prompt screen.
