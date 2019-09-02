import psycopg2 as db
conn = db.connect("dbname=zemian")
with conn:
    cursor = conn.cursor()
    with cursor:
        #print(cursor)
        cursor.execute("SELECT * FROM information_schema.tables")
        records = cursor.fetchall()
        for row in records:
            print(row)
