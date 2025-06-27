lista_numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(lista_numeros)

lista_numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

for i, valor in enumerate(lista_numeros):
    if i == 5:
        print(f"O elemento na posição {i} é: {valor}")
        break
