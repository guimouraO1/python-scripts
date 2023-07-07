
# função que transforma bytes em gigabites %f.2
def gerar_gigabytes_arquivo(nome_arquivo_bytes, nome_arquivo_giga):
    # Abri o arquivo de bytes para leitura
    with open(nome_arquivo_bytes, "r") as arquivo_bytes:
        # Lê as linhas do arquivo
        linhas = arquivo_bytes.readlines()

    # Gera os gigabytes correspondentes de cada linha do arquivo
    for linha in linhas:
        # Remove os espaços em branco e converte para inteiro
        bytes = int(linha.strip()) 
        kilobytes = bytes / 1024
        megabytes = kilobytes / 1024
        gigabytes = megabytes / 1024
        
        # Arredonda o valor para duas casas decimais
        gigabytes_formatado = round(gigabytes, 3)

        # Escreve o resultado no arquivo gigabytes
        with open(nome_arquivo_giga, "a") as arquivo_giga:
            arquivo_giga.write(str(gigabytes_formatado) + "\n")

# Chamar a função para processar o arquivo
gerar_gigabytes_arquivo("bytes.txt", "gigabytes.txt")