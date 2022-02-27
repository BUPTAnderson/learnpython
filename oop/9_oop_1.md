#### 基础
1. **类，一群有着相同属性和函数的对象的集合。**
    ```angular2html
    class Document():
        def __init__(self, title, author, context):
            print('init function called')
            self.title = title
            self.author = author
            self.__context = context # __开头的属性是私有属性
    
        def get_context_length(self):
            return len(self.__context)
    
        def intercept_context(self, length):
            self.__context = self.__context[:length]
    
    harry_potter_book = Document('Harry Potter', 'J. K. Rowling', '... Forever Do not believe any thing is capable of thinking independently ...')
    
    print(harry_potter_book.title)
    print(harry_potter_book.author)
    print(harry_potter_book.get_context_length())
    
    harry_potter_book.intercept_context(10)
    
    print(harry_potter_book.get_context_length())
    
    print(harry_potter_book.__context)
    
    ########## 输出 ##########
    
    init function called
    Harry Potter
    J. K. Rowling
    77
    10
    
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-5-b4d048d75003> in <module>()
         22 print(harry_potter_book.get_context_length())
         23 
    ---> 24 print(harry_potter_book.__context)
    
    AttributeError: 'Document' object has no attribute '__context'
    ```
    - **__init__ 表示构造函数，意即一个对象生成时会被自动调用的函数。** 通过`__init__`可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。注意到`__init__`方法的第一个参数永远是`self`，表示创建的实例本身，因此，在`__init__`方法内部，就可以把各种属性绑定到`self`，因为`self`就指向创建的实例本身。
    有了`__init__`方法，在创建实例的时候，就不能传入空的参数了，必须传入与`__init__`方法匹配的参数，但`self`不需要传，Python解释器自己会把实例变量传进去。
   我们能看到， harry_potter_book = Document(...)这一行代码被执行的时候，'init function called'字符串会被打印出来。而 get_context_length() 和 intercept_context() 则为类的普通函数，我们调用它们来对对象的属性做一些事情。  
    - class Document 还有三个属性，title、author 和 __context 分别表示标题、作者和内容，通过构造函数传入。这里代码很直观，我们可以看到， intercept_context 能修改对象 harry_potter_book 的 __context 属性。  
    - 这里唯一需要强调的一点是，如果一个属性以 `__` （注意，此处有两个 `_`） 开头，我们就默认这个属性是**私有属性** 。私有属性，是指不希望在类的函数之外的地方被访问和修改的属性。所以，你可以看到，title 和 author 能够很自由地被打印出来，但是 print(harry_potter_book.__context)就会报错。  
      需要注意的是，在Python中，变量名类似`__xxx__`的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用`__name__`、`__score__`这样的变量名。有些时候，你会看到以一个下划线开头的实例变量名，比如`_name`，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。  
      双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问`__name`是因为Python解释器对外把`__name`变量改成了`_Student__name`，所以，仍然可以通过`_Student__name`来访问`__name`变量：
      ```angular2html
      class Student(object):
        def __init__(self, name, score):
          self.__name = name
          self.__score = score

        def print_score(self):
          print('%s: %s' % (self.__name, self.__score))
      
      >>> bart = Student('Bart Simpson', 59)
      >>> bart._Student__name
      'Bart Simpson'
      ```
      但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
      最后注意下面的这种错误写法：
      ```angular2html
      >>> bart = Student('Bart Simpson', 59)
      >>> bart.get_name()
      'Bart Simpson'
      >>> bart.__name = 'New Name' # 设置__name变量！
      >>> bart.__name
      'New Name'
      ```
      表面上看，外部代码“成功”地设置了`__name`变量，但实际上这个`__name`变量和class内部的`__name`变量不是一个变量！内部的`__name`变量已经被Python解释器自动改成了`_Student__name`，而外部代码给bart新增了一个`__name`变量。不信试试：
      ```angular2html
      >>> bart.get_name() # get_name()内部返回self.__name
      'Bart Simpson'
      ```
    - 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量`self`，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
    - 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
        ```angular2html
        class Student(object):
         def __init__(self, name, score):
                self.name = name
                self.score = score
        
            def print_score(self):
                print('%s: %s' % (self.name, self.score))
        
        >>> bart = Student('Bart Simpson', 59)
        >>> lisa = Student('Lisa Simpson', 87)
        >>> bart.age = 8
        >>> bart.age
        8
        >>> lisa.age
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        AttributeError: 'Student' object has no attribute 'age'
        ```


