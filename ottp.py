'''import random
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
'''

''''for i in range(3):
    for j in range(2):
        print(i,j)'''

'''for i in range(3):
    for j in range(4):
        print("*",end=" ")
    print()'''

'''for i in range(2):
    for j in range(1,4):
        print(j,end=" ")
    print()'''
    
'''for i in range(1,4):
    for j in range(3):
        print(i,end="")
    print()'''
#column number pattern
'''for i in range(3):
    for j in range(1,4):
        print('''
#star pyramid(half)
'''for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()'''
#inverted number triangle
'''for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()  '''  
#multiplication grid
'''for i in range(1,4):
    for j in range(1,4):
        print(i*j,end=" ")
    print()
    '''
#checker board pattern
'''for i in range(3):
    for j in range(3):
        print((i+j)%2,end=" ")#prints remainder value
    print()'''
#alphabet pattern
'''for i in range(4):
    for j in range(4):
        print(chr(65+i),end=" ")
    print() '''   


#row-column display
'''for i in range(3):
    for j in range(3):
        print(f"({i},{j})",end=" ")
    print()'''
#even/odd grid
'''for i in range(0,3):
    for j in range(0,3):
        if(i+j)%2==0:
            print("E",end=" ")
        else:
            print("O",end=" ")
    print()'''
#countdown grid
'''num=5
for i in range(3):
    for j in range(3):
        print(num,end=" ")
        num=num-1
    print()'''
#mini quiz
'''questions=["what is capital of India",
           "what is oops?",
           "what is function"]
answers=["delhi","def","for"]
score=0
for i in range(len(questions)):
    print("Question:",questions[i])
    user_answer=input("your answer:").lower()
    if user_answer==answers[i]:
        print("correct")
        score+=1
    else:
        print("wrong")
print("quiz completed")
print("your score:",score,"/",len(questions))'''
#hollow square
'''n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() '''
#left aligned number triangle
'''
num=1
for i in range(1,5):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
'''
#inverted number pyramid
'''for i in range(4,0,-1):
   for j in range(1,i+1):
        print(j,end=" ")
   print()  '''
#alternative star
'''
for i in range(3):
    for j in range(3):
        print("*",end=" ")
    print()    

'''
for i in range(3):
    for j in range(5):
        if j%2==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  


#diagonal star pattern

'''   0  1  2   3
0   *
1       *
2          *
3              *'''
'''for i in range(4):
    for j in range(4):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        

'''
#multiplication table upto 1 to 5
'''for i in range(1,6):
    for j in range(1,6):
        print(i*j,end=" ")
    print()'''    
''' 1   2    3    4    5    
1
2
3
4
5'''
#border number pattern
'''  1 2  3  4
1 1 1  1  1
2 1       1
3 1       1
4 1 1  1  1'''
'''for i in range(1,5):
    for j in range(1,5):
        if i==1 or j==1 or i==4 or j==4:
            print("1",end=" ")
        else:
            print(" ",end=" ")
    print() '''
#chess board
'''  0 1 2 3
0 X 0 X 0
1 0 X 0 X
2
3'''
'''for i in range(4):
    for j in range(4):
        if (i+j)%2==0:
            print("X",end=" ")
        else:
            print("0",end=" ")
    print()  '''      

'''def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, name="Navy", age=20)
'''

#*args
'''
def multiply(*args):
    result=1
    for i in args:
        result=result*i
    print(result)
multiply(3, 4)
'''

#**kwargs
'''def multiply(**kwargs):
    result=1
    for i in kwargs.values():
        result=result*i
    print(result)

multiply(a=3,b=4)'''

'''squares = [i**2 for i in range(1, 6)]
evens = [i for i in range(1, 11) if i % 2 == 0]
div3 = [i for i in range(1, 16) if i % 3 == 0]

print("Squares:", squares)
print("Even numbers:", evens)
print("Divisible by 3:", div3)
'''
#hollow
'''for i in range(5):
    for j in range(5):
        if i==0 or j==0 or i==4 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#
'''num=1
for i in range(3):
    for j in range(3):
        print(num,end=" ")
        num+=1
    print()    
'''
#split list into even and odd
'''num=list(map(int,input("enter elements:").split()))
even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
    
print(even)
print(odd)
'''


'''s = input("Enter a string: ").lower()

vowels = "aeiou"
v_count = 0
c_count = 0

for i in s:
    if i.isalpha():          # ignore spaces, digits, symbols
        if i in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)'''

'''d = {}

n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

swapped = {}

for k, v in d.items():
    swapped[v] = k

print("Original:", d)
print("Swapped:", swapped)      '''   


'''def check_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return "Anagram"
    else:
        return "Not Anagram"

# taking input
str1 = input("Enter input1: ")
str2 = input("Enter input2: ")

# function call
print(check_anagram(str1, str1))'''

'''class student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def calculate_sum(self):
        return self.m1+self.m2+self.m3
    def cal_avg(self):
        return self.calculate_sum()/3
    def display(self):
        print(self.name)
        print(self.calculate_sum())
        print(self.cal_avg())
name=input()
m1=int(input())
m2=int(input())
m3=int(input())
obj=student(name,m1,m2,m3)
obj.display()'''

'''class student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1 + self.m2 + self.m3

    def avg(self):
        return self.total() / 3


# taking user input
name = input("Enter name: ")
m1 = int(input("Enter marks1: "))
m2 = int(input("Enter marks2: "))
m3 = int(input("Enter marks3: "))

# creating object using input
s = student(name, m1, m2, m3)

print("Total:", s.total())
print("Average:", s.avg())'''

'''words = input("Enter words: ").split()

result = list(map(lambda x: x[0], words))

print(result)'''

'''def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")
'''
'''n=int(input())
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()    
    

'''
'''ch=input()
if ch.isalpha():
    print("alphabet")
elif ch.isdigit():
    print("digit")
else:
    print("special characters")'''

s1, s2 = input().split()

count = 0

for ch in s1:
    for ch in s2:
        count += 1
        s2 = s2.replace(ch, "", 1)

print(count)

'''def student(name,age,course):
    print(name,age,course)
student(name="ha",age=12,course="d")  '''  


'''def add_default(a=10,b=1):
    print(a+b)
add_default(5) '''

'''def string(s):
    return s[::-1].upper()
s=input()
print(string(s))'''




'''def count_word(sentence):
    words=sentence.split()
    return len(words)
s=input()
print(count_word(s))'''

'''import math
a=float(input())
result=math.ceil(a)
print(result)
'''
'''from math import sqrt
a=int(input())
reult=sqrt(a)
print(reult)'''




'''from random import choice
a=input().split()
result=choice(a)
print(result)'''
 
 
            
    

        
