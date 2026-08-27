# Loops

# Used to execute a block of code repeatedly n times

employees = ["Ravi", "priya", "John"]

print("Ravi")

for e in employees:
    print(e)

# for loop - iterating over collections

# for variable in collection:
#     statements

name = "python"

for character in name:
    print(character)

# range() - generates of sequence of numbers

for i in range(5): # start with 0 , end with 4
    print(i)

for i in range(2, 6):
    print(i)
print("EVEN")
for i in range(2, 10, 2):
    print(i)

nums = [10, 20, 30, 35,  40, 50]

for num in nums:
    if num % 2 == 0:
        print(num)

for n in range(10):
    if n == 5:
        break # loop terminates
    print(n)

for n in range(10):
    if n == 5:
        continue # skip current iteration & continue with next iteration
    print(n)

# while - runs as long as condition is true

# while condition:
#     statement

count = 1

while count <= 5:
    print(count)
    count += 1