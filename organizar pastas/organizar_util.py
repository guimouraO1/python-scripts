#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path
import os.path
import logging
import shutil
import re

###########################################################################
#                           Script de funções                             #
###########################################################################
#  Metodo: anual                                                          #
#  Descricao: Script das funções de organizar l1 e l2                     #
#  Autor: Guilherme de Moura Oliveira  <guimoura@unicamp.br>              #
#  Data: 07/07/2023                                                       #
#  Atualizacao: 07/07/2023                                                #
###########################################################################

# Configura o log
def config_log(arq_log):
    # Pasta destino log
    logging.basicConfig(filename=arq_log, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
    
    
    
# log início
def logging_inicio():
    logging.info('')
    logging.info('==================================================================================================================')
    logging.info('                                                     INICIO                                                       ')
    logging.info('==================================================================================================================')
    logging.info('')

    
# log fim
def logging_fim():
    logging.info('')
    logging.info("==================================================================================================================")
    logging.info("=                                                     FIM                                                        =")
    logging.info("==================================================================================================================")
    logging.info('')
    


# converte para dia juliano
def convert_to_julian_day(day):
    if not day is None or day != int() or day <= 0:
        return str(day).zfill(3)


def verifica_destino(destino):
    
    # Verifica se a pasta de destino existe, se não existir, cria
    if not os.path.exists(destino):
        os.makedirs(destino)
        logging.info('')
        logging.info(f'A pasta {destino} Não existe.')
        logging.info('')
        logging.info(f'Criando...')
        logging.info('')
        logging.info(f'A pasta {destino} foi criada.')
        logging.info('')
            

# Obter uma lista de arquivos apenas no diretório  ordena e retorna lista e quantidade de arquivos PARA PASTAS COM ARQUIVOS SEM DATA
def obtem_lista_arquivos(origem):       
    
    try:
        # Obter uma lista de arquivos e não diretorios
        arquivos = [arquivo for arquivo in os.listdir(origem) if os.path.isfile(os.path.join(origem, arquivo))]
        # Ordenando a lista
        arquivos.sort()
        logging.info('')
        logging.info(f'Obtendo lista de arquivos ')

        # Apegans logs
        if len(arquivos) > 0:
            logging.info('')
            logging.info(f'A lista de arquivos foi obtida com sucesso! ')
            logging.info('')
            logging.info(f'A lista tem {len(arquivos)} arquivos ')
            logging.info('')
        else:
            logging.info('')
            logging.info(f'Não há arquivos na lista. ')
            logging.info('')
            
    except:
        logging.info('')
        logging.info(f'Não conseguiu obter lista de arquivos na pasta {origem}')
        logging.info('')
        
    return arquivos



# Move os arquivos para suas respectivas pastas USAR MOVE TODOS OS ARQUIVOS
def movendo_arquivos(origem, quantidade_arquivos, lista_arquivos, ano):
    
    # quantidade de arquivos transferidos
    arquivos_transferidos = 0
    
    # começa o loop entre arquivos
    for x in range(0, quantidade_arquivos):
        try:
            # Obtem o arquivo na casa correspondente
            arquivo = lista_arquivos[x]
            logging.info(f'Começando a mover o Arquivo: {arquivo} ')

        except:
            logging.info('')
            logging.info('Nenhum arquivo no diretório.')
            logging.info('')
        
        # Extrair o dia do arquivo
        match = re.search(r'_e2023(\d{3})', arquivo)

        # Se ele conseguiu extrair  continua ->
        if match:
            # Receber o dia extraído do arquivo
            dia = match.group(1)
            # Transformar o dia em inteiro em uma string com 3 dígitos
            dia_txt = str(convert_to_julian_day(dia))
            logging.info(f'O arquivo contém o dia {dia_txt}')
            # encontra o destino do arquivo
            destino = Path(f'{origem}/ano{ano}/dia{dia_txt}')
            # verifica se o destino existe, se não existir é criado
            verifica_destino(destino)
        else:
            logging.info(f'A sequência "e2023{dia_txt}" não foi encontrada no nome do arquivo.')
            logging.info('')
            
        # Caminho do arquivo
        caminho_arquivo = str(origem + arquivo)

        # Move o arquivo para a pasta de destino
        try:
            logging.info(f'Movendo arquivo para a pasta de destino')
            shutil.move(caminho_arquivo, destino)
            logging.info(f'Arquivo: {arquivo} Foi movido com sucesso! ')
            logging.info('------------------------------------------------------------------------------------------------------------------------------------')
            arquivos_transferidos += 1
        except:
            logging.info(f'Não foi possível transferir o arquivo: {arquivo}.')
            logging.info('')
    
    return arquivos_transferidos
