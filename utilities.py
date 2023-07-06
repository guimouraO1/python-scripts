import os
from pathlib import Path
import os.path
import logging


# Configura o log
def config_log(arq_log):
    # Pasta destino log
    logging.basicConfig(filename=arq_log, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
    
# log início
def logging_inicio():
    logging.info('')
    logging.info('')
    logging.info('==================================================================================================================')
    logging.info('                                INICIO        verificando o arquivo                                               ')
    logging.info('==================================================================================================================')
    logging.info('')
    logging.info('')
    
# log fim
def logging_fim():
    logging.info('')
    logging.info('')
    logging.info("==================================================================================================================")
    logging.info("=                                                     FIM                                                        =")
    logging.info("==================================================================================================================")
    logging.info('')
    logging.info('')
    
# salva no log a quantidade de arquivos
def quantidade_arq(quantidade_arquivos):
    logging.info('==================================================================================================================')
    logging.info(f'                      Quantidade de arquivos a serem transferidos {str(quantidade_arquivos)}                      ')
    logging.info('==================================================================================================================')
    logging.info('\n')

    logging.info('Começando... ')

# converte para dia juliano
def convert_to_julian_day(day):
    if not day is None or day != int() or day <= 0:
        return str(day).zfill(3)

# Pegando os arquivos que ele dejesa mover 
def retorna_ano_dia():
    # Pegando o ano 
    ano = str(input('Digite o Ano que deseja mover: '))
    # Pegando o dia
    dia = str(input('Digite o Dia em dia juliano que deseja mover: '))
    return ano, dia


def verifica_destino(destino):
    
    # Verifica se a pasta de destino existe, se não existir, cria
    if not os.path.exists(destino):
        os.makedirs(destino)
        logging.info(f'A pasta {destino} foi criada.')
    
    
    
