#!/usr/bin/python3
import MySQLdb
import sys

# Get MySQL login credentials from command line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

# Connect to MySQL server running on localhost at port 3306
db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                     passwd=mysql_password, db=database_name)

# create a cursor object to execute queries
cursor = db.cursor()

# Execute the query to get all states from the database and sort id
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all the rows and print them
for row in cursor.fetchall():
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()
