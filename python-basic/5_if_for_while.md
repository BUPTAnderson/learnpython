#### 条件语句
```angular2html

if condition_1:
    statement_1
elif condition_2:
    statement_2
...
elif condition_i:
    statement_i
else:
    statement_n
```
**注意：**
- 和其他语言不一样，我们不能在条件语句中加括号，写成下面这样的格式。`if (x < 0)`
- Python 不支持 switch 语句
- if 语句是可以单独使用的，但 elif、else 都必须和 if 成对使用。
- 一切皆Bool：  

    |  数据类型   | 结果  |
    |  ----  | ----  |
    |  String  | 空字符串解析为False，其余为True  |
    |  Int  | 0解析为False，其余为True  |
    |  Bool  | True为True，False为False  |
    |  list/tuple/dict/set  | Iterable为空解析为False，其余为True  |
    |  Object  | Node解析为False，其余为True|
    不过，切记，在实际写代码时，我们鼓励，除了 boolean 类型的数据，条件判断最好是显性的。比如，在判断一个整型数是否为 0 时，我们最好写出判断的条件：  
    `if i != 0:`而不是只写变量名：`if i:`
  
#### 循环语句
1. Python 中的数据结构只要是可迭代的（iterable），比如列表、集合等等，那么都可以通过下面这种方式遍历：
    ```angular2html
    for item in <iterable>:
        ...
    ```
2. 这里需要单独强调一下字典。字典本身只有键是可迭代的，如果我们要遍历它的值或者是键值对，就需要通过其内置的函数 values() 或者 items() 实现。其中，values() 返回字典的值的集合，items() 返回键值对的集合。
    ```angular2html
    
    d = {'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}
    for k in d: # 遍历字典的键
        print(k)
    name
    dob
    gender
    
    for v in d.values(): # 遍历字典的值
        print(v)
    jason
    2000-01-01
    male    
    
    for k, v in d.items(): # 遍历字典的键值对
        print('key: {}, value: {}'.format(k, v))
    key: name, value: jason
    key: dob, value: 2000-01-01
    key: gender, value: male 
    ```
   
3. 有没有办法通过集合中的索引来遍历元素呢？当然可以，其实这种情况在实际工作中还是很常见的，甚至很多时候，我们还得根据索引来做一些条件判断。我们通常通过 range() 这个函数，拿到索引，再去遍历访问集合中的元素。
    ```angular2html
    l = [1, 2, 3, 4, 5, 6, 7]
    for index in range(0, len(l)):
        if index < 5:
            print(l[index])        
            
    1
    2
    3
    4
    5
    ```
   当我们同时需要索引和元素时，还有一种更简洁的方式，那就是通过 Python 内置的函数 enumerate()。用它来遍历集合，不仅返回每个元素，并且还返回其对应的索引，这样一来，上面的例子就可以写成:
    ```angular2html
    l = [1, 2, 3, 4, 5, 6, 7]
    for index, item in enumerate(l):
        if index < 5:
            print(item)  
                  
    1
    2
    3
    4
    5
    ```
   
4. while循环，它表示当 condition 满足时，一直重复循环内部的操作，直到 condition 不再满足，就跳出循环体。
    ```angular2html
    
    while condition:
        ....
    ```
   **while与for区别：**  
   - 如果你只是遍历一个已知的集合，找出满足条件的元素，并进行相应的操作，那么使用 for 循环更加简洁。但如果你需要在满足某个条件前，不停地重复某些操作，并且没有特定的集合需要去遍历，那么一般则会使用 while 循环。
   - for 循环和 while 循环的效率问题。比如：
        ```angular2html
        i = 0
        while i < 1000000:
            i += 1
        ```
     和等价的for循环：
        ```angular2html
    
        for i in range(0, 1000000):
            pass
        ```
     要知道，range() 函数是直接由 C 语言写的，调用它速度非常快。而 while 循环中的“i += 1”这个操作，得通过 Python 的解释器间接调用底层的 C 语言；并且这个简单的操作，又涉及到了对象的创建和删除（因为 i 是整型，是 immutable，i += 1 相当于 i = new int(i + 1)）。所以，显然，for 循环的效率更胜一筹。
    

5. 条件与循环的复用  
在阅读代码的时候，你应该常常会发现，有很多将条件与循环并做一行的操作，例如：
    ```angular2html
    expression1 if condition else expression2 for item in iterable
    ```
    将这个表达式分解开来，其实就等同于下面这样的嵌套结构：
   ```angular2html
    for item in iterable:
        if condition:
            expression1
        else:
            expression2
    ```
   而如果没有 else 语句，则需要写成：`expression for item in iterable if condition`  
   **实际就是所谓的列表推导式：** `[表达式 for 迭代变量 in 可迭代对象 [if 条件表达式] ]` 见(9_generator.py)
   举个例子，比如我们要绘制 y = 2*|x| + 5 的函数图像，给定集合 x 的数据点，需要计算出 y 的数据集合，那么只用一行代码，就可以很轻松地解决问题了：
   ```angular2html
    y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]
   ```
   再比如我们在处理文件中的字符串时，常常遇到的一个场景：将文件中逐行读取的一个完整语句，按逗号分割单词，去掉首位的空字符，并过滤掉长度小于等于 3 的单词，最后返回由单词组成的列表。这同样可以简洁地表达成一行：
    ```angular2html
    text = ' Today, is, Sunday'
    text_list = [s.strip() for s in text.split(',') if len(s.strip()) > 3]
    print(text_list)
    ['Today', 'Sunday']
    ```
   当然，这样的复用并不仅仅局限于一个循环。比如，给定两个列表 x、y，要求返回 x、y 中所有元素对组成的元组，相等情况除外。那么，你也可以很容易表示出来：
    ```angular2html
    [(xx, yy) for xx in x for yy in y if xx != yy]
    ```
   这样的写法就等价于：
    ```angular2html
    l = []
    for xx in x:
        for yy in y:
            if xx != yy:
                l.append((xx, yy))
    ```
   列表生成式也可以使用两个变量来生成list：
    ```angular2html
    >>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
    >>> [k + '=' + v for k, v in d.items()]
    ['y=B', 'x=A', 'z=C']
    ```
   
#### 思考
给定下面两个列表 attributes 和 values，要求针对 values 中每一组子列表 value，输出其和 attributes 中的键对应后的字典，最后返回字典组成的列表。
```angular2html

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], 
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

# expected output:
[{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}, 
{'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'}, 
{'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]
```
解答：
```angular2html
[dict(zip(attributed, v)) for v in values]
```
zip 语法：`zip([iterable, ...])`  
作用：zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
示例：
```angular2html
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a, b, c)
list(zipped)
[(1, 4, 4), (2, 5, 5), (3, 6, 6)]
list(zipped) # 注意，上面的list(zipped)执行完后zipped对象为空了
[]
```

