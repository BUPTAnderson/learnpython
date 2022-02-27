#### 函数基础
函数就是为了实现某一功能的代码段，只要写好以后，就可以重复利用。
```angular2html
def my_func(message):
    print('Got a message: {}'.format(message))

# 调用函数 my_func()
my_func('Hello World')
# 输出
Got a message: Hello World
```
其中：
- def 是函数的声明；
- my_func 是函数的名称；
- 括号里面的 message 则是函数的参数；
- 而 print 那行则是函数的主体部分，可以执行相应的语句；
- 在函数最后，你可以返回调用结果（return 或 yield），也可以不返回。  
  
总结一下，大概是下面的这种形式：
```angular2html
def name(param1, param2, ..., paramN):
    statements
    return/yield value # optional
```
- 和其他需要编译的语言（比如 C 语言）不一样的是，def 是可执行语句，这意味着函数直到被调用前，都是不存在的。当程序调用函数时，def 语句才会创建一个新的函数对象，并赋予其名字。
- 主程序调用函数时，必须保证这个函数此前已经定义过，不然就会报错
- 如果我们在函数内部调用其他函数，函数间哪个声明在前、哪个在后就无所谓，因为 def 是可执行语句，函数在调用之前都不存在，我们只需保证调用时，所需的函数都已经声明定义：
```angular2html
def my_func(message):
    my_sub_func(message) # 调用my_sub_func()在其声明之前不影响程序执行
    
def my_sub_func(message):
    print('Got a message: {}'.format(message))

my_func('hello world')

# 输出
Got a message: hello world
```
- Python 不用考虑输入的数据类型，而是将其交给具体的代码去判断执行
- 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。
- Python 函数的另一大特性，是 Python 支持函数的嵌套。所谓的函数嵌套，就是指函数里面又有函数
    ```angular2html
    def f1():
        print('hello')
        def f2():
            print('world')
        f2()
    f1()
    
    # 输出
    hello
    world
    ```
  函数的嵌套，主要有下面两个方面的作用。
  - 第一，函数的嵌套能够保证内部函数的隐私。内部函数只能被外部函数所调用和访问，不会暴露在全局作用域
  - 第二，合理的使用函数嵌套，能够提高程序的运行效率。
   
#### 空函数
如果想定义一个什么事也不做的空函数，可以用pass语句：
```angular2html
def nop():
    pass
```
pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。  
pass还可以用在其他语句里，比如：
```angular2html
if age >= 18:
    pass
```
缺少了pass，代码运行就会有语法错误。

#### 返回多个值
```angular2html
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

>>> x, y = move(100, 100, 60, math.pi / 6)
>>> print(x, y)
151.96152422706632 70.0
```
但其实这只是一种假象，Python函数返回的仍然是单一值：
```angular2html
>>> r = move(100, 100, 60, math.pi / 6)
>>> print(r)
(151.96152422706632, 70.0)
```
原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。


#### 参数传递
- **可更改(mutable)与不可更改(immutable)对象**  
    在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
    - 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
    - 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
    
    python 函数的参数传递：
    - 不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
    - 可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
    python 中一切都是对象，严格意义我们不能说值传递还是引用传递，**我们应该说传不可变对象和传可变对象。**  
      
- python 传不可变对象实例
    ```angular2html
    def change(a):
        print(id(a))   # 指向的是同一个对象
        a=10
        print(id(a))   # 一个新对象
     
    a=1
    print(id(a))
    change(a)
    # 输出
    4379369136
    4379369136
    4379369424
    ```
  可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），在函数内部修改形参后，形参指向的是不同的 id。
- 传可变对象实例
    ```angular2html
    # 可写函数说明
    def changeme( mylist ):
       "修改传入的列表"
       mylist.append([1,2,3,4])
       print ("函数内取值: ", mylist)
       return
     
    # 调用changeme函数
    mylist = [10,20,30]
    changeme( mylist )
    print ("函数外取值: ", mylist)
    
    # 输出：
    函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
    函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
    ```

#### 函数参数
1. 必需参数（位置参数）  
    调用 printme() 函数，你必须传入一个参数，不然会出现语法错误：
    ```angular2html
    def printme( str ): # 对于printme(str)函数，参数str就是一个位置参数。
       "打印任何传入的字符串"
       print (str)
       return
     
    # 调用 printme 函数，不加参数会报错
    printme()
    # 输出：
    Traceback (most recent call last):
      File "test.py", line 10, in <module>
        printme()
    TypeError: printme() missing 1 required positional argument: 'str'
    ```
