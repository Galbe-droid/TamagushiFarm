class Tamagushi:
    humor = 0
    fome = 100
    saude = 100
    fomeTurno = 15
    saudeTurno = 10

    def __init__(self, nome,idade):
        self.nome = nome
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

    def reduzir(self):
        self.saude -= Tamagushi.saudeTurno
        self.fome -= Tamagushi.fomeTurno

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

        if(Tamagushi.fomeTurno < 0):
            Tamagushi.fomeTurno = 0
        if (Tamagushi.saudeTurno < 0):
            Tamagushi.saudeTurno = 0

    def resetar(self):
        if (Tamagushi.fomeTurno != 15):
            Tamagushi.fomeTurno = 15
        if (Tamagushi.saudeTurno != 15):
            Tamagushi.saudeTurno = 15


class Comidas:
    def __init__(self, id, nome, fome, humor, reduzirFomeTurno, reduzirSaudeTurno):
        self.id = id
        self.nome = nome
        self.fome = fome
        self.humor = humor
        self.reduzirFomeTurno = reduzirFomeTurno
        self.reduzirSaudeTurno = reduzirSaudeTurno


class Brincadeiras:
    def __init__(self, id, nome, diversao):
        self.id = id
        self.nome = nome
        self.diversao = diversao


class Medicinas:
    def __init__(self, id, nome, cura):
        self.id = id
        self.nome = nome
        self.cura = cura
