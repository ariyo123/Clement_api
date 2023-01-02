import cdata.sparksql as mod
conn = mod.connect("User=user@domain.com; Password=password;")
 
#Create cursor and iterate over results
cur = conn.cursor()
cur.execute("SELECT * FROM ApacheSpark")
 
rs = cur.fetchall()
 
for row in rs:
    print(row)      