def power(x, y):
    if y == 0:
        return 1

    if y == 1:
        return x

    if y < 0:
        if x == 0:
            raise Exception('zero elevado a expoente negativo não é definido')
        return 1 / power(x, -y)

    return x * power(x, y - 1)


def power_contado(x, y):
    if y == 0:
        return 1, 1

    if y == 1:
        return x, 1

    if y < 0:
        resultado, chamadas = power_contado(x, -y)
        return 1 / resultado, chamadas

    resultado, chamadas = power_contado(x, y - 1)
    return x * resultado, chamadas + 1


print('=== Exercício 3 – Potenciação recursiva com expoentes negativos ===')
print()

testes = [
    ('expoente zero', 5, 0),
    ('expoente um', 5, 1),
    ('base positiva', 2, 10),
    ('base negativa, expoente par', -3, 4),
    ('base negativa, expoente ímpar', -3, 5),
    ('base zero', 0, 5),
    ('zero elevado a zero', 0, 0),
    ('expoente negativo', 2, -3),
    ('base negativa, expoente negativo par', -2, -2),
    ('base negativa, expoente negativo ímpar', -2, -3),
    ('base 1', 1, -50),
]

for nome, x, y in testes:
    resultado = power(x, y)
    esperado = x ** y
    print(f'Caso: {nome} -> power({x}, {y})')
    print(f'  Resultado: {resultado}')
    print(f'  Esperado:  {esperado}')
    print(f'  Confere:   {resultado == esperado}')
    print()

print('Erro tratado')
try:
    power(0, -2)
except Exception as erro:
    print(f'  power(0, -2) -> ERRO tratado: {erro}')
print()

print('Crescimento do número de chamadas')
print(f'{"Expoente":<10}{"Chamadas"}')
print('-' * 18)
for expoente in [1, 5, 10, 20, 40, 80, -5, -40]:
    resultado, chamadas = power_contado(2, expoente)
    print(f'{expoente:<10}{chamadas}')
