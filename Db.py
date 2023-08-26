import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "israel",
    "database": "phonepe",
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

insert_query = "INSERT INTO your_table (Transaction_Type, Instrument_Type, Count, Amount) VALUES (%s, %s, %s, %s)"

for index, row in df.iterrows():
    data_tuple = (row["Transaction Type"], row["Instrument Type"], row["Count"], row["Amount"])
    cursor.execute(insert_query, data_tuple)

connection.commit()
cursor.close()
connection.close()
