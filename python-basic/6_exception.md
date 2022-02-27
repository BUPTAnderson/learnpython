#### 错误与异常
通常来说，程序中的错误至少包括两种，一种是语法错误，另一种则是异常。  
- 错误：
    ```angular2html
    if name is not None
        print(name)
    ```
If 语句漏掉了冒号，不符合 Python 的语法规范，所以程序就会报错invalid syntax。  
- 异常：
    ```angular2html
    10 / 0
    Traceback (most recent call last): 
      File "", line 1, in <module>
    ZeroDivisionError: integer division or modulo by zero
    ```

#### 如何处理异常
```angular2html

try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ... 
except ValueError as err:
    print('Value Error: {}'.format(err))

print('continue')
...
```
这里默认用户输入以逗号相隔的两个整形数字，将其提取后，做后续的操作（注意 input 函数会将输入转换为字符串类型）。如果我们输入a,b，程序便会抛出异常invalid literal for int() with base 10: 'a'，然后跳出 try 这个 block。  
由于程序抛出的异常类型是 ValueError，和 except block 所 catch 的异常类型相匹配，所以 except block 便会被执行，最终输出Value Error: invalid literal for int() with base 10: 'a'，并打印出continue。

还是刚刚这个例子，如果我们只输入1，程序抛出的异常就是IndexError: list index out of range，与 ValueError 不匹配，那么 except block 就不会被执行，程序便会终止并退出（continue 不会被打印）。
```angular2html
please enter two numbers separated by comma: 1
IndexError Traceback (most recent call last)
IndexError: list index out of range
```
- 一种解决方案，是在 except block 中加入多种异常的类型，比如下面这样的写法：
    ```
    try:
        s = input('please enter two numbers separated by comma: ')
        num1 = int(s.split(',')[0].strip())
        num2 = int(s.split(',')[1].strip())
        ...
    except (ValueError, IndexError) as err:
        print('Error: {}'.format(err))
        
    print('continue')
    ...
    ```
-  或者第二种写法：
    ```angular2html
    try:
        s = input('please enter two numbers separated by comma: ')
        num1 = int(s.split(',')[0].strip())
        num2 = int(s.split(',')[1].strip())
        ...
    except ValueError as err:
        print('Value Error: {}'.format(err))
    except IndexError as err:
        print('Index Error: {}'.format(err))
    
    print('continue')
    ...
    ```
- 不过，很多时候，我们很难保证程序覆盖所有的异常类型，所以，更通常的做法，是在最后一个 except block，声明其处理的异常类型是 Exception。Exception 是其他所有非系统异常的基类，能够匹配任意非系统异常。
    ```angular2html
    try:
        s = input('please enter two numbers separated by comma: ')
        num1 = int(s.split(',')[0].strip())
        num2 = int(s.split(',')[1].strip())
        ...
    except ValueError as err:
        print('Value Error: {}'.format(err))
    except IndexError as err:
        print('Index Error: {}'.format(err))
    except Exception as err:
        print('Other error: {}'.format(err))
    
    print('continue')
    ...
    ```
- 或者，你也可以在 except 后面省略异常类型，这表示与任意异常相匹配（包括系统异常等）：
    ```angular2html
    try:
        s = input('please enter two numbers separated by comma: ')
        num1 = int(s.split(',')[0].strip())
        num2 = int(s.split(',')[1].strip())
        ...
    except ValueError as err:
        print('Value Error: {}'.format(err))
    except IndexError as err:
        print('Index Error: {}'.format(err))
    except:
        print('Other error')
    
    print('continue')
    ...
    ```
  
- 异常处理中，还有一个很常见的用法是 finally，经常和 try、except 放在一起来用。无论发生什么情况，finally block 中的语句都会被执行，哪怕前面的 try 和 excep block 中使用了 return 语句。
```angular2html
import sys
try:
    f = open('file.txt', 'r')
    .... # some data processing
except OSError as err:
    print('OS error: {}'.format(err))
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    f.close()
```

#### 用户自定义异常
实际工作中，如果内置的异常类型无法满足我们的需求，或者为了让异常更加详细、可读，想增加一些异常类型的其他功能，我们可以自定义所需异常类型。
```angular2html
class MyInputError(Exception):
    """Exception raised when there're errors in input"""
    def __init__(self, value): # 自定义异常类型的初始化
        self.value = value
    def __str__(self): # 自定义异常类型的string表达形式
        return ("{} is invalid input".format(repr(self.value)))
    
try:
    raise MyInputError(1) # 抛出MyInputError这个异常
except MyInputError as err:
    print('error: {}'.format(err))
```
如果你执行上述代码块并输出，便会得到下面的结果：
```angular2html
error: 1 is invalid input
```

#### 异常的使用场景与注意点
- 通常来说，在程序中，如果我们不确定某段代码能否成功执行，往往这个地方就需要使用异常处理。
    ```angular2html
    try:
        data = json.loads(raw_data)
        ....
    except JSONDecodeError as err:
        print('JSONDecodeError: {}'.format(err))
    ```
- 不过，有一点切记，我们不能走向另一个极端——滥用异常处理。  
  比如，当你想要查找字典中某个键对应的值时，绝不能写成下面这种形式：
    ```angular2html
    d = {'name': 'jason', 'age': 20}
    try:
        value = d['dob']
        ...
    except KeyError as err:
        print('KeyError: {}'.format(err))
    ```
    对于 flow-control（流程控制）的代码逻辑，我们一般不用异常处理。字典这个例子，写成下面这样就很好。
    ```angular2html
    
    if 'dob' in d:
        value = d['dob']
        ...
    ```
  
#### 思考
- 在异常处理时，如果 try block 中有多处抛出异常，需要我们使用多个 try except block 吗？以数据库的连接、读取为例，下面两种写法，你觉得哪种更好呢？  
第一种：
    ```angular2html
    try:
        db = DB.connect('<db path>') # 可能会抛出异常
        raw_data = DB.queryData('<viewer_id>') # 可能会抛出异常
    except (DBConnectionError, DBQueryDataError) as err:
        print('Error: {}'.format(err))
    ```
   第二种：
    ```angular2html
    try:
        db = DB.connect('<db path>') # 可能会抛出异常
        try:
            raw_data = DB.queryData('<viewer_id>')
        except DBQueryDataError as err:
             print('DB query data error: {}'.format(err))
    except DBConnectionError as err:
         print('DB connection error: {}'.format(err))
    ```
  
  ①与②的运行逻辑一致，①可以看作②的简化版；
  ②的写法，如出现异常，多次调用异常处理，降低程序运行效率；
  
- 问题
    ```angular2html
    e = 1
    try:
        1 / 0
    except ZeroDivisionError as e:
        pass
    
    print(e) # NameError: name 'e' is not defined
    ```
    这里为什么会显示e没有被定义呢？
  
    可以阅读官方文档：https://docs.python.org/3/reference/compound_stmts.html#the-try-statement
    "When an exception has been assigned using as target, it is cleared at the end of the except clause."

    比如下面这个code block：
    ```angular2html
    except E as N:
            foo
        
        # 就等于
    except E as N:
        try:
            foo
        finally:
            del N
    ```
    因此你例子中的e最后被delete了，所以会抛出NameError