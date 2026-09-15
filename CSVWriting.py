
import csv

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["id", "name", "course"])
    writer.writerow([101, "Alice", "JAVA"])
    students = [
        [101, "Alice", "JAVA"],
        [101, "Alice", "JAVA"],
        [101, "Alice", "JAVA"]
    ]

    writer.writerows(students)