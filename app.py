from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = ""
app.config["MYSQL_DATABASE_DB"] = "sitio"
mysql.init_app(app)


@app.route("/")
def inicio():
    return render_template("indexSitio.html")


@app.route("/libros")
def libros():
    return render_template("sitio/books.html")


@app.route("/nosotros")
def nosotros():
    return render_template("sitio/about.html")


@app.route("/admin")
def admin_index():
    return render_template("admin/indexAdmin.html")


@app.route("/admin/signin")
def admin_signin():
    return render_template("admin/login.html")


@app.route("/admin/libros")
def admin_libros():
    conexion = mysql.connect()
    print(conexion)
    return render_template("admin/books.html")


@app.route("/admin/libros/guardar", methods=["POST"])
def admin_libros_guardar():
    nombre = request.form["txtNombre"]
    imagen = request.files["txtImagen"]
    url = request.form["txtUrl"]
    sql = "INSERT INTO `libros` (`id`, `nombre`, `imagen`, `url`) VALUES (NULL, %s, %s, %s);"
    datos = (nombre, imagen.filename, url)
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()

    print(nombre)
    print(imagen)
    print(url)

    return "Archivo guardado exitosamente"


if __name__ == "__main__":
    app.run(debug=True)
