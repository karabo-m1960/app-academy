#numeric data

num = 1
print(num)
print(type(num))

num = 1.0
print(num)
print(type(num))

#numeric data operations

x = 10
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)

x=10
x -= 2
print(x)

#conditional statements 

score = int(input("Enter the student's score: "))

if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score < 90:
    print("Grade B")
elif score >= 70 and score < 80:
    print("Grade C")
elif score >= 60 and score < 70:
    print("Grade D")
else:
    print("Grade F")


#control statements

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
 print(num1, "is greater than", num2)
elif num2 > num1:
 print(num2, "is greater than", num1)
else:
 print("Both numbers are equal")