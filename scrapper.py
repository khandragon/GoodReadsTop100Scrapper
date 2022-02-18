import random
import requests 
from bs4 import BeautifulSoup
import json

class Book:
    def __init__(self,name,sellerName,description,category, imgUrl) -> None:
        self.id="1",
        self.name=name,
        self.sellerName=sellerName,
        self.decription=description,
        self.price = random.randint(2,50),
        self.shipping = random.randint(1,10),
        self.category = category,
        self.sale = random.randint(1,50),
        self.ISBN = random.randint(1000000000000,9999999999999),
        self.imgUrl = imgUrl
    def printBook(self):
        return self.name
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)
        


# bookJson = Book("test","Tester","Testing Book Class", "TestCat","tst.com" )
bookJsons ={}
# bookJsons.append(bookJson.toJSON());
pageUrl = "https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century"
bookUrls = []
pageInfo = requests.get(pageUrl)
results = BeautifulSoup(pageInfo.content, "html.parser")
for link in results.find_all("a", class_="bookTitle"):
    bookUrls.append("https://www.goodreads.com"+link.get('href'))

with open("test.json", "a") as data:
    information = {'name': {'surname': 'ted', 'age': '20'}}
    information1 = {'name': {'surname': 'mike', 'age': '10'}}
    informations = []

    informations.append(information)
    informations.append(information1)


    for bookUrl in bookUrls:
        try:
            bookPage = requests.get(bookUrl)
            # print("1")
            # bookPage = requests.get("https://www.goodreads.com/book/show/2657.To_Kill_a_Mockingbird")
            # print("2")
            bookInfo = BeautifulSoup(bookPage.content,"html.parser")
            # print("3")
            bookImg = bookInfo.find("div", class_="editionCover").find("img")["src"]
            # print("4")
            bookTitle = bookInfo.find("h1", id="bookTitle").text.strip();
            # print("5")
            bookAuthor = bookInfo.find("span", itemprop="name").text.strip();
            # print("6")
            bookDescription = bookInfo.find("div", id="description").find_next("span");
            # print("7")
            bookGenres = bookInfo.find_all("a", class_="bookPageGenreLink")[3].string;
            # print("8")
            newBook = {"title":bookTitle,"sellerName":bookAuthor,"description":bookDescription,"category":bookGenres,"imgUrl":bookImg}
            print(bookTitle)
            print(1)
            informations.append(newBook);
            print(2)
            # print(informations)
            # print(3)
            # data.write(informations)
    
            # bookJsons.append(newBook)
            # print("10")
            # print(type(bookJsons))

            # print(book)
            # print(bookImg)
            # print(bookAuthor)
            # print(bookDescription.prettify())
            # print(bookGenres)
            # print(bookISBN)

        except Exception as x:
            print("failed due to "+x.__class__.__name__)    
    print(informations)
    data.close()
    