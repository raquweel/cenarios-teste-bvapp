'''
UC003 - Cadastrar conta a pagar recorrente

Objetivo: Permitir que o tesoureiro cadastre uma conta recorrente exigindo intervalo em dias para geração cíclica de parcelas.

Requisitos:
- RF05012

Ator:
- Tesoureiro
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página de cadastro de contas a pagar e seleciona o Tipo "Recorrente".

# O ator preenche os dados obrigatórios: Nome, Descrição, Fornecedor, Categoria, Valor (R$), 
# Data de lançamento, Intervalo entre parcelas (dias), Tipo de juros, Taxa de juros (%) e Status inicial "Aberta".

# O ator seleciona a opção "Salvar".

# O sistema valida que o intervalo entre parcelas (dias) foi preenchido e salva a conta recorrente. [RN1]

# O sistema exibe a mensagem "Conta a pagar cadastrada com sucesso!".


# 🟣 [RN1] - REGRA DE CONTA RECORRENTE
# ---------------------------------------------------------------

# Conta recorrente exige intervalo entre parcelas (dias) e gera uma nova parcela a cada ciclo 
# pela rotina automática do sistema (mesma rotina do RF05004).