'''
UC001 - Manter contas a pagar 

Objetivo: Permitir que o tesoureiro possa cadastrar, consultar, editar e remover logicamente contas a pagar no sistema.

Requisitos:
- RF05012

Ator:
- Tesoureiro
'''

# 🟢 [FP] - FLUXO PRINCIPAL (CRUD COMPLETO)
# ---------------------------------------------------------------
# O ator (Tesoureiro) acessa a página de cadastro de contas a pagar. Ele verifica que existem os campos:
# - Tipo (Parcelada ou Recorrente)
# - Nome
# - Descrição
# - Prestador  
# - Valor (R$)
# - Data de lançamento
# - Número de parcelas (exibido quando Parcelada)
# - Intervalo entre parcelas (dias)
# - Tipo de juros
# - Taxa de juros (%)
# - Anexo da nota fiscal ou boleto (opcional)
# - Status inicial (Aberta ou Cancelada)
# - Opções: Botão "Salvar" e Botão "Cancelar"

# O ator seleciona o Tipo "Recorrente" e define o Intervalo entre parcelas como "0" dias 
# para caracterizar uma conta única (sem recorrência e sem número de parcelas).

# O ator preenche os demais dados: Nome, Descrição, Prestador existente, 
# Valor (R$), Data de lançamento, Tipo de juros, Taxa de juros (%) e Status inicial "Aberta". 
# Quando o tesoureiro preenche o formulário, antes de clicar em salvar, 
# ele pode escolher anexar um boleto [A4].

# Ao concluir o cadastro, ele seleciona a opção "Salvar". [A2][A3]

# O sistema verifica que os dados estão corretos. [RN1]

# O sistema salva a conta a pagar e exibe a mensagem "Conta a pagar cadastrada com sucesso!".

# O ator acessa a consulta de detalhes da conta.

# O sistema exibe os dados da conta, sua parcela única, os comprovantes e o histórico de alterações.


# 🟠 [A1] - CONSULTAR DETALHES DA CONTA A PAGAR
# ---------------------------------------------------------------
# O ator acessa a listagem geral (RF05020) e seleciona uma conta cadastrada.
# O sistema exibe o detalhe contendo os dados da conta, suas parcelas, os comprovantes e o histórico de alterações.


# 🟠 [A2] - EDITAR CONTA A PAGAR
# ---------------------------------------------------------------
# O ator executa [A1] e seleciona a opção para editar a conta.
# O sistema exibe o formulário de edição com os campos preenchidos.
# O ator altera o valor da conta e seleciona "Salvar".
# O sistema atualiza a conta e as parcelas ainda não pagas.


# 🟠 [A3] - REMOVER CONTA A PAGAR (EXCLUSÃO LÓGICA)
# ---------------------------------------------------------------
# O ator (Tesoureiro) executa [A1] e seleciona uma conta sem parcela paga e com status "Aberta" ou "Atrasada".
# O ator seleciona a opção 'Remover', informa o motivo da remoção e confirma.
# O sistema realiza a remoção lógica e a conta deixa de aparecer nas listagens.


# 🟠 [A4] - ANEXAR NOTA FISCAL OU BOLETO
# ---------------------------------------------------------------
# O ator seleciona o campo "Anexo da nota fiscal ou boleto" e escolhe um arquivo nos formatos PDF, JPEG, JPG ou PNG.
# O sistema anexa o arquivo ao cadastro da conta.


# 🟣 [RN1] - REGRAS DE CADASTRO E PERMISSÃO
# ---------------------------------------------------------------
# Somente o Tesoureiro cadastra e remove contas a pagar. Fornecedor e Categoria vêm dos cadastros existentes.
# Uma conta única é cadastrada selecionando o tipo Recorrente com intervalo de 0 dias (sem recorrência). 
# Anexo é opcional (PDF, JPEG, JPG, PNG).