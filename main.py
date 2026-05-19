import psycopg2
from dotenv import load_dotenv
import os
# Load DATABASE_URL from your .env file
load_dotenv()
conn = psycopg2.connect(os.getenv("DATABASE_URL") )
# A cursor lets you send SQL commands
cursor = conn.cursor()
# --- Swap in any query from the Query Reference section ---
cursor.execute("SELECT * FROM customer;")
# Fetch and print every row returned
rows = cursor.fetchall()
for row in rows:
    print(row)
# Always close when finished
cursor.close()
conn.close()