import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()


request = ("CREATE TABLE IF NOT EXISTS services "
            "(id INTEGER PRIMIRY KEY AUTOICREMENT,"
            "name VARCHAR(255),"
            "description VARCHAR(255),"
            "minimal_price INTEGER,"
            "max_price INTEGER)")
cursor.execute(request)

insert_request = ("INSERT INTO services"
                 "(name, description, minimal_price, max_price) VALUES (?, ?, ?, ?)")
cursor.execute(insert_request, ("ремонт телевизора", "описание", "350", "800"))
cursor.execute(insert_request, ("ремонт стиральной машины", "описание", "350", "1000"))
cursor.execute(insert_request, ("ремонт компьютеров", "описание", "500", "1500"))
cursor.execute(insert_request, ("ремонт холодильников", "описание", "350", "9900"))
cursor.execute(insert_request, ("ремонт другой техники", "описание", "350", "10000"))

request = ("CREATE TABLE IF NOT EXISTS images "
            "(id INTEGER PRIMIRY KEY AUTOICREMENT,"
            "name VARCHAR(255),"
            "description VARCHAR(255),"
            "Механик1.jpg"
            "Механик2.jpg"
            "Механик3.jpg")

insert_request = ("INSERT INTO images"
                  "name, description, image) VALUES(?, ?, ?")
cursor.execute(insert_request, ("Механик 1", "Описание" "Механик1.jpg"))
cursor.execute(insert_request, ("Механик 2", "Описание" "Механик2.jpg"))
cursor.execute(insert_request, ("Механик 3", "Описание" "Механик3.jpg"))



connection.commit()
connection.close()


