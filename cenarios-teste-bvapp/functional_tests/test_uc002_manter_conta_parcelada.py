'''
UC002 - Manter conta a pagar parcelada 

Objetivo: Permitir que o tesoureiro possa cadastrar, consultar, editar e remover logicamente contas a pagar parceladas no sistema.

Requisitos:
- RF05012

Ator:
- Tesoureiro
'''

# 🟢 [FP] - FLUXO PRINCIPAL 
# ---------------------------------------------------------------
# O ator (Tesoureiro) acessa a página de cadastro de contas a pagar e seleciona o Tipo "Parcelada".

# O sistema exibe os campos específicos para o parcelamento:
# - Valor total (R$)
# - Número de parcelas
# - Intervalo entre parcelas (dias)

# O ator preenche os dados obrigatórios da conta: Nome, Descrição, Prestador existente, Valor total (R$), Data de lançamento, 
# Número de parcelas (maior que 1), Intervalo entre parcelas (dias), Tipo de juros, Taxa de juros (%) e Status inicial "Aberta". [A4]

# Ao concluir o preenchimento, o ator seleciona a opção "Salvar". [A2][A3]

# O sistema verifica que o número de parcelas e o intervalo foram informados, calcula e gera 
# automaticamente as parcelas correspondentes ao valor total. [RN1]

# O sistema salva a conta parcelada e exibe a mensagem "Conta a pagar cadastrada com sucesso!".

# O ator acessa a consulta de detalhes da conta parcelada. [A1]

# O sistema exibe os dados da conta e a lista de todas as parcelas geradas com seus respectivos valores e vencimentos.


# 🟠 [A1] - CONSULTAR DETALHES DA CONTA PARCELADA
# ---------------------------------------------------------------
# O ator acessa a listagem geral (RF05020) e seleciona uma conta parcelada cadastrada.

# O sistema exibe o detalhe contendo os dados gerais da conta, todas as parcelas geradas, 
# os comprovantes e o histórico de alterações.


# 🟠 [A2] - EDITAR CONTA PARCELADA
# ---------------------------------------------------------------
# O ator executa [A1] e seleciona a opção para editar a conta parcelada.

# O sistema exibe o formulário de edição com os campos preenchidos.

# O ator altera o valor total da conta e seleciona "Salvar".

# O sistema atualiza a conta e recalcula automaticamente apenas o valor das parcelas ainda não pagas.


# 🟠 [A3] - REMOVER CONTA PARCELADA (EXCLUSÃO LÓGICA)
# ---------------------------------------------------------------
# O ator executa [A1] e seleciona uma conta parcelada que não possua nenhuma parcela paga e esteja com status "Aberta" ou "Atrasada".

# O ator seleciona a opção 'Remover', informa o motivo da remoção e confirma.

# O sistema realiza a remoção lógica e a conta parcelada deixa de aparecer nas listagens.


# 🟠 [A4] - CAMPOS DE PARCELAMENTO NÃO PREENCHIDOS
# ---------------------------------------------------------------
# O ator seleciona o Tipo "Parcelada", mas tenta salvar deixando o Número de parcelas ou o Intervalo 
# entre parcelas em branco.

# O sistema bloqueia o salvamento e exibe mensagem de erro exigindo o preenchimento obrigatório 
# desses campos.


# 🟣 [RN1] - GERAÇÃO E INTEGRIDADE DE PARCELAS
# ---------------------------------------------------------------
# No cadastro do tipo Parcelada, o tesoureiro informa o valor total, o número de parcelas (> 1) e o 
# intervalo em dias (> 0). O sistema divide e gera automaticamente as parcelas cuja soma equivale ao 
# valor total.