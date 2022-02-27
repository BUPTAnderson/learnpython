### 字典和集合
#### 基础
- 字典是一系列由键（key）和值（value）配对组成的元素的集合，在 Python3.7+，字典被确定为有序。相比于列表和元组，字典的性能更优，特别是对于查找、添加和删除操作，字典都能在常数时间复杂度内完成。
  `python3.7后字典变成有序，python3.5之前，创建字典保存：hash(key)，key的内存地址， value的内存地址 3个值来保存一个键值对，因此底层是一个二维数组，各个键值对存放的位置由hash(key)取余后得出，因此存放位置不是按顺序的。 python3.7之后，字典底层是2个数组，一个为一维数组，存放hash(key)取余后的值作为数组的索引，对应索引位置存放键值对在二维数组的索引位置。因此二维数组是一个有序的数组。`
- 集合和字典基本相同，唯一的区别，就是集合没有键和值的配对，是一系列无序的、唯一的元素组合。
- 字典对应类是dict，集合对应类是set(可以直接查看类对应的内置函数)
#### 1. 创建
- 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：  
```
d = {key1 : value1, key2 : value2, key3 : value3 }
d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male') 
d1 == d2 == d3 ==d4
True
```
- 创建空字典使用{}
- 使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。  
```angular2html
parame = {value01,value02,...}
或者
set(value) # 注意set函数只能传入一个元素
s1 = {1, 2, 3}
s2 = set([1, 2, 3])
s1 == s2
True
```
**注意:** 
- Python 中字典和集合，无论是键还是值，都可以是混合类型。比如下面这个例子，我创建了一个元素为1，'hello'，5.0的集合：<br/>
`s = {1, 'hello', 5.0}`
- 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行 
#### 2. 访问
- 字典访问可以直接索引键，如果不存在，就会抛出异常
```angular2html
d = {'name': 'jason', 'age': 20}
d['name'] # 类似列表访问方式，以key作为访问的索引
'jason'
d['location'] # 不存在会报错
Traceback (most recent call last): 
  File "", line 1, in <module>
KeyError: 'location'
```
- 也可以使用 get(key, default) 函数来进行索引。如果键不存在，调用 get() 函数可以返回一个默认值。比如下面这个示例，返回了'null'。
```angular2html
d = {'name': 'jason', 'age': 20}
d.get('name')
'jason'
d.get('location', 'null')
'null'
```
- **集合并不支持索引操作，因为集合本质上是一个哈希表，和列表不一样。所以，下面这样的操作是错误的，Python 会抛出异常：**
```angular2html
s = {1, 2, 3}
s[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
```
- 想要判断一个元素在不在字典或集合内，我们可以用 value in dict/set 来判断。
```angular2html

s = {1, 2, 3}
1 in s
True
10 in s
False

d = {'name': 'jason', 'age': 20}
'name' in d
True
'location' in d
False
```
#### 3. 增加/更新
```angular2html
d = {'name': 'jason', 'age': 20}
d['dob'] = '1999-02-01' # 增加元素对'dob': '1999-02-01'
d['dob'] = '1998-01-01' # 更新键'dob'对应的值
s = {1, 2, 3}
s.add(4) # 增加元素4到集合, 如果元素已存在，则不进行任何操作。
```

还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
`s.update( x )`
```angular2html
a = {'one': 1, 'two': 2, 'three': 3}
a.update({'one':4.5, 'four': 9.3})
print(a)
{'one': 4.5, 'two': 2, 'three': 3, 'four': 9.3} # 于被更新的 dict 中已包含 key 为“one”的键值对，因此更新时该键值对的 value 将被改写；但如果被更新的 dict 中不包含 key 为“four”的键值对，那么更新时就会为原字典增加一个键值对。

x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
x.update(y) 
print(x)
{'banana', 'apple', 'google', 'runoob', 'cherry'} # 合并两个集合，重复元素只会出现一次
```

