#demoFile.py
for x in range(1,6):
    print(x, "*", x, "=", x*x)

print("---서식지정 1---")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))

print("---서식지정 2---")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).zfill(3))

#서식지정
print("{0:x}".format(10))  #16진수
print("{0:b}".format(10))  #2진수
print("{0:e}".format(4/3)) #지수
print("{0:f}".format(4/3)) #실수
print("{0:.2f}".format(4/3))
print("{0:,}".format(400000000))

#파일쓰기
f = open("c:\\work\\3일차\\demo.txt", "wt", encoding="utf-8") #유니코드 지정 (한글, 일본어 등)
#f = open(r"c:\work\3일차\demo.txt", "wt", encoding="utf-8")  #r을 붙이면 특수문자 표기 \\ => \ 로 가능
#f = open("c:/work/3일차/demo.txt","rt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일 읽기
#f = open(r"c:\work\3일차\demo.txt","rt", encoding="utf-8")
f = open("c:/work/3일차/demo.txt","rt", encoding="utf-8")
#처음부터 끝까지 하나의 문자열
result = f.read()
print(result)
#어디쯤 읽고 있니?
print( f.tell() )
#리셋
f.seek(0)
lst = f.readlines()
print(lst)
f.close()