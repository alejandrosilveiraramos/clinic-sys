import psycopg2

try:
    conn = psycopg2.connect(
    host = "localhost",
    port ="5435",
    database = "postgres", 
    user="clinicsys", password = "123456")
    print('Connection Stablished.')

except Exception:
    print('Connection Error.')


if conn is not None:
    
    print('Your connection are granted!')

    cursor = conn.cursor()
    
    cursor.execute('CREATE TABLE  admin (id serial, name VARCHAR(64)NOT NULL, password VARCHAR(64)NOT NULL, email VARCHAR(64)NOT NULL, cpf varchar(14) NOT NULL, position varchar(64) NOT NULL, PRIMARY KEY(id));')
    print('Table Admin Created!')

    cursor.execute('CREATE TABLE  person (id serial, name VARCHAR(64)NOT NULL, email VARCHAR(64)NOT NULL, cpf varchar(14) NOT NULL, PRIMARY KEY(id));')
    print('Table Person Created!')

    # Create the 2 tables first than comment those lines and create this one.
    # cursor.execute('CREATE TABLE  reports (id serial, idPerson int, date_report date NULL, description varchar(128) NOT NULL, PRIMARY KEY(id)) inherits (person);')
    # print('Table Reports Created!')

    conn.commit()
    cursor.close()
    conn.close()