from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from backend.database import Base


class Predio(Base):
    __tablename__ = "predios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)

    andares = relationship("Andar", back_populates="predio", cascade="all, delete-orphan")
    custos = relationship("CustoLocal", back_populates="predio", cascade="all, delete-orphan")


class Andar(Base):
    __tablename__ = "andares"

    id = Column(Integer, primary_key=True, index=True)
    predio_id = Column(Integer, ForeignKey("predios.id"), nullable=False)
    numero = Column(Integer, nullable=False)
    nome = Column(String(50))          # "Térreo", "1º Andar", etc.
    imagem_path = Column(String(500))  # PNG exportado do PowerPoint

    predio = relationship("Predio", back_populates="andares")
    salas = relationship("Sala", back_populates="andar", cascade="all, delete-orphan")


class Sala(Base):
    __tablename__ = "salas"

    id = Column(Integer, primary_key=True, index=True)
    andar_id = Column(Integer, ForeignKey("andares.id"), nullable=False)

    # Contrato atual que ocupa esta sala (null = sala disponível)
    # 1 contrato → N salas | 1 sala → no máximo 1 contrato ativo
    contrato_id = Column(Integer, ForeignKey("contratos.id"), nullable=True)

    nome = Column(String(100), nullable=False)  # "Sala 101", "Coworking", etc.
    area_m2 = Column(Float)
    is_coworking = Column(Boolean, default=False)

    # Coordenadas sobre a imagem do andar para overlay dinâmico (em %)
    coord_x = Column(Float)
    coord_y = Column(Float)
    coord_largura = Column(Float)
    coord_altura = Column(Float)

    andar = relationship("Andar", back_populates="salas")
    contrato = relationship("Contrato", back_populates="salas", foreign_keys=[contrato_id])
