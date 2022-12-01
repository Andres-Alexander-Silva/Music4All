from flask import Flask
from flask import render_template
from config import config
from models.UsuarioDao import UsuarioDao as user
from entities.Usuario import Usuario
from models.InformacionURLDao import InformacionURLDao as url
from entities.InformacionURL import InformacionURL 

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    usuario1 = Usuario("Madi", "Garcia", "MadiG56", "contraseña879")
    infoUrl = InformacionURL("Mojando asientos", "4:12", "Maluma y Feid")
    
    return url.consultar().__str__()

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()