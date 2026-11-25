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


def gerar_cenarios(tamanho):
    random.seed(42)
    aleatoria = random.sample(range(tamanho * 10), tamanho)
    ordenada = list(range(tamanho))
    invertida = list(range(tamanho, 0, -1))
    return {
        'aleatória': aleatoria,
        'já ordenada': ordenada,
        'invertida': invertida,
    }


print('=== Exercício 10 – Instrumentação do QuickSort (uma troca = 3 cópias) ===')
print()

lista_teste = [8, 3, 7, 1, 9, 2, 5]
saida, comparacoes, copias = quicksort_contado(lista_teste)
print('Teste pequeno')
print(f'  Entrada:     {lista_teste}')
print(f'  Saída:       {saida}')
print(f'  Comparações: {comparacoes}')
print(f'  Cópias:      {copias}')
print()

print(f'{"N":<8}{"Cenário":<16}{"Comparações":<14}{"Cópias":<10}{"N(N-1)/2":<12}{"Ordenou"}')
print('-' * 66)

for tamanho in [50, 100, 200, 400]:
    for nome, lista in gerar_cenarios(tamanho).items():
        saida, comparacoes, copias = quicksort_contado(lista)
        maximo = tamanho * (tamanho - 1) // 2
        print(f'{tamanho:<8}{nome:<16}{comparacoes:<14}{copias:<10}{maximo:<12}{saida == sorted(lista)}')
    print()
