l1 = [11,2,3,11,3,9,6,3]

#列表去重,并保持原来的顺序
l2=list(set(l1))
#按下标排序
l2.sort(key=l1.index)
print(l2)
print()

l3 = [{'name':'dandan','age':28},{'name':'nana','age':20},{'name':'cici','age':32}]
#按年龄排序，从小到大
def func(i):
    return i['age']
l3.sort(key=lambda i:i['age'])
print(l3)