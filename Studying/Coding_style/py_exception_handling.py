def f1():
	print("f1")
	return 1

def f2():
        print("f2")
	return f1()

def f3():
        print("f3")
	return f2()

f3()
