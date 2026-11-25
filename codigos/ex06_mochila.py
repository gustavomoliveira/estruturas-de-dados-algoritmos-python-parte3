def knapsack(target, weights, index):
    if target == 0:
        return [[]]

    if target < 0 or index >= len(weights):
        return []

    resultado = []

    for combinacao in knapsack(target - weights[index], weights, index + 1):
        resultado.append([weights[index]] + combinacao)

    for combinacao in knapsack(target, weights, index + 1):
        resultado.append(combinacao)

    return resultado


print('=== Exercício 6 – Problema da mochila (knapsack recursivo) ===')
print()

casos = [
    ('vários resultados', 10, [1, 2, 3, 4, 5, 6]),
    ('poucos resultados', 9, [2, 3, 4, 5, 8]),
    ('alvo igual a um peso', 7, [3, 7, 4, 1]),
    ('sem solução', 20, [3, 5, 7]),
    ('pesos repetidos', 4, [1, 1, 2, 2]),
    ('lista vazia', 5, []),
    ('alvo zero', 0, [1, 2, 3]),
]

for nome, alvo, pesos in casos:
    resultado = knapsack(alvo, pesos, 0)
    todas_somam = True
    for combinacao in resultado:
        soma = 0
        for peso in combinacao:
            soma += peso
        if soma != alvo:
            todas_somam = False

    print(f'Caso: {nome}')
    print(f'  Alvo:        {alvo}')
    print(f'  Pesos:       {pesos}')
    print(f'  Combinações: {resultado}')
    print(f'  Quantidade:  {len(resultado)}')
    print(f'  Todas somam o alvo: {todas_somam}')
    print()
