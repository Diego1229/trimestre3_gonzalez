import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ld1"
)
cursor=db.cursor()
cursor.execute('SHOW DATABASES')
for dbs in cursor:
    print(dbs)

print('--------------------')
cursor.execute("SHOW TABLES")
for n in cursor:
    print(n)

#cursor.execute("""INSERT INTO products ( id_categories, name, description  , image   ,price, inventory, id_sellers )VALUES (  1,'CARRO GOKU','ES UN CARRO','c: carrogoku.jpg ','2000000','3', 1 ) """)
#db.commit()                                                
#cursor.execute('select * from products')
#for ap in cursor:
#    print(ap)