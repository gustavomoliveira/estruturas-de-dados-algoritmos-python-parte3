def factor(x, lowest=2):
    if x == 0 or x == 1:
        return [x]

    if x < 0:
        return [-1] + factor(-x, lowest)

    for divisor in range(lowest, int(x ** 0.5) + 1):
        if x % divisor == 0:
            return [divisor] + factor(x // divisor, divisor)

    return [x]


print('=== Exercício 2 – Fatoração recursiva de inteiros ===')
print()

casos = [
    ('número composto', 360, [2, 2, 2, 3, 3, 5]),
    ('três primos diferentes', 1001, [7, 11, 13]),
    ('potência de 2', 1024, [2] * 10),
    ('quadrado de primo', 49, [7, 7]),
    ('número primo pequeno', 2, [2]),
    ('número primo', 97, [97]),
    ('número primo grande', 1000003, [1000003]),
    ('número 1', 1, [1]),
    ('número 0', 0, [0]),
    ('número negativo', -12, [-1, 2, 2, 3]),
    ('negativo primo', -7, [-1, 7]),
]

for nome, entrada, esperado in casos:
    resultado = factor(entrada)
    produto = 1
    for fator in resultado:
        produto *= fator

    print(f'Caso: {nome}')
    print(f'  Entrada:   {entrada}')
    print(f'  Fatores:   {resultado}')
    print(f'  Esperado:  {esperado}')
    print(f'  Produto:   {produto}')
    print(f'  Confere:   {resultado == esperado}')
    print()

print('Efeito do parâmetro lowest')
print(f'  factor(90)    -> {factor(90)}')
print(f'  factor(45, 3) -> {factor(45, 3)}')
print(f'  factor(15, 4) -> {factor(15, 4)}')
