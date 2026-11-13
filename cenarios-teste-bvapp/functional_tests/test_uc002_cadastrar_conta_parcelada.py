'''
UC002 - Cadastrar conta a pagar parcelada

Objetivo: Permitir que o tesoureiro cadastre uma conta parcelada exigindo número de parcelas, intervalo e validando que a soma das parcelas seja igual ao valor total.

Requisitos:
- RF05012

Ator:
- Tesoureiro
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página de cadastro de contas a pagar e seleciona o Tipo "Parcelada".

# O ator preenche os dados obrigatórios: Nome, Descrição, Fornecedor, Categoria, Valor (R$), 
# Data de lançamento, Número de parcelas (> 1), Intervalo entre parcelas (dias), Tipo de juros, 
# Taxa de juros (%) e Status inicial "Aberta". [A1]

# O ator seleciona a opção "Salvar".

# O sistema valida que o número de parcelas e o intervalo foram preenchidos e que a soma 
# das parcelas é igual ao valor total informado. [RN1]

# O sistema salva a conta parcelada e exibe a mensagem "Conta a pagar cadastrada com sucesso!".


# 🟠 [A1] - SOMA DAS PARCELAS DIFERENTE DO VALOR TOTAL
# ---------------------------------------------------------------

# Quando a soma das parcelas difere do valor total informado, o sistema impede o salvamento 
# e exibe mensagem de erro de validação.


# 🟣 [RN1] - VALIDAÇÃO DE CONTA PARCELADA
# ---------------------------------------------------------------

# Conta parcelada exige número de parcelas e intervalo entre parcelas (dias). 
# A soma das parcelas deve ser obrigatoriamente igual ao valor total.