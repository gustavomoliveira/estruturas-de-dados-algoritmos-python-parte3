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


def ordenar(lista, inicio, fim):
    if inicio >= fim:
        return

    posicao_pivo = particionar(lista, inicio, fim)
    ordenar(lista, inicio, posicao_pivo - 1)
    ordenar(lista, posicao_pivo + 1, fim)


def quicksort(lista):
    resultado = lista.copy()
    ordenar(resultado, 0, len(resultado) - 1)
    return resultado


print('=== Exercício 9 – QuickSort recursivo (pivô = último elemento) ===')
print()

lista_teste = [8, 3, 7, 1, 9, 2, 5]
pivo = lista_teste[len(lista_teste) - 1]
copia = lista_teste.copy()
posicao = particionar(copia, 0, len(copia) - 1)
print('Uma partição')
print(f'  Entrada:        {lista_teste}')
print(f'  Pivô:           {pivo}')
print(f'  Após partição:  {copia}')
print(f'  Posição do pivô: {posicao}')
print()

casos_pequenos = [
    ('desordenada', [8, 3, 7, 1, 9, 2, 5]),
    ('já ordenada', [1, 2, 3, 4, 5]),
    ('invertida', [9, 7, 5, 3, 1]),
    ('com repetidos', [4, 2, 4, 1, 2, 4]),
    ('negativos', [3, -1, 0, -5, 2]),
    ('um elemento', [7]),
    ('lista vazia', []),
]

print('Casos pequenos')
for nome, lista in casos_pequenos:
    saida = quicksort(lista)
    print(f'  {nome}: {lista} -> {saida}  correta: {saida == sorted(lista)}')
print()

print('Casos maiores')
print(f'{"N":<8}{"Estado inicial":<18}{"Ordenou"}')
print('-' * 34)

for tamanho in [50, 100, 200, 400]:
    random.seed(42)
    casos = [
        ('aleatória', random.sample(range(tamanho * 10), tamanho)),
        ('já ordenada', list(range(tamanho))),
        ('invertida', list(range(tamanho, 0, -1))),
    ]

    for nome, lista in casos:
        saida = quicksort(lista)
        print(f'{tamanho:<8}{nome:<18}{saida == sorted(lista)}')
    print()
