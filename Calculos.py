# Calculadora

# Entradas
a = int(input('Digite o primeiro numero:'))
operacao = input('Escolha uma operacao:')
b = input('Digite o segundo numero:')

# SOMA

if operacao == '+':
    if b == '':
        b = '0'
    b = int(b)
    soma = a + b
    print(soma)

# SUBTRACÃO

elif operacao == '-':
    if b == '':
        b = '0'
    b = int (b)
    subtracao = a - b
    print(subtracao)

# MULTIPLICAÇÃO

elif operacao == '*':
    if b == '':
        b = '0'
    b = int(b)
    multiplicacao = a * b
    print(multiplicacao)

# DIVISÃO

elif operacao == '/':
    if b == '':
        b = '0'
    b = int(b)
    divisao = a / b
    print(divisao)

# PORCENTAGEM

elif operacao =='p':
    if b == '':
        b = '0'
    b = int(b)
    porcentagem = (a/100)*b
    print(porcentagem)

# POTENCIALIZAÇÃO

elif operacao == '**':
    if b == '':
        b = '0'
    b = int(b)
    potencializacao = a**b
    print(potencializacao)

# RAIZ QUADRADA

elif operacao == 'r':

    raiz = a ** 0.5
    print(raiz)
    print('Operação 'r',irá considerar apenas o primeiro número e já trará o resultado para o usuário')

else:
    print('Digite uma operação válida:')
