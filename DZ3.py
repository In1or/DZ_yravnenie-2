import math
def calc_quadration_equation(a,b,c):
    def calc_discriminant(a,b,c):
    	return b**2 - 4*a*c

    D = calc_discriminant(a,b,c)
    if D > 0:
    	return (-b + math.sqrt(D)) / 2*a, (-b - math.sqrt(D)) / 2*a
    elif D == 0:
    	return -b / 2*a
    elif D < 0:
    	return 'no roots'

def calc_nepolnoe_equation(a,c):
	if ((c > 0) and (a < 0)) or((c < 0) and (a > 0)):
		return math.sqrt(-c / a), -1 * math.sqrt(-c / a)
	elif c == 0:
		return 0, 0
	else:
		return 'no roots'

def calc_linear_equation(b,c):
	return -c / b


a, b, c = map(int, input('Введите коэффициенты квадратного уравнения: ').split())
if (a == 0) and (b == 0) and (c != 0):
	print('no roots')
elif (a == 0) and (b == 0) and (c == 0):
	print('Корень любое число')
elif (b == 0):
	print(calc_nepolnoe_equation(a,c))
elif a != 0:
	print(calc_quadration_equation(a,b,c))
else:
	print(calc_linear_equation(b,c))
input()