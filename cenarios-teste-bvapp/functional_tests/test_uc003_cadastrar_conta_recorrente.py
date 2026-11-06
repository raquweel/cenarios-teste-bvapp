"""
UC003 - Cadastrar Conta Recorrente

Objetivo: Permitir a configuração de contas a pagar do tipo Recorrente (com intervalo em dias e sem campo de número de parcelas).

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
# O ator seleciona a opção "Recorrente".

# O sistema atualiza a tela, oculta o campo "Número de parcelas" e exibe os campos:
# - Nome
# - Descrição (opcional)
# - Data de lançamento
# - Valor
# - Prestador
# - Status (aberta/cancelada)
# - Intervalo em dias

# O ator preenche: Nome "Licença de Software", Data de lançamento "01/12/2026", Valor "250.00", Prestador "Sistemas Brasil", Status "aberta" e Intervalo em dias "30".
# O ator clica em "Salvar".
# O sistema salva os dados da conta recorrente com sucesso. [RN1]


# 🟣 [RN1] - REGRAS DO TIPO RECORRENTE
# ---------------------------------------------------------------
# Para contas do tipo Recorrente, os campos Nome, Data de lançamento, Valor, Prestador, Status e Intervalo em dias são obrigatórios. O campo Número de parcelas não é exibido nem exigido.