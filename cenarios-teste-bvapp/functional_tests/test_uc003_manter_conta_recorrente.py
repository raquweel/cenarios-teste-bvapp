'''
UC003 - Manter conta a pagar recorrente 

Objetivo: Permitir que o tesoureiro possa cadastrar, consultar, editar e remover logicamente contas a pagar recorrentes no sistema.

Requisitos:
- RF05012

Ator:
- Tesoureiro
'''

# 🟢 [FP] - FLUXO PRINCIPAL (CRUD COMPLETO - CONTA RECORRENTE)
# ---------------------------------------------------------------

# O ator (Tesoureiro) acessa a página de cadastro de contas a pagar e seleciona o Tipo "Recorrente".

# O ator preenche os dados obrigatórios da conta: Nome, Descrição, Fornecedor existente, 
# Categoria de despesa existente, Valor (R$), Data de lançamento, Intervalo entre parcelas (dias maior que 0), 
# Tipo de juros, Taxa de juros (%) e Status inicial "Aberta". [A4]

# Ao concluir o preenchimento, o ator seleciona a opção "Salvar". [A2][A3]

# O sistema valida que o intervalo entre parcelas (dias) foi preenchido e salva a conta recorrente. [RN1]

# O sistema exibe a mensagem "Conta a pagar cadastrada com sucesso!".

# O ator acessa a consulta de detalhes da conta recorrente. [A1]

# O sistema exibe os dados da conta recorrente, as parcelas já geradas por ciclo, os comprovantes e o histórico de alterações.


# 🟠 [A1] - CONSULTAR DETALHES DA CONTA RECORRENTE
# ---------------------------------------------------------------
# O ator acessa a listagem geral (RF05020) e seleciona uma conta recorrente cadastrada.

# O sistema exibe o detalhe contendo a periodicidade em dias, os dados da conta e as parcelas vinculadas.


# 🟠 [A2] - EDITAR CONTA RECORRENTE
# ---------------------------------------------------------------
# O ator executa [A1] e seleciona a opção para editar a conta recorrente.

# O sistema exibe o formulário de edição com os campos preenchidos.

# O ator altera o valor ou o intervalo em dias da conta e seleciona "Salvar".

# O sistema atualiza a conta e aplica os novos dados às parcelas em aberto e aos próximos ciclos gerados.


# 🟠 [A3] - REMOVER CONTA RECORRENTE (EXCLUSÃO LÓGICA)
# ---------------------------------------------------------------
# O ator executa [A1] e seleciona uma conta recorrente sem parcela paga e com status "Aberta" ou "Atrasada".

# O ator seleciona a opção 'Remover', informa o motivo da remoção e confirma.

# O sistema realiza a remoção lógica, interrompendo novos ciclos e ocultando a conta das listagens.


# 🟠 [A4] - INTERVALO DE RECORRÊNCIA NÃO PREENCHIDO
# ---------------------------------------------------------------
# O ator seleciona o Tipo "Recorrente", mas tenta salvar sem informar o Intervalo entre parcelas (dias).

# O sistema bloqueia o salvamento e exige o preenchimento do intervalo em dias.


# 🟣 [RN1] - REGRA DE CONTA RECORRENTE
# ---------------------------------------------------------------
# Conta recorrente exige intervalo entre parcelas (dias > 0) e gera uma nova parcela a cada ciclo 
# pela rotina automática do sistema (mesma rotina do RF05004).