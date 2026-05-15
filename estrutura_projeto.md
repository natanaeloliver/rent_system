# Visão geral
Sistema/programa/fluxo/BI em que eu coloque todas as informações de vários contratos de locação de centro de inovação tecnológico.

# Objetivo
Desenvolver uma ferramenta que permite a gestão e visualização dos dados dos contratos.

## Visões
### Gerencial
Permite enxergar tudo o que já foi cobrado da empresa e tudo o que será cobrando em faixas de tempo customizadas (parte BI do projeto), por modalidade de contrato, visão total do período, por local em que a empresa está locada.
Permite uma visão que mostra em qual sala a empresa está atualmente em um formado de mapa.

### Jurídica
- Adicionar e administrar os contratos de cada empresa, adicionando clausulas e editando elas. Conseguindo finalizar um contrato e abrir outro com a mesma empresa mantendo a rastreabilidade.
- Permite informar qual é a data de reajuste do contrato e por qual taxa ele deve ser ajustado.
- O programa deve avisar ao ser iniciado, quais empresas estão com o contrato próximo do fim da vigência em dias a partir de 60 dias.
- Contratos vencidos, devem aparecer como alerta, junto aos contratos com dias para vencer, até que seja flaget como resolvido.

### Financeira
- Permite adicionar luz, gás, ou outros custos customizáveis em cada mês para gerar o valor de cobrança mesla real da empresa (extra + valor do contrato);
- Permite adiconar descontos fixos, ou percentuais mensais, assim como descontros contratuais (um ano de isenção);
- Perminte informar em uma sessão de taxas, os valores de cada taxa mensais, para realizar o cálculo do reajuste acumulado.

# Arquitetura
A ferramente deve ser simples ao ponto de que possa ser executado em um computador de um não programador, que não tem infraestrutura de código ou progrmação alguma, controlando a sua infraestrutura sozinha, sem a dependência de programas terceiros, sem a necessidade de manutenção.
Esta estrutura deve salvar todos os dados dos contratos, permitindo incluir, alterar, colocar novas cláusulas, vinculando contratos com a mesma empresa (saindo de uma modalidade para outra), salvando os dados dos representantes legais (são dados típicos de locatários);

# Detalhamento
## Estrutura por empresa (CNPJ/CPF) com cobrança mensal
- Cada contrato contém suas datas iniciais e datas finais de cobranças mensais, com valores por metro quadrado, ou valores fixos.
- Cada contrato contém um tipo de modalidade que devem ser: Locação, Incubação, Adesão,;

## Modalidades de contrato
### Locação
São contrato que tem data fim = prazo determinado, ou seja, geralmente de um ano e após este prazo, o contrato automaticamente vira "Prazo intederminado" a menos que haja uma extinção do contratual. Sendo assim, quem está com "prazo indeterminado" possui a cobrança sendo reajustada e a empresa continua no banco de dados com o contrato ativo.

### Incubação
- Possui uma data fim = data de extinção contratual; 
- São contratos de 3 anos, podendo ser prorrogado por mais um ano;
#### Incubação presencial
- Tem sala física;

#### Incubação hibrida
- Tem acesso ao coworking e um endereço fiscal;

#### Incubação a distância
- Não tem endereço fiscal e nem acesso ao coworking, apenas este presente no banco de dados e paga para participar do programa de incubação.

### Adesão
- Possue uma taxa fixa para fazer parte do sistema, mas não aluga uma sala física;

### Termo de cooperação
- É um contrato em que a empresa troca um serviço que ela presta para poder utilizar a sala locada, sem pagar nenhum valor por isso, pois já realiza o serviço.