2. 关键字参数  
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。  
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
    ```angular2html
    def printinfo( name, age ):
       "打印任何传入的字符串"
       print ("名字: ", name)
       print ("年龄: ", age)
       return
     
    #调用printinfo函数
    printinfo( age=50, name="runoob" )
    ```
   
3. 默认参数  
调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：
    ```angular2html
    def printinfo( name, age = 35 ):
       "打印任何传入的字符串"
       print ("名字: ", name)
       print ("年龄: ", age)
       return
     
    #调用printinfo函数
    printinfo( age=50, name="runoob" )
    print ("------------------------")
    printinfo( name="runoob" )
    ```
 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；  
二是如何设置默认参数。  
当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。  
使用默认参数有什么好处？最大的好处是能降低调用函数的难度。  
 **定义默认参数要牢记一点：默认参数必须指向不变对象！** 
```angular2html
def add_end(L=[]):
    L.append('END')
    return L
>>> add_end()
['END']
>>> add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']
```
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。  
要修改上面的例子，我们可以用None这个不变对象来实现：  
```angular2html
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```
现在，无论调用多少次，都不会有问题：
```angular2html
>>> add_end()
['END']
>>> add_end()
['END']
```

4. 不定长参数  
 4.1 基本语法如下：
    ```angular2html
    def functionname([formal_args,] *var_args_tuple ):
       "函数_文档字符串"
       function_suite
       return [expression]
    ```
   **加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。**    
示例：
    ```angular2html
    def printinfo( arg1, *vartuple ):
       "打印任何传入的参数"
       print ("输出: ")
       print (arg1)
       print (vartuple)
     
    # 调用printinfo 函数
    printinfo( 70, 60, 50 )
    # 输出：
    70
    (60, 50)
    ```
   4.2 如果在函数调用时没有给可变参数指定参数，它就是一个**空元组**。我们也可以不向函数传递未命名的变量。如下实例：  
    ```angular2html
    def printinfo( arg1, *vartuple ):
       "打印任何传入的参数"
       print ("输出: ")
       print (arg1)
       for var in vartuple:
          print (var)
       return
     
    # 调用printinfo 函数
    printinfo( 10 )
    # 输出：
    10
    printinfo( 70, 60, 50 )
    # 输出:
    70
    60
    50
    ```
    4.3 如果已经有一个list或者tuple，要调用一个可变参数怎么办？
    ```angular2html
    def calc(*numbers):
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum
   
    >>> nums = [1, 2, 3]
    >>> calc(nums[0], nums[1], nums[2])
    14
    ```
    这种写法当然是可行的，问题是太繁琐，所以**Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：**  
    ```angular2html
    >>> nums = [1, 2, 3]
    >>> calc(*nums)
    14
    ```
    4.4 声明函数时，参数中星号 * 可以单独出现，例如:  
    ```angular2html
    def f(a,b,*,c):
        return a+b+c
    ```
    如果单独出现星号 * 后的参数必须用关键字传入。
    ```angular2html
    >>> def f(a,b,*,c):
    ...     return a+b+c
    ... 
    >>> f(1,2,3)   # 报错
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: f() takes 2 positional arguments but 3 were given
    >>> f(1,2,c=3) # 正常
    6
    >>>
    ```
   
5. 还有一种就是参数带两个星号 **基本语法如下：
    ```angular2html
    def functionname([formal_args,] **var_args_dict ):
       "函数_文档字符串"
       function_suite
       return [expression]
    ```
   加了两个星号 ** 的参数会以字典的形式导入。
    ```angular2html
    def printinfo( arg1, **vardict ):
       "打印任何传入的参数"
       print ("输出: ")
       print (arg1)
       print (vardict)
     
    # 调用printinfo 函数
    printinfo(1, a=2,b=3)
    ```
    以上实例输出结果：
    ```angular2html
    输出: 
    1
    {'a': 2, 'b': 3}
    ```
6. 强制位置参数
Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。  
在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参:  
    ```angular2html
    def f(a, b, /, c, d, *, e, f):
        print(a, b, c, d, e, f)
    ```   
    以下使用方法是正确的:
    ```angular2html
    f(10, 20, 30, d=40, e=50, f=60)
    ```
    以下使用方法会发生错误:
    ```angular2html
    f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
    f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式
    ```
