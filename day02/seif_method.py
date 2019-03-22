
def list_bianli():
    alist = ['1','j','9','0']
    for i in alist:
        print(i)

# if __name__ == '__main__':
#     for i in range(9,0,-1):
#         for j in range(1,i+1):
#             print('%s*%s=%s '%(i,j,i*j),end = '')
#         print('')

#
# if __name__ == '__main__':
#     a = 10
#     b = 20
#     if a>b:
#         print(a)
#     else:
#         print(b)

    pass
# if __name__ == '__main__':
#     # nub = 0
#     # for i in range(1,51,2):
#     #     nub=nub+i
#     # print(nub)
#     nub=1
#     for i in range(5,  20):
#         nub=nub+i
#     print(nub)



def list_demo(a,b):
    aa=0
    if a>b:
        for i in range(b+1,a):
            if i%2 == 0:
               aa = aa + i
        print(aa)
    else:
        for i   in range(a+1,b):
            if i%2 == 0:
               aa = aa + i
        print(aa)

if __name__ == '__main__':
    list_demo(130,10)
