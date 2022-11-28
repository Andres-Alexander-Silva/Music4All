from flask import Flask
from flask import render_template
from config import config
from entities.Persona import Persona
from models.PersonaDao import PersonaDao as pd

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    persona = Persona("Madi","Quintero")
    
    ##persona = pd.consultar_id(3)
    
    return pd.borrar(3)

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()