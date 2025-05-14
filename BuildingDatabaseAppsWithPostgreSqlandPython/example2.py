import psycopg2
def table():
    connect = psycopg2.connect(dbname="postgres",user="postgres",password="postgres",host="localhost",port="5432")
    cursor = connect.cursor()
    cursor.execute('''create table employees(Name Text,Id int,Age int)''')

    print('Table created successfully')
    connect.commit()
    connect.close()



def data():
    connect = psycopg2.connect(dbname="postgres",user="postgres",password="postgres",host="localhost",port="5432")
    cursor = connect.cursor()

    name = input("enter name")
    id = input("enter id")
    age = input("enter age")
    query = '''INSERT INTO employees (Name, Id, Age) VALUES (%s,%s,%s);'''
    cursor.execute(query,(name,id,age))
    print('Data Inserted successfully')
    connect.commit()
    connect.close()


def extract():
    connect = psycopg2.connect(dbname="postgres",user="postgres",password="postgres",host="localhost",port="5432")
    cursor = connect.cursor()
    cursor.execute('''select * from employees ''')
    print(cursor.fetchone())
    connect.commit()
    connect.close()

data()