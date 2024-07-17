#연습문제6
def fun(x) :
    result = []
    for var in x :
        result.append(int(var*1.1))
    return result

x = [100,200,300]
print(fun(x))




