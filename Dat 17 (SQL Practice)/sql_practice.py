import sqlite3

def connect_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn,cursor

def questions(cursor : sqlite3.Cursor):

    print("-" * 30 + "Questions - Basic" + "-" * 30)
    print("\n")

    #1
    print("-" * 30 + "Bring all data from courses" + "-" * 30)
    cursor.execute("SELECT * FROM Courses")
    course_data = cursor.fetchall()
    for i in course_data:
        print(f"id : {i[0]}, Course Name : {i[1]}, Instructor : {i[2]}, Credits : {i[3]}")
    print("\n")

    #2
    print("-" * 30 + "Bring insturctor name and course name from  courses" + "-" * 30)
    cursor.execute("SELECT instructor, course_name FROM Courses")
    instructor_and_course_name = cursor.fetchall()
    for i in instructor_and_course_name:
        print(f"Instructor : {i[0]}, Course Name : {i[1]}"),
    print("\n")

    #3
    print("-" * 30 + "Bring students who are 21 years old" + "-" * 30)
    cursor.execute("SELECT * FROM Students WHERE age = 21")
    age_data = cursor.fetchall()
    for i in age_data:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

    #4
    print("-" * 30 + "Bring students who live in Chicago" + "-" * 30)
    cursor.execute("SELECT * FROM Students WHERE city = 'Chicago'")
    city_data = cursor.fetchall()
    for i in city_data:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

    #5
    print("-" * 30 + "Bring Dr.Anderson's courses" + "-" * 30)
    cursor.execute("SELECT * FROM Courses WHERE instructor = 'Dr. Anderson'")
    insturctor_data = cursor.fetchall()
    for i in insturctor_data:
        print(f"id : {i[0]}, Course Name : {i[1]}, Instructor : {i[2]}, Credits : {i[3]}")
    print("\n")

    #6
    print("-" * 30 + "Bring students whose name starts with A" + "-" * 30)
    cursor.execute("SELECT * FROM Students WHERE name LIKE 'A%'")
    name_data = cursor.fetchall()
    for i in name_data:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

    #7
    print("-" * 30 + "Bring courses that have 3 or more credits" + "-" * 30)
    cursor.execute("SELECT * FROM Courses WHERE credits >= 3")
    credits_data = cursor.fetchall()
    for i in credits_data:
        print(f"id : {i[0]}, Course Name : {i[1]}, Instructor : {i[2]}, Credits : {i[3]}")
    print("\n")


    print("-" * 30 + "Questions - Detailed" + "-" * 30)
    print("\n")

    #1
    print("-" * 30 + "Bring students alphabetical order by name" + "-" * 30)
    cursor.execute("SELECT * FROM Students ORDER BY name")
    order_by_name_data = cursor.fetchall()
    for i in order_by_name_data:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

    #2
    print("-" * 30 + "Bring students who are aged 21 or older ordered by name" + "-" * 30)
    cursor.execute("SELECT * FROM Students WHERE age >= 21 ORDER BY name")
    aged_21_or_older_ordered_by_name = cursor.fetchall()
    for i in aged_21_or_older_ordered_by_name:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

    #3
    print("-" * 30 + "Bring students who lives in Chicago or New York" + "-" * 30)
    cursor.execute("SELECT * FROM Students WHERE city IN ('Chicago','New York')")
    aged_21_or_older_ordered_by_name = cursor.fetchall()
    for i in aged_21_or_older_ordered_by_name:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

    #4
    print("-" * 30 + "Bring students who do not lives in New York" + "-" * 30)
    cursor.execute("SELECT * FROM Students WHERE city != 'New York'")
    aged_21_or_older_ordered_by_name = cursor.fetchall()
    for i in aged_21_or_older_ordered_by_name:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")


if __name__ == "__main__":
    try:
        conn,cursor = connect_database()
    except sqlite3.Error as e:
        print(e)
    try:
        questions(cursor)
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()