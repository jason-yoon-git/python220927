
from bs4 import BeautifulSoup

page = open("c:\\work\\4일차\\test01.html", "rt", encoding="utf-8").read()
#검색 용이한 객체
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())
#모든 p 검색
# print(soup.find_all("p"))
#첫번째 p 검색
# print(soup.find("p"))
#조건을 주고 필터링
# print(soup.find_all("p", class_="outer-text"))
#특정 id 검색
# print(soup.find_all(id="first"))

#태그 내부에 컨텐츠만 ㄴ검색 (.text  속성 사용)
for tag in soup.find_all("p"):
    title = tag.text.strip() #앞뒤공백 없앰
    title = title.replace("\n", "") #빈줄없앰
    print(title)