# - to opening a file   - open(filename, mode)
file = open("orders.txt", "r")
# File Modes
# r - read
# w - write
# a - append
# x - create
# r+ - Read + write

data = file.read()

print(data)
file.close()

with open("orders.txt", "r") as file:
    data = file.read()
    print(data)


print("Read line by line")
with open("orders.txt", "r") as file:
    for line in file:
        print(line)

with open("orders.txt", "r") as file:
     print(file.readline())
     print(file.readline())

with open("orders.txt", "r") as file:
    print(file.readlines())

file = open("data.txt", "w")
file.write("Hello Python\n Hello c++\n")
file.write("Hello JAVA\n") # except string
file.write(str(25))
file.close()

order_id = 101
amount = 5000
status = "SUCCESS"

orders = [
    {"id":101, "amount":500},
{"id":102, "amount":200},
{"id":103, "amount":600}
]
with open("data.txt", "a") as file:
    file.write("New Line\n")
    file.write(f"{order_id},{amount},{status}\n")
with open("data.txt", "a") as file:
    for order in orders:
        file.write(f"{order['id']},{order['amount']}\n")

with open("data.txt", "r+") as file:
    data = file.read()
    print(data)

    file.write("New data\n")

with open("data.txt", "w+") as file:
    file.write("New data1\n")

    data = file.read()
    print(data)
with open("data.txt", "a+") as file:
    file.write("New data2\n")
    file.seek(0)
    data = file.read(5)
    print(data)
    print(file.tell())

    # data1 = file.read()
    # print(data1)

