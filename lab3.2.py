from math import *
def func(x: int) -> int:
    y = None
    match x:
        case n if n < 1:
            y = (5*x**2+9*x)**(1/3)+3*x
        case x if x >= 4:
            y = 6*x+cos(5*x**3+8)
        case _:
            y = (x**5-2*x**4-5)/(2*x**3+e**(-x))
    return y

flag = True
while flag:
    try:
        print('-'*50)
        x = int(input("Введите x: \n"))
        print(func(x))
        if input("еще раз? (y/n)\n") != "y":
            flag = False
    except:
        print("\n\033[31m\033[1mДОЛЖНО БЫТЬ ЧИСЛО\033[0m\n")
print("Усё")            