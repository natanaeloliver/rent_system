from sqlalchemy import Column, Integer, String, DateTime, Date, Float, ForeignKey, Enum, func
from sqlalchemy.orm import relationship
from backend.database import Base
from backend.enums import CriterioRateioEnum


class CustoLocal(Base):
    """Custo mensal de um prédio (água, luz, condomínio, etc.) a ser rateado entre os locatários."""
    __tablename__ = "custos_locais"

    id = Column(Integer, primary_key=True, index=True)
    predio_id = Column(Integer, ForeignKey("predios.id"), nullable=False)
    mes_referencia = Column(Date, nullable=False)      # primeiro dia do mês de referência
    descricao = Column(String(200), nullable=False)    # "Água", "Luz", "Condomínio", etc.
    valor_total = Column(Float, nullable=False)

    # Define como este custo é distribuído entre os contratos ativos do prédio
    criterio_rateio = Column(Enum(CriterioRateioEnum), nullable=False, default=CriterioRateioEnum.por_area)

    created_at = Column(DateTime, server_default=func.now())

    predio = relationship("Predio", back_populates="custos")
