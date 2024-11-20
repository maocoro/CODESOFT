from codesft import db

class User (db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    lastname = db.Column(db.String(50), nullable = False)
    company = db.Column(db.String(50), nullable = False)
    username = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.Text, nullable = False)
    photo = db.Column(db.String (200))

    def __init__(self, name, lastname, company, username, email, password, photo = None):
        self.name = name
        self.lastname = lastname
        self.company = company
        self.username = username
        self.email = email
        self.password = password
        self.photo = photo

    def __repr__(self):
        return f"User: '{self.username}'"
    
from datetime import datetime



class Computer (db.Model):
    __tablename__ = 'computers'
    id = db.Column(db.Integer, primary_key = True)
    compañia = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    serial = db.Column(db.String(100), unique = True, nullable = False)
    responsable = db.Column(db.String(50))
    empresa = db.Column(db.String(50), nullable = False)
    marca = db.Column(db.String(50), nullable = False)
    modelo = db.Column(db.String(50), nullable = False)
    procesador = db.Column(db.String(50), nullable = False)
    ram = db.Column(db.String(50), nullable = False)
    almacenamiento = db.Column(db.String(50), nullable = False)
    descripcion = db.Column(db.Text)
    create = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, compañia, serial, responsable, empresa, marca, modelo, procesador, ram, almacenamiento, descripcion) -> None:
        self.compañia = compañia
        self.serial = serial
        self.responsable = responsable
        self.empresa = empresa
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.descripcion = descripcion

    def __repr__(self) -> str:
        return f"Post: '{self.serial}'"
    



class Transacciones (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    id_equipo = db.Column(db.Integer, db.ForeignKey('computers.id'), nullable = False)
    fecha = db.Column(db.String(50))
    tipo = db.Column(db.String(50))
    responsable = db.Column(db.String(100))
    
    def __init__(self, id_equipo, fecha, tipo, responsable):
        self.id_equipo = id_equipo
        self.fecha = fecha
        self.tipo = tipo
        self.responsable = responsable

    def __repr__(self) -> str:
        return f"Post: '{self.id_equipo}'"
    


class Alertas (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    id_equipo = db.Column(db.Integer, db.ForeignKey('computers.id'), nullable = False)
    fecha_alerta = db.Column(db.String(50))
    tipo_alerta = db.Column(db.String(50))
    descripcion = db.Column(db.String(500))

    def __init__(self, id_equipo, fecha_alerta, tipo_alerta,descripcion):
        self.id_equipo = id_equipo
        self.fecha_alerta = fecha_alerta
        self.tipo_alerta = tipo_alerta
        self.descripcion = descripcion
    
    def __repr__(self) -> str:
        return f"Post: '{self.id_equipo}'"