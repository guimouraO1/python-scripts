<br><br>
<h1 align="Center">Documentação scripts</h1>

<br><br>
<br><br>

Documentação dos scripts criados no Centro de Pesquisas Meteorológicas e Climáticas Aplicadas à Agricultura - CEPAGRI/UNICAMP - Universidade Estadual de Campinas.

Autor `Guilherme de Moura Oliveira`
<div align="left">
<a href="https://www.linkedin.com/in/guilherme-moura-oliveira/">
  <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/linkedin/default.svg" width="52" height="40" alt="linkedin logo"  />
</a>
</div>

<br><br>

## SCRIPTS

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

- Tratamento para dias com perda de dados

`aws_para_Nuvem.sh`
`copia_nuvem_to_storage.sh`





###

<h2 align="center">Desenvolvido com:</h2>

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


<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=guimouraO1&hide_title=false&hide_rank=false&show_icons=true&include_all_commits=true&count_private=true&disable_animations=false&theme=dracula&locale=en&hide_border=false&order=1" height="150" alt="stats graph"  />
  <img src="https://github-readme-stats.vercel.app/api/top-langs?username=guimouraO1&locale=en&hide_title=false&layout=compact&card_width=320&langs_count=5&theme=dracula&hide_border=false&order=2" height="150" alt="languages graph"  />
</div>



<br><br>
# Backups
<br><br>
<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="40" alt="bash logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="40" alt="googlecloud logo"  />
</div>

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

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="40" alt="bash logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="40" alt="googlecloud logo"  />
</div>

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

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="40" alt="bash logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="40" alt="googlecloud logo"  />
</div>

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

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="40" alt="bash logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="40" alt="linux logo"  />
</div>

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

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="40" alt="bash logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="40" alt="linux logo"  />
</div>

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

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="40" alt="bash logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="40" alt="linux logo"  />
</div>

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
<br><br>

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
</div>

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
<br><br>

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
</div>

## Script para Arrumar Planilha de Dados `arrumar_tamanho_para_csv.py`

Este é um script em Python projetado para arrumar os dados de um arquivo de entrada no formato TXT e salvá-los em um arquivo CSV. Ele foi criado para processar e organizar informações específicas de um arquivo de entrada e gravar esses dados em um arquivo CSV.

## Uso
Certifique-se de ter o Python 3 instalado no seu sistema.

1. Crie um arquivo de entrada no formato TXT contendo as informações desejadas.
2. Abra o arquivo `arrumar_tamanho_para_csv.py` em um editor de texto.
3. No código, atualize o valor da variável `arquivo_entrada` para o nome do seu arquivo de entrada (sem a extensão).
4. Salve o arquivo `arrumar_tamanho_para_csv.py`.
5. Abra um terminal ou prompt de comando.
6. Navegue até o diretório onde o script `arrumar_tamanho_para_csv.py` está localizado.
7. Execute o seguinte comando:
```bash
python3 arrumar_tamanho_para_csv.py
```
8. Verifique se um arquivo CSV chamado `saida.csv` foi criado no mesmo diretório.

## Funcionamento
1. O script define duas funções: `escrever_arquivo` e `ler_arquivo`.
2. A função `escrever_arquivo` recebe o nome do arquivo CSV, o dia, o número total de objetos e o tamanho total como parâmetros.
   - Ela abre o arquivo CSV em modo de anexação (`'a'`) e escreve os dados formatados no arquivo.
3. A função `ler_arquivo` recebe o nome do arquivo de entrada como parâmetro.
   - O nome do arquivo de saída é definido como "saida".
   - O arquivo de entrada é aberto para leitura (`'r'`) e as linhas são armazenadas na variável `linhas`.
   - Cada linha é verificada para determinar qual informação está contida nela.
     - Se a linha começar com "rclone size /mnt/storage/level1b/ano2023/", o dia é extraído da linha.
     - Se a linha começar com "Total objects:", o número total de objetos é extraído.
     - Se a linha começar com "Total size:", o tamanho total é extraído.
   - Os dados extraídos são formatados e passados para a função `escrever_arquivo` para serem gravados no arquivo CSV de saída.
   - Se ocorrer um erro ao gravar os dados, uma mensagem de erro é exibida.
4. A variável `arquivo_entrada` é definida com o nome do arquivo de entrada.
5. A função `ler_arquivo` é chamada com o arquivo de entrada como argumento.

## Exemplo de Saída (saida.csv)
```
dia,total_objects,total_size
001,100,10
002,150,15
003,200,20
...
```

Certifique-se de ter o arquivo de entrada no formato correto e de que os dados esperados estejam presentes nas linhas correspondentes.

