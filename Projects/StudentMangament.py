import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="800800",
    database="college"
)
print("Connected!!!")

cursor = connection.cursor() # create cursor

cursor.execute("select * from students") # send select query by using execute

students = cursor.fetchall()
print(students)

# Inserting

query = """
      insert into students(name,age) values(%s, %s)
"""
values = ("Alice", 30)
cursor.execute(query, values)
connection.commit()

# Parameterized query - with placeholders and provide values separately

query = """
      update students set age = %s where id = %s
"""
values = (50, 1)
cursor.execute(query, values)
connection.commit()




# for student in cursor: - # row by row
#     print(student)

# students = cursor.fetchall() - all rows
#
# students1 = cursor.fetchone() - one row
#
# print(students)
#
# print(students1)

connection.close()