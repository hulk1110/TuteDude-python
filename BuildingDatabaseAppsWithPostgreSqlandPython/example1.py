import psycopg2
connect = psycopg2.connect(dbname="postgres",user="postgres",password="postgres",host="localhost",port="5432")
cursor = connect.cursor()
cursor.execute('''create table employees(Name Text,Id int,Age int)''')

print('Table created successfully')
connect.commit()
connect.close()

