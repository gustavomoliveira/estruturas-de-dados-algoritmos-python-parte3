import random


def particionar(lista, inicio, fim):
    pivo = lista[fim]
    posicao = inicio

    for atual in range(inicio, fim):
        if lista[atual] < pivo:
            auxiliar = lista[posicao]
            lista[posicao] = lista[atual]
            lista[atual] = auxiliar
            posicao += 1

    auxiliar = lista[posicao]
    lista[posicao] = lista[fim]
    lista[fim] = auxiliar

    return posicao


def selecionar(lista, inicio, fim, indice):
    posicao_pivo = particionar(lista, inicio, fim)

    if posicao_pivo == indice:
        return lista[posicao_pivo]

    if indice < posicao_pivo:
        return selecionar(lista, inicio, posicao_pivo - 1, indice)

    return selecionar(lista, posicao_pivo + 1, fim, indice)


def quickselect(lista, indice):
    if indice < 0 or indice >= len(lista):
        raise Exception('índice fora dos limites da lista')

    resultado = lista.copy()
    return selecionar(resultado, 0, len(resultado) - 1, indice)


def mediana(lista):
    tamanho = len(lista)

    if tamanho % 2 == 1:
        return quickselect(lista, tamanho // 2)

    inferior = quickselect(lista, tamanho // 2 - 1)
    superior = quickselect(lista, tamanho // 2)
    return (inferior + superior) / 2


def testar_mediana(nome, lista):
    resultado = mediana(lista)
    esperado = sorted(lista)[len(lista) // 2]
    print(f'{len(lista):<8}{nome:<18}{resultado:<10}{esperado:<10}{resultado == esperado}')


print('=== Exercício 11 – QuickSelect recursivo ===')
print()

lista_teste = [9, 4, 7, 1, 8, 3, 6]
ordenada = sorted(lista_teste)

print('Seleção de cada índice')
print(f'  Lista:     {lista_teste}')
print(f'  Ordenada:  {ordenada}')
print(f'{"Índice":<10}{"QuickSelect":<14}{"Esperado":<10}{"Confere"}')
print('-' * 42)
for indice in range(len(lista_teste)):
    valor = quickselect(lista_teste, indice)
    print(f'{indice:<10}{valor:<14}{ordenada[indice]:<10}{valor == ordenada[indice]}')
print()

print('Mediana')
casos = [
    ('tamanho ímpar', [9, 4, 7, 1, 8, 3, 6], 6),
    ('tamanho par', [10, 2, 8, 4, 6, 12], 7.0),
    ('um elemento', [5], 5),
    ('com repetidos', [3, 1, 3, 2, 3], 3),
    ('negativos', [-4, 10, -7, 0, 2], 0),
]
for nome, lista, esperado in casos:
    resultado = mediana(lista)
    print(f'  {nome}: {lista} -> {resultado}  esperado: {esperado}  confere: {resultado == esperado}')
print()

print('Mediana em listas maiores')
print(f'{"N":<8}{"Estado inicial":<18}{"Mediana":<10}{"Esperado":<10}{"Confere"}')
print('-' * 54)

random.seed(42)
tamanho = 401

testar_mediana('aleatória', random.sample(range(tamanho * 10), tamanho))
testar_mediana('já ordenada', list(range(tamanho)))
testar_mediana('invertida', list(range(tamanho, 0, -1)))
print()

print('Índice inválido')
try:
    quickselect([1, 2, 3], 5)
except Exception as erro:
    print(f'  quickselect([1, 2, 3], 5) -> ERRO tratado: {erro}')