#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###########################################################################
#                  Script para arrumar planilha dados                     #
###########################################################################
#  Metodo: anual                                                          #
#  Descricao:                                                             #
#  Autor: Guilherme de Moura Oliveira  <guimoura@unicamp.br>              #
#  Data: 07/07/2023                                                       #
#  Atualizacao: 07/07/2023                                                #
###########################################################################

def escrever_arquivo(nome_arquivo, dia, total_objects, total_size):
    with open(f'{nome_arquivo}.csv', 'a') as arquivo:
        arquivo.write(f'{dia} ')
        arquivo.write(f'{total_objects} ')
        arquivo.write(f'{total_size} \n')

def ler_arquivo(arquivo_entrada):
    arquivo_saida = 'saida'
    with open(f'{arquivo_entrada}.txt', 'r') as arquivo:
        linhas = arquivo.read().split('\n')
    
    dia = None
    total_objects = None
    total_size = None

    for linha in linhas:
        if linha.startswith('rclone size /mnt/storage/level1b/ano2023/'):
            if dia is not None:
                # Escreve as informações associadas ao dia anterior
                escrever_arquivo(arquivo_saida, dia, total_objects, total_size)
            dia = linha.split('/')[-1].strip()
            total_objects = None
            total_size = None
        elif linha.startswith('Total objects:'):
            total_objects = linha.split(' ')[2].replace('k', '').replace('.', '')
        elif linha.startswith('Total size:'):
            total_size = linha.split(' ')[2].replace('GiB', '')
    
    # Escreve as informações para o último dia
    if dia is not None and total_objects is not None and total_size is not None:
        escrever_arquivo(arquivo_saida, dia, total_objects, total_size)

arquivo_entrada = 'level1'
ler_arquivo(arquivo_entrada)
