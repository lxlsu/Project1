import random

# people = {
#     'Alice':{
#         'phone': '2345',
#         'addr':'foo drive 23'
#     },
#     'Beth':{
#         'phone':'2353',
#         'addr':'bar street 33'
#     },
#     'Cecil':{
#         'phone':'333435',
#         'addr':'baz avenu 89'
#     }
# }
#
# labels = {
#     'phone':'phone number',
#     'addr':'address'
# }
#
# name = input('name:')
# request = input('Phone number(P) or address(A):')
#
# if request == 'P': key = 'phone'
# if request == 'A': key = 'addr'
#
# if name in people : print("{}'s {} is {}.".format(name, labels[key], people[name][key]))

#!/usr/bin/python

dict1 = {'Name': 'Zara', 'Age': 7}

#print("Value : %s" % dict1.keys())

# d = {'key1':1, 'key2':2}
#
# print('hello', 'a', sep='__*_')
#
# name = input("what is your name")
# if name.endswith('Sandy'):
#     print('hello, Miss Sandy')
# else:
#     print("sorry, may I have your name?")
#
# status = "friend" if name.endswith("Jack") else "stranger"
# print(status)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7]
# idChar = 'ID:'
# for number in numbers:
#     if number > 0:
#         print(idChar, number, sep='')  //可去除空格
#     else:
#         print('ID:0')
# from math import sqrt
# for n in range(99,0,-1):
#     root = sqrt(n)
#     print("root:", root, "\n")
#     print("int root", int(root), "\n")
#     if root == int(root):
#         print(n)
#         break
#     else:
#         print("Don't find it!")
#  print([x*x for x in range(10) if x % 3 == 0])

#计算-斐波纳契数


# def print_params_1(x, y, z=3, *pospar, **keypar):
#     print(x, y, z)
#     print(pospar, keypar)
#     return
#
# print_params_1(1, 2, 3, 4, 5, 6, 7, foo = 1, bar = 2)
#
# def hello_3(name, greeting):
#     print(greeting+',', name)
#     return
#
# params = {'name': 'Sir Robin', 'greeting': 'Well met'}
#
# hello_3(**params)

def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:
        stop = start
        start = 0
# start, stop = 0, start   #start = 0, stop = start
    #应该先赋值stop,否则start的值会被覆盖

'''
        print("下一步，申请return")
    result = []

    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


print(interval(10))
print(interval(2, 23))
print(interval(1, 12, 3))


def combine(parameter):
    print(parameter + external)


#parameter = 'hello'
external = 'berry'

combine('shrub')
'''

'''
def multiplier(factor):
    def mutiplyByFactor(number):
        return number * factor
    return mutiplyByFactor

double = multiplier(2)
print(double(5))

multi1 = multiplier(4)(5)
print(multi1)

class Class:
    def method(self):
        print("I have a self")

def funciton():
    print("I don't...")

instance = Class()
instance.method()
instance.method = funciton

instance.method()


class Bird:
    __song = 'shgia'    # 私有
    song = '33333'
    def sing(self):
        print(self.__song)


bird = Bird()
bird.sing()
print(Bird._Bird__song)
'''

'''
while 1:
    try:
        x = int(input('Enter the first number:'))
        y = int(input('Enter the second number:'))
        print(x/y)
    except Exception as e:
        print("Invalid input: ", e)
        print("Please try again")
    else:
        break
 '''

'''
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Aaah..")
            self.hungry = False
        else:
            print("No, thanks")


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = "Squawk"

    def sing(self):
        print(self.sound)


sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
'''


#创建无穷序列
def check_index(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        print("__getitem__ Chekc_index\n")
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key*self.step

    def __setitem__(self, key, value):
        print("__setitem__ Chekc_index\n")
        check_index(key)
        self.changed[key] = value


s = ArithmeticSequence(1, 2)
print(s[10000000])       # 调用了__getitem__
s[2] = 1


class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)


c1 = CounterList(range(0, 10, 2))
print(c1)


# 静态方法和类方法
# 装饰器
class Myclass:

    @staticmethod         # 静态方法包装在staticmethod类的对象中
    def smeth():
        print("This is a static method")

    @classmethod         # 类方法包装在classmethod类的对象中
    def cmeth(cls):
        print("This is a class method of", cls)


Myclass.smeth()
Myclass.cmeth()


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


nested = [[1, 2, 3], [4, 5], [8,10]]
for num in flatten(nested):
    print(num)


# 八皇后问题
def conflict(state, nextX):
    nextY = len(state)

    for i in range(nextY):

        if abs(state[i] - nextX) in (0, nextY - i):
            return True

    return False


def queens(num = 8, state = ()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:       # 递归
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
    for pos in solution:
        print(line(pos))


prettyprint(random.choice(list(queens(8))))

'''
def queens(num, state):
    if len(state) == num - 1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos
            else:
                for pos in range(num):
                    if not conflict(state, pos):
                        for result in queens(num, state + (pos,)):
                            yield (pos,) + result
'''

