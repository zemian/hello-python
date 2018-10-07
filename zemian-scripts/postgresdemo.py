import psycopg2
conn = psycopg2.connect("dbname=som user=test")
cur = conn.cursor()
cur.execute("SELECT * FROM ur_user")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()
