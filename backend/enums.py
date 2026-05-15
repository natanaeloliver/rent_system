import enum


class ModalidadeEnum(str, enum.Enum):
    locacao = "locacao"
    incubacao_presencial = "incubacao_presencial"
    incubacao_hibrida = "incubacao_hibrida"
    incubacao_distancia = "incubacao_distancia"
    adesao = "adesao"
    termo_cooperacao = "termo_cooperacao"


class StatusContratoEnum(str, enum.Enum):
    ativo = "ativo"
    prazo_indeterminado = "prazo_indeterminado"
    vencido = "vencido"
    encerrado = "encerrado"


class ValorTipoEnum(str, enum.Enum):
    fixo = "fixo"
    por_m2 = "por_m2"


class IndiceEnum(str, enum.Enum):
    igpm = "IGPM"
    ipca = "IPCA"
    inpc = "INPC"
    ivar = "IVAR"
    customizado = "customizado"
    nenhum = "nenhum"


class TipoDescontoEnum(str, enum.Enum):
    fixo = "fixo"
    percentual = "percentual"
    contratual = "contratual"
