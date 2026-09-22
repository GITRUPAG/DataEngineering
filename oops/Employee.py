class Employee:

    def __init__(self, name):
        self.name = name


class Developer(Employee):

    def __init__(self, name, language):
        self.name = name
        self.language = language


d1 = Developer("Alice", "Python")

