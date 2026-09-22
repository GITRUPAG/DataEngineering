class Student:

    college = "SVEC"
    def __init__(self, name, age = None):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)


# creating object
s1 = Student("Rupa", 21) # __init__("Rupa",21)
s2 = Student("Alice", 50)

s1.display()

print(s1.college)

print(s2.college)

print(s1.name)

# Attributes
# s1.name = "Rupa"
# s1.age = 50
#
# s2 = Student() # creating a object
# s2.name = "Alice"
#
# print(s1.name)
# print(s1.age)
# print(s2.name)
#
# print(type(s1))