class Tamagushi:
    humor = 0

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def definirHumor(self):
        self.humor = (self.saude + self.fome)/2

    def redefinirNome(self, novoNome):
        self.nome = novoNome

    def redefinirFome(self, comida):
        self.fome += comida

    def redefinirSaude(self, tempo, diversao):
        self.saude += tempo * diversao

    def redefinirIdade(self, novaIdade):
        self.idade = novaIdade

    def printTamagushi(self):
        print("Nome: {} Idade: {}\nHumor: {}\n  Fome: {}\n Saude: {}".format(self.nome, self.idade, self.humor, self.fome, self.saude))

    def limite(self):
        if(self.fome > 100):
            self.fome = 100
        if(self.saude > 100):
            self.saude = 100

        if(self.fome < 0):
            self.fome = 0
        if(self.saude < 0):
            self.saude = 0


class Comidas:
    def __init__(self, nome, fome, humor):
        self.nome = nome
        self.fome = fome
        self.humor = humor


class Brincadeiras:
    def __init__(self, nome, diversao):
        self.nome = nome
        self.diversao = diversao

