### 数据类型
![](../resources/type.png)

Python3 中有六个标准的数据类型：
- Number（数字）：a = 111
- String（字符串）：str = 'Runoob'
- List（列表）：list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
- Tuple（元组）：可以看作不可变List，tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
- Set（集合）：sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
- Dictionary（字典）：tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

Python3 的六个标准数据类型中：

- 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
- 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

- 序列对象（3个）：String（字符串）、List（列表）、Tuple（元组）

### 列表和数组
- 列表对应类是list, 元组对应的类是tuple(可以直接查看类包含的内置函数)
#### 1. 创建
- 构造包含 0 或 1 个元素的元组的特殊语法规则。
```
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号，否则括号会被当作运算符使用：
区别：区别主要在于list()是一个function call，Python的function call会创建stack，并且进行一系列参数检查的操作，比较expensive，反观[]是一个内置的C函数，可以直接被调用，因此效率高。
```
- 构造空的列表
```angular2html
# 创建空列表
# option A
empty_list = list()

# option B
empty_list = [] # 效率更高

# 区别主要在于list()是一个function call，Python的function call会创建stack，并且进行一系列参数检查的操作，比较expensive，反观[]是一个内置的C函数，可以直接被调用，因此效率高。
```  
- 列表和元组都可以随意嵌套
```
l = [[1, 2, 3], [4, 5]] # 列表的每一个元素也是一个列表
tup = ((1, 2, 3), (4, 5, 6)) # 元组的每一个元素也是一个元组
```  
- 两者也可以通过 list() 和 tuple() 函数相互转换：
```
list((1, 2, 3))
[1, 2, 3]

tuple([1, 2, 3])
(1, 2, 3)
```

#### 2. 访问
下标访问, 可以直接通过下面索引访问，也可以通过index()方法获取元素的下标。
```angular2html
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( list[0] )
print( list[-1] )
print( list[0：4] ) # 结果还是列表
tup1 = ('Google', 'Runoob', 1997, 2000)
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5]) # 结果还是元组
```
#### 3. 更新/修改
列表可以直接通过下标修改，也可以使用append(), insert() 方法来添加列表项
```angular2html
list = ['Google', 'Runoob', 1997, 2000]
list[1] = 2001 # 将'Runoob'更新为2001
list.append('Baidu') # list最后增加'Baidu'
list.insert(0, 'Ali') # 在索引为0的地方插入'Ali'
```
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合(实际创建了新的元组)
```angular2html
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
tup3 = tup1 + tup2
```
#### 4. 删除
可以使用 del 语句来删除列表的的元素
```angular2html
list = ['Google', 'Runoob', 1997, 2000]
del list[2]
```
可以使用 remove()方法来删除列表的的元素
```angular2html
list = ['Google', 'Runoob', 1997, 2000]
list.remove(2000)
```
可以使用clear()方法来清空列表
```angular2html
list = ['Google', 'Runoob', 1997, 2000]
list.clear()
```
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
```angular2html
tup = ('Google', 'Runoob', 1997, 2000)
del tup # 删除后tup就不存在了，访问会报错
print(tup)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tup' is not defined
```

#### 5. 其它操作

