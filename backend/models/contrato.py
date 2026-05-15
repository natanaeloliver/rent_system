from sqlalchemy import Column, Integer, String, DateTime, Date, Float, Boolean, ForeignKey, Enum, Text, func
from sqlalchemy.orm import relationship
from backend.database import Base
from backend.enums import ModalidadeEnum, StatusContratoEnum, ValorTipoEnum, IndiceEnum, StatusJuridicoEnum


class Contrato(Base):
    __tablename__ = "contratos"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)

    # TA aponta para o contrato que emenda; contratos subsequentes formam cadeia
    contrato_anterior_id = Column(Integer, ForeignKey("contratos.id"), nullable=True)

    numero_contrato = Column(String(50), unique=True)
    modalidade = Column(Enum(ModalidadeEnum), nullable=False)
    status = Column(Enum(StatusContratoEnum), nullable=False, default=StatusContratoEnum.ativo)

    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=True)  # null = prazo indeterminado

    valor_tipo = Column(Enum(ValorTipoEnum), nullable=False, default=ValorTipoEnum.fixo)
    valor_base = Column(Float, nullable=False)  # valor fixo ou valor por m²
    area_m2 = Column(Float, nullable=True)      # obrigatório quando valor_tipo = por_m2

    indice_reajuste = Column(Enum(IndiceEnum), default=IndiceEnum.igpm)
    mes_reajuste = Column(Integer, nullable=True)   # 1–12
    dia_reajuste = Column(Integer, nullable=True)   # 1–31

    # Jurídico
    status_juridico = Column(Enum(StatusJuridicoEnum), nullable=True)
    numero_espaider = Column(String(50), nullable=True)
    valor_multa_penal = Column(Float, nullable=True)
    periodo_max_prorrogacao = Column(String(100), nullable=True)

    # Incubação: fase informativa — texto livre (Incubada / Consolidada / Graduada)
    fase_incubacao = Column(String(100), nullable=True)

    # Adesão: nome da organização configurável por contrato (ex: "Tecnosinos")
    nome_programa = Column(String(200), nullable=True)

    # Flag de qualidade dos dados (principal.csv validado='sim')
    dados_validados = Column(Boolean, default=False, nullable=False)

    # Alerta de vencimento: True = operador marcou como resolvido
    flagged_resolvido = Column(Boolean, default=False, nullable=False)
    observacoes = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relacionamentos
    empresa = relationship("Empresa", back_populates="contratos")
    salas = relationship("Sala", back_populates="contrato")
    clausulas = relationship(
        "Clausula", back_populates="contrato",
        cascade="all, delete-orphan", order_by="Clausula.numero",
    )
    cobranças = relationship("Cobranca", back_populates="contrato", cascade="all, delete-orphan")
    descontos = relationship("Desconto", back_populates="contrato", cascade="all, delete-orphan")
    historico_reajustes = relationship(
        "HistoricoReajuste", back_populates="contrato", cascade="all, delete-orphan",
    )
    fiadores = relationship("Fiador", back_populates="contrato", cascade="all, delete-orphan")

    contrato_anterior = relationship(
        "Contrato", remote_side=[id],
        foreign_keys=[contrato_anterior_id],
        back_populates="contratos_subsequentes",
    )
    contratos_subsequentes = relationship(
        "Contrato",
        foreign_keys=[contrato_anterior_id],
        back_populates="contrato_anterior",
    )


class Clausula(Base):
    __tablename__ = "clausulas"

    id = Column(Integer, primary_key=True, index=True)
    contrato_id = Column(Integer, ForeignKey("contratos.id"), nullable=False)
    numero = Column(Integer, nullable=False)
    titulo = Column(String(200))
    texto = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    contrato = relationship("Contrato", back_populates="clausulas")
