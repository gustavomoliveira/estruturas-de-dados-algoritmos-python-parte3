import os


def criar_estrutura_teste(raiz):
    pastas = [
        'projeto',
        'projeto/docs',
        'projeto/src',
        'projeto/src/modelos',
        'projeto/src/utilidades',
        'projeto/testes',
        'projeto/vazia',
    ]
    arquivos = [
        'projeto/README.md',
        'projeto/docs/manual.txt',
        'projeto/docs/notas.txt',
        'projeto/src/main.py',
        'projeto/src/modelos/usuario.py',
        'projeto/src/modelos/produto.py',
        'projeto/src/utilidades/arquivos.py',
        'projeto/testes/teste_main.py',
    ]

    for pasta in pastas:
        os.makedirs(os.path.join(raiz, pasta), exist_ok=True)

    for arquivo in arquivos:
        caminho = os.path.join(raiz, arquivo)
        if not os.path.exists(caminho):
            conteudo = open(caminho, 'w')
            conteudo.write('exemplo')
            conteudo.close()


def listar_diretorio(caminho, nivel=0):
    recuo = '    ' * nivel
    nomes = sorted(os.listdir(caminho))
    total_arquivos = 0

    for nome in nomes:
        caminho_completo = os.path.join(caminho, nome)
        if not os.path.isdir(caminho_completo):
            print(f'{recuo}[arquivo] {nome}')
            total_arquivos += 1

    for nome in nomes:
        caminho_completo = os.path.join(caminho, nome)
        if os.path.isdir(caminho_completo):
            print(f'{recuo}[pasta]   {nome}/  (nível {nivel + 1})')
            total_arquivos += listar_diretorio(caminho_completo, nivel + 1)

    return total_arquivos


print('=== Exercício 4 – Navegação recursiva em estrutura de diretórios ===')
print()

raiz = 'pasta_teste'
criar_estrutura_teste(raiz)

print(f'Percorrendo: {raiz}/ (nível 0)')
total = listar_diretorio(raiz)
print()
print(f'Total de arquivos encontrados: {total}')