|  Python 表达式   | 结果  | 描述  |
|  ----  | ----  | ----  |
| len([1, 2, 3])  | 3 | 长度 |
| len((1, 2, 3))  | 3 | 计算元素个数 |
| max([1, 2, 3])  | 3 | 最大值 |
| max((1, 2, 3))  | 3 | 最大值 |
| min([1, 2, 3])  | 1 | 最小值 |
| min((1, 2, 3))  | 1 | 最小值 |
| [1, 2, 3].index(2)  | 1 | 从列表中找出某个值第一个匹配项的索引位置 |
| (1, 2, 3).index(2)  | 1 | 从元组中找出某个值第一个匹配项的索引位置 |
| [1, 2, 3, 2].count(2)  | 2 | 统计某个元素在列表中出现的次数 |
| (1, 2, 3, 2).count(2)  | 2 | 统计某个元素在元组中出现的次数 |
| [1, 2, 3] + [4, 5, 6]  | [1, 2, 3, 4, 5, 6] | 组合 |
| (1, 2, 3) + (4, 5, 6)  | (1, 2, 3, 4, 5, 6) | 连接 |
| ['Hi!'] * 4  | ['Hi!', 'Hi!', 'Hi!', 'Hi!'] | 重复 |
| ('Hi!',) * 4  | ('Hi!', 'Hi!', 'Hi!', 'Hi!') | 复制 |
| 3 in [1, 2, 3]  | True | 元素是否存在于列表中 |
| 3 in (1, 2, 3)  | True | 元素是否存在 |
| for x in [1, 2, 3]: print(x, end=" ")  | 1 2 3 | 迭代 |
| for x in (1, 2, 3): print (x,)  | 1 2 3 | 迭代 |
| list( (1, 2, 3) )  | [1, 2, 3] | 将可迭代系列转化为列表 |
| tuple( [1, 2, 3] )  | (1, 2, 3) | 将可迭代系列转化为元组 |



**注意：**
- insert() remove() reverse() clear() copy() 都是列表有的方法，元组没有
- 列表和元组，都是一个可以放置任意数据类型的有序集合。 
- 列表是动态的，长度大小不固定，可以随意地增加、删减或者改变元素（mutable）。
- 而元组是静态的，长度大小固定，无法增加删减或者改变（immutable）。


#### 列表和元祖常用的内置函数
```

l = [3, 2, 3, 7, 8, 1]
l.count(3) 
2
l.index(7)
3
l.reverse() # void函数，l发生了变化
l
[1, 8, 7, 3, 2, 3]
l.sort() # void函数，l发生了变化
l
[1, 2, 3, 3, 7, 8]

tup = (3, 2, 3, 7, 8, 1)
tup.count(3)
2
tup.index(7)
3
list(reversed(tup)) # tup不变
[1, 8, 7, 3, 2, 3]
sorted(tup)  # tup不变
[1, 2, 3, 3, 7, 8]
```
- count(item) 表示统计列表 / 元组中 item 出现的次数。
- index(item) 表示返回列表 / 元组中 item 第一次出现的索引。 
- list.reverse() 和 list.sort() 分别表示原地倒转列表和排序（注意，元组没有内置的这两个函数)。
- reversed() 和 sorted() 同样表示对列表 / 元组进行倒转和排序，reversed() 返回一个倒转后的迭代器（上文例子使用 list() 函数再将其转换为列表）；sorted() 返回排好序的新列表。
- 列表的存储空间略大于元组，元组的性能速度要略优于列表。
- list和tuple的内部实现，里边是linked list 还是array，还是把array linked一下这种。
```angular2html
list和tuple的内部实现都是array的形式，list因为可变，所以是一个over-allocate的array，tuple因为不可变，所以长度大小固定。具体可以参照源码
list: https://github.com/python/cpython/blob/master/Objects/listobject.c.
tuple: https://github.com/python/cpython/blob/master/Objects/tupleobject.c
```




#### isinstance 和 type 的区别在于：
- type()不会认为子类是一种父类类型。
- isinstance()会认为子类是一种父类类型。
```angular2html
from collections import Iterable
isinstance('abc', Iterable)
```
- isinstance可以接收多个类型
```angular2html
>>> isinstance('a', (str, unicode))
True
>>> isinstance(u'a', (str, unicode))
True
```

type(B()) == A

### id 与 is 与 == 区别：
- id()：获取的是对象在内存中的地址(不是变量/引用的地址)
- is 比对2个变量的对象引用（对象在内存中的地址。即id() 获得的值）是否同样。假设同样则返回True。否则返回False。换句话说，就是比对2个变量的对象引用是否指向同一个对象。
- == 比对2个变量指向的对象的内容是否同样。