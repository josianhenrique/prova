class Carro:
    def __init__(self, nome, marca):
        self.__nome = nome
        self.__marca = marca

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

# Criando uma instância da classe Carro
carro1 = Carro("Fusca", "Volkswagen")

# Imprimindo os atributos usando os métodos get
print("Nome:", carro1.get_nome())
print("Marca:", carro1.get_marca())

# Modificando o nome e a marca usando os métodos set
carro1.set_nome("Gol")
carro1.set_marca("Volkswagen")

# Imprimindo os atributos modificados
print("Nome modificado:", carro1.get_nome())
print("Marca modificada:", carro1.get_marca())
