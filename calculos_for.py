import classe_teste as ct

alunas = ["Maria", "Ana", "Joana", "Carla", "Paula"]
notas = [7.5, 8.0, 6.0, 9.0, 5.5]

soma = 0
qtd = len(notas)
# Utilizando o for:
# Nota por aluna
for i, nota in enumerate(notas):  # i = índice, nota = valor
    soma += nota
    print(f"A aluna {alunas[i]} tirou {nota}")

# Calculo da média:
media = soma / qtd
print(f"A média da turma é {media}")

# Alunas que ficaram acima/abaixo
for i, nota in enumerate(notas):
    if nota >= media:
        print(f"{alunas[i]} ficou acima ou igual à média")
    else:
        print(f"{alunas[i]} ficou abaixo da média")
