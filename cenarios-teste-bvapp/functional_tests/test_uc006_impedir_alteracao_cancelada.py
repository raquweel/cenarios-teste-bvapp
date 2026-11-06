"""
UC006 - Impedir Alteração de Conta Já Cancelada

Objetivo: Bloquear qualquer tentativa de alterar o status de uma conta que esteja com status "cancelada".

Requisitos: 
- [26084] CA05 - O status Cancelada não pode ser alterada para outro status
- [24398] US - Alteração de status de Contas e Cobranças

Ator:
- Membro Tesoureiro da Diretoria
"""

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator realiza login como membro tesoureiro da diretoria.
# O ator acessa a lista de contas e seleciona uma conta com status "cancelada".
# O ator tenta alterar o status dessa conta para "paga".
# O ator aciona a opção para salvar.
# O sistema reconhece que a conta possui o status "cancelada". [RN1]
# O sistema impede a alteração.
# O sistema exibe uma mensagem informando que a conta está cancelada e não pode ser alterada.


# 🟣 [RN1] - IMUTABILIDADE DO STATUS CANCELADA
# ---------------------------------------------------------------
# O status "cancelada" não pode ser alterado para nenhum outro status, então a operação é bloqueada pelo sistema.