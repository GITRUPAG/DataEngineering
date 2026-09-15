# CSV - Comma separated values
# stores data in rows and columns

import csv

with open("employee.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        employee_id = int(row[0])
        name = row[1]
        salary = float(row[2])

        print(employee_id, name, salary)
with open("employee.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

with open("students.csv", "w") as file:
    writer = csv.writer(file)

    writer.writerow("id","name","course")
    writer.writerow(101,"Alice","JAVA")


