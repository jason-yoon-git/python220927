#db1.py
import sqlite3

#연결객체(d일단은 메모리에서 작업)
con = sqlite3.connect(":memory:")
#구문을 실행하는 커서
cur = con.cursor()
#데이터 구조(Table)
cur.execute("create table PhoneBook (Name text, PhoneNum text);") #빈칸 유의
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-1111-1111');") #단일 따옴표 사용 유의 ' '
#입력 파라미터 처리
name = "gildong"
phoneNumber = "010-4567-1234"
cur.execute("insert into PhoneBook values (?,?);", (name, phoneNumber))
#검색
cur.execute("select * from PhoneBook;") #튜플로 리턴
for row in cur:
    print(row)