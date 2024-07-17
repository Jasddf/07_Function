# #연습문제2
# a = input('문자를 입력하세요 : ')
# def fun(a):
#     return a
# result = fun(a)
# if len(result) <= 20 :
#     print('문자 요금은 50원입니다.')
# else :
#     print('문자 요금은 100원입니다.')

def find_len(x) :
    result = 0
    if len(x) <= 20 :
        result = 50
    elif len(x) > 20 :
        result = 100
    return result
text = input('문자를 입력하세요 : ')
var = find_len(text)
print(var)