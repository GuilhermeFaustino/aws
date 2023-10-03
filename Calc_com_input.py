def calculador():


    while True:
        print("Operações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        escolha = input("Digite o número para a operação desejada: ")

        if escolha == '0':
            print("Saindo da calculadora.")
            break
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))

        if escolha == '1':
            print("A  Soma dos valoes é ", valor1 + valor2)
        elif escolha == '2':
            print("A  Subtração dos valoes é ", valor1 - valor2)
        elif escolha == '3':
            print("A  Multiplicacao dos valoes é ", valor1 * valor2)
        else:
            print("A  Divisao dos valoes é ", valor1 / valor2)

calculador()
