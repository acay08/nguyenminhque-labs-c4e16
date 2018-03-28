from random import randint,choice
#
# x = randint(1, 10)
# y = randint(1,10)
# err = choice([1, 0, -1])
# op = choice(["+","-","*", "/"])
#
# if op == "+":
#     result = x + y
# elif op =="-":
#     result = x - y
# elif op =="*":
#     result = x * y
# elif op =="/":
#     result = x / y

# print(result)

def calc(x, y, op):
    err = choice([1, 0, -1])

    if op == "+":
        result = x + y
    elif op =="-":
        result = x - y
    elif op =="*":
        result = x * y
    elif op =="/":
        result = x / y

    return result

# res = calc(3, 7, "+")
# print(res)
#arguement, parameter
# op = choice(["+","-","*", "/"])
# calc(4, 8, op)
