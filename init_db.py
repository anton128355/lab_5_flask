import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

br = "Виробник: "
mo = "Модель: "
tr = "Трансмісія: "
ye = "Рік: "
po = "Потужність (кінські сили): "
fu = "Паливо: "
mi = "Пробіг: "
pr = "Ціна: "

cur.execute("INSERT INTO cars (brand, model, transmission, year, power, fuel, mileage, price, photo) VALUES (?, ?, ?, "
            "?, ?, ?, ?, ?, ?)",
            (f'{br}ЗАЗ', f'{mo}Таврія 1102', f'{tr}механіка', f'{ye}2001', f'{po}58', f'{fu}газ/бензин',
             f'{mi}250 000 км', f'{pr}500$', "tavria.jpg")
            )

cur.execute("INSERT INTO cars (brand, model, transmission, year, power, fuel, mileage, price, photo) VALUES (?, ?, ?, "
            "?, ?, ?, ?, ?, ?)",
            (f'{br}ВАЗ', f'{mo}2101', f'{tr}механіка', f'{ye}1986', f'{po}59', f'{fu}газ/бензин', f'{mi}500 000 км',
             f'{pr}400$', "2101.jpg")
            )

cur.execute("INSERT INTO cars (brand, model, transmission, year, power, fuel, mileage, price, photo) VALUES (?, ?, ?, "
            "?, ?, ?, ?, ?, ?)",
            (f'{br}ВАЗ', f'{mo}Niva Legend', f'{tr}механіка', f'{ye}2013', f'{po}80', f'{fu}газ/бензин',
             f'{mi}150 000 км', f'{pr}8000$', "niva.jpg")
            )

cur.execute("INSERT INTO cars (brand, model, transmission, year, power, fuel, mileage, price, photo) VALUES (?, ?, ?, "
            "?, ?, ?, ?, ?, ?)",
            (f'{br}Toyota', f'{mo}Land Cruiser 200', f'{tr}механіка', f'{ye}2006', f'{po}180', f'{fu}дизель',
             f'{mi}200 000 км', f'{pr}30 000$', "cruzak_200.jpg")
            )

cur.execute("INSERT INTO cars (brand, model, transmission, year, power, fuel, mileage, price, photo) VALUES (?, ?, ?, "
            "?, ?, ?, ?, ?, ?)",
            (f'{br}Tesla', f'{mo}Cybertruck', f'{tr}автомат', f'{ye}2022', f'{po}830', f'{fu}електро',
             f'{mi}0 км', f'{pr}200 000$', "cybertruck.jpg")
            )

cur.execute("INSERT INTO cars (brand, model, transmission, year, power, fuel, mileage, price, photo) VALUES (?, ?, ?, "
            "?, ?, ?, ?, ?, ?)",
            (f'{br}Toyota', f'{mo}RAV4', f'{tr}автомат', f'{ye}2020', f'{po}120', f'{fu}гібрид',
             f'{mi}40 000 км', f'{pr}35 000$', "rav4.jpg")
            )


connection.commit()
connection.close()
