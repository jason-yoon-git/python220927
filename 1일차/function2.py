#function2.py
#지역변수

from re import X


x = 5
def func(a):
    return a+x
print( func(1))

#지역변수
def func2(a):
    x = 1
    return a+x
#호출
print( func2(1) )

#디버깅 연습
def intersect(prelist, postlist):
    #지여겹ㄴ수에 리스트 초기화
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print( intersect("HAM", "SPAM"))