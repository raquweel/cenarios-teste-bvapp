"""
UC008 - Atualizar Status para Atrasada Automaticamente

Objetivo: Executar a rotina automática de alerta de vencimento para alterar o status das contas vencidas e não pagas para "Atrasada".

Requisitos: 
- [27182] Alerta de vencimento
- [24390] CA02 - O status Atrasada deve ser gerado automaticamente pelo sistema, se a conta não estiver marcada como Paga no período após sua data de vencimento

Ator:
- Sistema (Rotina de Backend)
"""

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
# O ciclo de verificação de pagamentos vencidos do backend é acionado periodicamente.
# O sistema identifica todas as contas cadastradas que não estão marcadas como "Paga".
# O sistema verifica quais dessas contas possuem a data de vencimento anterior à data atual (vencidas). [RN1]
# O sistema atualiza automaticamente o status dessas contas para "Atrasada".
# O sistema gera o log de execução da rotina.


# 🟣 [RN1] - REGRA DE TRANSIÇÃO PARA ATRASADA
# ---------------------------------------------------------------
# Se a conta não estiver marcada como Paga e o período atual for posterior à sua data de vencimento, o sistema deve gerar automaticamente o status "Atrasada".