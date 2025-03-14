import sys


def method3():
    raise IndexError('foo')  # raise indexerror line


def method2():
    return method3()  # reraise on method2


def method1():
    try:
        method2()  # handle on method1
    except:
        pass  # Ok, handled
    exc = sys._getframe().f_locals.get('__exception__', None)
    assert exc is None


if __name__ == '__main__':
    method1()
    print('TEST SUCEEDED!')
