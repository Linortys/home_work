def task_1(a: int, b: float, c: str, d: list, g: bool) -> str:

    print (a, 'Тип данных', type(a))
    print (b, 'Тип данных', type(b))
    print(c, 'Тип данных', type(c))
    print(d, 'Тип данных', type(d))
    print(g, 'Тип данных', type(g))

task_1('1',7.3, 5, [5,5], True)

def task_2() -> list:

    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3])   #числа Фибоначчи

task_2()

def task_3(a: int) -> int:
    return a ** 2

print(task_3(4))