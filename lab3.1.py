def treug(a,b,c):
	return a+b>c and a+c>b and b+c>a
flag = True
while flag:
	try:
		print('-'*50)
		t = [int(input(f"Длина стороны {i}:\n")) for i in "abc"]
		if not treug(*t):
			print("\n\033[31m\033[1mНе треугольник\033[0m\n")
			continue
		p = (t[0]+t[1]+t[2])/2
		S = (p*(p-t[0])*(p-t[1])*(p-t[2]))**0.5
		print(f"\n\033[32m\033[1mПлощадь треугольника = {S}\033[0m\n")
		if input("еще раз? (y/n)\n") != "y":
			flag = False
	except:
		print("\n\033[31m\033[1mДОЛЖНО БЫТЬ ЧИСЛО\033[0m\n")
print("Усё")
