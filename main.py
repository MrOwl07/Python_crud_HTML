from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
#conexion a base de datos
mysql = MySQL()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbcrud'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def index_clientes():
    

    sql = 'SELECT * FROM db_clientes'
    conex = mysql.connection
    cursor = conex.cursor()
    cursor.execute(sql)
    clientes = cursor.fetchall()
    conex.commit()
    return render_template('modulos/clientes/index.html', clientes = clientes)



if __name__ == '__main__':
    app.run(debug=True)
    
    