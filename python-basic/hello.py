# print("Hello world!")
# for i in range(1, 10):
#     print(i)

def trim(s):
    l = len(s)
    if l == 0:
        return ''
    else:
        x = y = 0
        for i in range(l):
            if s[i] != ' ':
                x = i
                break
        for j in range((l - 1), -1, -1):
            if s[j] != ' ':
                y = j + 1
                break
        if x == y:
            return ''
        else:
            return s[x:y]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')