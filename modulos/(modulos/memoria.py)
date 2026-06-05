import sqlite3
import datetime

def registrar(cmd, res):
    conn = sqlite3.connect('amiti_memoria.db')
    conn.execute('CREATE TABLE IF NOT EXISTS registro_conocimiento (c TEXT, r TEXT, f TIMESTAMP)')
    conn.execute('INSERT INTO registro_conocimiento VALUES (?, ?, ?)', (cmd, res, datetime.datetime.now()))
    conn.commit()
    conn.close()

def contar_registros():
    try:
        conn = sqlite3.connect('amiti_memoria.db')
        c = conn.execute('SELECT count(*) FROM registro_conocimiento').fetchone()[0]
        conn.close()
        return c
    except: return 0
