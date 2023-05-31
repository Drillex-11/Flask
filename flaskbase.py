from flask import Flask, render_template, request
import sqlite3
from datetime import datetime 

app = Flask(__name__)
DATABASE = 'cuyes_inia_2023.db'

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE cuyes_inia
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha DATE,
                    id_cuy VARCHAR(50),
                    raza VARCHAR(50),
                    peso FLOAT,
                    ancho FLOAT,
                    largo FLOAT,
                    bcs VARCHAR(50))''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return '¡Bienvenido a la base de datos!'

@app.route('/guardar')
def guardar():
    fecha = datetime.now()
    id_cuy = str(1111)
    raza = "Perú"
    peso = 123.0
    ancho = 1231
    largo = 1231
    bcs = "Bueno"

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO cuyes_inia (fecha,id_cuy,raza,peso,ancho,largo,bcs)
                      VALUES (?, ?, ?, ?, ?, ?)''',
                   (fecha,id_cuy,raza,peso,ancho,largo,bcs))
    conn.commit()
    conn.close()

    return 'Datos guardados exitosamente'

if __name__ == '__main__':
    create_table()
    app.run()