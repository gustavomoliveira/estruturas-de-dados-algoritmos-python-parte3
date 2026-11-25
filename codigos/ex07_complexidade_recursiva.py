def knapsack_contado(target, weights, index, estados, contagem):
    contagem['chamadas'] += 1
    chave = (target, index)
    estados[chave] = estados.get(chave, 0) + 1

    if target == 0:
        return [[]]

    if target < 0 or index >= len(weights):
        return []

    resultado = []

    for combinacao in knapsack_contado(target - weights[index], weights, index + 1, estados, contagem):
        resultado.append([weights[index]] + combinacao)

    for combinacao in knapsack_contado(target, weights, index + 1, estados, contagem):
        resultado.append(combinacao)

    return resultado


print('=== Exercício 7 – Análise de complexidade: knapsack recursivo ===')
print()

pesos_pequenos = [1, 2, 3, 4]
estados = {}
contagem = {'chamadas': 0}
resultado = knapsack_contado(5, pesos_pequenos, 0, estados, contagem)

print('Exemplo pequeno')
print(f'  Pesos:               {pesos_pequenos}')
print(f'  Alvo:                5')
print(f'  Combinações:         {resultado}')
print(f'  Chamadas:            {contagem["chamadas"]}')
print(f'  Estados distintos:   {len(estados)}')
print()
print('  Estados (alvo, índice) chamados mais de uma vez')
for chave in estados:
    if estados[chave] > 1:
        print(f'    {chave} -> {estados[chave]} vezes')
print()

print('Crescimento do número de chamadas (pesos 1, 2, ..., N e alvo = soma dos pesos / 2)')
print(f'{"N":<6}{"Alvo":<8}{"Chamadas":<12}{"Estados distintos":<20}{"Redundantes":<14}{"Razão (N-2)"}')
print('-' * 80)

anterior = None

for n in range(6, 25, 2):
    pesos = list(range(1, n + 1))
    alvo = n * (n + 1) // 4
    estados = {}
    contagem = {'chamadas': 0}
    knapsack_contado(alvo, pesos, 0, estados, contagem)

    chamadas = contagem['chamadas']
    distintos = len(estados)
    redundantes = chamadas - distintos

    if anterior is None:
        razao = '-'
    else:
        razao = f'{chamadas / anterior:.2f}'

    print(f'{n:<6}{alvo:<8}{chamadas:<12}{distintos:<20}{redundantes:<14}{razao}')
    anterior = chamadas
