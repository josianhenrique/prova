def main():
    # Solicita ao usuário que insira um número de 1 a 12
    numero = int(input("Digite um número de 1 a 12: "))

    # Usa match case para determinar o mês correspondente
    mes = match numero:
        case 1:
            "Janeiro"
        case 2:
            "Fevereiro"
        case 3:
            "Março"
        case 4:
            "Abril"
        case 5:
            "Maio"
        case 6:
            "Junho"
        case 7:
            "Julho"
        case 8:
            "Agosto"
        case 9:
            "Setembro"
        case 10:
            "Outubro"
        case 11:
            "Novembro"
        case 12:
            "Dezembro"
        case _:
            "Número inválido"

    # Imprime o mês correspondente
    print("Mês correspondente:", mes)

# Chamada da função principal
if __name__ == "__main__":
    main()
