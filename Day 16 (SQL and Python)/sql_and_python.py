import sqlite3
import os

def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    return conn, cur

def create_tables(cursor : sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
                                        id INTEGER PRIMARY KEY,
                                        name VARCHAR(255) NOT NULL,
                                        age INTEGER,
                                        email VARCHAR UNIQUE,
                                        city VARCHAR
                                        )
                    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
                                        id INTEGER PRIMARY KEY,
                                        course_name VARCHAR(255) NOT NULL,
                                        insturctor TEXT,
                                        credits INTEGER
                                        )
                    ''')

def insert_data(cursor : sqlite3.Cursor):
    students = [
        (1, "Alice Johnson", 20, "janedoe@gmail.com", "California"),
        (2, "Bob Smith", 19, "bob@gmail.com", "Chicago"),
        (3, "Carol White", 21, "carol@gmail.com", "Boston"),
        (4, "David Brown", 23, "david@gmail.com", "New York"),
        (5, "Emma Davis", 22, "emma@gmail.com", "Seattle")
    ]
    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", students)

    courses = [
        (1, "Python Programming", "Dr. Anderson", 3),
        (2, "Web Development", "Prof. Wilson", 4),
        (3, "Data Science", "Dr. Taylor", 5),
        (4, "Mobile Apps", "Prof. Garcia", 6)
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)", courses)

def basic_sql_query(cursor : sqlite3.Cursor):
    print("\n")
    # SELECT ALL
    print("-" * 30 + " Select All " + "-" * 30)
    cursor.execute("SELECT * FROM Students")
    all_data = cursor.fetchall()
    for i in all_data:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

    # SELECT COLUMNS
    print("-" * 30 + " Select Columns " + "-" * 30)
    cursor.execute("SELECT name, age FROM Students")
    column_data = cursor.fetchall()
    for i in column_data:
        print(f"Name : {i[0]} Age : {i[1]}")
    print("\n")

    # WHERE Clause
    print("-" * 30 + " WHERE age = 20 " + "-" * 30)
    cursor.execute("SELECT * FROM Students WHERE age = 20")
    age_data = cursor.fetchall()
    for i in age_data:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

    # WHERE Clause
    print("-" * 30 + " WHERE city = New York " + "-" * 30)
    cursor.execute("SELECT * FROM Students WHERE city = 'New York' ")
    city_data = cursor.fetchall()
    for i in city_data:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

    # ORDER BY
    print("-" * 30 + " ORDER BY age " + "-" * 30)
    cursor.execute("SELECT * FROM Students ORDER BY age ")
    order_data = cursor.fetchall()
    for i in order_data:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

    # LIMIT 
    print("-" * 30 + " LIMIT 3 " + "-" * 30)
    cursor.execute("SELECT * FROM Students LIMIT 3 ")
    limit_data = cursor.fetchall()
    for i in limit_data:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

def sql_update_delete_insert(conn : sqlite3.Connection , cursor : sqlite3.Cursor):

    # INSERT
    print("-" * 30 + " INSERT " + "-" * 30)
    cursor.execute("INSERT INTO Students VALUES (6, 'Frank Miller', 23, 'frank@gmail.com', 'Miami')")
    conn.commit()
    cursor.execute("SELECT * FROM Students WHERE id = 6")
    id_6_data = cursor.fetchall()
    for i in id_6_data:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

    # UPDATE
    print("-" * 30 + " UPDATE " + "-" * 30)
    cursor.execute("UPDATE Students SET age = 24 WHERE id = 6")
    conn.commit()
    cursor.execute("SELECT * FROM Students WHERE id = 6")
    id_6_data = cursor.fetchall()
    for i in id_6_data:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

    # DELETE
    print("-" * 30 + " DELETE " + "-" * 30)
    cursor.execute("DELETE FROM Students WHERE id = 6")
    conn.commit()
    cursor.execute("SELECT * FROM Students WHERE id = 6")
    id_6_data = cursor.fetchall()
    for i in id_6_data:
        print(f"id : {i[0]} Name : {i[1]} Age : {i[2]} Email : {i[3]} City : {i[4]}")
    print("\n")

def aggreagate_functions(cursor = sqlite3.Cursor):

    # COUNT
    print("-" * 30 + " COUNT " + "-" * 30)
    cursor.execute("SELECT COUNT(*) FROM Students")
    count = cursor.fetchone()
    print(count[0])
    print("\n")

    # Average
    print("-" * 30 + " AVERAGE " + "-" * 30)
    cursor.execute("SELECT AVG(age) FROM Students")
    average = cursor.fetchone()
    print(average[0])
    print("\n")

    # MAX - MIN
    print("-" * 30 + " MAX - MIN " + "-" * 30)
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    max_min_age = cursor.fetchall()
    for i in max_min_age:
        print(f"Max Age : {i[0]}")
        print(f"Min Age : {i[1]}")
    print("\n")

    # GROUP BY
    print("-" * 30 + " GROUP BY " + "-" * 30)
    cursor.execute("SELECT city, COUNT(*) FROM Students GROUP BY city ")
    city_count = cursor.fetchall()
    for i in city_count:
        print(f"{i[0]} : {i[1]}")
    print("\n")

def main():
    conn, cursor = create_database()
    try:
        create_tables(cursor)
        insert_data(cursor)
        basic_sql_query(cursor)
        sql_update_delete_insert(conn,cursor)
        aggreagate_functions(cursor)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    main()