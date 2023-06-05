#!/bin/bash

###########################################################################
#        Script para mover arquivos para uma pasta na storage             #
###########################################################################
#  Metodo: Diario                                                         #
#  Descricao: Script para copiar apenas o dia anterior para uma pasta em  #
#  nuvem GOES-16                                                          #
#  Autor: Guilherme de Moura Oliveira  <guimoura@unicamp.br>              #
#  Data: 9/05/2023                                                        #
#  Atualizacao: 18/05/2023                                                #
###########################################################################

ARQ_LOG="okul-CopyTo-Bellatrix-storage`date +%Y-%m-%d`.log"
DIR_LOG=/Scripts/level1b/logs/

#Obtendo o ano e dia anterior em dia juliano
ano=$(date +%Y -d "-1 day")
dia_anterior=$(date +%j -d "-1 day")

# Diretório de origem
origem="okul:/ess/data/satellite/goes/grb/level1b/"

# Diretório de destino
destino="/mnt/storage/level1b/ano$ano/dia$dia_anterior/"

#Inicia o script
echo "=========================================================================================================" &>> $DIR_LOG/$ARQ_LOG
echo "=========================================================================================================" &>> $DIR_LOG/$ARQ_LOG
echo "=                           INICIANDO SCRIPT BACKUP PARA STORAGE $(date '+%Y-%m-%d %H:%M:%S')           =" &>> $DIR_LOG/$ARQ_LOG
echo "=========================================================================================================" &>> $DIR_LOG/$ARQ_LOG
echo "=========================================================================================================" &>> $DIR_LOG/$ARQ_LOG
echo "" &>> $DIR_LOG/$ARQ_LOG
echo "" &>> $DIR_LOG/$ARQ_LOG

# Padrão a ser buscado
padrao="{*L1b*e$ano$dia_anterior*,*GLM-L2-LCFA*e$ano$dia_anterior*}"

# Move o arquivo para o diretório de destino
rclone move $origem --include "$padrao" $destino --transfers=100 --log-file=$DIR_LOG$ARQ_LOG -v

# Verifica se o arquivo rodou corretamente
if [ $? -eq 0 ]; then
    echo "Dados copiados com sucesso." >> "$DIR_LOG/$ARQ_LOG"
else
    echo "Ocorreu um erro na operação." >> "$DIR_LOG/$ARQ_LOG"
fi

echo "=========================================================================================================" >> "$DIR_LOG/$ARQ_LOG"
echo "=========================================================================================================" >> "$DIR_LOG/$ARQ_LOG"
echo "=                                 FINALIZANDO O SCRIPT $(date '+%Y-%m-%d %H:%M:%S')                     =" >> "$DIR_LOG/$ARQ_LOG"
echo "=========================================================================================================" >> "$DIR_LOG/$ARQ_LOG"
echo "=========================================================================================================" >> "$DIR_LOG/$ARQ_LOG"
echo "" &>> $DIR_LOG/$ARQ_LOG
echo "" &>> $DIR_LOG/$ARQ_LOG