#### 2. 更进一步
- 如何在一个类中定义一些常量，每个对象都可以方便访问这些常量而不用重新构造？
- 如果一个函数不涉及到访问修改这个类的属性，而放到类外面有点不恰当，怎么做才能更优雅呢？
- 既然类是一群相似的对象的集合，那么可不可以是一群相似的类的集合呢？
    ```angular2html
    class Document():
        
        WELCOME_STR = 'Welcome! The context for this book is {}.'
        
        def __init__(self, title, author, context):
            print('init function called')
            self.title = title
            self.author = author
            self.__context = context
        
        # 类函数
        @classmethod
        def create_empty_book(cls, title, author):
            return cls(title=title, author=author, context='nothing')
        
        # 成员函数
        def get_context_length(self):
            return len(self.__context)
        
        # 静态函数
        @staticmethod
        def get_welcome(context):
            return Document.WELCOME_STR.format(context)
    
    
    empty_book = Document.create_empty_book('What Every Man Thinks About Apart from Sex', 'Professor Sheridan Simove')
    
    
    print(empty_book.get_context_length())
    print(empty_book.get_welcome('indeed nothing'))
    
    ########## 输出 ##########
    
    init function called
    7
    Welcome! The context for this book is indeed nothing.
    ```
  
  第一个问题，在 Python 的类里，你只需要和函数并列地声明并赋值，就可以实现这一点，例如这段代码中的 WELCOME_STR。一种很常规的做法，是用全大写来表示常量，因此我们可以在类中使用 self.WELCOME_STR ，或者在类外使用 Entity.WELCOME_STR ，来表达这个字符串。(这种属性是类属性，归Entity类所有)
    ```angular2html
    >>> class Student(object):
    ...     name = 'Student'
    ...
    >>> s = Student() # 创建实例s
    >>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
    Student
    >>> print(Student.name) # 打印类的name属性
    Student
    >>> s.name = 'Michael' # 给实例绑定name属性
    >>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
    Michael
    >>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
    Student
    >>> del s.name # 如果删除实例的name属性
    >>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
    Student
    ```  
  从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。  
  **实例属性属于各个实例所有，互不干扰； 类属性属于类所有，所有实例共享一个属性；不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。**  
  <br/>
  而针对第二个问题，我们提出了类函数、成员函数和静态函数三个概念。它们其实很好理解，前两者产生的影响是动态的，能够访问或者修改对象的属性；而静态函数则与类没有什么关联，最明显的特征便是，静态函数的第一个参数没有任何特殊性。  
  <br/>
  具体来看这几种函数。一般而言，静态函数可以用来做一些简单独立的任务，既方便测试，也能优化代码结构。静态函数还可以通过在函数前一行加上 @staticmethod 来表示，代码中也有相应的示例。这其实使用了装饰器的概念，我们会在后面的章节中详细讲解。  
  <br/>
  而类函数的第一个参数一般为 cls，表示必须传一个类进来。类函数最常用的功能是实现不同的 init 构造函数，比如上文代码中，我们使用 create_empty_book 类函数，来创造新的书籍对象，其 context 一定为 'nothing'。这样的代码，就比你直接构造要清晰一些。类似的，类函数需要装饰器 @classmethod 来声明。  
  <br/>
  成员函数则是我们最正常的类的函数，它不需要任何装饰器声明，第一个参数 self 代表当前对象的引用，可以通过此函数，来实现想要的查询 / 修改类的属性等功能。
  
#### 3. 继承  
类的继承，顾名思义，指的是一个类既拥有另一个类的特征，也拥有不同于另一个类的独特特征。在这里的第一个类叫做子类，另一个叫做父类，特征其实就是类的属性和函数。

    ```angular2html
    class Entity():
        def __init__(self, object_type):
            print('parent class init called')
            self.object_type = object_type
        
        def get_context_length(self):
            raise Exception('get_context_length not implemented')
        
        def print_title(self):
            print(self.title)
    
    class Document(Entity):
        def __init__(self, title, author, context):
            print('Document class init called')
            Entity.__init__(self, 'document')
            self.title = title
            self.author = author
            self.__context = context
        
        def get_context_length(self):
            return len(self.__context)
        
    class Video(Entity):
        def __init__(self, title, author, video_length):
            print('Video class init called')
            Entity.__init__(self, 'video')
            self.title = title
            self.author = author
            self.__video_length = video_length
        
        def get_context_length(self):
            return self.__video_length
    
    harry_potter_book = Document('Harry Potter(Book)', 'J. K. Rowling', '... Forever Do not believe any thing is capable of thinking independently ...')
    harry_potter_movie = Video('Harry Potter(Movie)', 'J. K. Rowling', 120)
    
    print(harry_potter_book.object_type)
    print(harry_potter_movie.object_type)
    
    harry_potter_book.print_title()
    harry_potter_movie.print_title()
    
    print(harry_potter_book.get_context_length())
    print(harry_potter_movie.get_context_length())
    
    ########## 输出 ##########
    
    Document class init called
    parent class init called
    Video class init called
    parent class init called
    document
    video
    Harry Potter(Book)
    Harry Potter(Movie)
    77
    120
    ```
