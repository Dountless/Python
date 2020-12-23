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

class Bca:
    count_instance=0
    def __init__(self,name,age):
        Bca.count_instance+=1
        self.name=name
        self.age=age

    @classmethod
    def count(cls):
        return f"you have created {cls.count_instance} instance of {cls.__name__} class"


s1=Bca("deepak",16)
s2=Bca("aman",18)
s3=Bca("amit",16)
s4=Bca("herry",78)
print(Bca.count())