7. 参数组合
    ```angular2html
    def f1(a, b, c=0, *args, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
    
    def f2(a, b, c=0, *, d, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    ```
    在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
    ```angular2html
    >>> f1(1, 2)
    a = 1 b = 2 c = 0 args = () kw = {}
    >>> f1(1, 2, c=3)
    a = 1 b = 2 c = 3 args = () kw = {}
    >>> f1(1, 2, 3, 'a', 'b')
    a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
    >>> f1(1, 2, 3, 'a', 'b', x=99)
    a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
    >>> f2(1, 2, d=99, ext=None)
    a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
    ```
   最神奇的是通过一个tuple和dict，你也可以调用上述函数：
    ```angular2html
    >>> args = (1, 2, 3, 4)
    >>> kw = {'d': 99, 'x': '#'}
    >>> f1(*args, **kw)
    a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
    >>> args = (1, 2, 3)
    >>> kw = {'d': 88, 'x': '#'}
    >>> f2(*args, **kw)
    a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
    ```
    所以，对于任意函数，都可以通过类似**func(\*args, \*\*kw)** 的形式调用它，无论它的参数是如何定义的。



#### 函数变量作用域
- Python 函数中变量的作用域和其他语言类似。如果变量是在函数内部定义的，就称为局部变量，只在函数内部有效。一旦函数执行完毕，局部变量就会被回收，无法访问，比如下面的例子：
    ```angular2html
    def read_text_from_file(file_path):
        with open(file_path) as file:
            ...
    ```
  我们在函数内部定义了 file 这个变量，这个变量只在 read_text_from_file 这个函数里有效，在函数外部则无法访问。

- 全局变量则是定义在整个文件层次上的，比如下面这段代码：
    ```angular2html
    MIN_VALUE = 1
    MAX_VALUE = 10
    def validation_check(value):
        if value < MIN_VALUE or value > MAX_VALUE:
            raise Exception('validation check fails')
    ```
  这里的 MIN_VALUE 和 MAX_VALUE 就是全局变量，可以在文件内的任何地方被访问，当然在函数内部也是可以的。
- 我们不能在函数内部随意改变全局变量的值。比如，下面的写法就是错误的：
    ```angular2html
    MIN_VALUE = 1
    MAX_VALUE = 10
    def validation_check(value):
        ...
        MIN_VALUE += 1
        ...
    validation_check(5)
    ```
  如果运行这段代码，程序便会报错：
    ```angular2html
    UnboundLocalError: local variable 'MIN_VALUE' referenced before assignment
    ```
  这是因为，**Python 的解释器会默认函数内部的变量为局部变量，但是又发现局部变量 MIN_VALUE 并没有声明，因此就无法执行相关操作。所以，如果我们一定要在函数内部改变全局变量的值，就必须加上 global 这个声明：**
    ```angular2html
    MIN_VALUE = 1
    MAX_VALUE = 10
    def validation_check(value):
        global MIN_VALUE
        ...
        MIN_VALUE += 1
        ...
    validation_check(5)
    ```
  这里的 global 关键字，并不表示重新创建了一个全局变量 MIN_VALUE，而是告诉 Python 解释器，函数内部的变量 MIN_VALUE，就是之前定义的全局变量，并不是新的全局变量，也不是局部变量。这样，程序就可以在函数内部访问全局变量，并修改它的值了。
- 如果遇到函数内部局部变量和全局变量同名的情况，那么在函数内部，局部变量会覆盖全局变量，比如下面这种：
    ```angular2html
    MIN_VALUE = 1
    MAX_VALUE = 10
    def validation_check(value):
        MIN_VALUE = 3
        ...
    ```
    在函数 validation_check() 内部，我们定义了和全局变量同名的局部变量 MIN_VALUE，那么，MIN_VALUE 在函数内部的值，就应该是 3 而不是 1 了。
- 类似的，对于嵌套函数来说，内部函数可以访问外部函数定义的变量，但是无法修改，若要修改，必须加上 nonlocal 这个关键字：
    ```angular2html
    def outer():
        x = "local"
        def inner():
            nonlocal x # nonlocal关键字表示这里的x就是外部函数outer定义的变量x
            x = 'nonlocal'
            print("inner:", x)
        inner()
        print("outer:", x)
    outer()
    # 输出
    inner: nonlocal
    outer: nonlocal
    ```
  如果不加上 nonlocal 这个关键字，而内部函数的变量又和外部函数变量同名，那么同样的，内部函数变量会覆盖外部函数的变量。
    ```angular2html
    def outer():
        x = "local"
        def inner():
            x = 'nonlocal' # 这里的x是inner这个函数的局部变量
            print("inner:", x)
        inner()
        print("outer:", x)
    outer()
    # 输出
    inner: nonlocal
    outer: local
    ```
  
