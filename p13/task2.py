def addition_subtraction(a: int = 0, b: int = 0, action: str = '+'):
    if action == '+':
        return a + b
    elif action == '-':
        return a - b


res = addition_subtraction(5, 8, '-')
print(res)
