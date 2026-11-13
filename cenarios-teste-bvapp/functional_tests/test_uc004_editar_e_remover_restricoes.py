'''
UC004 - Validar regras de edição e remoção lógica de contas a pagar

Objetivo: Garantir que a edição preserve parcelas pagas, impeça edição de contas canceladas e que a remoção lógica seja feita apenas pelo tesoureiro em contas sem parcela paga e com status "Aberta" ou "Atrasada".

Requisitos:
- RF05012

Ator:
- Tesoureiro
'''

# 🟢 [FP] - FLUXO PRINCIPAL (EDIÇÃO PRESERVANDO PARCELAS PAGAS)
# ---------------------------------------------------------------

# O ator acessa uma conta a pagar que possui parcelas com status "Paga" e parcelas ainda não pagas. [A1][A2]

# O ator edita os dados da conta e seleciona "Salvar".

# O sistema atualiza automaticamente apenas as parcelas ainda não pagas, mantendo as parcelas pagas inalteradas. [RN1]


# 🟠 [A1] - TENTATIVA DE EDITAR CONTA CANCELADA
# ---------------------------------------------------------------

# O ator seleciona uma conta com status "Cancelada" e tenta editá-la.

# O sistema bloqueia a edição, pois contas canceladas não podem ser editadas.


# 🟠 [A2] - TENTATIVA DE REMOVER CONTA COM PARCELA PAGA OU STATUS INVÁLIDO
# ---------------------------------------------------------------

# O ator (Tesoureiro) tenta remover uma conta que possui parcela paga ou que não esteja com status "Aberta" ou "Atrasada".

# O sistema bloqueia a remoção lógica e impede que o registro seja excluído.


# 🟣 [RN1] - INTEGRIDADE NA EDIÇÃO E REMOÇÃO
# ---------------------------------------------------------------

# Parcelas pagas permanecem inalteradas na edição e contas canceladas não podem ser editadas.
# Somente o Tesoureiro pode remover contas, informando o motivo, apenas quando não houver parcela paga e o status for "Aberta" ou "Atrasada".