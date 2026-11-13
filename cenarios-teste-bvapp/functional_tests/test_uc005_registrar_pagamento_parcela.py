'''
UC005 - Registrar pagamento de parcela de conta a pagar

Objetivo: Permitir que o tesoureiro registre o pagamento externo de uma parcela mediante comprovante obrigatório e recalcule o status da conta.

Requisitos:
- RF05013

Ator:
- Tesoureiro
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa os detalhes de uma conta a pagar e seleciona uma parcela para registrar pagamento.

# O ator informa a Data do pagamento, anexa o Comprovante de pagamento (PDF, JPEG, JPG ou PNG) 
# e preenche Observações. [A1]

# O ator confirma o registro do pagamento.

# O sistema valida o formato do comprovante obrigatório, altera o status da parcela para "Paga" 
# e recalcula o status geral da conta. [RN1]

# O ator verifica nos detalhes da conta que o comprovante está visível para usuários com permissão, 
# identificando a parcela e o usuário que o enviou.


# 🟠 [A1] - TENTATIVA DE REGISTRO SEM COMPROVANTE OU COM FORMATO INVÁLIDO
# ---------------------------------------------------------------

# O ator tenta registrar o pagamento sem anexar o comprovante ou enviando arquivo fora dos formatos 
# PDF, JPEG, JPG e PNG.

# O sistema bloqueia o registro e exige um comprovante válido.


# 🟣 [RN1] - COMPROVANTE OBRIGATÓRIO E RECÁLCULO DE STATUS
# ---------------------------------------------------------------

# O pagamento ocorre fora do sistema. O comprovante é obrigatório (PDF, JPEG, JPG e PNG). 
# Ao registrar, a parcela passa para "Paga", o status da conta é recalculado e o comprovante exibe parcela e autor.