import functools
def demo(a=2,b=3):
    print(a)
    print(b)
    print(a + b)

# demo(1,2)

demo1 = functools.partial(demo,b=100)

demo1(200)