# allows a program to make a decisions based on condition

# if condition:
#     statement

age = 15
salary = 852963
if age >= 18 and salary > 5000:
    print("Adult")
else:
    print("Minor")

active = True

if not active:
  print("Active!!")

marks = 75
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")

if age >= 18:
    if active:
        print("Acess ganted!!!")

customer_name = None

if customer_name is None:
    print("name is missing!!")

email = "ravi@gmail.com"

if "@" in email:
    print("valid email")
else:
    print("Not Valid")

status = "Adult" if age >= 18 else "Minor"
print(status)

name = []
if name:
    print("exists")
else:
    print("empty")