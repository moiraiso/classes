import modulo_teste as mt

alunas = ["Maria", "Ana", "Joana", "Carla", "Paula"]
notas = [7.5, 8.0, 6.0, 9.0, 5.5]

# Utilizando a classe:
# Calculando a média:
resultado = mt.calcular_media(notas)
print(f"A média da turma é {resultado}")
# Aluna com a maior nota:
aluna, nota_maxima = cm.maior_nota(notas,alunas)
print(f"A maior nota foi {nota_maxima}, da aluna {aluna}")
