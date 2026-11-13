'''
UC006 - Visualizar balanço financeiro da cooperativa por período

Objetivo: Permitir que o tesoureiro visualize Entradas, Saídas, Saldo e o gráfico correspondente apurados estritamente pela data de pagamento em um período determinado.

Requisitos:
- RF05017

Ator:
- Tesoureiro
'''

# 🟢 [FP] - FLUXO PRINCIPAL (APURAÇÃO POR DATA DE PAGAMENTO)
# ---------------------------------------------------------------
# O ator (Tesoureiro) acessa a funcionalidade de Balanço Financeiro no sistema.

# O sistema exibe os campos de filtro de período (Data inicial e Data final) e o botão para consultar/filtrar.

# O ator informa a data inicial (ex: 01/11/2026) e a data final (ex: 30/11/2026) e solicita a apuração do balanço. [A1][A2]

# O sistema busca todas as parcelas quitadas cuja data de pagamento esteja dentro do intervalo informado, 
# ignorando parcelas apenas lançadas ou vencidas no período que ainda não foram pagas: [A3][RN1]
# - Entradas: soma das parcelas de cobranças com pagamento confirmado no período (ex: R$ 10.000,00)
# - Saídas: soma das parcelas de contas a pagar registradas como pagas no período (ex: R$ 4.000,00)
# - Saldo: cálculo automático de Entradas menos Saídas (ex: R$ 6.000,00)

# O sistema exibe na tela os indicadores consolidados de Entradas, Saídas e Saldo, 
# acompanhados de um gráfico comparativo entre entradas e saídas.


# 🟠 [A1] - PERÍODO COM SALDO NEGATIVO (SAÍDAS MAIORES QUE ENTRADAS)
# ---------------------------------------------------------------
# O ator consulta um período em que o total de Saídas pagas supera o total de Entradas confirmadas.

# O sistema calcula corretamente o Saldo negativo (Entradas menos Saídas) e atualiza o gráfico 
# refletindo a proporção maior de saídas no período.


# 🟠 [A2] - PERÍODO SEM MOVIMENTAÇÃO FINANCEIRA PAGA
# ---------------------------------------------------------------
# O ator informa um período em que não houve nenhuma parcela de cobrança confirmada nem parcela de 
# conta a pagar quitada.

# O sistema exibe Entradas = R$ 0,00, Saídas = R$ 0,00, Saldo = R$ 0,00 e o gráfico zerado sem apresentar erro.


# 🟠 [A3] - PARCELA VENCIDA NO PERÍODO, MAS PAGA EM OUTRA DATA
# ---------------------------------------------------------------
# Existe uma parcela com data de vencimento dentro do período consultado, porém sua data de pagamento ocorreu 
# fora desse intervalo (ou ainda está em aberto).

# O sistema não contabiliza essa parcela no balanço do período consultado, respeitando exclusivamente a 
# data de pagamento.


# 🟣 [RN1] - REGIME DE APURAÇÃO POR DATA DE PAGAMENTO
# ---------------------------------------------------------------
# Entradas (parcelas de cobranças pagas) e Saídas (parcelas de contas a pagar quitadas) são apuradas 
# exclusivamente pela data de pagamento dentro do período selecionado. O Saldo corresponde a Entradas 
# menos Saídas, exibido juntamente com o gráfico de entradas e saídas.