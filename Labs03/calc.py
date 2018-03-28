x = int(input('x = '))
func = input('Operations(+,-,*,/): ')
y = int(input('y ='))

result = -999
if func == '+':
    result = x + y
elif func == '-':
    result = x - y
elif func == '*':
    result = x * y
elif func == '/':
    result = x / y

print("{0} {1} {2} = {3}".format(x,func,y,result))
