import psycopg2
import csv

with psycopg2.connect(host='localhost', database='north', user='postgres', password='12345') as conn:
    with conn.cursor() as cur:
        with open('north_data/employees_data.csv', encoding='utf-8') as f:
            rows = csv.DictReader(f)
            for row in rows:
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', (row['employee_id'],
                                                                                      row['first_name'],
                                                                                      row['last_name'],
                                                                                      row['title'],
                                                                                      row['birth_date'],
                                                                                      row['notes']))

                cur.execute('SELECT * FROM employees')

        with open('north_data/customers_data.csv', encoding='utf-8') as f:
            rows = csv.DictReader(f)
            for row in rows:
                # print(row)
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (row['customer_id'],
                                                                                      row['company_name'],
                                                                                      row['contact_name']))

                cur.execute('SELECT * FROM customers')

        with open('north_data/orders_data.csv', encoding='utf-8') as f:
            rows = csv.DictReader(f)
            for row in rows:
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', (row['order_id'],
                                                                                      row['customer_id'],
                                                                                      row['employee_id'],
                                                                                      row['order_date'],
                                                                                      row['ship_city']))

                cur.execute('SELECT * FROM orders')

conn.close()