<br>
<br>

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="40" alt="bash logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="40" alt="googlecloud logo"  />
</div>

## Script para Verificar Tamanho de Pastas `tamanhol1Nuvem.sh`

Este é um script em bash projetado para verificar o tamanho em GB das pastas l1b e l2 no storage ou na nuvem. Ele foi criado para ser executado anualmente e registrar as informações de tamanho em um arquivo de log.

## Uso
```bash
bash tamanhol1Nuvem.sh
```

## Configuração
Antes de executar o script, você precisa ajustar algumas configurações:

- `log_file`: Caminho e nome do arquivo de log onde as informações de tamanho serão registradas.
- `origem`: Diretório de origem das pastas l1b ou l2. Você pode escolher entre o storage ou a nuvem, descomentando a linha correspondente.

## Funcionamento
1. O script configura o arquivo de log especificado em `log_file`.
2. Define o diretório de origem das pastas l1b ou l2 de acordo com a configuração em `origem`.
3. Para cada dia de 1 a 193, o script executa o comando `rclone size` para verificar o tamanho da pasta correspondente ao dia atual.
   - O resultado é redirecionado para o arquivo de log especificado.
4. No final do script, há um trecho de código comentado que pode ser usado para verificar o tamanho total da pasta. Descomente essas linhas apenas quando a pasta estiver totalmente preenchida, pois pode demorar para processar.
   - O resultado é redirecionado para o arquivo de log especificado.

## Exemplo de Saída do Log
```
------------------------------------------
------------DIA001--------------
------------------------------------------
rclone size /mnt/storage/level1b/ano2023/dia001
Total objects: 100
Total size: 10 GiB (10737418240 Bytes)

------------------------------------------
------------DIA002--------------
------------------------------------------
rclone size /mnt/storage/level1b/ano2023/dia002
Total objects: 150
Total size: 15 GiB (16106127360 Bytes)

...

```

Certifique-se de que o script tenha permissões de execução adequadas antes de executá-lo. Você pode fazer isso usando o comando `chmod +x tamanhol1Nuvem.sh`. Além disso, verifique se o utilitário `rclone` está instalado no sistema e devidamente configurado para acessar o diretório de origem das pastas l1b ou l2.

**Nota:** Este script presume que você esteja familiarizado com o uso básico de scripts bash e o utilitário `rclone`.


<br>
<br>

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="40" alt="bash logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="40" alt="googlecloud logo"  />
</div>

## Script para Verificar Tamanho de Pastas `tamanhol2Nuvem.sh`

Este é um script em bash projetado para verificar o tamanho em GB das pastas l1b e l2 no storage ou na nuvem. Ele foi criado para ser executado anualmente e registrar as informações de tamanho em um arquivo de log.

## Uso
```bash
bash tamanhol2Nuvem.sh
```

## Configuração
Antes de executar o script, você precisa ajustar algumas configurações:

- `log_file`: Caminho e nome do arquivo de log onde as informações de tamanho serão registradas.
- `origem`: Diretório de origem das pastas l1b ou l2. Você pode escolher entre o storage ou a nuvem, descomentando a linha correspondente.

## Funcionamento
1. O script configura o arquivo de log especificado em `log_file`.
2. Define o diretório de origem das pastas l1b ou l2 de acordo com a configuração em `origem`.
3. Para cada dia de 1 a 180, o script executa o comando `rclone size` para verificar o tamanho da pasta correspondente ao dia atual.
   - O resultado é redirecionado para o arquivo de log especificado.
4. No final do script, há um trecho de código comentado que pode ser usado para verificar o tamanho total da pasta. Descomente essas linhas apenas quando a pasta estiver totalmente preenchida, pois pode demorar para processar.
   - O resultado é redirecionado para o arquivo de log especificado.

## Exemplo de Saída do Log
```
------------------------------------------
------------DIA001--------------
------------------------------------------
rclone size /mnt/storage/level2/ano2023/dia001
Total objects: 100
Total size: 10 GiB (10737418240 Bytes)

------------------------------------------
------------DIA002--------------
------------------------------------------
rclone size /mnt/storage/level2/ano2023/dia002
Total objects: 150
Total size: 15 GiB (16106127360 Bytes)

...

```

Certifique-se de que o script tenha permissões de execução adequadas antes de executá-lo. Você pode fazer isso usando o comando `chmod +x tamanhol2Nuvem.sh`. Além disso, verifique se o utilitário `rclone` está instalado no sistema e devidamente configurado para acessar o diretório de origem das pastas l1b ou l2.

**Nota:** Este script presume que você esteja familiarizado com o uso básico de scripts bash e o utilitário `rclone`.

