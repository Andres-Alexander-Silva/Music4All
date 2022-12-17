from flask import Flask
from flask import render_template
from flask import session
from flask import request
from flask import url_for
from flask import flash
from config import config
from models.UsuarioDao import UsuarioDao as userD
from entities.Usuario import Usuario
from models.InformacionURLDao import InformacionURLDao as url
from models.DescargaDao import DescargaDao as dow

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo"
@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        nombre = "Andres"
        apellido = "Silva"
        usuario = "AndresSilva26"
        contrsegna = "andres26112002"
        
        user = Usuario()
        contrasegna_hash = user.createPassword(contrsegna)
        
        user = Usuario(nombre, apellido, usuario, contrasegna_hash)
        
        userD.insertar(user)
        
        if userD:
            flash("Usuario creado con exito!")
            return render_template("register.html")

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()