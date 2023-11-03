# def foo(a=2, b):
#     return a + b


# getting error because once you define the default value to a arguments you have define for succeding arguments as well or you can define a at the last
def foo(a=2, b=0):
    return a + b


def foo(b, a=2):
    return a + b
