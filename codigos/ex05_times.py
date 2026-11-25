import math


def teams(candidates, k):
    if k == 0:
        return ['']

    if len(candidates) < k:
        return []

    primeiro = candidates[0]
    restantes = candidates[1:]
    resultado = []

    for time in teams(restantes, k - 1):
        resultado.append(primeiro + time)

    for time in teams(restantes, k):
        resultado.append(time)

    return resultado


print('=== Exercício 5 – Geração recursiva de combinações (times) ===')
print()

candidatos = 'ABCDE'

print(f'Candidatos: {candidatos}')
print()

for k in range(0, 7):
    resultado = teams(candidatos, k)
    esperado = math.comb(len(candidatos), k)
    sem_repeticao = len(set(resultado)) == len(resultado)

    print(f'k = {k}')
    print(f'  Times:          {resultado}')
    print(f'  Quantidade:     {len(resultado)}')
    print(f'  Esperado:       {esperado}')
    print(f'  Sem repetições: {sem_repeticao}')
    print(f'  Confere:        {len(resultado) == esperado and sem_repeticao}')
    print()

maior = 'ABCDEFGHIJ'
print(f'Candidatos maiores: {maior}')
print(f'{"k":<6}{"Quantidade":<14}{"Esperado":<12}{"Sem repetições"}')
print('-' * 44)
for k in [2, 3, 5, 8]:
    resultado = teams(maior, k)
    sem_repeticao = len(set(resultado)) == len(resultado)
    print(f'{k:<6}{len(resultado):<14}{math.comb(len(maior), k):<12}{sem_repeticao}')
