from math import sqrt

num = 2
print("Global variable:", num)

def getNum():
    num = 5
    print("GetNum:", num)
    def inner():
        nonlocal num
        num = 10
        print("Inner:", num)
    inner()
    print("GetNum:", num)

getNum()
print("Built-in function: ", sqrt(9))