'''
UC007 - Consultar, filtrar, ordenar e exportar listagem de cooperados inadimplentes

Objetivo: Permitir que o tesoureiro consulte cooperados com duas ou mais mensalidades em atraso, aplique filtros, ordene colunas, exporte em PDF/CSV e acesse o atalho de acordo.

Requisitos:
- RF05009

Ator:
- Tesoureiro
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator (Tesoureiro) acessa a funcionalidade de Listagem de Cooperados Inadimplentes. [A3]

# O sistema lista os cooperados com duas ou mais mensalidades em atraso, exibindo em cada linha:
# - Cooperado
# - Quantidade de mensalidades em atraso
# - Valor original em atraso
# - Valor atualizado
# - Dias do atraso mais antigo
# - Acordo vigente [RN1]

# O ator filtra a lista por faixa de atraso e por valor, ordena clicando em uma coluna e exporta em PDF ou CSV. [A1]

# O ator clica no atalho disponível na linha do cooperado para oferecer um acordo (RF05010). [A2]

# O sistema redireciona/abre o fluxo de oferta de acordo para o cooperado selecionado.


# 🟠 [A1] - EXPORTAR LISTAGEM EM CSV
# ---------------------------------------------------------------

# O ator seleciona a opção de exportação em CSV e o sistema gera o arquivo com os dados filtrados.


# 🟠 [A2] - SAÍDA DA LISTA APÓS REGULARIZAÇÃO OU ACORDO ACEITO
# ---------------------------------------------------------------

# Quando o cooperado regulariza as parcelas em atraso ou fecha um acordo aceito (recalculado diariamente), 
# o sistema remove o cooperado da condição de inadimplente na listagem.


# 🟠 [A3] - TENTATIVA DE ACESSO POR USUÁRIO NÃO TESOUREIRO
# ---------------------------------------------------------------

# Um usuário sem perfil de Tesoureiro tenta acessar a listagem de cooperados inadimplentes e o sistema bloqueia o acesso.


# 🟣 [RN1] - CRITÉRIO DE INADIMPLÊNCIA E RESTRIÇÃO DE ACESSO
# ---------------------------------------------------------------

# É considerado inadimplente o cooperado com 2 ou mais mensalidades em atraso. A condição é recalculada 
# diariamente e cessa com regularização ou acordo aceito. Acesso restrito ao Tesoureiro.