import csv
import sqlite3
from pymongo import MongoClient

# Ask user whether to use SQL or NoSQL
db_type = input("Enter database type (SQL or NoSQL): ").lower()

# Ask user whether to use local or server-based database
location = input("Enter database location (local or server): ").lower()

# Read cleaned CSV data file
with open("cleaned_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    data = [row for row in csv_reader]

# Convert data to SQL or NoSQL format
if db_type == "sql":
    # Use SQLite for local database or MySQL for server-based database
    if location == "local":
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        c.execute(f"CREATE TABLE data ({', '.join(headers)})")
        for row in data:
            c.execute(f"INSERT INTO data VALUES ({', '.join(['?' for _ in range(len(row))])})", row)
        conn.commit()
        conn.close()
    else:
        # Replace these values with your own MySQL server credentials
        conn = sqlite3.connect(host="localhost", user="myuser", password="mypassword", database="mydatabase")
        c = conn.cursor()
        c.execute(f"CREATE TABLE data ({', '.join(headers)})")
        for row in data:
            c.execute(f"INSERT INTO data VALUES ({', '.join(['?' for _ in range(len(row))])})", row)
        conn.commit()
        conn.close()
else:
    # Use MongoDB for local or server-based database
    if location == "local":
        client = MongoClient()
        db = client.mydb
        db.data.insert_many([{headers[i]: row[i] for i in range(len(headers))} for row in data])
        client.close()
    else:
        # Replace these values with your own MongoDB server credentials
        client = MongoClient("mongodb://myuser:mypassword@localhost:27017/")
        db = client.mydatabase
        db.data.insert_many([{headers[i]: row[i] for i in range(len(headers))} for row in data])
        client.close()
