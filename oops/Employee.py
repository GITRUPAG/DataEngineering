class Employee:

    def __init__(self, name,age = None):
        self.name = name
        self.age = age

    def display(self):
        print("This is a employee")

# Super() - allows a child class access functionality from its parent class

class Developer(Employee):

    def __init__(self, name, language):
        # self.name = name
        super().__init__(name)  # Employee.__init__()
        self.language = language

    # Method Overriding
    # when a child class provides its own implementations of a method that already exists in the parent class
    def display(self):
        super().display()
        print("This is Developer")


d1 = Developer("Alice", "Python")

print(d1.name)
print(d1.language)

d1.display()


class Tester(Developer, Employee):   # Multiple Inheritance
    None





