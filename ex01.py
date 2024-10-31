""" Dado Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado
um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não
a sequência.a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado
um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não
a sequência. """

def fibonacci_sequencia(n):
    sequencia = [0, 1]
    while True:
        valor = sequencia[-1] + sequencia[-2]
        if valor > n:
            break
        sequencia.append(valor)
    return sequencia

def check_fibonacci(numero):
    if numero < 0:
        return False
    return numero in fibonacci_sequencia(numero)

def main():
    n = int(input("Informe um número: "))
    if check_fibonacci(n):
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
