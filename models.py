from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, SmallInteger, Date, Time, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


db = SQLAlchemy()
Base = declarative_base()

class WS_LEADS(Base):
    __tablename__ = 'WS_LEADS'

    IDENT = Column(Integer, primary_key=True, nullable=False)
    idTimeStamp = Column(String(50))
    IdUnico = Column(String(50), server_default="")
    FECHA_ENTRADA = Column(DateTime, server_default=func.current_timestamp())
    duplicado = Column(SmallInteger)
    cargado = Column(SmallInteger)
    fecha_carga = Column(DateTime, server_default=func.current_timestamp())
    cod_proveedor = Column(String(5))
    id = Column(String(50))
    campana = Column(String(50))
    fecha_captacion = Column(DateTime)
    nombre = Column(String(50))
    ape1 = Column(String(50))
    ape2 = Column(String(50))
    telefono = Column(String(9))
    telefonoMD5 = Column(String(50))
    email = Column(String(150))
    acepta1 = Column(String(2))
    acepta2 = Column(String(2))
    acepta3 = Column(String(2))
    num1 = Column(Integer)
    num2 = Column(Integer)
    num3 = Column(Integer)
    dual1 = Column(String(2))
    dual2 = Column(String(2))
    dual3 = Column(String(2))
    variable1 = Column(String(50))
    variable2 = Column(String(50))
    variable3 = Column(String(50))
    memo = Column(Text)
    fecha = Column(Date)
    hora = Column(Time)
    foto1 = Column(String(500))
    foto2 = Column(String(500))
    comercial = Column(String(50))
    centro = Column(String(50))
    codigo_postal = Column(String(5))
    direccion = Column(String(50))
    poblacion = Column(String(50))
    provincia = Column(String(50))
    nif = Column(String(50))


class WS_LEADS_DISOCIADOS(db.Model):
    IDENT = db.Column(db.Integer, primary_key=True, nullable=False)
    IDENT_ORI = db.Column(db.Integer, nullable=False)
    idTimeStamp = db.Column(db.DateTime, nullable=True)
    IdUnico = db.Column(db.String(50), nullable=True) 
    FECHA_ENTRADA = db.Column(db.DateTime, nullable=True)
    duplicado = db.Column(db.Integer, nullable=True)
    cargado = db.Column(db.Integer, nullable=True)
    fecha_carga = db.Column(db.DateTime, nullable=True)
    cod_proveedor = db.Column(db.String(50), nullable=True)
    id = db.Column(db.String(50), nullable=True)
    campana = db.Column(db.String(50), nullable=True)
    fecha_captacion = db.Column(db.DateTime, nullable=True)
    nombre = db.Column(db.String(50), nullable=True)
    ape1 = db.Column(db.String(50), nullable=True)
    ape2 = db.Column(db.String(50), nullable=True)
    telefono = db.Column(db.String(9), nullable=True)
    telefonoMD5 = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(150), nullable=True)
    acepta1 = db.Column(db.String(2), nullable=True)
    acepta2 = db.Column(db.String(2), nullable=True)
    acepta3 = db.Column(db.String(2), nullable=True)
    num1 = db.Column(db.Integer, nullable=True)
    num2 = db.Column(db.Integer, nullable=True)
    num3 = db.Column(db.Integer, nullable=True)
    dual1 = db.Column(db.String(2), nullable=True)
    dual2 = db.Column(db.String(2), nullable=True)
    dual3 = db.Column(db.String(2), nullable=True)
    variable1 = db.Column(db.String(50), nullable=True)
    variable2 = db.Column(db.String(50), nullable=True)
    variable3 = db.Column(db.String(50), nullable=True)
    memo = db.Column(db.Text, nullable=True)
    fecha = db.Column(db.Date, nullable=True)
    hora = db.Column(db.Time(timezone=True), nullable=True)
    foto1 = db.Column(db.String(500), nullable=True)
    foto2 = db.Column(db.String(500), nullable=True)
    comercial = db.Column(db.String(50), nullable=True)
    centro = db.Column(db.String(50), nullable=True)
    codigo_postal = db.Column(db.String(5), nullable=True)
    direccion = db.Column(db.String(50), nullable=True)
    poblacion = db.Column(db.String(50), nullable=True)
    provincia = db.Column(db.String(50), nullable=True)
    nif = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<WS_LEADS_DISOCIADOS {self.IDENT}>"
    

class AUX_CAMPANAS(db.Model):
    IDENT = db.Column(db.Integer, primary_key=True, nullable=False)
    servidor = db.Column(db.String(50), nullable=False)
    bbdd_report = db.Column(db.String(50))
    IdCampana = db.Column(db.Integer, nullable=False)
    sistema = db.Column(db.String(50), nullable=False)
    Nombre = db.Column(db.String(50))
    activo = db.Column(db.SmallInteger)
    spcarga_ws_salesland_leads = db.Column(db.String(50))
    admite_duplicado = db.Column(db.SmallInteger)


class AUX_DISOCIAR(db.Model):
    campo = db.Column(db.String(50), primary_key=True, nullable=False)


class AUX_PROVEEDORES(db.Model):
    IDENT = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    cod_proveedor = db.Column(db.String(5))
    proveedor = db.Column(db.String(50))