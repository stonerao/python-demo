# 函数
import math
# 内置函数
abs(-100) # 100 输出绝对值 只能传一个参数
max(1,2,34,522) # 522 返回最大数值 只能输入数值


int("10") #10
float("12.34") # 12.34
str(123) #'123'
bool(1) #true
bool('') #False

# 变量可以直接指向函数
i = int
i("10") #10


# 定义函数
arr = []
def add_arr(x):
    arr.append(x)
    return arr
arr # []
add_arr(1)
arr # [1]
add_arr(10) # [1,10]


def nop():
    pass  # 定义空函数 可使用pass站位

def quadratic(a,b,c):
