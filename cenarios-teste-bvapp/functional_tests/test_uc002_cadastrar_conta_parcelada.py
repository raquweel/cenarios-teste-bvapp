'''
UC002 - Cadastrar conta a pagar parcelada

Objetivo: Permitir que o tesoureiro cadastre uma conta parcelada informando o valor total, o número de parcelas e o intervalo entre elas.

Requisitos:
- RF05012

Ator:
- Tesoureiro
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator acessa a página de cadastro de contas a pagar e seleciona o Tipo "Parcelada".

# O ator preenche os dados obrigatórios: Nome, Descrição, Fornecedor, Categoria, Valor total (R$), 
# Data de lançamento, Número de parcelas (maior que 1), Intervalo entre parcelas (dias), Tipo de juros, 
# Taxa de juros (%) e Status inicial "Aberta". [A1]

# O ator seleciona a opção "Salvar".

# O sistema valida que o número de parcelas e o intervalo foram preenchidos e gera automaticamente 
# as parcelas dividindo o valor total pelo número de parcelas informado. [RN1]

# O sistema salva a conta parcelada e exibe a mensagem "Conta a pagar cadastrada com sucesso!".


# 🟠 [A1] - TENTATIVA DE SALVAR SEM NÚMERO DE PARCELAS OU INTERVALO
# ---------------------------------------------------------------
# O ator seleciona o Tipo "Parcelada", mas deixa o Número de parcelas ou o Intervalo entre parcelas em branco.

# O sistema impede o salvamento e exibe mensagem de erro exigindo o preenchimento obrigatório desses campos.


# 🟣 [RN1] - VALIDAÇÃO DE CONTA PARCELADA
# ---------------------------------------------------------------
# No cadastro de conta parcelada, o usuário informa o valor total, o número de parcelas e o intervalo em dias, 
# cabendo ao sistema gerar e dividir automaticamente as parcelas correspondentes ao valor total.