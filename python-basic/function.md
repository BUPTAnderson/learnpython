## 函数   
### 格式
```
def 函数名（参数列表）:
    函数体
```
### 参数传递
- **不可变类型**：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
- **可变类型**：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
### 参数
以下是调用函数时可使用的正式参数类型：
- 必选参数/必须参数
- 默认参数
- 可变参数/不定长参数
- 命名关键字参数
- 关键字参数

#### 必选参数/必须参数
`def printme( str ): print(str)`  
&emsp; 调用 printme 函数，不加参数会报错

#### 默认参数
`def printinfo(name, age=35): print("名字: %s\n年龄: %s" % (name, age)) #默认参数要定义在必选参数后面`  
&emsp; 调用函数时，如果没有传递参数，则会使用默认参数。上述实例中如果没有传入 age 参数，则使用默认值
```
printinfo("runoob")
printinfo(name="runoob")
printinfo("runoob", 50)
printinfo(name="runoob", age=50)
printinfo(age=50, name="runoob")
printinfo("runoob", age=50) # printinfo(name="runoob", 50)不可以
```
**NOTE:** Python函数在定义的时候，默认参数L的值就被计算出来了, 定义默认参数要牢记一点：默认参数必须指向不变对象！
```angular2html
def add_end(L=[]):
    L.append('END')
    return L
```
&emsp;  连续调用`add_end()`两次，输出为：`['END', 'END']` 原因解释如下：  
&emsp; &emsp; Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。要修改上面的例子，我们可以用None这个不变对象来实现：  
```
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

#### 可变参数
格式：
```angular2html
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
```
***加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。***
```
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```
定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数:  
```
calc(1, 3, 5, 7)
```
Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：  
```
nums = [1, 2, 3]
calc(*nums)
```
`*nums`表示把`nums`这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。  
#### 关键字参数
基本语法：
```angular2html
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
```
加了两个星号 ** 的参数(关键字参数)会以字典的形式导入。关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：

```
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Adam', 45, gender='M', job='Engineer')
```
另一种调用:  
```
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
```
 ** extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
 
#### 命名关键字参数
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
```angular2html
def person(name, age, *, city, job):
    print(name, age, city, job)
```
和关键字参数`**kw`不同，命名关键字参数需要一个特殊分隔符`*`，`*`后面的参数被视为命名关键字参数。  
调用方式：`person('Jack', 24, city='Beijing', job='Engineer')`  
如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了：
```angular2html
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
```
命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
```angular2html
person('Jack', 24, 'Beijing', 'Engineer')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: person() takes 2 positional arguments but 4 were given
```
命名关键字参数可以有缺省值，从而简化调用：
```angular2html
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
```
由于命名关键字参数`city`具有默认值，调用时，可不传入`city`参数：`person('Jack', 24, job='Engineer')`  
**NOTE：** 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数

#### 参数组合
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：**必选参数、默认参数、可变参数、命名关键字参数和关键字参数**。
```angular2html
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
```
最神奇的是通过一个tuple和dict，你也可以调用上述函数：
```angular2html
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
```

#### 强制位置参数
Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。  
在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参:
```angular2html
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
```
调用：
```angular2html
f(10, 20, 30, d=40, e=50, f=60)       # 正确
f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式
```

#### 匿名函数