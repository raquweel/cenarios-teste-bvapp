'''
UC007 - Consultar, filtrar, ordenar e exportar listagem de cooperados inadimplentes

Objetivo: Permitir que o tesoureiro consulte cooperados com duas ou mais mensalidades em atraso, aplique filtros por faixa de atraso e valor, ordene por qualquer coluna, exporte a listagem em PDF e CSV e acione o atalho para oferta de acordo.

Requisitos:
- RF05009

Ator:
- Tesoureiro
- Usuário sem permissão de Tesoureiro (para validação de bloqueio)
'''

# 🟢 [FP] - FLUXO PRINCIPAL (CONSULTA, FILTRO, ORDENAÇÃO, EXPORTAÇÃO PDF E ATALHO DE ACORDO)
# ---------------------------------------------------------------
# O ator (Tesoureiro) acessa a funcionalidade de Listagem de Cooperados Inadimplentes no sistema. [A4]

# O sistema verifica o perfil do usuário e exibe a listagem contendo exclusivamente os cooperados 
# que possuem 2 ou mais mensalidades em atraso, apresentando as seguintes colunas por registro: [A2][RN1]
# - Cooperado
# - Quantidade de mensalidades em atraso
# - Valor original em atraso
# - Valor atualizado
# - Dias do atraso mais antigo
# - Acordo vigente

# O ator preenche os filtros disponíveis por faixa de atraso (dias) e por faixa de valor em atraso e aciona a busca.

# O sistema atualiza a tabela exibindo apenas os cooperados inadimplentes que atendem aos critérios filtrados.

# O ator clica no cabeçalho de uma coluna (ex: "Dias do atraso mais antigo") para ordenar os resultados.

# O sistema reordena a listagem conforme a coluna selecionada (decrescente).

# O ator seleciona a opção de exportação em "PDF". [A1]

# O sistema gera e disponibiliza para download o arquivo PDF contendo os dados da listagem.

# O ator localiza a linha de um cooperado inadimplente e clica no atalho de ação para oferecer um acordo (RF05010).

# O sistema abre/redireciona para a tela de oferta de acordo já vinculada ao cooperado selecionado.


# 🟠 [A1] - COOPERADO COM APENAS 1 MENSALIDADE EM ATRASO (NÃO INADIMPLENTE)
# ---------------------------------------------------------------
# Existe um cooperado cadastrado com apenas 1 mensalidade em atraso no sistema.

# O sistema não exibe esse cooperado na listagem de inadimplentes, pois a regra exige 2 ou mais mensalidades 
# em atraso.


# 🟠 [A2] - RECÁLCULO DIÁRIO E SAÍDA DA LISTA APÓS REGULARIZAÇÃO OU ACORDO ACEITO
# ---------------------------------------------------------------
# Cenário A (Saída): Um cooperado anteriormente listado regulariza as parcelas em atraso (ficando com menos 
# de 2 em atraso) ou fecha um acordo aceito. Após o recálculo diário do sistema, o cooperado deixa de constar 
# como inadimplente na listagem.

# Cenário B (Entrada): Um cooperado atinge 2 mensalidades em atraso. No recálculo diário automático, 
# o sistema passa a exibi-lo na listagem de inadimplentes.


# 🟠 [A3] - TENTATIVA DE ACESSO POR USUÁRIO NÃO TESOUREIRO
# ---------------------------------------------------------------
# Um usuário que não possui o perfil de Tesoureiro (ex: cooperado comum) tenta acessar a Listagem de Cooperados Inadimplentes.

# O sistema bloqueia o acesso e impede a visualização dos dados financeiros de inadimplência.

# 🟣 [RN1] - CRITÉRIO DE INADIMPLÊNCIA, RECÁLCULO E PERMISSÃO
# ---------------------------------------------------------------
# 1. Critério: Considera-se inadimplente o cooperado com duas ou mais mensalidades em atraso.
# 2. Atualização: A condição é recalculada diariamente e deixa de valer quando o cooperado regulariza 
# as parcelas ou fecha um acordo aceito.
# 3. Recursos e Segurança: Suporta filtros por faixa de atraso e valor, ordenação por qualquer coluna, 
# exportação em PDF/CSV e atalho para acordo (RF05010). Acesso estritamente restrito ao Tesoureiro.