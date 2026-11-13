'''
UC004 - Validar regras de edição e remoção lógica de contas a pagar

Objetivo: Garantir que a edição de uma conta atualize automaticamente apenas as parcelas ainda não pagas, preservando as parcelas pagas intactas, impeça a edição de contas canceladas e valide todas as restrições de permissão, status e parcelas na remoção lógica.

Requisitos:
- RF05012

Ator:
- Tesoureiro
- Usuário sem permissão de Tesoureiro (para validação de bloqueio)
'''

# 🟢 [FP] - FLUXO PRINCIPAL (EDIÇÃO PRESERVANDO PARCELAS PAGAS)
# ---------------------------------------------------------------
# O ator (Tesoureiro) acessa a listagem geral de contas a pagar (RF05020) e seleciona uma conta parcelada 
# com status "Aberta" que possui 3 parcelas cadastradas:
# - Parcela 1: status "Paga" (Valor: R$ 500,00)
# - Parcela 2: status "Aberta" (Valor: R$ 500,00)
# - Parcela 3: status "Aberta" (Valor: R$ 500,00)

# O sistema exibe a tela de detalhes da conta com a relação das parcelas e suas respectivas situações.

# O ator seleciona a opção "Editar" na conta a pagar. [A1]

# O sistema exibe o formulário de edição preenchido com os dados atuais da conta (Nome, Descrição, Fornecedor, 
# Categoria, Valor, Tipo de juros, Taxa de juros e Status).

# O ator altera o campo Descrição e atualiza o Valor das parcelas pendentes para "R$ 650,00".

# O sistema valida os dados e atualiza automaticamente apenas as parcelas que ainda não foram pagas (Parcelas 2 e 3). [RN1]

# O sistema exibe mensagem de confirmação da edição e retorna aos detalhes da conta.

# O ator verifica na lista de parcelas que:
# - A Parcela 1 (status "Paga") permaneceu completamente inalterada com seu valor original de R$ 500,00.
# - As Parcelas 2 e 3 (status "Aberta") foram atualizadas automaticamente com os novos valores.


# 🟠 [A1] - TENTATIVA DE EDITAR CONTA COM STATUS "CANCELADA"
# ---------------------------------------------------------------
# O ator (Tesoureiro) acessa os detalhes de uma conta a pagar cujo status atual seja "Cancelada".

# O ator tenta acionar a opção "Editar" (ou tenta submeter alterações na conta).

# O sistema bloqueia a operação e exibe mensagem informando que contas canceladas não podem ser editadas.


# 🟠 [A2] - TENTATIVA DE REMOVER CONTA COM PARCELA PAGA
# ---------------------------------------------------------------
# O ator (Tesoureiro) acessa os detalhes de uma conta que possui pelo menos uma parcela com status "Paga" 
# (mesmo que ainda existam outras parcelas em aberto).

# O ator seleciona a opção "Remover", o sistema pede confirmação da ação e o ator confirma.

# O sistema verifica o histórico das parcelas da conta, bloqueia a exclusão lógica e exibe mensagem informando 
# que contas com parcela paga não podem ser removidas.


# 🟠 [A3] - TENTATIVA DE REMOVER CONTA COM STATUS DIFERENTE DE "ABERTA" OU "ATRASADA"
# ---------------------------------------------------------------
# O ator (Tesoureiro) seleciona uma conta cujo status seja "Paga" ou "Cancelada" (sem parcelas pagas) e tenta removê-la.

# O sistema bloqueia a remoção lógica e informa que apenas contas com status "Aberta" ou "Atrasada" podem ser removidas.


# 🟠 [A4] - TENTATIVA DE REMOÇÃO SEM MOTIVO OU POR USUÁRIO NÃO TESOUREIRO
# ---------------------------------------------------------------
# Um usuário que não possui o perfil de Tesoureiro tenta acessar a funcionalidade de remoção de contas a pagar. 
# O sistema bloqueia a ação por falta de permissão.


# 🟣 [RN1] - REGRAS DE INTEGRIDADE NA EDIÇÃO E REMOÇÃO LÓGICA
# ---------------------------------------------------------------
# 1. Na edição: apenas parcelas ainda não pagas são atualizadas automaticamente; parcelas com status "Paga" 
# permanecem inalteradas. Contas com status "Cancelada" não podem ser editadas.
# 2. Na remoção: somente o Tesoureiro pode remover contas. A remoção é lógica (oculta a conta das listagens) 
# e só é permitida para contas sem nenhuma parcela paga e com status "Aberta" ou "Atrasada".