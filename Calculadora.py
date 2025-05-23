# Calculadora

# Autor: Antony Rafael dos Santos Rufino

def calculadora():
    print("Calculadora")
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolha = input("Digite sua escolha (1/2/3/4): ")

        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = num1 + num2
                operacao = '+'
            elif escolha == '2':
                resultado = num1 - num2
                operacao = '-'
            elif escolha == '3':
                resultado = num1 * num2
                operacao = '*'
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    operacao = '/'
                else:
                    print("Erro: Divisão por zero não é permitida.")
                    continue

            print(f"{num1} {operacao} {num2} = {resultado}")
        else:
            print("Opção inválida. Tente novamente.")

        proxima_operacao = input("Deseja realizar outra operação? (s/n): ")
        if proxima_operacao.lower() != 's':
            break