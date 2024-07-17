#연습문제3
def fun(var) :
    result = ''
    if 81 <= var <= 100 :
        result = 'A학점입니다.'
    elif 61 <= var <= 80 :
        result = 'B학점입니다.'
    elif 41 <= var <= 60 :
        result = 'C학점입니다.'
    elif 21 <= var <= 40 :
        result = 'D학점입니다.'
    else :
        result = 'E학점입니다.'
    return result

sc = int(input('점수를 입력하세요 : '))
res = fun(sc)
print(res)
