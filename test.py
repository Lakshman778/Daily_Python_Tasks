# 1)What is python
#Python is a high-level,dynamically typed,interpreted programming language used in many domains like web dev,data science,AIML etc.It is a language used to communicate btw human and the machine.

# 2)what are keywords and identifiers and write rules for identifiers.
# Keywords are the pre-defined words in python which have meaning and cant be usedd as variable names. Identifiers are the names given to variables,they save the memory address of the variable in the database.
# Rules:
# -->No special characters except underscore
# -->Cant start with numbers but can contain them
# -->Cant be a keyword
# -->Should start with alphabets(a-z,A-Z) or underscore.

# 3) Write a program to check a number Is even or odd
n=int(input("Enter a number:"))
if n%2==0:
    print("Even")
else:
    print("Odd")

# 4)prime number checker
n= int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("Not Prime")

# 5)prime number without counting factors
n= int(input("Enter a number:"))
if n>1:
    for i in range(2,int(n/2)+1):
        if n%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")

# 6)check whether a string is palindrome or not
s=input()
rev=s[::-1]
if s==rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# 7)count the number of digits  ex :- 12345 --> 5
n=int(input("Enter a number:"))
count=0
while n>0:
    n=n//10
    count+=1
print("No.of digits:",count)
# (or)
n=int(input("Enter a number:"))
s=str(n)
count=len(s)
print("No.of digits:",count)

# 8)find even count and odd count in a number ex: 23412  even=3 odd=2
n=int(input("Enter a number:"))
even_count=0
odd_count=0
while n>0:
    digit=n%10
    if digit%2==0:
        even_count+=1
    else:
        odd_count+=1
    n=n//10
print("Even count:",even_count)
print("Odd count:",odd_count)

# 9)Take year and input from the user and check whether it is leap year or not
n=int(input("Enter a year:"))
if n%4==0 and n%100!=0 or n%400==0:
    print("Leap year")
else:
    print("Not a Leap Year")

# 10)Take input from user
# marks > 95 --> grade A
# marks >80 -->grade B
# marks >70-->grade c
# marks > 60 --> grade d
n=int(input("Enter marks:"))
if n>95:
    print("Grade A")
elif n>80:
    print("Grade B")
elif n>70:
    print("Grade C")
elif n>60:
    print("Grade D")
else:
    print("Better luck next time")