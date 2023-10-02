def calculadora(numero1, numero2, oper):
    match oper:
        case "+":
            return  numero1 + numero2
        case 'Digite 2 Subtração':
            return numero1 - numero2
        case 'Digite 3. Multiplicação':
            return  numero1 * numero2
        case 'Digite 4 Divisão':
            return numero1 / numero2
        case _:
            return '0';

resultado = calculadora( 10, 20, '+')
print(resultado)
# lembrando que como é uma funcao ja esta declarado os valores e a operacao