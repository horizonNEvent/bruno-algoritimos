def pesquisa_binaria(lista, alvo):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2  # Calcula o índice do meio
        chute = lista[meio]

        if chute == alvo:
            return meio  # Retorna o índice onde o alvo foi encontrado
        if chute < alvo:
            baixo = meio + 1  # Ajusta o limite inferior para procurar na metade superior
        else:
            alto = meio - 1  # Ajusta o limite superior para procurar na metade inferior

    return None  # Retorna None se o alvo não for encontrado

# Exemplo de uso:
lista_numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
alvo = 13

resultado = pesquisa_binaria(lista_numeros, alvo)

if resultado is not None:
    print(f"Elemento encontrado no índice {resultado}")
else:
    print("Elemento não encontrado")
