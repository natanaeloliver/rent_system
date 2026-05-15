from sqlalchemy import Column, String, Text, DateTime, func
from backend.database import Base


class Configuracao(Base):
    """Configurações globais do sistema em formato chave-valor."""
    __tablename__ = "configuracoes"

    chave = Column(String(100), primary_key=True)
    valor = Column(Text, nullable=False)
    descricao = Column(String(500))
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
