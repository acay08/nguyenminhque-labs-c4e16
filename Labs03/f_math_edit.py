from random import randint,choice
from eval import calc
x = randint(1, 10)
y = randint(1,10)
err = choice([1, 0, -1])
op = choice(["+","-","*", "/"])


result = calc(x, y, op)
result += err
print('{0} {1} {2} = {3}'.format(x, op, y, result))
ans = input('check Y/N? ').upper()

if (ans == "Y" and err == 0) or (ans == "N" and err != 0):
    print('correct')
else:
    print('incorrect')
