#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
from utilities import config_log, logging_inicio as inicio, logging_fim as fim, quantidade_arq, convert_to_julian_day, retorna_ano_dia, verifica_destino
import logging
import shutil

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
arq_log = "C:/Users/Gui/OneDrive/Documentos/python-scripts/logs/arquivo.log"

# Configura log
config_log(arq_log)

# Inicia log
inicio()

# convertendo para dia juliano
convert_to_julian_day(dia)

# Diretório de destino
destino = f'C:/Users/Gui/OneDrive/Documentos/python-scripts/ano{ano}/dia{dia}/'   

try:
    verifica_destino(destino)
    # Mover os arquivos
    arquivos = os.listdir(origem)
    for arquivo in arquivos:
        if f'e{ano}{dia}' in arquivo:
            origem_arquivo = os.path.join(origem, arquivo)
            destino_arquivo = os.path.join(destino, arquivo)
            shutil.move(origem_arquivo, destino_arquivo)
            logging.info(f'Arquivo {arquivo} movido para {destino_arquivo}')

# Tratamento de erros
except Exception as error:
    logging.error(f'Erro ao mover arquivos: {str(error)}')

# finalizando log  
fim()