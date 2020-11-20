from Classes import Tamagushi
import Objetos


def acaoComida():
    print("Escolha uma Comida por numeração: ")
    x = 0
    while(x < len(Objetos.listaComida)):
        print(Objetos.listaComida[x].id, ", ", Objetos.listaComida[x].nome)
        x += 1


def acaoBrincar():
    print("Escolha uma Brincadeira por numeração: ")
    x = 0
    while (x < len(Objetos.listaBrincadeira)):
        print(Objetos.listaBrincadeira[x].id, ", ", Objetos.listaBrincadeira[x].nome)
        x += 1


def acaoCuidar():
    print("Escolha uma Medicina por numeração: ")
    x = 0
    while (x < len(Objetos.listaMedicina)):
        print(Objetos.listaMedicina[x].id, ", ", Objetos.listaMedicina[x].nome)
        x += 1

