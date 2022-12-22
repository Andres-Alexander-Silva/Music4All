from flask import Flask
from flask import render_template
from flask import redirect
from flask import session
from flask import request
from flask import url_for
from flask import flash
from pytube import YouTube
from werkzeug.security import check_password_hash, generate_password_hash
from config import config
from models.UsuarioDao import UsuarioDao as userD
from entities.Usuario import Usuario as user
from entities.InformacionURL import InformacionURL as infoU
from models.InformacionURLDao import InformacionURLDao as urlD
from models.DescargaDao import DescargaDao as dow
import pafy

app = Flask(__name__)

@app.route("/")
@app.route("/Music4All")
def index():
    titulo = "Music4All"
        
    return render_template("index.html", title=titulo)

@app.route("/Music4All/buscar", methods=["POST"])
def buscar():
    
    if request.method == "POST":
        global url
        url = request.form["link"]
        link = YouTube(url)
        tituloL = link.title
        minutos = float((link.length) / 60)
        minutos_redondeados = round(minutos,2)
        autor = link.author
        img = link.thumbnail_url
        
        info_Link = infoU(tituloL,minutos_redondeados,autor)
        urlD.insertar(info_Link)
        
        return render_template("index.html", title2=tituloL, duration=minutos_redondeados, author=autor, image=img)

@app.route("/Music4All/Descarga-video", methods=["POST"])
def descargar_video():
    if request.method == "POST":
        path = "/Downloads"
        link = YouTube(url)
        
        video = link.streams.get_by_itag(22)
        video.download(output_path=path)
        
        message_ok = "La descarga a terminado, el archivo se guardo en C:/Downloads"
        flash(message_ok)
        
        return redirect(url_for("index"))
    
@app.route("/Music4All/Descarga-audio", methods=["POST"])
def descargar_audio():
    if request.method == "POST":
        path = "/Downloads"
        audio = pafy.new(url)
        
        bestaudio = audio.getbestaudio()
        bestaudio.download(path)
        
        message_ok = "La descarga a terminado, el archivo se guardo en C:/Downloads"
        flash(message_ok)
        
        return redirect(url_for("index"))

@app.route("/Music4All/Login", methods=["GET","POST"])
def login():
    titulo = "Login"
    
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasegna = request.form["contraseña"]
        
        userI = userD.consultar_id(usuario)
        
        if userI:
            if usuario == userI[0] and check_password_hash(userI[1], contrasegna):
                session["usuario"] = userI[0]
                return redirect(url_for('index'))
        
    return render_template("log_in.html", title=titulo)

@app.route("/Music4All/Sign-Up", methods=["GET","POST"])
def sign_up():
    titulo = "Sing-Up"
    
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        usuario = request.form["usuario"]
        contrasegna = request.form["contraseña"]
        
        contrasegna_hash = user.createPassword(contrasegna)
        userI = user(nombre, apellido, usuario, contrasegna_hash)
        userD.insertar(userI)
        
        if userD:
            return redirect(url_for('sign_up'))
        
    return render_template("sing_up.html", title=titulo)

@app.route("/Music4All/Salir")
def salir():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()