- 在这段代码中，Document 和 Video 它们有相似的地方，都有相应的标题、作者和内容等属性。我们可以从中抽象出一个叫做 Entity 的类，来作为它俩的父类。  
- 首先需要注意的是构造函数。每个类都有构造函数，继承类在生成对象的时候，是不会自动调用父类的构造函数的，因此你必须在 init() 函数中显式调用父类的构造函数。它们的执行顺序是 子类的构造函数 -> 父类的构造函数。  
- 最后需要注意到 print_title() 函数，这个函数定义在父类中，但是子类的对象可以毫无阻力地使用它来打印 title，这也就体现了继承的优势：减少重复的代码，降低系统的熵值（即复杂度）
- “鸭子类型”
    ```angular2html
    def run_twice(animal):
        animal.run()
        animal.run()
    ```
  对于静态语言（例如Java）来说，如果需要传入`Animal`类型，则传入的对象必须是`Animal`类型或者它的子类，否则，将无法调用`run()`方法。  
  对于Python这样的动态语言来说，则不一定需要传入`Animal`类型。我们只需要保证传入的对象有一个`run()`方法就可以了：
    ```angular2html
    class Timer(object):
        def run(self):
            print('Start...')
    ```  
  这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。  
  Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个`read()`方法，返回其内容。但是，许多对象，只要有`read()`方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了`read()`方法的对象。
  
#### 获取对象信息
- 首先，我们来判断对象类型，使用type()函数
    ```angular2html
    >>> type(123)
    <class 'int'>
    >>> type('str')
    <class 'str'>
    >>> type(None)
    <type(None) 'NoneType'>
    ```
  如果一个变量指向函数或者类，也可以用type()判断  
  但是`type()`函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在`if`语句中判断，就需要比较两个变量的type类型是否相同：
    ```angular2html
    >>> type(123)==type(456)
    True
    >>> type(123)==int
    True
    >>> type('abc')==type('123')
    True
    >>> type('abc')==str
    True
    >>> type('abc')==type(123)
    False
    ```  
  判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
    ```angular2html
    >>> import types
    >>> def fn():
    ...     pass
    ...
    >>> type(fn)==types.FunctionType
    True
    >>> type(abs)==types.BuiltinFunctionType
    True
    >>> type(lambda x: x)==types.LambdaType
    True
    >>> type((x for x in range(10)))==types.GeneratorType
    True
    ```
  
- 使用isinstance()
对于class的继承关系来说，使用`type()`就很不方便。我们要判断class的类型，可以使用`isinstance()`函数。  
我们回顾上次的例子，如果继承关系是：`object -> Animal -> Dog -> Husky`  
那么，`isinstance()`就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：
    ```angular2html
    >>> a = Animal()
    >>> d = Dog()
    >>> h = Husky()
    # 然后，判断：
    >>> isinstance(h, Husky)
    True
    # 再判断：
    >>> isinstance(h, Dog)
    True
    ```
  `h`虽然自身是`Husky`类型，但由于Husky是从Dog继承下来的，所以，`h`也还是Dog类型。换句话说，**`isinstance()`判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上**。因此，我们可以确信，`h`还是Animal类型.  
  但是，`d`不是Husky类型：
    ```angular2html
    >>> isinstance(d, Husky)
    False
    ```
  能用`type()`判断的基本类型也可以用`isinstance()`判断：
    ```angular2html
    >>> isinstance('a', str)
    True
    >>> isinstance(123, int)
    True
    >>> isinstance(b'a', bytes)
    True
    ```
  并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
    ```angular2html
    >>> isinstance([1, 2, 3], (list, tuple))
    True
    >>> isinstance((1, 2, 3), (list, tuple))
    True
    ```
  **总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。**

