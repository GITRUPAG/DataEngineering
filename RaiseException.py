age = int(input("Enter age: "))

#raise

# raise ExceptionType("Invalid value")

if age < 18:
    raise ValueError("Age must be 18 or above")
print("Valid age")

def calculate_salary(salary):
    if salary < 0:
        raise ValueError("Salary cannot be negative!!")
    return salary

calculate_salary(5000)

try:
    age = 15
    if age < 18:
        raise ValueError("Invalid age")
except ValueError as e:
    print("Error : ", e)
    raise
else:
    print("No error!!")
finally:
    print("Error Handling!!")

try:
    age = 15
    if age < 18:
        raise ValueError("Invalid age")
except ValueError as e:
    print("Error : ", e)
    raise
else:
    print("No error!!")
finally:
    print("Error Handling!!")