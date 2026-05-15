from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from backend.database import Base


class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    cnpj_cpf = Column(String(18), unique=True, nullable=False, index=True)
    razao_social = Column(String(200), nullable=False)
    nome_fantasia = Column(String(200))
    email = Column(String(100))
    telefone = Column(String(20))
    created_at = Column(DateTime, server_default=func.now())

    representantes = relationship("Representante", back_populates="empresa", cascade="all, delete-orphan")
    contratos = relationship("Contrato", back_populates="empresa")


class Representante(Base):
    __tablename__ = "representantes"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)
    nome = Column(String(200), nullable=False)
    cpf = Column(String(14))
    rg = Column(String(20))
    cargo = Column(String(100))
    email = Column(String(100))
    telefone = Column(String(20))
    created_at = Column(DateTime, server_default=func.now())

    empresa = relationship("Empresa", back_populates="representantes")
