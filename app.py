from flask import Flask
from config import config
from flask_mysqldb import MySQL
from entities.Persona import Persona
from models.PersonaDao import PersonaDao

app = Flask(__name__)
db = MySQL(app)

@app.route("/", methods=['GET','POST'])
def index():
    persona = Persona("Andres", "Silva")
    return PersonaDao.insert(db, persona)

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()