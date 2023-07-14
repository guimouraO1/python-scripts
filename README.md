<p align="left"></p>

###

<h2 align="left"></h2>


# Documentação scripts

Documentação dos scripts criados no Centro de Pesquisas Meteorológicas e Climáticas Aplicadas à Agricultura - CEPAGRI/UNICAMP - Universidade Estadual de Campinas.

Autor `Guilherme de Moura Oliveira`


## Documentação

- Backups


`backup_nuvemflash.sh`
`backup_nuveml1b.sh`
`backup_nuveml2`

`backup_storageflash.sh`
`backup_storagel1b`
`backup_storagel2`


- Deletar arquivos

`deleteNAVF.py`

- Total size (GB) gerenciamento do armazenamento de dados

`arrumar_tamanho_para_csv.py`
`tamanhol1Nuvem.sh`
`tamanhol2Nuvem.sh`

- Organizar pastas

`organiza_l1.py`
`organiza_l2.py`
`organizar_util.py`

- Tratamento de dias com perda de dados

`aws_para_Nuvem.sh`
`copia_nuvem_to_storage.sh`




<div align="left">
<a href="default.asp">
  <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/linkedin/default.svg" width="52" height="40" alt="linkedin logo"  />
</a>
</div>

###

<h2 align="left">Desevolvido com</h2>

###

<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="40" alt="bash logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="40" alt="linux logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/anaconda/anaconda-original.svg" height="40" alt="anaconda logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original.svg" height="40" alt="amazonwebservices logo"  />
</div>

###

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=guimouraO1&hide_title=false&hide_rank=false&show_icons=true&include_all_commits=true&count_private=true&disable_animations=false&theme=dracula&locale=en&hide_border=false&order=1" height="150" alt="stats graph"  />
  <img src="https://github-readme-stats.vercel.app/api/top-langs?username=guimouraO1&locale=en&hide_title=false&layout=compact&card_width=320&langs_count=5&theme=dracula&hide_border=false&order=2" height="150" alt="languages graph"  />
</div>




# Script de Backup para Nuvem `backup_nuvemflash.sh`

Este é um script em bash projetado para copiar arquivos Flash para um armazenamento em nuvem específico. Ele foi criado para executar backups diários dos arquivos Flash do dia anterior para uma pasta na nuvem GOES-16. Abaixo estão as informações essenciais e instruções para utilizar o script.

## Uso
```
./backup_nuvemflash.sh
```

## Configuração
Antes de executar o script, é necessário configurar algumas variáveis de acordo com suas necessidades:

- `ARQ_LOG`: Nome do arquivo de log gerado pelo script.
- `DIR_LOG`: Diretório onde o arquivo de log será armazenado.
- `origem`: Diretório de origem dos arquivos Flash a serem copiados.
- `destino`: Diretório de destino na nuvem onde os arquivos Flash serão armazenados.

## Funcionamento
1. O script cria um arquivo de log com o nome `bkp_flash-nuvem<DATA_ATUAL>.log` no diretório especificado em `DIR_LOG`.
2. Obtém a data do dia anterior em formato de dois dígitos para o ano, mês e dia.
3. Inicia a cópia dos arquivos Flash do dia anterior usando o comando `rclone copy`.
   - Apenas os arquivos correspondentes à data do dia anterior, no formato `*<ANO><MES><DIA_ANTERIOR>*.GLM--FLASH.txt`, serão copiados.
   - Utiliza a opção `--transfers=50` para definir 50 transferências simultâneas, o que pode ser ajustado de acordo com a capacidade do sistema.
   - O progresso e os detalhes da cópia serão registrados no arquivo de log especificado em `--log-file`.
4. O script registra a conclusão do backup no arquivo de log.

## Exemplo de Saída do Log
```
=========================================================================================================
=========================================================================================================
=                           INICIANDO SCRIPT BACKUP PARA O DRIVE 2023-05-10 12:34:56           =
=========================================================================================================
=========================================================================================================


=========================================================================================================
=========================================================================================================
=                                 FINALIZANDO O SCRIPT 2023-05-10 12:45:23                     =
=========================================================================================================
=========================================================================================================
```

Certifique-se de que o script tenha permissões de execução adequadas antes de executá-lo. Você pode fazer isso usando o comando `chmod +x backup_nuvemflash.sh`. Além disso, verifique se o utilitário `rclone` está instalado no sistema e devidamente configurado para acesso ao destino na nuvem.

**Nota:** Esta documentação presume que você está familiarizado com o uso básico de scripts em bash e o uso do `rclone` para cópia de arquivos para a nuvem.

