#hello name
name=input("Enter you name: ")
print("Hello",name)


#sum
a=int(input("Enter number: "))
b=int(input("Enter number: "))
sum = a+b
print("the sum is:",sum)


#print age eligible for voting
age=int(input("Enter your age: "))
if age>=18:
    print("User is eligible for voting")
else:
    print("Not eligible for voting")

#even odd number
number=int(input("Enter a number: "))
if number%2 == 0:
    print("Even number")
else:
    print("Odd number")


#square number
number=int(input("Enter a number: "))
square=number ** 2
print("Square:",square)


#largest number
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

if a>=b and a>=c:
    print("largest number is:",a)
elif b>=a and b>=c:
    print("largest number is:",b)
else:
    print("largest number is:",c)


#positive negative zero number
n=int(input("enter a number:"))
if n>0:
    print("Positive Number")
elif n<0:
    print("Negative Number")
else:
    print("Zero")


#print marks
marks=int(input("Enter the marks:"))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail!")



#print number 1 to 10
for i in range(1,11):
    print(i)

for i in range(1,21):
    if i%2 == 0:
        print(i)


n=int(input("Enter number:"))
total = 0
for i in range(1,n+1):
    total += i
print("Sum =",total)


#table    
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


#reverse counting
for i in range(10,0,-1):
    print(i)