<br>
<br>


<br><br><br>
# Organizar pastas
<br><br>


<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
</div>

## Script para Organização de Arquivos no Storage `organiza_l1.py`

Este é um script em Python projetado para organizar os arquivos do GOES-R no storage. Ele cria pastas separadas para cada dia com base nos dados contidos nos nomes dos arquivos. Os arquivos são movidos para suas respectivas pastas de acordo com o dia.

## Uso
```python
python3 organiza_l1.py
```

## Configuração
Antes de executar o script, você precisa ajustar algumas configurações:

- `arq_log`: Caminho e nome do arquivo de log onde as informações serão registradas.

## Dependências
Certifique-se de que você tenha o Python 3 instalado no seu sistema. Além disso, verifique se você possui o pacote `pathlib` e o módulo `shutil` incluídos na sua instalação do Python.

## Funcionamento
1. O script importa funções do módulo `organizar_util`.
2. Configura o arquivo de log especificado em `arq_log`.
3. Inicia o log.
4. Define o ano dos arquivos a serem organizados.
5. Define o diretório de origem dos arquivos.
6. Obtém uma lista de todos os arquivos no diretório de origem.
7. Obtém a quantidade de arquivos na lista.
8. Move os arquivos para as pastas correspondentes com base nos dias.
9. Finaliza o log.

O script utiliza funções auxiliares do módulo `organizar_util.py` para realizar as etapas de organização. Certifique-se de que o arquivo `organizar_util.py` esteja no mesmo diretório que o script `organiza_l1.py` para que as funções sejam corretamente importadas.

Certifique-se de que o script e o arquivo de log tenham permissões de gravação adequadas antes de executá-los.

<br>
<br>

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
</div>

## Script para Organização de Arquivos no Storage `organiza_l2.py`

Este é um script em Python projetado para organizar os arquivos do GOES-R no storage. Ele cria pastas separadas para cada dia com base nos dados contidos nos nomes dos arquivos. Os arquivos são movidos para suas respectivas pastas de acordo com o dia.

## Uso
```python
python3 organiza_l2.py
```

## Configuração
Antes de executar o script, você precisa ajustar algumas configurações:

- `arq_log`: Caminho e nome do arquivo de log onde as informações serão registradas.

## Dependências
Certifique-se de que você tenha o Python 3 instalado no seu sistema. Além disso, verifique se você possui o pacote `pathlib` e o módulo `shutil` incluídos na sua instalação do Python.

## Funcionamento
1. O script importa funções do módulo `organizar_util`.
2. Configura o arquivo de log especificado em `arq_log`.
3. Inicia o log.
4. Define o ano dos arquivos a serem organizados.
5. Define o diretório de origem dos arquivos.
6. Obtém uma lista de todos os arquivos no diretório de origem.
7. Obtém a quantidade de arquivos na lista.
8. Move os arquivos para as pastas correspondentes com base nos dias.
9. Finaliza o log.

O script utiliza funções auxiliares do módulo `organizar_util.py` para realizar as etapas de organização. Certifique-se de que o arquivo `organizar_util.py` esteja no mesmo diretório que o script `organiza_l2.py` para que as funções sejam corretamente importadas.

Certifique-se de que o script e o arquivo de log tenham permissões de gravação adequadas antes de executá-los.

<br>
<br>

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
</div>

## Script para Organização de Arquivos `organizar_util.py`

Este script em Python contém um conjunto de funções para organizar arquivos em diretórios com base em determinados critérios.

### Funções

- `config_log(arq_log)`: Configura o log para o registro de informações e erros durante a execução do script.
- `logging_inicio()`: Registra o início da execução do script no arquivo de log.
- `logging_fim()`: Registra o fim da execução do script no arquivo de log.
- `convert_to_julian_day(day)`: Converte um número inteiro em uma string de três dígitos representando o dia juliano.
- `verifica_destino(destino)`: Verifica se a pasta de destino existe e, se não existir, cria-a.
- `obtem_lista_arquivos(origem)`: Obtém uma lista de arquivos apenas no diretório especificado, ordena-os e retorna a lista e a quantidade de arquivos.
- `movendo_arquivos(origem, quantidade_arquivos, lista_arquivos, ano)`: Move os arquivos da lista fornecida para suas respectivas pastas de destino, com base no ano.

### Uso

```python
from organizar_util import *
```

### Configuração do Log

Antes de utilizar as funções do script, é necessário configurar o arquivo de log. Utilize a função `config_log(arq_log)` para definir o caminho e o nome do arquivo de log onde as informações serão registradas.

Exemplo de configuração do log:

```python
config_log('arquivo_log.txt')
```

