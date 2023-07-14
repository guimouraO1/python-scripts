#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import logging
import datetime
from datetime import timedelta

###########################################################################
#                             Script Apagar NAVF                          #
###########################################################################
#  Metodo: Diario                                                         #
#  Descricao: Apaga os arquivos NAVF da okul - level2                     #
#  Autor: Guilherme de Moura Oliveira  <guimoura@unicamp.br>              #
#  Data: 14/07/2023                                                       #
#  Atualizacao: 14/07/2023                                                #
###########################################################################


# Configura o log
def config_log(arq_log):
    logging.basicConfig(filename=arq_log, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%d/%m/%Y %H:%M:%S")

# log início
def logging_inicio():
    logging.info('')
    logging.info('==================================================================================================================')
    logging.info('                                    Iniciando exclusão dos arquivos NAVF                                          ')
    logging.info('==================================================================================================================')
    logging.info('')

# log início
def fim():
    logging.info('')
    logging.info('==================================================================================================================')
    logging.info('                                           Finalizando os script                                                  ')
    logging.info('==================================================================================================================')
    logging.info('')

# Pasta destino log
arq_log = "/Scripts/level2/logs/deleteNAVF" + str(datetime.date.today()) + ".log"

# Configura log
config_log(arq_log)

# Inicia log
logging_inicio()

# O diretório em que estão as imagens
origem = f'okul:/ess/data/satellite/goes/grb/level2/'

# retorna o ano
ano = datetime.datetime.today().year

# retorna o dia de ontem em formato juliano
data_atual = datetime.datetime.now()
dia_anterior = data_atual - timedelta(days=1)
dia_anterior_juliano = dia_anterior.strftime("%j")

# Padrão a ser procurado
padrao = f'*NAVF*e{ano}{dia_anterior_juliano}*'

try:
    os.system(f'rclone delete {origem} --include {padrao} --log-file="{arq_log}" -v')
    logging.info('')
    logging.info(f'Os arquivos do dia {dia_anterior_juliano} com padrão {padrao}, fora deletados com sucesso!')
    logging.info('')
except Exception as error:
    logging.info('')
    logging.error(f'Erro ao deletar os arquivos: {str(error)}')
    logging.info('')


fim()