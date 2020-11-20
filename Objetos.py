from Classes import Comidas
from Classes import Brincadeiras
from Classes import Medicinas

maca = Comidas(1, "Maça", 10, 0, 2, 3)
banana = Comidas(2, "Banana", 15, 0, 3, 3)
hamburguer = Comidas(3, "Hamburguer", 50, -5, 0, 0)

pega = Brincadeiras(1, "Pega-pega", 10)
brinquedos = Brincadeiras(2, "Brinquedos", 20)

capsula = Medicinas(1, "Capsula", 15)
remedios = Medicinas(2, "Remedios", 30)

listaBrincadeira = [pega, brinquedos]
listaComida = [maca, banana, hamburguer]
listaMedicina = [capsula, remedios]