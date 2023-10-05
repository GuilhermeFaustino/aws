def data_aniversario():
    try:
        nome = input("Digite seu nome: ")
        dataInicial = int(input("Digite ano de nascimento: "))
        dataFinal = int(input("Digite o ano atual: "))

        result = dataFinal - dataInicial
        resultAno = 2022 - dataInicial

        print("Seu nome é " + nome + " em 2023 sua idade é :", result)
        print("Sua idade que você completaria ou completou em 2022 é:", resultAno)

        if 1922 <= dataInicial <= 2022:
            idade = dataFinal - dataInicial
            print("Nome: " + nome)
            print("Idade em 2023:", idade, "anos")
        else:
            print("Favor verificar os anos.")
    except ValueError:
        print("Ano de nascimento fora do intervalo válido.")


data_aniversario()

