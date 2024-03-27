# Função para ler as variáveis do arquivo
def ler_variaveis(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        nome_maquina = linhas[0].strip()
        tempo_uso = int(linhas[1].strip())
        ligado = linhas[2].strip() == 'True'
    return nome_maquina, tempo_uso, ligado

# Função para exibir os valores e seus tipos
def exibir_valores_e_tipos(nome_maquina, tempo_uso, ligado):
    print("Valores lidos do arquivo:")
    print("Nome da máquina:", nome_maquina, "- Tipo:", type(nome_maquina))
    print("Tempo de uso:", tempo_uso, "- Tipo:", type(tempo_uso))
    print("Ligado:", ligado, "- Tipo:", type(ligado))

# Nome do arquivo contendo as variáveis
nome_arquivo = "variaveis.txt"

# Chamada das funções
nome_maquina, tempo_uso, ligado = ler_variaveis(nome_arquivo)
exibir_valores_e_tipos(nome_maquina, tempo_uso, ligado)

