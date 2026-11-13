'''
UC006 - Visualizar balanço financeiro da cooperativa por período

Objetivo: Permitir que o tesoureiro visualize Entradas, Saídas, Saldo e o gráfico correspondente apurados pela data de pagamento em um período determinado.

Requisitos:
- RF05017

Ator:
- Tesoureiro
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a funcionalidade de Balanço Financeiro no sistema.

# O ator informa a data inicial e a data final do período desejado e solicita a consulta.

# O sistema apura os valores considerando estritamente a data de pagamento dentro do período informado:
# - Entradas: soma das parcelas de cobranças com pagamento confirmado no período
# - Saídas: soma das parcelas de contas a pagar registradas como pagas no período
# - Saldo: cálculo de Entradas menos Saídas [RN1]

# O sistema exibe os valores consolidados de Entradas, Saídas e Saldo na tela, acompanhados 
# de um gráfico comparativo de entradas e saídas.


# 🟣 [RN1] - APURAÇÃO POR DATA DE PAGAMENTO
# ---------------------------------------------------------------

# Os valores de Entradas e Saídas são apurados exclusivamente pela data de pagamento dentro do período 
# selecionado, exibindo Saldo (entradas menos saídas) e gráfico de entradas e saídas.