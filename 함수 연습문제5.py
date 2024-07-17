#연습문제5
def fun(var):
    result = ''
    if var % 2 == 0 :
        result = '짝수입니다.'
    else :
        result = '홀수입니다.'
    return result

num = int(input('숫자를 입력하세요 : '))
print(fun(num))