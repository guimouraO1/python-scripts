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



<br><br><br>
# Backups
<br><br><br>

## Script de Backup para Nuvem `backup_nuvemflash.sh`

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


<br>
<br>
<br>


## Script de Backup para Nuvem `backup_nuveml1b.sh`

Este é um script em bash projetado para copiar arquivos para uma pasta em nuvem específica. Ele foi criado para executar backups diários dos arquivos do dia anterior para uma pasta na nuvem GOES-16.

## Uso
```bash
bash backup_nuveml1b.sh
```

## Configuração
Antes de executar o script, é necessário configurar algumas variáveis de acordo com suas necessidades:

- `ARQ_LOG`: Nome do arquivo de log gerado pelo script.
- `DIR_LOG`: Diretório onde o arquivo de log será armazenado.
- `origem`: Diretório de origem dos arquivos a serem copiados.
- `destino`: Diretório de destino na nuvem onde os arquivos serão armazenados.

## Funcionamento
1. O script cria um arquivo de log com o nome `bkp_level1b-nuvem<DATA_ATUAL>.log` no diretório especificado em `DIR_LOG`.
2. Obtém o ano e o dia anterior em formato de dia juliano.
3. Inicia a cópia dos arquivos do dia anterior usando o comando `rclone copy`.
   - Apenas os arquivos correspondentes ao padrão definido em `padrao` serão copiados. O padrão procura por arquivos contendo `L1b` ou `GLM-L2-LCFA` no nome e que correspondam ao ano e dia juliano do dia anterior.
   - Utiliza a opção `--transfers=100` para definir 100 transferências simultâneas, o que pode ser ajustado de acordo com a capacidade do sistema.
   - O progresso e os detalhes da cópia serão registrados no arquivo de log especificado em `--log-file`.

## Exemplo de Saída do Log
```
=========================================================================================================
=========================================================================================================
=                                 INICIANDO SCRIPT BACKUP PARA O DRIVE LEVEL1                           =
=========================================================================================================
=========================================================================================================


=========================================================================================================
=========================================================================================================
=                                 FINALIZANDO O SCRIPT 2023-05-18 12:34:56                     =
=========================================================================================================
=========================================================================================================
```

Certifique-se de que o script tenha permissões de execução adequadas antes de executá-lo. Você pode fazer isso usando o comando `chmod +x backup_nuveml1b.sh`. Além disso, verifique se o utilitário `rclone` está instalado no sistema e devidamente configurado para acesso ao destino na nuvem.

**Nota:** Esta documentação presume que você está familiarizado com o uso básico de scripts em bash e o uso do `rclone` para cópia de arquivos para a nuvem.


<br>
<br>
<br>


# Script de Backup para Nuvem `backup_nuveml2.sh`

Este é um script em bash projetado para copiar arquivos para uma pasta em nuvem específica. Ele foi criado para executar backups diários dos arquivos do dia anterior para uma pasta na nuvem GOES-16.

## Uso
```bash
bash backup_nuveml2.sh
```

## Configuração
Antes de executar o script, é necessário configurar algumas variáveis de acordo com suas necessidades:

- `ARQ_LOG`: Nome do arquivo de log gerado pelo script.
- `DIR_LOG`: Diretório onde o arquivo de log será armazenado.
- `origem`: Diretório de origem dos arquivos a serem copiados.
- `destino`: Diretório de destino na nuvem onde os arquivos serão armazenados.

## Funcionamento
1. O script cria um arquivo de log com o nome `bkp_level2-nuvem<DATA_ATUAL>.log` no diretório especificado em `DIR_LOG`.
2. Obtém o ano e o dia anterior em formato de dia juliano.
3. Inicia a cópia dos arquivos do dia anterior usando o comando `rclone copy`.
   - Apenas os arquivos correspondentes ao padrão definido em `padrao` serão copiados. O padrão procura por arquivos contendo `CMIPF` no nome e que correspondam ao ano e dia juliano do dia anterior.
   - Utiliza a opção `--transfers=100` para definir 100 transferências simultâneas, o que pode ser ajustado de acordo com a capacidade do sistema.
   - O progresso e os detalhes da cópia serão registrados no arquivo de log especificado em `--log-file`.

## Exemplo de Saída do Log
```
=========================================================================================================
=========================================================================================================
=                                 INICIANDO SCRIPT BACKUP PARA O DRIVE LEVEL2                           =
=========================================================================================================
=========================================================================================================


=========================================================================================================
=========================================================================================================
=                                 FINALIZANDO O SCRIPT 2023-06-22 12:34:56                     =
=========================================================================================================
=========================================================================================================
```

Certifique-se de que o script tenha permissões de execução adequadas antes de executá-lo. Você pode fazer isso usando o comando `chmod +x backup_nuveml2.sh`. Além disso, verifique se o utilitário `rclone` está instalado no sistema e devidamente configurado para acesso ao destino na nuvem.

