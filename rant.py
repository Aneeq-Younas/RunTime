from timeit import default_timer
def a (x):
    s = default_timer()

    for i in range(0,x):
        print(i)
    print(default_timer())

a(22)
a(15)