#연습문제1
a = input('몇단을 원하시나요? : ')
def add_numbers(a):
    return a
pre_result = add_numbers(a)
for i in range(1,10) :
    print(pre_result, 'X', i, '=', i*int(pre_result))


