# Lambda Functions -

# DAta processing and transformation
#
# Lambda
# Map
# filter
# reduce

# lambda arguments : expression

add = lambda a, b, c : a + b - c

check_age = lambda age : "adult" if age >=18 else "Minor"

print(check_age(18))

print(add(10, 10, 5))

students = [
    {"name": "alice", "marks": 50},
   {"name": "bob", "marks": 503},
  {"name": "john", "marks": 8},
]

marks = map(lambda m: m["marks"], students)

print("Marks")
print(list(marks))

get_marks = lambda student : student["marks"]

print(get_marks(students[0]))

numbers = [1, 2, 3, 4, 5] # Iterable

# Map() - Transform every item

result = map(lambda x : x * 2, numbers)
print(list(result))

nums = ["10", "20", "30"]

numbers = map(int, nums)

print("Strings - Integers")
print(list(numbers))


names = ["ravi", "priya"]

res = map(str.upper, names)

print(list(res))

# Filter() - to select items that satisfy a condition


# filter(function, iterable)

n = [10, 20, 30, 40, 50, 60, 70 ]

result = filter(lambda x : x > 20, n)

evens = filter(lambda x : x %2 == 0, n)

print(list(evens))

print(list(result))

def is_adult(age):
    return age>= 18

ages = [12, 18, 36]

adults = filter(is_adult, ages)

print(list(adults))
