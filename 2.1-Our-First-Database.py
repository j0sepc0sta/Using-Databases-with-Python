import sqlite3

# Create a database in RAM
db = sqlite3.connect(':memory:')

# Get a cursor object
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)''')


cursor.execute('''DELETE FROM Ages''')

# Insert users
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Clementine', 29)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Lillyanne', 18)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Kaycie', 34)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Sabila', 28)''')

#Select user
cursor.execute('''SELECT hex(name || age) AS X FROM Ages ORDER BY X''')

#retrieve the first row
user1 = cursor.fetchone()
#Print the first column retrieved(user's name)
print("To get credit for this assignment, perform the instructions below and enter the code you get here: "+user1[0])

#Commit changes into database
db.commit()
#Close database
db.close()
