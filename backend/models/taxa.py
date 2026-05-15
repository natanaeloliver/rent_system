from sqlalchemy import Column, Integer, String, DateTime, Date, Float, ForeignKey, Enum, func
from sqlalchemy.orm import relationship
from backend.database import Base
from backend.enums import IndiceEnum


class Taxa(Base):
    __tablename__ = "taxas"

    id = Column(Integer, primary_key=True, index=True)
    indice = Column(Enum(IndiceEnum), nullable=False)
    mes_referencia = Column(Date, nullable=False)  # primeiro dia do mês de referência
    valor_percentual = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())


class HistoricoReajuste(Base):
    __tablename__ = "historico_reajustes"

    id = Column(Integer, primary_key=True, index=True)
    contrato_id = Column(Integer, ForeignKey("contratos.id"), nullable=False)
    data_reajuste = Column(Date, nullable=False)
    indice_usado = Column(String(20))
    percentual_acumulado = Column(Float)  # % acumulado no período aplicado
    valor_anterior = Column(Float, nullable=False)
    valor_novo = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    contrato = relationship("Contrato", back_populates="historico_reajustes")
