from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base


class Predio(Base):
    __tablename__ = "predios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)

    andares = relationship("Andar", back_populates="predio", cascade="all, delete-orphan")


class Andar(Base):
    __tablename__ = "andares"

    id = Column(Integer, primary_key=True, index=True)
    predio_id = Column(Integer, ForeignKey("predios.id"), nullable=False)
    numero = Column(Integer, nullable=False)
    nome = Column(String(50))          # "Térreo", "1º Andar", etc.
    imagem_path = Column(String(500))  # caminho relativo ao PNG exportado do PowerPoint

    predio = relationship("Predio", back_populates="andares")
    salas = relationship("Sala", back_populates="andar", cascade="all, delete-orphan")


class Sala(Base):
    __tablename__ = "salas"

    id = Column(Integer, primary_key=True, index=True)
    andar_id = Column(Integer, ForeignKey("andares.id"), nullable=False)
    nome = Column(String(100), nullable=False)  # "Sala 101", "Coworking", etc.
    area_m2 = Column(Float)

    # Coordenadas sobre a imagem do andar para o overlay dinâmico (em pixels ou %)
    coord_x = Column(Float)
    coord_y = Column(Float)
    coord_largura = Column(Float)
    coord_altura = Column(Float)

    andar = relationship("Andar", back_populates="salas")
    contratos = relationship("Contrato", back_populates="sala")
