import enum


class ModalidadeEnum(str, enum.Enum):
    locacao = "locacao"
    incubacao_presencial = "incubacao_presencial"
    incubacao_hibrida = "incubacao_hibrida"
    incubacao_distancia = "incubacao_distancia"
    adesao = "adesao"
    termo_cooperacao = "termo_cooperacao"
    termo_aditivo = "termo_aditivo"  # TA — aditivo a um contrato-pai


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


class StatusJuridicoEnum(str, enum.Enum):
    ok = "ok"
    pendente = "pendente"


class CriterioRateioEnum(str, enum.Enum):
    por_area = "por_area"          # proporcional à área m² de cada locatário
    por_contrato = "por_contrato"  # divisão igualitária entre contratos ativos
    fixo_por_sala = "fixo_por_sala"  # valor fixo por sala (informado diretamente)
