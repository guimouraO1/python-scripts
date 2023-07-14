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

# Escreve no arquivo csv os dados recebidos da função ler_arquivos
def escrever_arquivo(nome_arquivo, dia, total_objects, total_size):
    with open(f'{nome_arquivo}.csv', 'a') as arquivo:
        arquivo.write(f'{dia} ')
        arquivo.write(f'{total_objects} ')
        arquivo.write(f'{total_size} \n')

# lê o arquivo txt para retornar os parametros pedidos
def ler_arquivo(arquivo_entrada):
    # Arquivo nome : para saida do CSV
    arquivo_saida = 'saida'

    # abre o arquivo para leitura(r) e salva na var arquivo
    with open(f'{arquivo_entrada}.txt', 'r') as arquivo:
        # as linhas são separadas por '\n' e atribuidas a variável linhas
        linhas = arquivo.read().splitlines()
    # Percorre todas as linhas
    for linha in linhas:
        # Se a linhas começar com : a variável dia vai receber a linha inteira
        if linha.startswith('rclone size /mnt/storage/level1b/ano2023/'):
            dia = linha.strip('-').strip()
            # dia recebe o dia só que separado do resto resultado ex: 001 ou 120 restando apenas os números
            dia = dia.replace('rclone size /mnt/storage/level1b/ano2023/dia','')
        # Se a linha começar com Total Objects a linha é separada com ' ' com .split, a variável total_objects recebe a casa [2] que tem a quantidade de objetos
        elif linha.startswith('Total objects:'):
            total_objects = linha.split(' ')[2]
            # Apenas tira o 'K', e o '.' da string
            total_objects = total_objects.replace(f'k', '').replace('.', '')
        # Se a linha começar com Total size: a linha é separada com ' ' com .split, a variável total_size recebe a casa [2] que contém os GB
        elif linha.startswith('Total size:'):
            total_size = linha.split(' ')[2]
            # Apenas tira o 'GiB' da string
            total_size = total_size.replace('GiB', '')
        
        try:
            # Grava as informações no arquivo de saída
            escrever_arquivo(arquivo_saida, dia, total_objects, total_size)
            print('Arquivo criado')
        # Printa o erro
        except Exception as error:
            print(f'Erro ao deletar os arquivos: {str(error)}')

            

arquivo_entrada = 'level1'

ler_arquivo(arquivo_entrada)