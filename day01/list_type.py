# 声明全局变量
blist = ['asd','sdad',2,8,2]

# 通过索引访问 元素
# 局部变量
def list_demo():
    alist = [1,'xiao',2,'da',3]
    print(alist)
    # 打印全局变量
    print(blist)

# 跟新列表中的元素
def alist_update(alist):
    alist[0] = 5
    print(alist[0])
    print(alist)

# len() 获取变量的长度
# 获取长度，size，是从1开始数，有几个元素，就是几
def len_demo(alist):
    print(len(blist))
    print(len(alist))

# 删除方法 list.pop()
def pop_demo(alist):
    # pop()方法两个作用 第一个取出最后一位的值 第二个从列表中删除取出的值
    print(alist.pop())
    print(alist)
    # pop（）带参数，填值 是取下标
    alist.pop(2)
    print(alist)

# 正序方法
def orderBy_demo():
    print('调用正序排的方法')
    sort_demo()
    print('调用倒序排的方法')
    reverse_demo()
    pass

# 正序方法
def sort_demo():
    # 将blist 正序排
    blist.sort()
    print(blist)
    pass

# 倒序方法
def reverse_demo():
    # 将blist 倒序排
    blist.reverse()
    print(blist)
    pass


if __name__ == '__main__':
    blist = [1, 5, 2, 9, 3]
    orderBy_demo()
    # pop_demo(alist)
    # list_demo()
    # 打印全局变量
    # print(blist)

