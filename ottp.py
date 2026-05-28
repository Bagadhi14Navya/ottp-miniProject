import random
import math
import smtplib#simple mail transfer protocol library
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
msg=OTP
email=input("enter the mail which you want to send otp")
s=smtplib.SMTP("smtp.gmail.com",587)
s.login("navyabagadhi@gmail.com","ivah whnl foco nsdn")
s.starttls()
user="navyabagadhi@gmail.com"
s.sendmail(user,msg,email)
while True:
    otp=input("enter the otp")
    if otp==otp:
        print("login successful")
    else:
        print("incorrect otp")

        return self.total() / 3













 
 
            
    

        
