# Collection - store multiple values in a single variable

emp = "Ravi"
emp1 = "Rahul"

employees = ["", ""]

# list
# tuple
# set
# dictionary

# list - ordered , mutable collection
nums = [10, 20, 30, 40, 40, 20]

sum = 0

for num in nums:
    sum += num
print(sum)

list1 = ["Ravi", "rahul"]

list1.append("Priya")

list1.insert(1, "Anu")

list1.remove("rahul")

print(list1.pop(0))

# list1.clear()

print(list1)

print(len(list1))

for name in list1:
    temp = name + "john"
    print(temp)

# list slicing
print(nums[0:2])

list2 = [10, "Ravi", 25.5]

print(nums)

print(list2)

print(nums[-1])

# Tuple - immutable collection

employee = ("Ravi", 25, 5000)

print(employee[0])

employee[1] = 50

#set - unordered , No duplicates

numbers = {10, 20, 30, 30, 40, 40, 50}

print(numbers)

# Dictionary  key -> value

student = {
    "name": "rupa",
    "age": 25,
    "salary": 25000,
    25: "R",
    "address": "AP"
}

print(student["name"])
print(student[25])

student["marks"] = 50

print(student)

student["marks"] = 500

print(student)

student.pop("age")

print(student)

# student.keys(), student.values(), student.items()

print(student.items())

for key, value in student.items():
    print(key, ' : ', value)

print(student.keys())

print(student.values())

company = {
    "name" : "ABC",
    "employees":
     [
         {"name":"ravi", "salary":25000},
         {"name":"ravi", "salary":2500}
     ],
    "address" : {
        "state": "AP",
        "Pincode":5241547
    }
}

print(company["employees"][0]["name"])