**Nota:** Esta documentação presume que você está familiarizado com o uso básico de scripts em bash e o uso do `rclone` para cópia de arquivos para a nuvem.

<br>
<br>
<br>

## Script de Backup para Storage `backup_storageflash.sh`

Este é um script em bash projetado para copiar arquivos Flash para um storage específico. Ele foi criado para executar backups diários dos arquivos Flash do dia anterior para uma pasta no storage GOES-16.

## Uso
```bash
bash backup_storageflash.sh
```

## Configuração
Antes de executar o script, é necessário configurar algumas variáveis de acordo com suas necessidades:

- `ARQ_LOG`: Nome do arquivo de log gerado pelo script.
- `DIR_LOG`: Diretório onde o arquivo de log será armazenado.
- `origem`: Diretório de origem dos arquivos Flash a serem copiados.
- `destino`: Diretório de destino no storage onde os arquivos Flash serão armazenados.

## Funcionamento
1. O script cria um arquivo de log com o nome `okul-moveTo-Bellatrix-storage<DATA_ATUAL>.log` no diretório especificado em `DIR_LOG`.
2. Obtém a data do dia anterior em formato de dois dígitos para o ano, mês e dia.
3. Inicia a movimentação dos arquivos Flash do dia anterior usando o comando `rclone move`.
   - Apenas os arquivos correspondentes à data do dia anterior, no formato `*<ANO><MES><DIA_ANTERIOR>*.GLM--FLASH.txt`, serão movidos.
   - Utiliza a opção `--transfers=50` para definir 50 transferências simultâneas, o que pode ser ajustado de acordo com a capacidade do sistema.
   - O progresso e os detalhes da movimentação serão registrados no arquivo de log especificado em `--log-file`.
4. O script registra a conclusão da movimentação no arquivo de log.

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

Certifique-se de que o script tenha permissões de execução adequadas antes de executá-lo. Você pode fazer isso usando o comando `chmod +x backup_storageflash.sh`. Além disso, verifique se o utilitário `rclone` está instalado no sistema e devidamente configurado para acesso ao storage.

**Nota:** Esta documentação presume que você está familiarizado com o uso básico de scripts em bash e o uso do `rclone` para movimentação de arquivos para o storage.


<br>
<br>
<br>

## Script de Backup para Storage `backup_storagel1b.sh`

Este é um script em bash projetado para mover arquivos para uma pasta em um storage específico. Ele foi criado para executar movimentações diárias dos arquivos do dia anterior para uma pasta no storage GOES-16.

## Uso
```bash
bash backup_storagel1b.sh
```

## Configuração
Antes de executar o script, é necessário configurar algumas variáveis de acordo com suas necessidades:

- `ARQ_LOG`: Nome do arquivo de log gerado pelo script.
- `DIR_LOG`: Diretório onde o arquivo de log será armazenado.
- `origem`: Diretório de origem dos arquivos a serem movidos.
- `destino`: Diretório de destino no storage onde os arquivos serão armazenados.

## Funcionamento
1. O script cria um arquivo de log com o nome `okul-CopyTo-Bellatrix-storage<DATA_ATUAL>.log` no diretório especificado em `DIR_LOG`.
2. Obtém o ano e o dia anterior em formato de dia juliano.
3. Inicia a movimentação dos arquivos do dia anterior usando o comando `rclone move`.
   - Apenas os arquivos correspondentes ao padrão definido em `padrao` serão movidos. O padrão procura por arquivos contendo `L1b` ou `GLM-L2-LCFA` no nome e que correspondam ao ano e dia juliano do dia anterior.
   - Utiliza a opção `--transfers=10` para definir 10 transferências simultâneas, o que pode ser ajustado de acordo com a capacidade do sistema.
   - O progresso e os detalhes da movimentação serão registrados no arquivo de log especificado em `--log-file`.

## Exemplo de Saída do Log
```
=========================================================================================================
=========================================================================================================
=                                 INICIANDO SCRIPT BACKUP PARA O DRIVE LEVEL1                           =
=========================================================================================================
=========================================================================================================


=========================================================================================================
=========================================================================================================
=                                 FINALIZANDO O SCRIPT 2023-05-18 12:34:56                     =
=========================================================================================================
=========================================================================================================
```

Certifique-se de que o script tenha permissões de execução adequadas antes de executá-lo. Você pode fazer isso usando o comando `chmod +x backup_storagel1b.sh`. Além disso, verifique se o utilitário `rclone` está instalado no sistema e devidamente configurado para acesso ao storage.

**Nota:** Esta documentação presume que você está familiarizado com o uso básico de scripts em bash e o uso do `rclone` para movimentação de arquivos para o storage.


