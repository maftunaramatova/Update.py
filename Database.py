import sqlite3 as sql

with sql.connect('malumot.db') as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS purchases(
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product_name TEXT,
        price INTEGER
    )""")
    
    cur.execute(""" INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(1, 'Maqsadbek', "Qo'ziyev", 15)""")
    
    cur.execute("""INSERT OR IGNORE INTO purchases(id, user_id, product_name, price)
                VALUES(1, 1, 'Olma', 15000)""")
    
    cur.execute(""" INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(2, 'Maqsadbek', "Qurbonboyev", 15)""")
    
    cur.execute("""INSERT OR IGNORE INTO purchases(id, user_id, product_name, price)
                VALUES(2, 2, 'Uzum', 15000)""")
    
    cur.execute(""" INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(3, 'Bobur', "Jovliyev", 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO purchases(id, user_id, product_name, price)
                VALUES(3, 3, 'Nok', 25000)""")
    
    cur.execute(""" INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(4, "Mominjon", "Rustamov", 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO purchases(id, user_id, product_name, price)
                VALUES(4, 4, 'Shaftoli', 35000)""")
    
    cur.execute(""" INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(5, 'Husniddin', "O'rinbayev", 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO purchases(id, user_id, product_name, price)
                VALUES(5, 5, 'Mandarin', 25000)""")
    
    cur.execute(""" INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(6, "Ganijon", "Norimov", 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO purchases(id, user_id, product_name, price)
                VALUES(6, 6, 'Olcha', 25000)""")
    
    cur.execute(""" INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(7, 'Ibrohimjon', "Qalandarov", 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO purchases(id, user_id, product_name, price)
                VALUES(7, 7, "O'rik", 15000)""")
    
    cur.execute(""" INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(8, 'Amirxon', "Komuljonov", 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO purchases(id, user_id, product_name, price)
                VALUES(8, 8, "Olxo'ri", 25000)""")
    
    cur.execute(""" INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(9, 'Ozodbek', "Sobirov", 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO purchases(id, user_id, product_name, price)
                VALUES(9, 9, 'Olma', 25000)""")
    
    cur.execute(""" INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(10, 'Ruxshona', "Jo'rabekov", 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO purchases(id, user_id, product_name, price)
                VALUES(10, 10, 'Apelsin', 45000)""")
    
    cur.execute(""" INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(11, 'Zuhra', "Jumanazarova", 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO purchases(id, user_id, product_name, price)
                VALUES(11, 11, 'Mango', 50000)""")
    
    cur.execute(""" INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(12, 'Marjona', "Setmamatova", 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO purchases(id, user_id, product_name, price)
                VALUES(12, 12, 'Kiwi', 35000)""")
    
    cur.execute(""" INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(13, 'Maftuna', "Ramatova", 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO purchases(id, user_id, product_name, price)
                VALUES(13, 13, 'Gilos', 35000)""")
    
    con.commit()

    
    #Bitta qatordagi ma'lumotni yangilash (WHERE bilan)
    #id = 1 bo'lgan foydalanuvchining yoshini o'zgartiramiz
    cur.execute("UPDATE users SET age = 25 WHERE id = 1")
    
    cur.execute("UPDATE users SET age = 26 WHERE id = 2")
    
    cur.execute("UPDATE users SET age = 37 WHERE id = 3")
    
    cur.execute("UPDATE users SET age = 28 WHERE id = 4")
    
    cur.execute("UPDATE users SET age = 39 WHERE id = 5")
    
    cur.execute("UPDATE users SET age = 30 WHERE id = 6")
    
    cur.execute("UPDATE users SET age = 31 WHERE id = 7")
    
    cur.execute("UPDATE users SET age = 24 WHERE id = 8")
    
    cur.execute("UPDATE users SET age = 33 WHERE id = 9")
    
    cur.execute("UPDATE users SET age = 22 WHERE id = 10")
    
    cur.execute("UPDATE users SET age = 23 WHERE id = 11")
    
    cur.execute("UPDATE users SET age = 21 WHERE id = 12")
    
    cur.execute("UPDATE users SET age = 22 WHERE id = 13")
    con.commit()



























