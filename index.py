import os
while True:

    print('///////////////////////////////////////////////////')
    print('/                                                 /')
    print('/                  calculadora                    /')
    print('/                                                 /')
    print('///////////////////////////////////////////////////')
    operacao = input('\nQual operação?\n \n1) Soma\n2) Subtração\n3) Multiplicação\n4) Divisão\nS) para sair\n \ndigite a opção desejada:')
    if operacao == 'S' or operacao == 's':
        os.system('cls')
        break

    elif operacao == '1' or operacao == '2' or operacao == '3' or operacao == '4':
        os.system('cls')

        x = int(input('Primeiro Valor: '))
        os.system('cls')

        y = int(input('Segundo Valor: '))
        os.system('cls')

        if operacao == '1':
            resultado = x + y

        elif operacao == '2':
            resultado = x - y

        elif operacao == '3':
            resultado = x * y

        elif operacao == '4':
            resultado = x / y

        else:
            print('Impossivel de Realizar a Operação')

        print(resultado)
        
        input('Aperter Enter Para continuar')
        os.system('cls')
        
    else:
        print('Erro')
        input('Aperter Enter')
        os.system('cls')