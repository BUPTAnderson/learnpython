import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
# def now():
#     print('2015-3-25')
#
#
# now = log(now)
# print(now.__name__)
int2 = functools.partial(int, base=2)
print(int2("10000", base=10))