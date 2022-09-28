#demoRe.py
import re

result = re.search("[0-9]*th", " 35th")
#매칭 오브젝트
print(result)
print(result.group())

# result = re.match("[0-9]*th", " 35th")
# print(result)
# print(result.group())

result = re.search("apple", "this is apple")
print(result.group())

print("---년도찾기---")
print(bool(re.search("\d{4}", "올해는 2022년도"))) #\d{4} digit 4자리
result = re.search("\d{5}", "우리 동네는 53000") #숫자 5자리만 찾기
print(result.group())