#### 闭包
闭包其实和刚刚讲的嵌套函数类似，不同的是，**这里外部函数返回的是一个函数，而不是一个具体的值。** 返回的函数通常赋于一个变量，这个变量可以在后面被继续执行调用。
```angular2html
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of # 返回值是exponent_of函数

square = nth_power(2) # 计算一个数的平方
cube = nth_power(3) # 计算一个数的立方 
square
# 输出
<function __main__.nth_power.<locals>.exponent(base)>

cube
# 输出
<function __main__.nth_power.<locals>.exponent(base)>

print(square(2))  # 计算2的平方
print(cube(2)) # 计算2的立方
# 输出
4 # 2^2
8 # 2^3
```
- 使用闭包的一个原因，是让程序变得更简洁易读。
- 和上面讲到的嵌套函数优点类似，函数开头需要做一些额外工作，而你又需要多次调用这个函数时，将那些额外工作的代码放在外部函数，就可以减少多次调用导致的不必要的开销，提高程序的运行效率。
- 另外还有一点，我们后面会讲到，闭包常常和装饰器（decorator）一起使用。

我们来看一个例子：
```
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
```
在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。  
你可能认为调用`f1()`，`f2()`和`f3()`结果应该是`1`，`4`，`9`，但实际结果是：
```angular2html
>>> f1()
9
>>> f2()
9
>>> f3()
9
```
全部都是`9`！原因就在于返回的函数引用了变量`i`，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量`i`已经变成了`3`，因此最终结果为`9`。  
**返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。**  
如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
```angular2html
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
```
再看结果：
```angular2html
>>> f1, f2, f3 = count()
>>> f1()
1
>>> f2()
4
>>> f3()
9
```
缺点是代码较长，可利用lambda函数缩短代码。

#### 实例
目标
```angular2html
def count():
    fs = []
    for i in range(1, 4):
        def f(i): return lambda: i * i
        fs.append(f(i))
    return fs
```

原始
```angular2html
def mycount():
    fs = []
    for i in range(1, 4):
        fs.append(lambda: i * i)
    return fs
```
以上造成错误答案，自然是因为调用 fs 诸项时 i 已迭代完了，旧值不再能找到。

变奏一
```angular2html
def mycount1():
    fs = []
    for i in range(1, 4):
        def f(): return i * i
        fs.append(f)
    return fs
```
以上就只是简单地把匿名函数展开。

变奏二
```angular2html
def mycount2():
    fs = []
    for i in range(1, 4):
        def f(): return lambda: i * i
        fs.append(f())
    return fs
```
以上是更简单的代换。但是泛函编程要注意 f 和 f() 的区别。

变奏三
```angular2html
def mycount3():
    fs = []
    for i in range(1, 4):
        def f(j): return lambda: i * i
        fs.append(f(i))
    return fs
```
以上和目标仅差一个字符，即形式参数故意从 i 改成 j 。但运行时以上三种变奏则和原始函数没有任何区别——错都能错成一样。  
变奏三和目标的这一字之差就能说明用实际参数保存循环变量旧值的重要性。  

目标的变奏
```angular2html
def count2():
    fs = []
    for i in range(1, 4):
        fs.append((lambda x: lambda: x * x)(i))
    return fs
```
以上使用匿名函数，进一步提炼出实际参数的重要性。

#### 测试
利用闭包返回一个计数器函数，每次调用它返回递增整数：  
```angular2html

def createCounter():
    def counter():
        return 1
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
```

解答：  
```angular2html
>>> def createCounter():
...     f = [0]
...     print('闭包外--')
...     def counter():
...         print('闭包内--')
...         f[0] = f[0] + 1
...         return f[0]
...     return counter
...
>>> counterA = createCounter()
闭包外--
>>> print(counterA(), counterA(), counterA(), counterA(), counterA())
闭包内--
闭包内--
闭包内--
闭包内--
闭包内--
1 2 3 4 5
```