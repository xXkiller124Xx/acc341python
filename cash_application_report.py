import psycopg2
from dotenv import load_dotenv
import os

# Load DATABASE_URL from your .env file
load_dotenv()

conn = psycopg2.connect(os.getenv("DATABASE_URL"))
cursor = conn.cursor()

# Cash Application Report
# For every payment, show the customer, the payment details,
# how much was applied to invoices, and how much is still unapplied.
cursor.execute("""
    SELECT
        c.company_name,
        p.reference_number,
        p.payment_method,
        p.amount_received,
        COALESCE(SUM(pa.amount_applied), 0) AS total_applied,
        p.amount_received - COALESCE(SUM(pa.amount_applied), 0) AS unapplied,
        COUNT(pa.application_id) AS invoices_paid
    FROM payment p
    JOIN customer c
        ON p.customer_id = c.customer_id
    LEFT JOIN payment_application pa
        ON p.payment_id = pa.payment_id
    GROUP BY
        c.company_name,
        p.payment_id,
        p.reference_number,
        p.payment_method,
        p.amount_received
    ORDER BY p.payment_id;
""")

# Fetch and print every row returned
rows = cursor.fetchall()

for row in rows:
    print(row)

# Always close when finished
cursor.close()
conn.close()