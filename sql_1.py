import sqlite3


connection = sqlite3.connect("user_data.db")

cursor = connection.cursor()

print("Database connected successfully!")

create_table_query = """
CREATE TABLE IF NOT EXISTS users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL,
   age INTEGER,
   email TEXT UNIQUE
);
"""
cursor.execute(create_table_query)


print("Table created successfully.")

insert_query = """
INSERT OR IGNORE INTO users (name, age, email)
VALUES ('Alice', 25, 'alice@example.com');
"""

cursor.execute(insert_query)
print("User added successfully!")

update_query = """
UPDATE users
SET age = 26
WHERE name = 'Alice'
"""
cursor.execute(update_query)

select_query = "SELECT* FROM users;"

cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.commit()
connection.close()    