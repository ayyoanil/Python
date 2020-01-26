import mysql.connector

NO_OUTPUT = 0
PRINT_OUTPUT = 1
FETCH_RESULTS = 2
COMMIT = 3


def connect_mysql():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='mysqlisg00d'
    )


def connect_mysql_db(db):
    return mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='mysqlisg00d',
        database=db
    )


SQL_CREATE_USERS_TABLE = [
    ['CREATE TABLE IF NOT EXISTS USER_TABLE'
     '(id INT AUTO_INCREMENT PRIMARY KEY,'
     ' name VARCHAR(50),'
     ' fav INT)', NO_OUTPUT],
    ['SHOW TABLES', PRINT_OUTPUT],
    ['INSERT INTO USER_TABLE VALUES (0,"Anil",100)', COMMIT],
    ['INSERT INTO USER_TABLE VALUES (0,"Vishnu",101)', COMMIT],
    ['INSERT INTO USER_TABLE VALUES (0,"Vipin",105)', COMMIT],
    ['SELECT * FROM USER_TABLE', FETCH_RESULTS]
]

SQL_CREATE_PRODUCTS_TABLE = [
    ['CREATE TABLE IF NOT EXISTS PRODUCT_TABLE'
     '(id INT AUTO_INCREMENT PRIMARY KEY,'
     ' name VARCHAR(50))', NO_OUTPUT],
    ['SHOW TABLES', PRINT_OUTPUT],
    ['INSERT INTO PRODUCT_TABLE VALUES (100,"Chocolate")', COMMIT],
    ['INSERT INTO PRODUCT_TABLE VALUES (101,"Vanilla")', COMMIT],
    ['INSERT INTO PRODUCT_TABLE VALUES (102,"Strawberry")', COMMIT],
    ['SELECT * FROM PRODUCT_TABLE', FETCH_RESULTS]
]

SQL_DROP_TABLES = [
    ['DROP TABLE USER_TABLE', NO_OUTPUT],
    ['DROP TABLE PRODUCT_TABLE', NO_OUTPUT],
    ['SHOW TABLES', PRINT_OUTPUT]
]

SQL_JOIN_TABLE = [
    ['SELECT'
     ' USER_TABLE.name AS user,'
     ' PRODUCT_TABLE.name AS icecream'
     ' FROM USER_TABLE'
     ' RIGHT JOIN PRODUCT_TABLE ON USER_TABLE.fav = PRODUCT_TABLE.id', FETCH_RESULTS]
]

mysql_db = connect_mysql_db("EMPLOYEE")
mysql_cursor = mysql_db.cursor()


for command in SQL_JOIN_TABLE:
    mysql_cursor.execute(command[0])
    if command[1] == PRINT_OUTPUT:
        for items in mysql_cursor:
            print(items)
    elif command[1] == FETCH_RESULTS:
        result = mysql_cursor.fetchall()
        for items in result:
            print(items)
    elif command[1] == COMMIT:
        mysql_db.commit()

