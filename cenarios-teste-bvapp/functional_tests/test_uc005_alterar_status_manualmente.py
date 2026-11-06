"""
UC005 - Alterar Status de Conta Manualmente

Objetivo: Permitir que o membro tesoureiro altere com sucesso o status de uma conta aberta para paga.

Requisitos: 
- [24386] CA01 - Uma conta deve apresentar, obrigatoriamente, um dos seguintes status: aberta, paga, atrasada, cancelada
- [24391] CA04 - Apenas os usuários tesoureiros podem atualizar os status das contas para Paga ou Cancelada
- [24398] US - Alteração de status de Contas e Cobranças

Ator:
- Membro Tesoureiro da Diretoria
"""

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator realiza login como membro tesoureiro da diretoria.
# O ator acessa a listagem e visualiza uma conta cadastrada com status "aberta".
# O ator seleciona a conta e altera o status para "paga".
# O ator aciona o botão de salvar.
# O sistema valida a permissão e atualiza o status da conta para "paga". [RN1]
# O sistema salva a alteração e exibe mensagem de sucesso.


# 🟣 [RN1] - ALTERAÇÃO COM SUCESSO
# ---------------------------------------------------------------
# Dado que o usuário seja tesoureiro e a conta esteja com status "aberta", a alteração para "paga" deve ser processada e salva com sucesso.