def fun(a):
    a.append(10)
    
def fun2():
    a=[]
    fun(a)
    print(a)

fun2()