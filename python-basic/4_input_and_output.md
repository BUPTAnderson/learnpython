#### 基础
```angular2html
name = input('your name:')
gender = input('you are a boy?(y/n)')

###### 输入 ######
your name:Jack
you are a boy?

welcome_str = 'Welcome to the matrix {prefix} {name}.'
welcome_dic = {
    'prefix': 'Mr.' if gender == 'y' else 'Mrs',  # python条件表达式
    'name': name
}

print('authorizing...')
print(welcome_str.format(**welcome_dic)) # **用途为： 用于指定函数传入参数的类型，**用于参数前则表示传入的(多个)参数将按照字典的形式存储，是一个字典。

########## 输出 ##########
authorizing...
Welcome to the matrix Mr. Jack.
```
input() 函数暂停程序运行，同时等待键盘输入；直到回车被按下，函数的参数即为提示语，输入的类型永远是字符串型（str）。
```angular2html
a = input()
1
b = input()
2

print('a + b = {}'.format(a + b))
########## 输出 ##############
a + b = 12
print('type of a is {}, type of b is {}'.format(type(a), type(b)))
########## 输出 ##############
type of a is <class 'str'>, type of b is <class 'str'>
print('a + b = {}'.format(int(a) + int(b)))
########## 输出 ##############
a + b = 3
```
**注意：** 把 str 强制转换为 int 请用 int()，转为浮点数请用 float()。而在生产环境中使用强制转换时，请记得加上 try except

#### 文件输入输出
案例：  
1. 读取文件in.txt；  
2. 去除所有标点符号和换行符，并把所有大写变成小写；  
3. 合并相同的词，统计每个词出现的频率，并按照词频从大到小排序；  
4. 将结果按行输出到文件 out.txt。
    ```angular2html
    
    import re
    
    # 你不用太关心这个函数
    def parse(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w ]', ' ', text) # \w = [a-zA-Z_] # 取反消除掉所有特殊字符， \W = '^[a-zA-Z_]' ，效果一样，但是大写不方便阅读
    
        # 转为小写
        text = text.lower()
        
        # 生成所有单词的列表
        word_list = text.split(' ')
        
        # 去除空白单词
        word_list = filter(None, word_list)
        
        # 生成单词和词频的字典
        word_cnt = {}
        for word in word_list:
            if word not in word_cnt:
                word_cnt[word] = 0
            word_cnt[word] += 1
        
        # 按照词频排序
        sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
        
        return sorted_word_cnt
    
    with open('in.txt', 'r') as fin:
        text = fin.read()
    
    word_and_freq = parse(text)
    
    with open('out.txt', 'w') as fout:
        for word, freq in word_and_freq:
            fout.write('{} {}\n'.format(word, freq))
    
    ########## 输出(省略较长的中间结果) ##########
    
    and 15
    be 13
    will 11
    to 11
    the 10
    of 10
    a 8
    we 8
    day 6
    
    ...
    
    old 1
    negro 1
    spiritual 1
    thank 1
    god 1
    almighty 1
    are 1
    ```
   
在拿到指针后，我们可以通过 read() 函数，来读取文件的全部内容。代码 text = fin.read() ，即表示把文件所有内容读取到内存中，并赋值给变量 text。这么做自然也是有利有弊：
  - 优点是方便，接下来我们可以很方便地调用 parse 函数进行分析；
  - 缺点是如果文件过大，一次性读取可能造成内存崩溃。  

这时，我们可以给 read 指定参数 size ，用来表示读取的最大长度。还可以通过 readline() 函数，每次读取一行，这种做法常用于数据挖掘（Data Mining）中的数据清洗，在写一些小的程序时非常轻便。如果每行之间没有关联，这种做法也可以降低内存的压力。而 write() 函数，可以把参数中的字符串输出到文件中，也很容易理解。

这里我需要简单提一下 with 语句（后文会详细讲到）。open() 函数对应于 close() 函数，也就是说，如果你打开了文件，在完成读取任务后，就应该立刻关掉它。而如果你使用了 with 语句，就不需要显式调用 close()。在 with 的语境下任务执行完毕后，close() 函数会被自动调用，代码也简洁很多。

ps: 按行读取
```angular2html
with open('in.txt', 'r') as fin:
    for text in fin.readlines():
        word_cnt = parse(text)
```

#### JSON序列化与实战
示例：
```angular2html
import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

params_str = json.dumps(params)

print('after json serialization')
print('type of params_str = {}, params_str = {}'.format(type(params_str), params))

original_params = json.loads(params_str)

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))

########## 输出 ##########

after json serialization
type of params_str = <class 'str'>, params_str = {'symbol': '123456', 'type': 'limit', 'price': 123.4, 'amount': 23}
after json deserialization
type of original_params = <class 'dict'>, original_params = {'symbol': '123456', 'type': 'limit', 'price': 123.4, 'amount': 23}
```
其中，  
- json.dumps() 这个函数，接受 Python 的基本数据类型，然后将其序列化为 string；
- 而 json.loads() 这个函数，接受一个合法字符串，然后将其反序列化为 Python 的基本数据类型。

