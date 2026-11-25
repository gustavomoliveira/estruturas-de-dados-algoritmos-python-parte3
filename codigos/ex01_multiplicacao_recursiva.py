def mult(x, y, nivel=0):
    espaco = '  ' * nivel
    print(f'{espaco}chamada: mult({x}, {y})')

    if y == 0:
        print(f'{espaco}caso base: mult({x}, 0) = 0')
        return 0

    resultado = mult(x, y - 1, nivel + 1)
    soma = x + resultado
    print(f'{espaco}retorno: mult({x}, {y}) = {x} + {resultado} = {soma}')
    return soma


print('=== Exercício 1 – Multiplicação recursiva por soma ===')
print()

testes = [
    ('multiplicação comum', 3, 4),
    ('multiplicador igual a 1', 5, 1),
    ('multiplicador igual a 0', 7, 0),
    ('multiplicando igual a 0', 0, 3),
    ('valores maiores', 12, 6),
]

for nome, x, y in testes:
    print(f'Caso: {nome} -> mult({x}, {y})')
    resultado = mult(x, y)
    print(f'  Resultado: {resultado}')
    print(f'  Esperado:  {x * y}')
    print(f'  Confere:   {resultado == x * y}')
    print()
