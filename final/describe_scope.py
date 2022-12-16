# from math import sqrt

# num = 2
# print("Global variable:", num)

# def getNum():
#     num = 5
#     print("GetNum:", num)
#     def inner():
#         nonlocal num
#         num = 10
#         print("Inner:", num)
#     inner()
#     print("GetNum:", num)

# getNum()
# print("Built-in function: ", sqrt(9))

# Global Scope:
# The Variable which can be read from anywhere in the program is known as a global scope. These variables can be accessed inside and outside the function. Here num=2 is a global variable.

# Local Scope:
# The Variables which are defined in the function are a local scope of the variable. Here num=5 is a local variable that is declared and printed inside the function getNum.

# Nonlocal Scope:
# Nonlocal Variable is the variable that is defined in the nested function. Here num=10 is a nonlocal variable.

# Built-in Scope:
# If a Variable is not defined in local, Enclosed or global scope, then python looks for it in the built-in scope. Here sqrt is imported from math, and the value of sqrt(9) is resulted from built-in scope , and it is not defined in global, local and enclosed.

from math import sqrt

value = 2
print("Global variable:", value)

def get_value_from_different_scope():
    value = 5
    print("value is :", value)
    def inner_func():
        nonlocal value
        value = 10
        print("From Inner Function value is:", value)
    inner_func()
    print("From Outer function value is :", value)

get_value_from_different_scope()
print("Built-in function: ", sqrt(9))
