#### 匿名函数基础
以下是匿名函数的格式：
```angular2html
lambda argument1, argument2,... argumentN : expression
```
示例：
```angular2html
square = lambda x: x**2
square(3)

9
```
匿名函数 lambda 和常规函数一样，返回的都是一个函数对象（function object），它们的用法也极其相似，不过还是有下面几点区别。
- 第一，lambda 是一个表达式（expression），并不是一个语句（statement）。不用写`return`，返回值就是该表达式的结果。
  - 所谓的表达式，就是用一系列“公式”去表达一个东西，比如x + 2、 x**2等等；
  - 而所谓的语句，则一定是完成了某些功能，比如赋值语句x = 1完成了赋值，print 语句print(x)完成了打印，条件语句 if x < 0:完成了选择功能等等。  
    
  因此，lambda 可以用在一些常规函数 def 不能用的地方，比如，lambda 可以用在列表内部，而常规函数却不能：
    ```angular2html
    [(lambda x: x*x)(x) for x in range(10)] # 这里的lambda里面的x参数和外面的for用的x是2个不同的意思，可能这样表述会清晰一些？ [(lambda x : x*x)(y) for y in range(10)]
    # 输出
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```
  再比如，lambda 可以被用作某些函数的参数，而常规函数 def 也不能：
    ```angular2html
    l = [(1, 20), (3, 0), (9, 10), (2, -1)]
    l.sort(key=lambda x: x[1]) # 按列表中元组的第二个元素排序
    print(l)
    # 输出
    [(2, -1), (3, 0), (9, 10), (1, 20)]
    ```
  常规函数 def 必须通过其函数名被调用，因此必须首先被定义。但是作为一个表达式的 lambda，返回的函数对象就不需要名字了。

- 第二，lambda 的主体是只有一行的简单表达式，并不能扩展成一个多行的代码块。  
这其实是出于设计的考虑。Python 之所以发明 lambda，就是为了让它和常规函数各司其职：lambda 专注于简单的任务，而常规函数则负责更复杂的多行逻辑。关于这点，Python 之父 Guido van Rossum 曾发了一篇 [文章](https://www.artima.com/weblogs/viewpost.jsp?thread=147358) 解释，你有兴趣的话可以自己阅读。
  

#### 为什么要使用匿名函数？
- 减少代码的重复性；  
  试想一下这样的情况。你需要一个函数，但它非常简短，只需要一行就能完成；同时它在程序中只被调用一次而已。那么请问，你还需要像常规函数一样，给它一个定义和名字吗？答案当然是否定的。这种情况下，函数就可以是匿名的，你只需要在适当的地方定义并使用，就能让匿名函数发挥作用了。  
  举个例子，如果你想对一个列表中的所有元素做平方操作，而这个操作在你的程序中只需要进行一次，用 lambda 函数可以表示成下面这样：  
    ```angular2html
    squared = map(lambda x: x**2, [1, 2, 3, 4, 5])
    ```
- 模块化代码。


#### Python 函数式编程
所谓函数式编程，是指代码中每一块都是不可变的（immutable），都由纯函数（pure function）的形式组成。这里的纯函数，是指函数本身相互独立、互不影响，对于相同的输入，总会有相同的输出，没有任何副作用。  
举个很简单的例子，比如对于一个列表，我想让列表中的元素值都变为原来的两倍，我们可以写成下面的形式：
```angular2html
def multiply_2(l):
    for index in range(0, len(l)):
        l[index] *= 2
    return l
```
这段代码就不是一个纯函数的形式，因为列表中元素的值被改变了，如果我多次调用 multiply_2() 这个函数，那么每次得到的结果都不一样。要想让它成为一个纯函数的形式，就得写成下面这种形式，重新创建一个新的列表并返回。
```angular2html
def multiply_2_pure(l):
    new_list = []
    for item in l:
        new_list.append(item * 2)
    return new_list
```
**函数式编程的优点，主要在于其纯函数和不可变的特性使程序更加健壮，易于调试（debug）和测试；缺点主要在于限制多，难写。**  
**Python 主要提供了这么几个函数：map()、filter() 和 reduce()，通常结合匿名函数 lambda 一起使用。**
- **map(function, iterable)** 函数，它表示，对 iterable 中的每个元素，都运用 function 这个函数，最后返回一个新的可遍历的集合。
```angular2html
l = [1, 2, 3, 4, 5]
new_list = list(map(lambda x: x * 2, l)) # [2， 4， 6， 8， 10]
```
因为 map() 函数直接由 C 语言写的，运行时不需要通过 Python 解释器间接调用，并且内部做了诸多优化，所以运行速度快。
- **filter(function, iterable)** 函数，它和 map 函数类似，function 同样表示一个函数对象。filter() 函数表示对 iterable 中的每个元素，都使用 function 判断，并返回 True 或者 False，最后将返回 True 的元素组成一个新的可遍历的集合。
```angular2html
l = [1, 2, 3, 4, 5]
new_list = list(filter(lambda x: x % 2 == 0, l)) # [2, 4]
```
- **reduce(function, iterable)** 函数，它通常用来对一个集合做一些累积操作。function 同样是一个函数对象，规定它有两个参数，表示对 iterable 中的每个元素以及上一次调用后的结果，运用 function 进行计算，所以最后返回的是一个单独的数值。
```angular2html
from functools import reduce # reduce函数需要引入
l = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, l) # 1*2*3*4*5 = 120
```
**map, filter返回的是map和filter对象，map和filter对象是Iterator子类, reduce返回的是一个对象(值)**
通常来说，在我们想对集合中的元素进行一些操作时，如果操作非常简单，比如相加、累积这种，那么我们优先考虑 map()、filter()、reduce() 这类或者 list comprehension（列表推导式） 的形式。至于这两种方式的选择：
- 在数据量非常多的情况下，比如机器学习的应用，那我们一般更倾向于函数式编程的表示，因为效率更高；
- 在数据量不多的情况下，并且你想要程序更加 Pythonic 的话，那么 list comprehension 也不失为一个好选择。
  
不过，如果你要对集合中的元素，做一些比较复杂的操作，那么，考虑到代码的可读性，我们通常会使用 for 循环，这样更加清晰明了。

**map()，filter() 和 reduce() 三个函数，与其他形式（for 循环，comprehension）的性能相比，函数式编程的性能效率是最优的。**
```angular2html
>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> def char2num(s):
...     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
...     return digits[s]
...
>>> reduce(fn, map(char2num, '13579'))
13579
```

#### 思考
如果让你对一个字典，根据值进行由高到底的排序，该怎么做呢？以下面这段代码为例，你可以思考一下。
```angular2html
d = {'mike': 10, 'lucy': 2, 'ben': 30}
```
解答：
```angular2html
sorted(d.items(), key = lambda x : x[1], reverse = True)
```