def knapsack_contado(target, weights, index, contagem):
    contagem['chamadas'] += 1

    if target == 0:
        return [[]]

    if target < 0 or index >= len(weights):
        return []

    resultado = []

    for combinacao in knapsack_contado(target - weights[index], weights, index + 1, contagem):
        resultado.append([weights[index]] + combinacao)

    for combinacao in knapsack_contado(target, weights, index + 1, contagem):
        resultado.append(combinacao)

    return resultado


def knapsack_memo(target, weights, index, memoria, contagem):
    contagem['chamadas'] += 1
    chave = (target, index)

    if chave in memoria:
        contagem['reaproveitados'] += 1
        return memoria[chave]

    if target == 0:
        return [[]]

    if target < 0 or index >= len(weights):
        return []

    resultado = []

    for combinacao in knapsack_memo(target - weights[index], weights, index + 1, memoria, contagem):
        resultado.append([weights[index]] + combinacao)

    for combinacao in knapsack_memo(target, weights, index + 1, memoria, contagem):
        resultado.append(combinacao)

    memoria[chave] = resultado
    return resultado


print('=== Exercício 8 – Otimização com programação dinâmica (memoização) ===')
print()

print('Comparação entre a versão recursiva pura e a versão com memoização')
print(f'{"N":<6}{"Alvo":<8}{"Chamadas (pura)":<18}{"Chamadas (memo)":<18}{"Reaproveitados":<16}{"Redução":<10}{"Iguais"}')
print('-' * 84)

for n in range(6, 25, 2):
    pesos = list(range(1, n + 1))
    alvo = n * (n + 1) // 4

    contagem_pura = {'chamadas': 0}
    resultado_puro = knapsack_contado(alvo, pesos, 0, contagem_pura)

    memoria = {}
    contagem_memo = {'chamadas': 0, 'reaproveitados': 0}
    resultado_memo = knapsack_memo(alvo, pesos, 0, memoria, contagem_memo)

    chamadas_puras = contagem_pura['chamadas']
    chamadas_memo = contagem_memo['chamadas']
    reducao = chamadas_puras / chamadas_memo
    iguais = resultado_puro == resultado_memo

    print(f'{n:<6}{alvo:<8}{chamadas_puras:<18}{chamadas_memo:<18}{contagem_memo["reaproveitados"]:<16}{reducao:<10.1f}{iguais}')

print()
print('Crescimento da versão com memoização')
print(f'{"N":<6}{"Alvo":<8}{"Chamadas (memo)":<18}{"Estados guardados"}')
print('-' * 50)

for n in [10, 15, 20, 25, 30]:
    pesos = list(range(1, n + 1))
    alvo = n * (n + 1) // 4
    memoria = {}
    contagem_memo = {'chamadas': 0, 'reaproveitados': 0}
    knapsack_memo(alvo, pesos, 0, memoria, contagem_memo)
    print(f'{n:<6}{alvo:<8}{contagem_memo["chamadas"]:<18}{len(memoria)}')