### Exemplo de Uso

Aqui está um exemplo de como utilizar as funções do script:

```python
# Configurar o log
config_log('arquivo_log.txt')

# Registrar o início da execução
logging_inicio()

# Definir o ano dos arquivos
ano = '2023'

# Definir o diretório de origem
origem = '/caminho/do/diretorio/origem'

# Obter a lista de arquivos
lista_arquivos, quantidade_arquivos = obtem_lista_arquivos(origem)

# Mover os arquivos para as pastas de destino
arquivos_transferidos = movendo_arquivos(origem, quantidade_arquivos, lista_arquivos, ano)

# Registrar o fim da execução
logging_fim()
```

### Dependências

Certifique-se de que você tenha o Python 3 instalado no seu sistema. Além disso, verifique se possui os seguintes pacotes/módulos:

- `pathlib`: Utilizado para lidar com caminhos de arquivos e diretórios.
- `shutil`: Utilizado para realizar operações de movimentação/cópia de arquivos.

Certifique-se de ter as dependências instaladas antes de executar o script.


<br>
<br>


<br><br><br>
# Tratamento para dias com perda de dados
<br><br>

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="40" alt="bash logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="40" alt="googlecloud logo"  />
</div>

## Script para Repor Dias Perdidos na Nuvem `aws_para_Numem.sh`

Este é um script em Bash que utiliza o rclone para copiar arquivos da AWS para a nuvem (level2). Ele é projetado para repor dias perdidos, copiando os arquivos correspondentes de um determinado intervalo de dias.

## Uso
```bash
bash aws_para_Numem.sh
```

## Configuração
Antes de executar o script, você precisa ajustar algumas configurações:

- `src`: Caminho de origem dos arquivos na AWS.
- `dest`: Caminho de destino dos arquivos na nuvem (level2).
- `log_dir`: Diretório onde os logs de execução serão armazenados.

Além disso, você precisa definir o intervalo de dias que deseja repor. No exemplo do script, está definido para o intervalo de 126 a 127 dias. Você pode modificar o valor das variáveis `day` no loop para especificar seu intervalo desejado.

Certifique-se de que o rclone esteja corretamente configurado e autenticado para acessar a AWS e a nuvem (level2) antes de executar o script.

## Funcionamento
1. Define as variáveis `src`, `dest` e `log_dir` com os caminhos apropriados.
2. Inicia um loop para cada dia no intervalo especificado.
3. Formata o número do dia para um formato de três dígitos (juliano).
4. Define o caminho de destino para o dia atual.
5. Executa o comando `rclone` para copiar os arquivos correspondentes do dia atual da AWS para a nuvem.
6. Registra os logs de execução em um arquivo de log específico para o dia.
7. Exibe uma mensagem de conclusão para cada dia processado.

Certifique-se de que o script tenha permissões de execução adequadas antes de executá-lo.


<br>
<br>

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="40" alt="bash logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="40" alt="googlecloud logo"  />
</div>

## Script para Copiar da Nuvem para a Storage `copia_nuvem_to_storage.sh`

Este é um script em Bash que utiliza o rclone para copiar arquivos da nuvem (level2) para a storage. Ele é projetado para copiar arquivos de um intervalo de dias julianos específico.

## Uso
```bash
bash copia_nuvem_to_storage.sh
```

## Configuração
Antes de executar o script, você precisa ajustar algumas configurações:

- `ARQ_LOG`: Nome do arquivo de log que será gerado com informações sobre a execução do script.
- `DIR_LOG`: Diretório onde o arquivo de log será armazenado.
- `ano`: Ano para o qual deseja copiar os arquivos.
- `dia`: Intervalo de dias julianos que você deseja copiar. No exemplo do script, está definido para o intervalo de 48 a 53 dias. Você pode modificar o valor das variáveis `dia` no loop para especificar seu intervalo desejado.

Certifique-se de que o rclone esteja corretamente configurado e autenticado para acessar a nuvem (level2) e a storage antes de executar o script.

## Funcionamento
1. Define as variáveis `ARQ_LOG`, `DIR_LOG`, `ano`, `dia` com os valores apropriados.
2. Inicia um loop para cada dia no intervalo especificado.
3. Formata o número do dia juliano para um formato de três dígitos.
4. Define o diretório de origem na nuvem.
5. Define o diretório de destino na storage.
6. Executa o comando `rclone` para copiar os arquivos do diretório de origem para o diretório de destino.
7. Registra os logs de execução no arquivo de log específico para a data atual.
8. Repete o processo para cada dia no intervalo especificado.

Certifique-se de que o script tenha permissões de execução adequadas antes de executá-lo.
