import sqlite3

connection = sqlite3.Cursor("database.db")
cursor = sqlite3.Cursor


requestt = ("CREATE TABLE IF NOT EXISTS services "
            "(id INTEGER PRIMIRY KEY AUTOICREMENT,"
            "name VARCHAR(255),"
            "description VARCHAR(255),"
            "minimal_price INTEGAR"
            "max_price INTEGAR")
cursor.execute(request)

inset_request = ("INSERT INTO PRODUCTS"
                 "(name, description, minimal_price, max_price) VALUES (?, ?, ?)")
cursor.execute(insert_request, ("ремонт телевизора","описание","350", "800"))
cursor.execute(insert_request, ("ремонт стиральной машины","описание","350", "1000"))
cursor.execute(insert_request, ("ремонт компьютеров","описание","500", "1500"))
cursor.execute(insert_request, ("ремонт холодильников","описание","350", ""))
cursor.execute(insert_request, ("ремонт другой техники","описание","350" "10000"))







text = cursor)

