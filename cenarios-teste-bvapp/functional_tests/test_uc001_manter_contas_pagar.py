'''
UC001 - Manter contas a pagar 

Objetivo: Permitir cadastrar, consultar, editar e remover logicamente contas a pagar no sistema.

Requisitos:
- RF05012

Ator:
- Tesoureiro
'''

# 🟢 [FP] - FLUXO PRINCIPAL (CRUD COMPLETO)
# ---------------------------------------------------------------
# O tesoureiro acessa a página de cadastro de contas a pagar. Ele verifica que existem os campos:
# - Tipo (Parcelada ou Recorrente)
# - Nome
# - Descrição
# - Fornecedor (selecionado do cadastro existente)
# - Categoria 
# - Valor (R$)
# - Data de lançamento
# - Número de parcelas
# - Intervalo entre parcelas (dias)
# - Tipo de juros
# - Taxa de juros (%)
# - Anexo da nota fiscal ou boleto (opcional)
# - Status inicial (Aberta ou Cancelada)
# - Opções: Botão "Salvar" e Botão "Cancelar"

# O ator preenche os dados de uma conta única: Tipo "Única", Nome, Descrição, Fornecedor existente,
# Categoria de despesa existente, Valor (R$), Data de lançamento, Número de parcelas "1", 
# Intervalo entre parcelas "0", Tipo de juros, Taxa de juros (%) e Status inicial "Aberta". [A4]

# Ao concluir o cadastro, ele seleciona a opção "Salvar". [A2][A3]

# O sistema verifica que os dados estão corretos. [RN1]

# O sistema salva a conta a pagar e exibe a mensagem "Conta a pagar cadastrada com sucesso!".

# O ator acessa a consulta de detalhes da conta.

# O sistema exibe os dados da conta, suas parcelas, os comprovantes e o histórico de alterações.


# 🟠 [A1] - CONSULTAR DETALHES DA CONTA A PAGAR
# ---------------------------------------------------------------

# O ator acessa a listagem geral (RF05020) e seleciona uma conta cadastrada.

# O sistema exibe a página/modal de detalhe contendo os dados da conta, suas parcelas, 
# os comprovantes anexados e o histórico completo de alterações.


# 🟠 [A2] - EDITAR CONTA A PAGAR
# ---------------------------------------------------------------

# O ator (Tesoureiro) executa [A1] e seleciona a opção para editar a conta.

# O sistema exibe o formulário de edição com os campos preenchidos.

# O ator altera o valor da conta e seleciona "Salvar".

# O sistema atualiza a conta e registra a edição no log de auditoria com usuário, data, hora 
# e os valores anterior e novo dos campos alterados.


# 🟠 [A3] - REMOVER CONTA A PAGAR (EXCLUSÃO LÓGICA)
# ---------------------------------------------------------------

# O ator (Administrador) executa [A1] e seleciona uma conta sem parcela paga e com status "Aberta" ou "Atrasada".

# O ator seleciona a opção 'Remover', informa o motivo da remoção e confirma.

# O sistema realiza a remoção lógica (oculta a conta das listagens) e registra no log de auditoria 
# o ID, o motivo, o usuário, a data e a hora da remoção.


# 🟠 [A4] - ANEXAR NOTA FISCAL OU BOLETO
# ---------------------------------------------------------------

# O ator seleciona o campo "Anexo da nota fiscal ou boleto" e escolhe um arquivo nos formatos PDF, JPEG, JPG ou PNG.

# O sistema anexa o arquivo ao cadastro da conta.


# 🟣 [RN1] - REGRAS DE CADASTRO E PERMISSÃO
# ---------------------------------------------------------------

# Somente o Tesoureiro cadastra contas a pagar. Fornecedor e Categoria vêm dos cadastros existentes.
# Conta única exige 1 parcela e intervalo 0. Anexo é opcional (PDF, JPEG, JPG, PNG).