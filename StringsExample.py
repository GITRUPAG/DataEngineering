# String is a sequence of characters enclosed inside quotes
name = 'RaviKumar'

# String Slicing
# print(name[start:end])

print(len(name))

print(name[:3])
str = """ Hello,
Morning"""
print(name[0])

name[0] = 'S'

name = "K " + name
print(name)

print("Python " * 3)

print(name.lower())
name.upper()

str = "   python java    "
print(str.title())

print(str.strip())
print(str.lstrip())
str.rstrip()

text = "python is difficult"
text = text.replace("difficult", "easy")
print(len(str))

languages = "Python,java,SQL"
languages = languages.split(",")
print(languages)

result = " ".join(["10, 20"])
print(result)

text = "Python data Engineering"
print(text.find("data"))

fruit = "bananaa"

print(fruit.count("n"))

filename = "orders.csv"

print(filename.startswith("orders"))

print(filename.endswith(".csv"))

value = "1234dddd"
print(value.isdigit())
print(value.isalpha())
print(value.isalnum())

email = "r@gmail.com"
print("@gmail.com" in email)

name = "Alice"
age = 20

message = f"my name is {name} and age is {age} "
print(message)

price = 500
quantity = 3

print(f"Total : {price * quantity}")

print("Hello\nWorld")

print("Hello\tWorld")

print("he said \"HELLO\"")

path = r"c:\users\ravi"

print(path)




