#연습문제4
# var = [1,2,3,4,5,6,7,8,9]
# def fun(var) :
#     result = 0
#     for i in var :
#         result = result + i
#     res = i / len(var)
# print(int(result))

def mean_list(x):
    result = 0
    for i in x:
        result = result + i
    avg = result / len(x)
    return avg

var = [1,2,3,4,5]
print(mean_list(var))


