import pandas as pd
import sqlalchemy as sql


DB_CONNECTION_STRING = "mysql+pymysql://root:mysqlisg0@d@localhost:3306/"

sql_engine = sql.create_engine(DB_CONNECTION_STRING)

null_table_qry = "select customer_id from employee.orders order by customer_id asc;"

df = pd.read_sql_query(null_table_qry, sql_engine)
df.fillna(value=0 , inplace=True)
print(df.astype('Int64'))