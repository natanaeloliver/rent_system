from sqlalchemy import Column, Integer, String, DateTime, Date, Float, Boolean, ForeignKey, Enum, Text, func
from sqlalchemy.orm import relationship
from backend.database import Base
from backend.enums import TipoDescontoEnum


class Cobranca(Base):
    __tablename__ = "cobrancas"

    id = Column(Integer, primary_key=True, index=True)
    contrato_id = Column(Integer, ForeignKey("contratos.id"), nullable=False)
    mes_referencia = Column(Date, nullable=False)  # primeiro dia do mês de referência

    valor_contrato = Column(Float, nullable=False)  # valor base do contrato naquele mês
    valor_extras = Column(Float, default=0.0)
    valor_desconto = Column(Float, default=0.0)
    valor_total = Column(Float, nullable=False)     # valor_contrato + extras - desconto

    pago = Column(Boolean, default=False)
    data_pagamento = Column(Date, nullable=True)
    observacoes = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

    contrato = relationship("Contrato", back_populates="cobranças")
    extras = relationship("ExtraMensal", back_populates="cobranca", cascade="all, delete-orphan")


class ExtraMensal(Base):
    __tablename__ = "extras_mensais"

    id = Column(Integer, primary_key=True, index=True)
    cobranca_id = Column(Integer, ForeignKey("cobrancas.id"), nullable=False)
    descricao = Column(String(200), nullable=False)  # "Luz", "Gás", personalizado
    valor = Column(Float, nullable=False)

    cobranca = relationship("Cobranca", back_populates="extras")


class Desconto(Base):
    __tablename__ = "descontos"

    id = Column(Integer, primary_key=True, index=True)
    contrato_id = Column(Integer, ForeignKey("contratos.id"), nullable=False)
    tipo = Column(Enum(TipoDescontoEnum), nullable=False)
    descricao = Column(String(200))
    valor = Column(Float, nullable=False)  # valor fixo (R$) ou percentual (0–100)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=True)  # null = vigente por prazo indeterminado

    contrato = relationship("Contrato", back_populates="descontos")
