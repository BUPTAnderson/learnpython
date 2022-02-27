MIN_VALUE = 1
MAX_VALUE = 10
L = [1, 2, 3]
def validation_check(value):
    global MIN_VALUE # 不加这行语句执行下面那行语句会报错
    MIN_VALUE += 1
    print(MIN_VALUE)
    L.append(4)
    print(L)


validation_check(5)
print(MIN_VALUE)
print(L)
