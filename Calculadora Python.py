while True:
    num1 = float(input("Digite o primeiro número: "))
    op = input("Digite o símbolo da operação (+, -, *, /): ").strip()
    num2 = float(input("Digite o segundo número: "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print("Operação inválida! Tente novamente.")
        continue  # Volta para o início do loop sem tentar mostrar o resultado

    # O print DEVE ter 4 espaços de recuo (mesmo nível do 'if')
    print('{} {} {} = {}'.format(num1, op, num2, result))

    # Pergunta se o usuário quer continuar ou fechar o programa
    continuar = input("\nDeseja fazer outro cálculo? (s/n): ").strip().lower()
    if continuar != 's':
        break