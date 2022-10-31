# def do_work(work):
#   print("Starting work")
#   work()
#   print("End work")

# def work():
#   print("I am from inside")

# do_work(work)

class A:
    def __init__(self):
        self.multiply(15)
    def multiply(self, i):
        self.i = 4 * i;
class B(A):
    def __init__(self):
        super().__init__()
        print(self.i)
 
    def multiply(self, i):
        self.i = 2 * i;
obj = B()


def mk(x):
    def mk1():
        print("Decorated")
        x()
    return mk1
def mk2():
    print("Ordinary")
p = mk(mk2)
p()

class Demo:
    def __check(self):
        return " Demo's check "
    def display(self):
        print(self.__check(),end="")
class Demo_Derived(Demo):
    def __check(self):
        return " Derived's check "
Demo().display()
Demo_Derived().display()