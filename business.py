from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()

class Entidad(Base):
    __tablename__ = 'entidades'
 
    id = Column(Integer, primary_key=True)
    cve_ent = Column(String(2))
    nom_ent = Column(String(50))
    nom_abr = Column(String(5))
    cve_cap = Column(String(7))
    nom_cap = Column(String(100))
    ptot = Column(Integer)
    pmas = Column(Integer)
    pfem = Column(Integer)
    vtot = Column(Integer)

    def __repr__(self):
        return "<Entidad(cve_ent='{cve_ent}', nombre='{nom_ent}')>".format(*self)

class Municipio(Base):
    __tablename__ = 'municipios'

    id = Column(Integer, primary_key=True)
    cve_ent = Column(String(2))
    nom_ent = Column(String(50))
    nom_abr = Column(String(5))
    cve_mun = Column(String(3))
    nom_mun = Column(String(100))
    cve_cab = Column(String(4))
    nom_cab = Column(String(100))
    ptot = Column(Integer)
    pmas = Column(Integer)
    pfem = Column(Integer)
    vtot = Column(Integer)

    def __repr__(self):
      return "<Municipio(cve_mun='{cve_mun}', nombre='{nom_mun}'".format(*self)
