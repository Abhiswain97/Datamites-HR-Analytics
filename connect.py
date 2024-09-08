from mysql.connector import connection
import csv
from tqdm import tqdm

# Database connection details
db_host = "18.136.157.135"
db_name = "project_hr_analytics"
db_user = "dm_team9"
db_password = "DM!$!Team9!20@4!23&"
db_table = "HR"

creds = {"user": db_user, "host": db_host, "database": db_name, "password": db_password}

conn = connection.MySQLConnection(**creds)

curr = conn.cursor()

curr.execute("SELECT * FROM HR")

res = curr.fetchall()

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(
        [
            "id",
            "first_name",
            "last_name",
            "birthdate",
            "age",
            "gender",
            "race",
            "department",
            "jobtitle",
            "location",
            "hire_date",
            "termdate",
            "location_city",
            "location_state",
        ]
    )

    for row in tqdm(res):
        writer.writerow(row)

conn.close()
