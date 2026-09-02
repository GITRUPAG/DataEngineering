# Python Comprehensions

numbers = [1, 2, 3, 4, 5]

# squares = []
#
# for num in numbers:
#     squares.append(num * num)
#
# print(squares)

squares = [num * num for num in numbers]

# syntax : [expression for variable in collection]

print(squares)

result = [ x * 2 for x in numbers]

print(result)

names = ["ravi", "priya", "john"]

upperNames = [name.upper() for name in names]

print(upperNames)

even_numbers = [num for num in numbers if num % 2 == 0 ]

print(even_numbers)

# list of dictionaries
employees = [
    {"name": "ravi", "salary": 2500},
    {"name": "priya", "salary": 500},
    {"name": "rahul", "salary": 400}
]

names = [emp["name"] for emp in employees if emp["salary"] > 2000]

print(names)

salaries = [1000, 2000, 3000, 4000]

revised = [ salary * 1.10 for salary in salaries if salary > 3000 ]

# [low, low , high, high ]

categories = [ "High" if salary >= 3000 else "low" for salary in salaries]


# 1:1, 2:4, 3:9, 4:16

# squares = {}
#
# for number in numbers:
#     squares[number] = number * number
#
# print(squares)

squares = { number : number * number   for number in numbers}

# { key_expression : value_expression for loop}
print(squares)

nums = [1, 2, 2, 3, 3, 4]

squares_nums = {num * num for num in nums}

list = squares_nums

print(squares_nums)

print(list)