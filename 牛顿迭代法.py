import math
#牛顿迭代法
def function1():
    a = float(input('初始值'))
    N = float(input('迭代次数'))
    x = a
    n = 1
    while n <= N:
        x=x-(x-math.exp(-x))/(1+x)
        print(n,x)
        n=n+1
#function1()
#普通不动点法
def function2():
    a = float(input('初始值'))
    N = float(input('迭代次数'))
    x = a
    n = 1
    while n <= N:
        x=math.exp(-x)
        print(n,x)
        n=n+1
function2()