- 使用dir()  
如果要获得一个对象的所有属性和方法，可以使用`dir()`函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
    ```angular2html
    >>> dir('ABC')
    ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
    ```
  类似`__xxx__`的属性和方法在Python中都是有特殊用途的，比如`__len__`方法返回长度。在Python中，如果你调用`len()`函数试图获取一个对象的长度，实际上，在`len()`函数内部，它自动去调用该对象的`__len__()`方法，所以，下面的代码是等价的：
    ```angular2html
    >>> len('ABC')
    3
    >>> 'ABC'.__len__()
    3
    ```
  我们自己写的类，如果也想用`len(myObj)`的话，就自己写一个`__len__()`方法：
    ```angular2html
    >>> class MyDog(object):
    ...     def __len__(self):
    ...         return 100
    ...
    >>> dog = MyDog()
    >>> len(dog)
    100
    ```
  仅仅把属性和方法列出来是不够的，配合`getattr()`、`setattr()`以及`hasattr()`，我们可以直接操作一个对象的状态：
    ```angular2html
    >>> class MyObject(object):
    ...     def __init__(self):
    ...         self.x = 9
    ...     def power(self):
    ...         return self.x * self.x
    ...
    >>> obj = MyObject()
    ```
  紧接着，可以测试该对象的属性：
    ```angular2html
    >>> hasattr(obj, 'x') # 有属性'x'吗？
    True
    >>> obj.x
    9
    >>> hasattr(obj, 'y') # 有属性'y'吗？
    False
    >>> setattr(obj, 'y', 19) # 设置一个属性'y'
    >>> hasattr(obj, 'y') # 有属性'y'吗？
    True
    >>> getattr(obj, 'y') # 获取属性'y'
    19
    >>> obj.y # 获取属性'y'
    19
    ```
  如果试图获取不存在的属性，会抛出AttributeError的错误：
    ```angular2html
    >>> getattr(obj, 'z') # 获取属性'z'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'MyObject' object has no attribute 'z'
    ```
  可以传入一个default参数，如果属性不存在，就返回默认值：
    ```angular2html
    >>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
    404
    ```
  也可以获得对象的方法：
    ```angular2html
    >>> hasattr(obj, 'power') # 有属性'power'吗？
    True
    >>> getattr(obj, 'power') # 获取属性'power'
    <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
    >>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
    >>> fn # fn指向obj.power
    <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
    >>> fn() # 调用fn()与调用obj.power()是一样的
    81
    ```

#### 抽象函数和抽象类
在python中，并没有接口类这种东西
```angular2html
from abc import ABCMeta, abstractmethod # 利用abc模块实现抽象类

class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):  # 定义抽象方法，无需实现功能
        pass

    @abstractmethod
    def set_title(self, title):  # 定义抽象方法，无需实现功能
        pass

class Document(Entity):
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title

document = Document()
document.set_title('Harry Potter')
print(document.get_title())

entity = Entity()

########## 输出 ##########

Harry Potter

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-266b2aa47bad> in <module>()
     21 print(document.get_title())
     22 
---> 23 entity = Entity()
     24 entity.set_title('Test')

TypeError: Can't instantiate abstract class Entity with abstract methods get_title, set_title
```
抽象类是一种特殊的类，它生下来就是作为父类存在的，一旦对象化就会报错。同样，抽象函数定义在抽象类之中，子类必须重写该函数才能使用。相应的抽象函数，则是使用装饰器 @abstractmethod 来表示。  
抽象类就是这么一种存在，它是一种自上而下的设计风范，你只需要用少量的代码描述清楚要做的事情，定义好接口，然后就可以交给不同开发人员去开发和对接。

- 第一个问题，面向对象编程四要素是什么？它们的关系又是什么？  
答：面向对象编程四要素是类，属性，函数，对象， 它们关系可以总结为：类是一群具有相同属性和函数的对象的集合。
- 第二个问题，讲了这么久的继承，继承究竟是什么呢？你能用三个字表达出来吗？  
三个字：父与子。儿子可以使用自己的东西，没有的可以使用父亲的东西。
  
#### 多重继承
具体实例见multi_extends_1.py和multi_extends_2.py  
多重继承，是基于mro进行查找，使用的是一种C3的算法。总结一下规律就是：  
B F

C G

D H

E I

  J  
在python3中，如果最顶层的两个类没有继承共同的类，那么查找顺序是，先从左找到头，再从右找到头，即，J->E->D->C->B->I->H->G->F

  A  
B F

C G

D H

E I

  J  
如果继承了共同的类，也就是形成了菱形结构，那么查找顺序为，先从左找，只找到倒数第二层，然后从右找到头，即J->E->D->C->B->I->H->G->F->A

示例代码参考search.py