"""
UC010 - Validação dos Campos Obrigatórios do Cadastro

Objetivo: Garantir que o sistema exija os campos obrigatórios do formulário e permita a gravação mantendo a Descrição vazia (campo opcional).

Requisitos: 
- [24154] Cadastro de contas a pagar
- [24172] CA01 - O cadastro da conta deve conter os seguintes campos obrigatórios

Ator:
- Membro Tesoureiro da Diretoria
"""

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator abre a tela de cadastro de contas a pagar.
# O ator preenche o campo "Nome", mas deixa "Data de lançamento", "Valor", "Prestador" e "Status" em branco.
# O ator clica em "Salvar".
# O sistema bloqueia o envio do formulário. [RN1]
# O sistema destaca os campos não preenchidos e exibe mensagem de alerta exigindo o preenchimento dos campos obrigatórios.


# 🟠 [A1] - CADASTRO COM CAMPO OPCIONAL EM BRANCO
# ---------------------------------------------------------------
# O ator preenche Nome, Data de lançamento, Valor, Prestador, Status (aberta/cancelada), Número de parcelas e Intervalo em dias, deixando a Descrição em branco.
# O ator clica em "Salvar".
# O sistema valida os campos obrigatórios e salva a conta com sucesso.


# 🟣 [RN1] - REGRA DE PREENCHIMENTO OBRIGATÓRIO
# ---------------------------------------------------------------
# Os campos Nome, Data de lançamento, Valor, Prestador, Status e dados de tipo/intervalo são estritamente obrigatórios. O campo Descrição é o único campo opcional.