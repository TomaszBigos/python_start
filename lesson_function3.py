"""
Function 3
"""
x = 0


def fun1(value):
    print('Fun1')
    return value


def fun2(value):
    print('Fun2')
    y = 0

    def fun3():
        nonlocal y
        y = value

    fun3()
    return value


def executor(value1, value2, **functions):
    global x
    x = functions.get("a")(value1) * functions.get("b")(value2)


executor(5, 6, a=fun1, b=fun2)
print(x)

executor(3, 7, a=fun1, b=fun2)
print(x)
