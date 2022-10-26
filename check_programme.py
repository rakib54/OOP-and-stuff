class A:
    def __init__(self) -> None:
        self.multiply(15)
        print(self.i)
    def multiply(self,i):
        self.i=4*i
class B(A):
    def __init__(self) -> None:
        super().__init__()
    def multiply(self, i):
        self.i=2*i
obj=B()