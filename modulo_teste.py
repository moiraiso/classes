def calcular_media(notas):
    soma = sum(notas)          
    qtd = len(notas)           
    media = soma / qtd
    return media

def maior_nota(notas, alunas):
    nota_max = max(notas)               
    indice = notas.index(nota_max)      
    aluna = alunas[indice]               
    return aluna, nota_max
