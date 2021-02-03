# d = {'a': 1, 'b': 2, 'c': 3}
# for item in d.items():
#     print(item[0], item[1])
#
#
# print(len([]))

def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        min = max = L[0]
        for i in L:
            if i < min:
                min = i
            if i > max:
                max = i
        return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')