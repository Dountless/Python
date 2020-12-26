# class Laptop:
#     def __init__(self,ram,hdd,os):
#         self.ram=ram
#         self.hdd=hdd
#         self.OS=os
#     def full_detail(self):
#         return f"ram is {self.ram} memory is {self.hdd} and operating system is {self.OS}"



# dell=Laptop(4,'1TB','window10')
# macbook=Laptop(8,'250ssd','mac')
# print(macbook.full_detail())
# print(Laptop.full_detail(macbook))


# print(macbook./OS)

# class Bca:
#     count_instance=0
#     def __init__(self,name,age):
#         Bca.count_instance+=1
#         self.name=name
#         self.age=age
#     @classmethod
#     def from_str(cls,stri):
#         a,b=stri.split(",")
#         return cls(a,b)
#     @classmethod
#     def count(cls):
#         return f"you have created {cls.count_instance} instance of {cls.__name__} class"


# s1=Bca("deepak",16)
# s2=Bca("aman",18)
# # s3=Bca("amit",16)
# # s4=Bca("herry",78)
# # s5=Bca.from_str("rahul,18")
# # print(s5.name)



# class Phone:
#     def  __init__(self,brand,modelName,price):
#         self.brand=brand
#         self.modelName=modelName
#         self.price=max(price,0)
#         # if price>0:
#         #     self.price=price
#         # else:
#         #     self.price=0
#     @property
#     def pri(self):
#         return self.price

#     @pri.setter
#     def prices(self,new):
#         self.price=max(new,0)

#     @property
#     def completeDetail(self):
#         return f"{self.brand} {self.modelName}  {self.price}"
    
#     def makecall(self,nu='intnumber'):
#         print(f"{nu} calling.....")
#     @property
#     def fullname(self):
#         print(f"{self.brand} {self.modelName}")


# class Smartphone(Phone):
#     def __init__(self,brand,modelName,price,ram,fingerprint):
#         super().__init__(brand,modelName,price)
#         self.ram=ram
#         self.fingerprint=fingerprint
#     @property
#     def fullname(self):
#         print(f"{self.brand} {self.modelName} {self.price} {self.ram}")

# class hifiphone(Smartphone):
#     def __init__(self,brand,modelName,price,ram,fingerprint,batterytime):
#         super().__init__(brand,modelName,price,ram,fingerprint)
#         self.batterytime=batterytime






# sumsung=Phone("sumsung",'M11',10000)
# sumsunga11=Smartphone("sumsung11111",'a11',50000,8,'yes')
# sumsunga11.prices=90000

# # print(sumsunga11.completeDetail)

# hifi=hifiphone('apple','pro',98000,8,'yes',5000)

# # hifi.fullname
# # print(help(hifiphone))

# print(isinstance(sumsunga11,hifiphone))
# print(issubclass(hifiphone,Phone))
# # print(help(hifiphone))

# import sqlite3

# con=sqlite3.connect("practical database.db")
# print("conneted successfully")
# cur=con.cursor()
# # cur.execute("create table Dictionary(id  int primary key autoincrement ,word text, meaning text)");
# # print("table created")
# # con.close()
# cur.execute("INSERT INTO Dictionary(id,word,meaning) values(1,deepak,diya)");
# print("data inserted...")
# con.commit()
# con.close()


# import sqlite3
# db=sqlite3.connect("deepak.db")
# cur=db.cursor()
# cur.execute("create table dictionary(word text ,meaning text)")
# # cur.execute("insert into dictionary(word,meaning) VALUES('doll','bool')");
# cur.execute("SELECT * FROM dictionary")
# for i in cur.fetchall():
#     print(i[0],i[1])

# cur.execute("DELETE FROM DICTIONARY WHERE  meaning='bool'")
# for i in cur.fetchall():
#     print(i[0],i[1])
# db.commit()
# # print("table inserted")
# db.close()


# def d():
#     for i in range(7):
#         yield i


# for i in d():
#     print(i)


# l=list(range(1,11))
# def sq(n):
#     return n*n
# l=map(sq,l)
# print(list(l))

# string="deepak"
# print(string[-1::-1])
# print(string[::-1])

# l=[
    
# from collections import namedtuple

# dost=namedtuple('friend',['aman','amit','hershit'])
# dost_no=dost(1,32,43)
# print(str(dost_no.amit))

# import json

# # a={
# #     'name':'deepak',
# #     'age':12,
# #     'class':'BCA'
# # }
# b=['deepak','aman']

# a=json.dumps(b)
# print(type(a))
# print(type(json.loads(a)))
# import requests,json
# import bs4
# a=requests.get('https://www.bing.com/images/search?q=image&form=HDRSC2&first=1&tsc=ImageBasicHover')
# soup=bs4.BeautifulSoup(a.text,'lxml')
# print(type(soup))
# a=soup.select('')
# print(a[0].getText())
a='deepak'
b='verma'
print(a+b)
print(a+""+b)
print(a+''+b)
