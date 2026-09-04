# Python Functions

price = 5000
quantity = 5
total = price * quantity
print(total)

# def function_name():
#     statements

# print("Hello")

def greet():
    print("Hello")

# print(greet() + "World!!")

def greet_name(name): # parameters
    print("Hello", name)

greet_name("Ravi") # arguments

def calculate_total(price, quantity):
    total = price * quantity
    print(total)

calculate_total(1020, 5)
calculate_total(100, 5)

def add(a, b):
    return a + b # sends the value back, reuse the result

print("total : ", add(1,2) + 3)

# greet_name()

def greet_name1(name, message="Hello"):
    print(message, name)

greet_name1("Tharun", "Good Morning!!")

def employee(name, salary):
    print(name, salary)

employee(salary=50000, name="Ravi")

def is_valid(amount, status):
    return amount > 0 and status =="SUCCESS"

print(is_valid(0, "PENDING"))

employees = [
    {"name": "ravi", "salary": 4000},
{"name": "rahul", "salary": 500},
{"name": "priya", "salary": 2000},
{"name": "john", "salary": 3000},
]

def clean_salary(salary):
    return float(salary)

for employee in employees:
    employee["salary"] = clean_salary(employee["salary"])

print(employees)

amount = 5000 # global variable
def calculate():
    amount = 1000 # local variable

print(amount)

calculate()

def calculate_new(a, b):
    total = a + b
    diff = a - b
    return total, diff

total, diff = calculate_new(10, 5), calculate_new(20,30)
print(total)
print(diff)


def calculate_total(numbers):
    return sum(numbers)

numbers = [1, 2 , 3 , 4 ]
print("Total : " , calculate_total(numbers))


def high_salary(employees):
    return [
        employee for employee in employees if employee["salary"] > 500
    ]

print(high_salary(employees))


# def sum(a, b):
#     return a + b

# variable positional arguments
# *args

def add_sum(*args):
    return sum(args)

print(add_sum(10, 20, 30, 40)) # tuple

def show_details(**details):
    for key, value in details.items():
        print(key, ":", value)

    print(details)
    print(type(details))

show_details(name="Ravi", age = 25, salary=2500)

# def square(x):
#     return x * x
# syntax lambda arguments : expression
square = lambda x : x * x

print(square(5))