import sqlite3

DB_NAME= "shop.db"

DB_PATH= "./sqlite/"

def openSqlLite():
    print(f"{DB_PATH}{DB_NAME}")
    connection = sqlite3.connect(f"{DB_PATH}{DB_NAME}")

    cursor = connection.cursor()

    return cursor