#### 4. 删除
- 字典没有remove()内置方法，集合有remove()方法
```angular2html
d = {'name': 'jason', 'age': 20, 'gender': 'male', 'dob': '1999-02-01'}
d.pop('dob') # 删除键为'dob'的元素对, 返回'dob'对应的value值
d.popitem() # 删除并返回字典中的最后一对键和值(返回的类型是tuple类型)
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
del dict         # 删除字典

s = {1, 2, 3， 4}
s.remove(4) # 从集合中删除元素4 # 不存在会发生错误
s.pop() # 随机删除集合中的一个元素
s.clear() # 情况集合
```
- 对于集合，还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：`s.discard( x )`
```angular2html
>>> thisset = set(("Google", "Runoob", "Taobao"))
>>> thisset.discard("Facebook")  # 不存在不会发生错误
>>> print(thisset)
{'Taobao', 'Google', 'Runoob'}
```
- 对于集合，集合的 pop 方法会将这个无序排列集合的左面第一个元素进行删除。

#### 5. 内置函数

可以分别查看类dict和set来查看字典和集合的内置函数
|  Python 表达式   | 结果  | 描述  |
|  ----  | ----  | ----  |
| len(dict/set)  | 元素个数 | 计算字典元素个数，即键的总数。 |
| str(dict)  | 字典的字符串形式 | 输出字典，以可打印的字符串表示。 |

- key in dict 如果键在字典dict里返回true，否则返回false
- key in set  判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。

#### 6. 字典和集合的工作原理
字典和集合的内部结构都是一张哈希表。为了提高存储空间的利用率，现在的哈希表除了字典本身的结构，会把索引和哈希值、键、值单独分开，也就是下面这样新的结构：
```angular2html

Indices
----------------------------------------------------
None | index | None | None | index | None | index ...
----------------------------------------------------

Entries
--------------------
hash0   key0  value0
---------------------
hash1   key1  value1
---------------------
hash2   key2  value2
---------------------
        ...
---------------------
```
示例：
```angular2html
{'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'}
# 存储形式：

indices = [None, 1, None, None, 0, None, 2]
entries = [
[1231236123, 'name', 'mike'],
[-230273521, 'dob', '1999-01-01'],
[9371539127, 'gender', 'male']
]
```
- 插入操作  
每次向字典或集合插入一个元素时，Python 会首先计算键的哈希值（hash(key)），这个hash值是indices的下标。  
再和 mask = PyDicMinSize - 1 做与操作（PyDicMinSize是entries的长度，比如8， 则mask是111），计算这个元素应该插入哈希表的位置 index = hash(key) & mask （index是entries的下标）。如果哈希表中此位置是空的，那么这个元素就会被插入其中。  
而如果此位置已被占用，Python 便会比较两个元素的哈希值和键是否相等。（可以理解mask应该是111， 1111这样的比较好，实际可以理解为entries[indices[hash(key) % PyDicMinSize]]， 这里采用与运算我理解是与运算比取余快多了）
若两者都相等，则表明这个元素已经存在，如果值不同，则更新值。
若两者中有一个不相等，这种情况我们通常称为哈希冲突（hash collision），意思是两个元素的键不相等，但是哈希值相等。这种情况下，Python 便会继续寻找表中空余的位置，直到找到位置为止。
值得一提的是，通常来说，遇到这种情况，最简单的方式是线性寻找，即从这个位置开始，挨个往后寻找空位。当然，Python 内部对此进行了优化（这一点无需深入了解，你有兴趣可以查看源码，我就不再赘述），让这个步骤更加高效。
  
- 查找操作  
和前面的插入操作类似，Python 会根据哈希值，找到其应该处于的位置；然后，比较哈希表这个位置中元素的哈希值和键，与需要查找的元素是否相等。如果相等，则直接返回；如果不等，则继续查找，直到找到空位或者抛出异常为止。
  
- 删除操作  
对于删除操作，Python 会暂时对这个位置的元素，赋于一个特殊的值，等到重新调整哈希表的大小时，再将其删除。（懒惰处理，减少每次删除的时间复杂度，让其均摊）  
不难理解，哈希冲突的发生，往往会降低字典和集合操作的速度。因此，为了保证其高效性，字典和集合内的哈希表，通常会保证其至少留有 1/3 的剩余空间。随着元素的不停插入，当剩余空间小于 1/3 时，Python 会重新获取更大的内存空间，扩充哈希表。不过，这种情况下，表内所有的元素位置都会被重新排放。  
虽然哈希冲突和哈希表大小的调整，都会导致速度减缓，但是这种情况发生的次数极少。所以，平均情况下，这仍能保证插入、查找和删除的时间复杂度为 O(1)。  