<br>
<br>
<br>

## Script de Backup para Storage `backup_storagelevel2.sh`

Este é um script em bash projetado para mover arquivos para uma pasta em um storage específico. Ele foi criado para executar movimentações diárias dos arquivos do dia anterior para uma pasta no storage GOES-16.

## Uso
```bash
bash backup_storagelevel2.sh
```

## Configuração
Antes de executar o script, é necessário configurar algumas variáveis de acordo com suas necessidades:

- `ARQ_LOG`: Nome do arquivo de log gerado pelo script.
- `DIR_LOG`: Diretório onde o arquivo de log será armazenado.
- `origem`: Diretório de origem dos arquivos a serem movidos.
- `destino`: Diretório de destino no storage onde os arquivos serão armazenados.

## Funcionamento
1. O script cria um arquivo de log com o nome `okul-CopyTo-Bellatrix-storage<DATA_ATUAL>.log` no diretório especificado em `DIR_LOG`.
2. Obtém o ano e o dia anterior em formato de dia juliano.
3. Inicia a movimentação dos arquivos do dia anterior usando o comando `rclone move`.
   - Apenas os arquivos correspondentes ao padrão definido em `padrao` serão movidos. O padrão procura por arquivos contendo `CMIPF` no nome e que correspondam ao ano e dia juliano do dia anterior.
   - Utiliza a opção `--transfers=50` para definir 50 transferências simultâneas, o que pode ser ajustado de acordo com a capacidade do sistema.
   - O progresso e os detalhes da movimentação serão registrados no arquivo de log especificado em `--log-file`.

## Exemplo de Saída do Log
```
=========================================================================================================
=========================================================================================================
=                                 INICIANDO SCRIPT BACKUP PARA O DRIVE LEVEL1                           =
=========================================================================================================
=========================================================================================================


=========================================================================================================
=========================================================================================================
=                                 FINALIZANDO O SCRIPT 2023-05-18 12:34:56                     =
=========================================================================================================
=========================================================================================================
```

Certifique-se de que o script tenha permissões de execução adequadas antes de executá-lo. Você pode fazer isso usando o comando `chmod +x backup_storagelevel2.sh`. Além disso, verifique se o utilitário `rclone` está instalado no sistema e devidamente configurado para acesso ao storage.

**Nota:** Esta documentação presume que você está familiarizado com o uso básico de scripts em bash e o uso do `rclone` para movimentação de arquivos para o storage.


<br><br><br>
# Deletar arquivos
<br><br><br>

## Script de Exclusão de Arquivos NAVF `deleteNAVF.py`

Este é um script em Python projetado para excluir arquivos NAVF da pasta okul - level2. Ele foi criado para executar uma exclusão diária dos arquivos NAVF do dia anterior.

## Uso
Certifique-se de ter o Python 3 instalado no seu sistema.

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde o script `deleteNAVF.py` está localizado.
3. Execute o seguinte comando:
```bash
python3 deleteNAVF.py
```

## Configuração
Antes de executar o script, você pode ajustar algumas configurações:

- `arq_log`: Caminho e nome do arquivo de log gerado pelo script.
- `origem`: Diretório de origem dos arquivos NAVF a serem excluídos.

## Funcionamento
1. O script configura o log de acordo com o arquivo especificado em `arq_log`.
2. Registra o início da exclusão dos arquivos NAVF no log.
3. Define o diretório de origem dos arquivos NAVF.
4. Obtém o ano atual e o dia anterior em formato juliano.
5. Define o padrão a ser procurado nos arquivos NAVF usando o ano e o dia anterior.
6. Executa o comando `rclone delete` para excluir os arquivos que correspondam ao padrão definido em `padrao`.
   - O progresso e os detalhes da exclusão são registrados no arquivo de log especificado em `--log-file`.
7. Registra a conclusão da exclusão dos arquivos NAVF no log.

## Exemplo de Saída do Log
```
==================================================================================================================
                                    Iniciando exclusão dos arquivos NAVF                                          
==================================================================================================================

Os arquivos do dia 193 com padrão *NAVF*2023193*, foram deletados com sucesso!

==================================================================================================================
                                           Finalizando os script                                                  
==================================================================================================================
```

Certifique-se de que o script tenha permissões de execução adequadas antes de executá-lo. Você pode fazer isso usando o comando `chmod +x deleteNAVF.py`. Além disso, verifique se o utilitário `rclone` está instalado no sistema e devidamente configurado para acessar o diretório de origem dos arquivos NAVF.

**Nota:** Esta documentação presume que você está familiarizado com o uso básico de scripts Python e o uso do `rclone` para exclusão de arquivos.

<br><br><br>
# Total size (GB) gerenciamento do armazenamento de dados
<br><br><br>




