"""
UC001 - Manter Contas a Pagar

Objetivo: Permitir que o tesoureiro possa cadastrar, consultar, alterar e excluir contas a pagar no sistema.

Requisitos: 
- [24154] Cadastro de contas a pagar
- [24172] CA01 - O cadastro da conta deve conter os seguintes campos obrigatórios
- [24175] CA02 - Apenas membros da tesouraria podem cadastrar contas

Ator:
- Membro Tesoureiro da Diretoria
"""
# 🟢 [FP] - FLUXO PRINCIPAL (CRUD COMPLETO)
# ---------------------------------------------------------------
# O ator acessa a página de cadastro de contas a pagar. Ele verifica que o 
# título da página é "Cadastro de Contas a Pagar". Ele observa os tipos para seleção:
# - Seletor/Botão "Única/Parcelada"
# - Seletor/Botão "Recorrente"
# E os campos de cadastro exibidos:
# - Nome
# - Descrição (opcional)
# - Data de lançamento
# - Valor
# - Prestador
# - Status (aberta/cancelada)
# - Número de parcelas
# - Intervalo em dias
# - Opções
# -- Botão "Salvar"
# -- Botão "Cancelar"

# O ator seleciona o tipo "Única/Parcelada".

# O ator preenche os campos obrigatórios: Nome "Conta de Luz", Data de lançamento "20/11/2026", 
# Valor "350.00", Prestador "Energisa", Status "aberta", Número de parcelas "1" e Intervalo em dias "0".

# Ao concluir o preenchimento, ele seleciona a opção "Salvar". [A2][A3]

# O sistema verifica que os dados estão corretos. [RN1]

# O sistema salva a conta e exibe a mensagem "Conta a pagar cadastrada com sucesso!".

# O ator seleciona 'Consultar' no menu.

# O sistema exibe a página de listagem de contas a pagar.

# O ator verifica que a conta cadastrada está na lista.


# 🟠 [A1] - BUSCAR CONTA A PAGAR
# ---------------------------------------------------------------
# O ator necessita realizar uma busca por contas na lista.
# Ele acessa a página "Listar contas a pagar".

# O sistema exibe a página de listagem de contas.

# Seleciona o campo específico para busca e digita o nome do prestador ou nome da conta.

# O ator seleciona 'Pesquisar'.

# O sistema exibe todas as contas que correspondem aos termos digitados.


# 🟠 [A2] - EDITAR CONTA A PAGAR
# ---------------------------------------------------------------
# O ator executa [A1].

# O ator seleciona a conta na lista e clica no botão para editar a conta.

# O sistema exibe a página de edição de contas a pagar com os campos preenchidos com os dados atuais.

# O ator altera o Valor e a Descrição da conta e clica no botão "Salvar".

# O sistema salva os dados atualizados.

# O ator seleciona 'Listar contas' no menu.

# O sistema exibe a lista de contas cadastradas.

# O ator verifica que a conta atualizada exibe os novos dados.


# 🟠 [A3] - EXCLUIR CONTA A PAGAR
# ---------------------------------------------------------------
# O ator decide excluir a conta e executa [A1].

# Ele visualiza a conta e seleciona a opção 'Excluir'.

# O sistema pergunta se o usuário realmente deseja excluir a conta a pagar.

# O ator confirma a exclusão.

# O sistema exclui a conta a pagar.

# O ator seleciona 'Listar contas' no menu.

# O sistema exibe a lista de contas cadastradas.

# O ator verifica que a conta excluída não está mais na lista.


# 🟣 [RN1] - VALIDAÇÃO DA CONTA ÚNICA/PARCELADA
# ---------------------------------------------------------------
# No cadastro do tipo Única/Parcelada, é obrigatório preencher Nome, Data de lançamento, Valor, Prestador, Status, Número de parcelas e Intervalo em dias. O campo Descrição é opcional.