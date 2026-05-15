from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func, Text
from sqlalchemy.orm import relationship
from backend.database import Base


class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    cnpj_cpf = Column(String(18), unique=True, nullable=True, index=True)  # nullable: alguns cadastros ainda sem CNPJ
    id_rm = Column(String(20), nullable=True, index=True)   # identificador interno legado (ID RM)
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


class Fiador(Base):
    """Fiador/garantidor vinculado a um contrato específico."""
    __tablename__ = "fiadores"

    id = Column(Integer, primary_key=True, index=True)
    contrato_id = Column(Integer, ForeignKey("contratos.id"), nullable=False)
    numero = Column(Integer, nullable=False)  # 1 ou 2 (até dois fiadores por contrato)

    nome = Column(String(200), nullable=False)
    cpf = Column(String(14))
    rg = Column(String(20))
    estado_civil = Column(String(50))
    regime_bens = Column(String(100))     # ex: "Comunhão parcial de bens"
    nome_conjuge = Column(String(200))
    profissao = Column(String(100))
    nacionalidade = Column(String(50))
    endereco = Column(Text)

    # Caminhos para imagens dos documentos (armazenadas em assets/)
    imagem_rg_path = Column(String(500))
    imagem_comprovante_path = Column(String(500))

    created_at = Column(DateTime, server_default=func.now())

    contrato = relationship("Contrato", back_populates="fiadores")
