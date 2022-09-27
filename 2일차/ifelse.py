#ifelse.py
#주석처리 단축키 ctrl + /
# score = int(input("점수를 입력:"))

# if 90 <= score <= 10:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

value = 5
while value > 0:
    print(value)
    value -= 1

d ={"apple":100, "orange":300}
for item in d.items():    
    print(item)

lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item > 5:
        break
    print("Item:{0}".format(item))


print("---continue---")
for item in lst:
    if item % 2 == 0:
        continue
    print("Item:{0}".format(item))

print("테스트{0} {1}".format(value, value))

print("---range함수---")
print( list(range(10)))
print( list(range(1,11)))
print( list(range(2000,2023))) #년도 범위 잡을때 유용함

print("---리스트 내장---")
lst = list(range(1,11))
print( [i**2 for i in lst if i > 5])
tp = ("apple", "orange", "kiwi")
print( [len(i) for i in tp])


print("---필터링 없음---")
lst = [20, 25, 30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

print("---필터링 있음 : 일종의 조건문---")
def getBiggerThan20(i):
    return i > 20   

lst = [20, 25, 30]
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

print("---람다함수 사용 : 일회용함수---")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)