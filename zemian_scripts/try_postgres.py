import psycopg2 as db

conn = db.connect('dbname=test user=zemian')

with conn:
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar)")
    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
    cur.execute("SELECT * FROM test")
    result = cur.fetchone()
    print(result)
    conn.commit()
    cur.close()
