import random


def particionar(lista, inicio, fim, contagem):
    pivo = lista[fim]
    posicao = inicio

    for atual in range(inicio, fim):
        contagem['comparacoes'] += 1
        if lista[atual] < pivo:
            if posicao != atual:
                auxiliar = lista[posicao]
                lista[posicao] = lista[atual]
                lista[atual] = auxiliar
                contagem['copias'] += 3
            posicao += 1

    if posicao != fim:
        auxiliar = lista[posicao]
        lista[posicao] = lista[fim]
        lista[fim] = auxiliar
        contagem['copias'] += 3

    return posicao


def ordenar(lista, inicio, fim, contagem):
    if inicio >= fim:
        return

    posicao_pivo = particionar(lista, inicio, fim, contagem)
    ordenar(lista, inicio, posicao_pivo - 1, contagem)
    ordenar(lista, posicao_pivo + 1, fim, contagem)


def quicksort_contado(lista):
    resultado = lista.copy()
    contagem = {'comparacoes': 0, 'copias': 0}
    ordenar(resultado, 0, len(resultado) - 1, contagem)
    return resultado, contagem['comparacoes'], contagem['copias']


def selecionar(lista, inicio, fim, indice, contagem):
    posicao_pivo = particionar(lista, inicio, fim, contagem)

    if posicao_pivo == indice:
        return lista[posicao_pivo]

    if indice < posicao_pivo:
        return selecionar(lista, inicio, posicao_pivo - 1, indice, contagem)

    return selecionar(lista, posicao_pivo + 1, fim, indice, contagem)


def quickselect_contado(lista, indice):
    resultado = lista.copy()
    contagem = {'comparacoes': 0, 'copias': 0}
    valor = selecionar(resultado, 0, len(resultado) - 1, indice, contagem)
    return valor, contagem['comparacoes'], contagem['copias']


def comparar(nome, lista):
    indice = len(lista) // 2
    ordenada, comp_sort, copias_sort = quicksort_contado(lista)
    valor, comp_select, copias_select = quickselect_contado(lista, indice)
    mesma = ordenada[indice] == valor
    razao = comp_sort / comp_select
    print(f'{len(lista):<6}{nome:<14}{comp_sort:<11}{copias_sort:<11}{comp_select:<12}{copias_select:<13}{razao:<9.2f}{mesma}')


print('=== Exercício 12 – Comparação entre QuickSort e QuickSelect (mediana) ===')
print()
print(f'{"N":<6}{"Cenário":<14}{"QS comp.":<11}{"QS cópias":<11}{"QSel comp.":<12}{"QSel cópias":<13}{"Razão":<9}{"Mesma mediana"}')
print('-' * 88)

for tamanho in [101, 201, 401]:
    random.seed(42)
    comparar('aleatória', random.sample(range(tamanho * 10), tamanho))
    comparar('já ordenada', list(range(tamanho)))
    comparar('invertida', list(range(tamanho, 0, -1)))
    print()