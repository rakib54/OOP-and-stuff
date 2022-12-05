import threading

def f1():
    for i in range(5):
        print(f"f1 - {i}")

def f2():
    for i in range(5):
        print(f"f2 - {i}")

def f3():
    for i in range(5):
        print(f"f3 - {i}")

def f4():
    for i in range(5):
        print(f"f4 - {i}")

th1 = threading.Thread(target=f1)
th2 = threading.Thread(target=f2)
th3 = threading.Thread(target=f3)
th4 = threading.Thread(target=f4)

th1.start()
th2.start()
th3.start()
th4.start()
