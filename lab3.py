def treug(a,b,c):
	return a+b>c and a+c>b and b+c>a
while True:
	try:
		t = [int ( input ( f"длина стороны {i}:\n")) for i in "abc"]
		if not treug(*t):
			print("не треугольник")
			continue
		break
	except:
		print("ЧИСЛО")
print("усё")