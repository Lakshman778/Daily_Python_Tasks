#1. Print even numbers from 1 to 20
n=20
for i in range(1,n+1):
    if i%2==0:
        print(i)

#2. Print odd numbers from 1 to 20
n=20
for i in range(1,n+1):
    if i%2!=0:
        print(i)

#3. Print numbers from 1 to 50
n=50
for i in range(1,n+1):
    print(i)

#4. Print multiples of 5 from 5 to 50
n=50
for i in range(5,n+1):
    if i%5==0:
        print(i)

#5. Print multiples of 3 from 3 to 30
n=30
for i in range(3,n+1):
    if i%3==0:
        print(i)

#6. Print the first 10 natural numbers
for i in range(1,11):
    print(i)

#7. Print the first 10 numbers in reverse order
for i in range(10,0,-1):
    print(i)

#8. Print numbers from 1 to n
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i)