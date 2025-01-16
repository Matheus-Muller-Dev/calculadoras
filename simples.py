def welcome():
    print('''
    Bem vindo a calculadora
          ''')
welcome()
# condicional
def calcular():
    operation = input('''
Por favor coloque o operador que deseja realizar a operação
    + Adição
    - Subtração
    * Multiplicação
    / Divisão
    ''')

    number_1 = float(input('Digite o primeiro número: '))
    number_2 = float(input('Digite o segunfo número: '))

    # adição
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    # subtração
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    # multiplicação
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    # Divisão
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você colocou um operador incorreto, por gentileza rode o programa novamente')

    novamente()

def novamente():
    calc_novamente = input(''' 
    gostaria de calcular novamente?
    digite Y para sim ou N para não:
''')
    
    if calc_novamente.upper() == 'Y':
        calcular()
    elif calc_novamente.upper() == 'N':
        print('Até depois.')
    else:
        novamente()

calcular()