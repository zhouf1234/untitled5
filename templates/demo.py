def func(*args,**kwargs):
    print(args)
    print(kwargs)

l1 = [1,2,3]
d1 = {'name':'nana','age':18}
#func(l1,d1)的写法默认是当做位置参数来传参
func(l1,d1)
#func(*l1,**d1)加*代表解开，相当于传了func(1,2,3,'name':'nana','age':18)
func(*l1,**d1)