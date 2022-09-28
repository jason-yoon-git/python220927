# try1.py
#함수 정의
def divide(a,b):
    return a/b

#에레처리
try:
    #호출
    # result = divide(5,0)    
    result = divide(5,"ㅁㅁㅁ")    
except ZeroDivisionError:
    print("0으로 나누면 안됨")
except TypeError:
    print("숫자이어야 연산 가능")
else:
    print("결과 :{0}".format(result))
finally:
    print("무조건 실행")

print("---전체 코드 종료---")