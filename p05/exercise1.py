import random

# for a in range(5):
#     print(a, end='')
#
# print()
# for a in range(2, 5):
#     print(a, end='')
#
# print()
# for a in range(4, 10, 2):
#     print(a, end='')


# start_range = int(input('start :'))
# end_range = int(input('end :'))
# step_range = int(input('step :'))
# for i in range(start_range, end_range, step_range):
#     print(i, end=', ')

# for x in range(100):
#     x = random.randint(0, 100)
#     print(x, end=', ')

# for a in range(1, 10):
#     print()
#     for i in range(1, 10):
#         print(f'{a}*{i}={a*i}', end=' ' )

start_range = int(input('start :'))
end_range = int(input('end :'))
for a in range(start_range, end_range):
    is_prime = True

    for i in range(2, a):
        if a % i == 0:
            is_prime = False
            break

    if is_prime:
        print('%d, ' % a, end='')
