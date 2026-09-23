# MAgic Methods -

# __str__()

class student:
    def __init__(self, name,age= None, salary= None):
        self.name = name
        self.age = age
        self.salary = salary
    def __str__(self): # defines the human readable string representaion of a object
       return f"{self.name} - {self.age}" # must return string
    def __len__(self):
        return len(self.name)
    def __eq__(self, other):
        return self.name == other.name
    def __add__(self, other):
        return self.salary + other.salary


s = student("Alice", 21)

print(s)
print(len(s))

s1 = student("Bob",20, 500)
s2 = student("John", 30, 500)

print(s1 == s2)

print( s1 + s2)