"""
UC007 - Cadastrar Conta Única

Objetivo: Permitir o cadastro de uma conta a pagar de parcela única selecionando o tipo Única/Parcelada.

Requisitos: 
- [24154] Cadastro de contas a pagar
- [24172] CA01 - O cadastro da conta deve conter os seguintes campos obrigatórios
- [24175] CA02 - Apenas membros da tesouraria podem cadastrar contas
- [36132] CA03 - O cadastro de uma conta única utiliza o formulário Única/Parcelada preenchendo obrigatoriamente o campo Número de parcelas com o valor 1 e o Intervalo em dias com o valor 0, caso contrário, a conta é parcelada

Ator:
- Membro Tesoureiro da Diretoria
"""

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator acessa a página de cadastro de contas a pagar.
# O ator seleciona o tipo "Única/Parcelada".
# O sistema disponibiliza os campos para preenchimento.
# O ator preenche os dados para uma conta de pagamento único:
# - Nome: "Taxa de Licenciamento"
# - Descrição: "Pagamento de taxa anual" (opcional)
# - Data de lançamento: "15/11/2026"
# - Valor: "450.00"
# - Prestador: "Prefeitura Municipal"
# - Status: "aberta"
# - Número de parcelas: "1"
# - Intervalo em dias: "0"

# O ator clica no botão "Salvar".
# O sistema valida o preenchimento, confirma que se trata de uma parcela única (1 parcela e 0 dias de intervalo) e salva a conta com sucesso. [RN1]


# 🟣 [RN1] - REGRA DE CONTA ÚNICA
# ---------------------------------------------------------------
# O cadastro de uma conta única utiliza o formulário Única/Parcelada preenchendo obrigatoriamente o campo Número de parcelas com o valor 1 e o Intervalo em dias com o valor 0.