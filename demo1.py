# 基础
# 输出
print("hello word")
# boolean
# 非运算
print(not False)
print(not True)
# 或运算 true
print(True or False)
# 与运算 false
print(True and False)
# 变量
num = 10;#数值类型 整类型
str="stonerao" #字符串类型
print(num,str)
# 通常全部大写表示常量 python没有任何机制保证不会被改变 书写习惯
CONST_NUM = 10;

print(10/3) #3.333333
print(10//3) #3 地板除

print('我是中文')

# list 有序集合 参考js Array
classmates=['stonerao','raoyan','ptt'] # classmates[0] === 'stonerao' 如果超出范围则会报错
len(classmates) #获取当前个数 3
classmates.append("raolele") #['stonerao', 'raoyan', 'ptt', 'raolele']
classmates.insert(1,"stone") #['stonerao', 'stone', 'raoyan', 'ptt', 'raolele']
classmates.pop() #['stonerao', 'stone', 'raoyan', 'ptt'] 删除最后一个
# pop(index) 带入参数 删除指定
# classmates[0] = '' 指定索引替换
# list 类型可以多样化
# 可包含其他list

# tuple元祖 类似于list 区别 tuple一旦初始化就不可修改

tuples = ('stonerao')
print(tuples)
# 循环
for name in classmates:
    print(name)

num = 0
while num < 100:
    num=num+5
    #print(num)
    if num==50:
        break

s = set([1,2,3])
print(s) # {1,3,4}
s.add(4) # {1,2,3,4}
s1 = set({3,4,5})
print(s & s1) # {3,4} 找出相同
print(s | s1) # {1,2,3,4,5,6} 无序重合

a = ['c', 'b', 'a']
a.sort()
print(a) # ['a','b','c']

a = 'abc'
print(a.replace('a','A')) # Abc
