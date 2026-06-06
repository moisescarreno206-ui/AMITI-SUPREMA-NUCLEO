import sqlite3

def obtener_estadisticas():
    conn = sqlite3.connect('amiti_memoria.db')
    cursor = conn.cursor()
    # Contamos cuántas veces ha ejecutado el ciclo
    cursor.execute("SELECT count(*) FROM registro_conocimiento")
    total = cursor.fetchone()[0]
    conn.close()
    return total
