import turtle as t

t.screensize(2000,2000)

def alterar_estilo(l):
    if (l*diminuir_comprimento_ram < tamanho_min_ram):
        t.color(folhas)
        t.width(grossura_folhas)
    else:
        t.color(galhos)
        t.width(grossura_galhos)

def linha(l, direcao):
    alterar_estilo(l)
    if direcao:
        t.right(r)
        t.forward(l)
    else:
        t.left(r)
        t.forward(l)

def voltar(l, direcao):
    alterar_estilo(l)

    if direcao:
        t.backward(l)
        t.right(r)
    else:
        t.backward(l)
        t.left(r)

def ramificar (l, direcao):
    if (l >= tamanho_min_ram):
        linha(l, direcao)
        ramificar(l*diminuir_comprimento_ram, direcao)
        voltar(l, not direcao)
        linha(l, not direcao)
        voltar(l, direcao)
        ramificar(l*diminuir_comprimento_ram, not direcao)

while True:
    t.clearscreen()
    t.hideturtle()
    t.speed(0)
    t.bgcolor('black')
    
    l = int(input('Medida base: '))
    r = float(input('Ângulação: '))
    diminuir_comprimento_ram = float(input('Quanto cada ramificação irá ficar com a medida base: '))
    tamanho_min_ram = float(input('Medida minima de uma rama: '))

    folhas = str(input('Cor das folhas: '))
    galhos = str(input('Cor dos galhos: '))

    grossura_folhas = int(input('Grussura das folhas: '))
    grossura_galhos = int(input('Grussura das galhos: '))

    t.color(galhos)
    t.width(grossura_galhos)
    t.goto(0, -l)
    t.left(90)
    t.forward(l*2)

    print('Construindo...\n')
    for i in range(2):
        isOdd = i%2==0
        ramificar(l, isOdd)
    print('Árvore construida com sucesso :)\n\n')
    continuar = str(input('Deseja construir outra árvore: (s/n)\n')).upper().strip()
    if continuar == 'N' or continuar == 'NO' or continuar == 'NÃO' or continuar == 'NAO':
        break
t.done()