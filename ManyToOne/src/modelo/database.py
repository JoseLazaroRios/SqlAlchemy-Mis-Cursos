from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Conectar a la base de datos (se crea si no existe)
engine = create_engine('sqlite:///cursos.db', echo=True)
Base = declarative_base()

# Definir clases (tablas)
class MisDatos(Base):
    __tablename__ = 'mis_datos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    sexo = Column(String, nullable=False)
    carrera = Column(String, nullable=False)
    asignaturas = relationship('Asignaturas', back_populates='mis_datos')

class Asignaturas(Base):
    __tablename__ = 'asignaturas'
    id = Column(Integer, primary_key=True)
    curso = Column(String, nullable=False)
    mis_datos_id = Column(Integer, ForeignKey('mis_datos.id'))
    mis_datos = relationship('MisDatos', back_populates='asignaturas')

# Crear tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
