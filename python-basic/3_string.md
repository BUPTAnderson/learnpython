#### 基础
字符串是由独立字符组成的一个序列，通常包含在单引号（''）双引号（""）或者三引号之中（''' '''或""" """，两者一样）  
Python 同时支持这三种表达方式，很重要的一个原因就是，这样方便你在字符串中，内嵌带引号的字符串。比如：  
`"I'm a student"`  
Python 的三引号字符串，则主要应用于多行字符串的情境，比如函数的注释等等。
```angular2html
def calculate_similarity(item1, item2):
    """
    Calculate similarity between two items
    Args:
        item1: 1st item
        item2: 2nd item
    Returns:
      similarity score between item1 and item2
    """
```
同时，Python 也支持转义字符。所谓的转义字符，就是用反斜杠开头的字符串，来表示一些特定意义的字符。我把常见的的转义字符，总结成了下面这张表格。

|  转义字符   | 说明  |
|  ----  | ----  |
|  \newline   | 接下一行  |
|  \\   | 接下一行  |
|  \'   | 表示单引号'  |
|  \"   | 表示双引号"  |
|  \n   | 换行  |
|  \t   | 横向制表符  |
|  \b   | 退格  |
|  \v   | 纵向制表符  |

#### 常用操作
- 你可以把字符串想象成一个由单个字符组成的数组，所以，Python 的字符串同样支持索引，切片和遍历等等操作。
    ```angular2html
    
    name = 'jason'
    name[0]
    'j'
    name[1:3]
    'as'
    for char in name: print(char) jason
    ```
  
- Python 的字符串是不可变的（immutable）。因此，用下面的操作，来改变一个字符串内部的字符是错误的，不允许的。
    ```angular2html
    s = 'hello'
    s[0] = 'H'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment
    ```
  Python 中字符串的改变，通常只能通过创建新的字符串来完成。
    ```angular2html
    s = 'H' + s[1:]
    s = s.replace('h', 'H')
    ```
  第一种方法，是直接用大写的'H'，通过加号'+'操作符，与原字符串切片操作的子字符串拼接而成新的字符串。  
  第二种方法，是直接扫描原字符串，把小写的'h'替换成大写的'H'，得到新的字符串。
  

- 着重讲解一下，使用加法操作符'+='的字符串拼接方法。因为它是一个例外，打破了字符串不可变的特性。
    ```angular2html
    str1 += str2  # 表示str1 = str1 + str2
    
    s = ''
    for n in range(0, 100000):
        s += str(n)
    ```
  每次循环，似乎都得创建一个新的字符串；而每次创建一个新的字符串，都需要 O(n) 的时间复杂度。因此，总的时间复杂度就为 O(1) + O(2) + … + O(n) = O(n^2)。这样到底对不对呢？  
  乍一看，这样分析确实很有道理，但是必须说明，这个结论只适用于老版本的 Python 了。自从 Python2.5 开始，每次处理字符串的拼接操作时（str1 += str2），Python 首先会检测 str1 还有没有其他的引用。如果没有的话，就会尝试原地扩充字符串 buffer 的大小，而不是重新分配一块内存来创建新的字符串并拷贝。这样的话，上述例子中的时间复杂度就仅为 O(n) 了。
  

- 对于字符串拼接问题，除了使用加法操作符，我们还可以使用字符串内置的 join 函数。string.join(iterable)，表示把每个元素都按照指定的格式连接起来。
    ```angular2html
    l = []
    for n in range(0, 100000):
        l.append(str(n))
    l = ' '.join(l) 
    ```
  由于列表的 append 操作是 O(1) 复杂度，字符串同理。因此，这个含有 for 循环例子的时间复杂度为 n*O(1)=O(n)。


- 字符串分割函数split(),string.split(separator)，表示把字符串按照 separator 分割成子字符串，并返回一个分割后子字符串组合的列表。
    ```angular2html
    def query_data(namespace, table):
        """
        given namespace and table, query database to get corresponding
        data         
        """
    
    path = 'hive://ads/training_table'
    namespace = path.split('//')[1].split('/')[0] # 返回'ads'
    table = path.split('//')[1].split('/')[1] # 返回 'training_table'
    data = query_data(namespace, table) 
    ```
  
- 其他常见函数：
    ```angular2html
    string.strip(str)，表示去掉首尾的 str 字符串；
    string.lstrip(str)，表示只去掉开头的 str 字符串；
    string.rstrip(str)，表示只去掉尾部的 str 字符串。
    string.find(sub, start, end)，表示从 start 到 end 查找字符串中子字符串 sub 的位置等等。
    ```
  

#### 字符串格式化
`print('no data available for person with id: {}, name: {}'.format(id, name))`  
其中的 string.format()，就是所谓的格式化函数；而大括号{}就是所谓的格式符，用来为后面的真实值——变量 name 预留位置。如果id = '123'、name='jason'，那么输出便是：  
`
'no data available for person with id: 123, name: jason'`  
string.format() 是最新的字符串格式函数与规范。自然，我们还有其他的表示方法，比如在 Python 之前版本中，字符串格式化通常用 % 来表示，那么上述的例子，就可以写成下面这样：  
`print('no data available for person with id: %s, name: %s' % (id, name))`  
其中 %s 表示字符串型，%d 表示整型等等，这些属于常识，你应该都了解。

**当然，现在你写程序时，我还是推荐使用 format 函数，毕竟这是最新规范，也是官方文档推荐的规范。**