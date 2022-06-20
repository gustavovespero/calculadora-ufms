from multiplica import multiplica
from soma import soma
from subtrai import subtrai
from divide import divide

def main():
    val1 = input('Valor1: ')
    val2 = input('Valor2: ')
    op = input('Operacao: ')

    if op == 'soma':
        resultado = soma(val1, val2)
    elif op == 'multiplicacao':
        resultado = multiplica(val1, val2)
    elif op == 'subtracao':
        resultado = subtrai(val1, val2)
    elif op == 'divide':
        resultado = divide(val1,val2)

    print(resultado)

if __name__ == '__main__':
    main()
