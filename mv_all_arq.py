#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utilities import config_log, logging_inicio as inicio, logging_fim as fim, obtem_lista_arquivos, movendo_arquivos

# Config log
arq_log = "C:/Users/Gui/OneDrive/Documentos/python-scripts/logs/mv_all_arq.log"

###########################################################################
#        Script para organização dos arquivos do GOES-R no Storage        #
###########################################################################
#  Metodo: Diario                                                         #
#  Descricao: Organiza os dados do GOES-R no storage em pastas            #
#  Autor: Guilherme de Moura Oliveira  <guimoura@unicamp.br>              #
#  Data: 04/04/2023                                                       #
#  Atualizacao: 05/07/2023                                                #
###########################################################################


# Configura log
config_log(arq_log)

# Inicia log
inicio()

ano = 2023

# O diretório em que estão as imagens
origem = f'C:/Users/Gui/OneDrive/Documentos/python-scripts/ano{ano}/'

# Config log
arq_log = "C:/Users/Gui/OneDrive/Documentos/python-scripts/logs/arquivo.log"

# Obtem a lista de todos os arquivos de uma pasta, retorna lista e quantidade de arquivos da lista
lista_arquivos = obtem_lista_arquivos(origem)

# Obtem a quantidade de arquivos
quantidade_arquivos = len(lista_arquivos)

# move os arquivos para as pastas
movendo_arquivos(origem, quantidade_arquivos, lista_arquivos)

# finalizando log  
fim()