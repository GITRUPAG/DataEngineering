# Collection of elements stored under one varoable name

from array import array

numbers = array('i', [10, 20, 30])

# typecodes
# i - signedinteger - -ve, 0, +ve
# I - unsignedInteger - 0, +ve
# f
# d
# q - signed long integer - -ve, 0, +ve
# Q - unsigned long Integer - 0, +ve
print(numbers[1])

# updating an element
numbers[1] = 100

# adding element - append()

# numbers.append(50) - adding element to the end

# extend() - to add multiples

numbers.extend([60, 70, 90])

# insert() - adds an element at a specifi position

numbers.insert(1, 15)

numbers.remove(30)

numbers.pop(5) # removes an element by using its index

# print(numbers.index(30))

print(numbers.count(10)) # counting elements

print(len(numbers))


for number in numbers:
    print(numbers)

print(numbers[3:])

numbers.reverse()

my_list = numbers.tolist()

print(my_list)

x = list(numbers)
print(x)
