from Classes import Tamagushi
import Metodos

print("Bem vindo a criação de seu Tamagushi")
nome = input("Qual o nome dele: ")
idade = input("E sua idade: ")

t = Tamagushi(nome, idade)

t.printTamagushi()
print()
print("Ações.\n1 - Comida\n2 - Brincadeiras\n3 - Medicamentos")
escolha = int(input("Escolha: "))

while(escolha != 1 or escolha != 2 or escolha != 3):
    escolha = int(input("Escolha: "))

if(escolha == 1):
    Metodos.acaoBrincar()
elif(escolha == 2):
    Metodos.acaoComida()
elif(escolha == 3):
    Metodos.acaoCuidar()

