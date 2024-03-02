while True:
    print("Calculator [+ - * / ^] Exit 'x' ")
    action = input('Action: ')
    if action == 'x':
        break
    n1 = float(input('number 1: '))
    n2 = float(input('number 2: '))
    if action == '+':
        result = n1 + n2
    elif action == '-':
        result = n1 - n2
    elif action == '*':
        result = n1 * n2
    elif action == '/':
        if n2 == 0:
            print("'you can't do that")
        result = n1 / n2
    elif action == '^':
        result = n1 ** n2
    else:
        print("unknown command")

    print('Result = ', result)