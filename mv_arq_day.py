#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
from utilities import config_log, logging_inicio as inicio, logging_fim as fim, convert_to_julian_day, retorna_ano_dia, verifica_destino, lista_e_move
import logging


###########################################################################
#        Script para organização dos arquivos do GOES-R no Storage        #
###########################################################################
#  Metodo: Diario                                                         #
#  Descricao: Organiza os dados do GOES-R no storage em pastas            #
#  Autor: Guilherme de Moura Oliveira  <guimoura@unicamp.br>              #
#  Data: 04/04/2023                                                       #
#  Atualizacao: 05/07/2023                                                #
###########################################################################


# recebe return ano e dia do retorna_ano_dia
ano, dia = retorna_ano_dia()

# O diretório em que estão as imagens
origem = f'C:/Users/Gui/OneDrive/Documentos/python-scripts/ano{ano}'

# Config log
arq_log = "C:/Users/Gui/OneDrive/Documentos/python-scripts/logs/mv_arq_day.log"

# Configura log
config_log(arq_log)

# Inicia log
inicio()

# convertendo para dia juliano
convert_to_julian_day(dia)

# Diretório de destino
destino = f'C:/Users/Gui/OneDrive/Documentos/python-scripts/ano{ano}/dia{dia}/'   

# Criar func depois
try:
    lista_e_move(origem, destino, ano, dia)

# Tratamento de erros
except Exception as error:
    logging.error(f'Erro ao mover arquivos: {str(error)}')

# finalizando log  
fim()