import sqlite3


connection = sqlite3.connect("user_data.db")

cursor = connection.cursor()

create_table_query = """
    CREATE TABLE IF NOT EXISTS new_users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
    );
    """
cursor.execute(create_table_query)
def add_user(name, age, email):
   insert_query = """
   INSERT INTO new_users(name, age, email)
   VALUES (?, ?, ?);"""

   cursor.execute(insert_query, (name, age, email))
   connection.commit()
   print(f"User {name} added successfully!")

def view_users():
   query = "SELECT * FROM  new_users;"
   cursor.execute(query)
   rows = cursor.fetchall()
   for row in rows:
      print(row)

def search_users(name):
   query = "SELECT * FROM new_users WHERE name = ?;"
   cursor.execute(query, (name,))
   rows = cursor.fetchall()
   for row in rows:
      print(row)

def update_user(name, age):
   query = "UPDATE new_users SET age = ? WHERE name = ?;"
   cursor.execute(query, (age, name))
   connection.commit()

def delete_user(name):
   query = "DELETE FROM new_users WHERE name = ?;"
   cursor.execute(query, (name,))


while True:
    print("\nUser Data Management System")
    print("1. Add User")
    print("2. View Users")
    print("3. Update User")
    print("4. Search User")
    print("5. Delete User")
    print("6. Exit") 

    choice = int(input("Enter your choice: "))
    if choice == 1:
       name = input("Enter name:") 
       age = int(input("Enter age: "))
       email = input("Enter email: ")
       add_user(name, age, email)
    elif choice == 2:
       view_users()
    elif choice == 3:
       name = input("Enter name: ")
       new_age = int(input("Enter new age: "))
       update_user(name, new_age)
    elif choice == 4:
       name = input("Enter name: ")
       search_users(name)
    elif choice == 5:
       name = input("Enter name: ")
       delete_user(name)    
    elif choice == 6:
       break
    else:
        print("Invalid choice! Please try again.") 