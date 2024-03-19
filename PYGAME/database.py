#import database engine
import sqlite3


#create database connection (db_name
DB_NAME ="mygame"
con = sqlite3.connect(DB_NAME)
#enable to execute CRUD commands/querys
cur = con.cursor()

#create players table
player_table = '''
   CREATE TABLE IF NOT EXISTS players (
     id INTEGER PRIMARY KEY, 
     fullname TEXT NOT NULL,
     nickname TEXT NOT NULL,
     email TEXT NOT NULL,
     password TEXT NOT NULL,
     status BOOLEAN DEFAULT true,
     created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
     updated_at TIMESTAMP NULL,
     deleted_at TIEMSTAMP NULL
    )
'''

#execute query
cur.execute(player_table)

#send changes to datababase
con.commit()