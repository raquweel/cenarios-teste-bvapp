"""
UC002 - Cadastrar Conta Parcelada

Objetivo: Permitir o cadastro de contas a pagar divididas em múltiplas parcelas no formulário Única/Parcelada.

Requisitos: 
- [24154] Cadastro de contas a pagar
- [24172] CA01 - O cadastro da conta deve conter os seguintes campos obrigatórios
- [24175] CA02 - Apenas membros da tesouraria podem cadastrar contas

Ator:
- Membro Tesoureiro da Diretoria
"""

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator acessa a página de cadastro de contas a pagar.
# O ator seleciona o tipo "Única/Parcelada". [A1]

# O sistema disponibiliza os campos específicos: Nome, Descrição (opcional), Data de lançamento, Valor, Prestador, Status, Número de parcelas e Intervalo em dias.
# O ator preenche os campos obrigatórios:
# - Nome: "Conta telfônica"
# - Data de lançamento: "10/12/2026"
# - Valor: "4500.00"
# - Prestador: "Claro"
# - Status: "aberta"
# - Número de parcelas: "3"
# - Intervalo em dias: "30"

# O ator clica no botão "Salvar".

# O sistema valida o preenchimento do número de parcelas e do intervalo em dias, salvando o cadastro com sucesso. [RN1]


# 🟠 [A1] - ALTERAR TIPO PARA RECORRENTE
# ---------------------------------------------------------------
# O ator altera a opção para "Recorrente".
# O sistema oculta o campo "Número de parcelas" e mantém apenas o campo "Intervalo em dias".


# 🟣 [RN1] - VALIDAÇÃO DE CAMPOS PARCELADOS
# ---------------------------------------------------------------
# No cadastro de tipo Única/Parcelada, os campos Número de parcelas e Intervalo em dias são de preenchimento obrigatório.