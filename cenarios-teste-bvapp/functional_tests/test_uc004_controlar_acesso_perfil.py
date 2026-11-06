"""
UC004 - Controlar Acesso por Perfil

Objetivo: Garantir que apenas usuários tesoureiros possam acessar a tela de cadastro e alteração de status de contas.

Requisitos: 
- [24175] CA02 - Apenas membros da tesouraria podem cadastrar contas
- [24391] CA04 - Apenas os usuários tesoureiros podem atualizar os status das contas para Paga ou Cancelada

Ator:
- Membro Não Tesoureiro
"""

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ator realiza login no BVapp com um perfil de um membro não-tesoureiro.
# O ator tenta navegar até a página de cadastro de contas a pagar.
# O sistema identifica que o usuário não é membro tesoureiro da diretoria. [RN1]
# O sistema bloqueia o acesso e exibe a mensagem "Acesso restrito: Apenas membros da tesouraria podem cadastrar e alterar contas."


# 🟣 [RN1] - PERMISSÃO EXCLUSIVA DE TESOURARIA
# ---------------------------------------------------------------
# Apenas usuários logados como membro tesoureiro da diretoria possuem autorização para cadastrar contas e alterar seus status.