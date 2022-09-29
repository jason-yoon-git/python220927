
from bs4 import BeautifulSoup

page = open("c:\\work\\4일차\\test01.html", "rt", encoding="utf-8").read()
#검색 용이한 객체
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())
#모든 p 검색
# print(soup.find_all("p"))
#첫번째 p 검색
# print(soup.find("p"))

print(soup.find_all("p", class_="outer-text"))