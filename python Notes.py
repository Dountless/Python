# # # TODO Expressions....
# # ''' operators...
# #     **
# #     /
# #     //
# #     %
# #     +
# #     -
# #     *

# # print(2+3*6 , (2+3)*6, 2**8 , 23/7, 23//7, 23%7, 2+  7)
# # print((5-1)*((7+1)/(3-1)))
# # '''
# # '''
# # TODO STRING CONCATINATION AND REPLICATION
# # #concatination
# # print("deepak"+' verma') # use only + operator 
# # #replication
# # print("deepak"*5)#only intiger value for replication not floating value

# # '''


# # '''
# # TODO FUNCTION....
# # input() :->take input from user
# # len(string) :-> return intiger value of lenghth of a string
# # str():-> convert intiger to string
# # int():->convert numeric string to intiger 
# # float():->convert float  string to float and int to float
# # round():->give roundoff floating no. and also use round(23.32651458,7) here 7 is how many round no...

# # '''

# # '''
# # TODO COMPARISION OPERATOR
# # ==
# # !=
# # <
# # >
# # <=
# # >=
# #  IT GIVE BOOLEAN VALUE ->TRUE YA FALSE
# #  '''

# # '''
# # # TODO FLOW CONTROL STATEMENT
# # # IF statement.............
# # if condition:
# #     statement

# # #ELSE statement............

# # else:
# #     statement

# # #ELIF statement...........
# # elif condition:
# #     statement

# # #WHILE LOOP..................
# # while condition:
# #     statement
# #     iteration #depend on condition

# # ex:->
# # i=0
# # while i<10:
# #     print(i)
# #     i+=1
    
# # name=''
# # while name!='deepak':
# #     print("enter name:->deepak")
# #     name=input()
# # print("thank you",name)

# # #NOTE:-> IF EMPTY STRING "" PUT IN CONDION THEN CONSIDERED A FALSE


# # #FOR LOOP...............

# # for i in range(20):
# #     print(i)

# # #NOTE:-> 1. range function give range of a number and bydefault number is 0 
# # #NOTE->also pass starting,stopping,stepping argument to range 
# # ex:->
# #     range(1,10,2)# starting=1,stopping=10,stepping=2 stepping meangs escape 2 value
# #     #NOTE:->stopping argument is EXCLUSIVE and strting is INCLUSVE

# # '''

# # '''
# # # TODO radom,sys module
# # random():-> it generate random item 
# # sys.exit():->it terminate the programme
# # abs():->it give the absolute number 0 to n ,n is a positive intiger 
# # '''


# # # TODO project1:->NUMBER GUESSING GAME
# # #TODO Project2:->ROCK,PAPER,SCISSORS



# # '''
# # #TODO FUNCTION

# # def fun(name):#name is a parameter
# #     statement

# # fun('deepak')#deepak is a argument
# # #NOTE:-> almost built-in function return NONE keyword e:->printf(),etc..
# # # NOTE:-> if u modified  variable globally then use keyword global before variable 
# # '''

# # '''
# # #TODO EXCEPTION HANDLING
# # try:
# #     statement # if you know here is error occuring
# # except error:  # use error if you know...
# #     statement

# # '''

# # #TODO Project zigzag animation...

# # '''
# # #TODO LIST 


# # LIST=["deepak",42,'aman',908.23]
# # # NOTE:-> WE CAM STORE ANY TYPE OF DATA IN LIST 
# # # LIST[0]:->  acess item in list by using indexing with square bracket 
# # #bydefault indexing number is 0
# # #List are orderd form 
# # # NOTE:-> you can access item only use intiger indexing floating not allow
# # # NOTE:->LIST[-1] it means last element of a list
# # # NOTE:->you can change item by using slicing or indexing ex:->List[2]='hamaridosti'
# # # NOTE:->USE STRING APPLIED FUNCTION IN A LIST 
# # # NOTE:->CONCATINATION EX:-> ['A,'D',43,'GG']+[1,2,'E',3]=>['A','D',43,'GG',1,2,'E',3] ALWAYS GIVE NEW LIST HAVE BOTH LIST ELEMENT
# # # NOTE:->REPLICATION EX:->[1,2,3]*2 ->[1,2,3,1,2,3] GVE NEW LIST 
# # # NOTE:->REMOVING element by using del method ex:->del LIST[1] it delete value in list not a list ..

# # # NOTE:->in or not in   keyword check in list have or not 
# # '''

# TODO LIST COMPREHENSION 

# list1=['deepk','aman','hershit']
# newList=[]
# for i in list1:
#     newList.append(i[::-1])

# print(newList)
# #by list cmprehension
# print([name[::-1] for name in list1])

# # '''
# # #TODO enumerate()

# # it work like a range but it give also a indexing but range not give so it is better to use instead of range()
# # ex:->
# #         pen=['blue','red','green'.'yellow']
# #         for i,j in enumerate(pen):
# #             print(i,j)
        
# # output:-> 0,blue
# #             1,red
# # '''


# # '''
# # #NOTE:->random.choice(list) it give a randomly any item in a list ...

# # # TODO METHOD IN LIST 
# #     list=[1.2.3.4]
# #   1 list.index("item"):-> it give index of a list itme
# # # 2 list.append(item):->it add item in last in list ...
# # # 3 list.insert(2,'fruits'):-> u can put item in between in list by using indexing here 2 is index and fruits is item to add in list 
# # # 4 list.remove("item"):-> you can remove item in a list easily 
# # # 5 list.sort():->u can sort item in a list 
# # # 6 list.reverse():-> you can reverse list ... 
# # # NOTE:->LIST  ARE MUTABLE BUT STRING ARE IMMUTABLE 

# # '''
# # '''
# # # TODO TUPLE 
# # # NOTE:->tuple are immutable 
# # write:->(1,2,3,4)  
# # # NOTE:->onle element in tuple look like :->(1,)

# # # NOTE:->list() it convert itterator to list ...
# # # NOTE:->tuple() it convert itterator to tuple
# # # NOTE:->id() it give the memory location id 


# # # NOTE:-> spam=[1,2,3] ctually spam point list not store a ctuall list spam have a id of a actual list and access that..
# # es:->> d=spam
# #     d and spam also point a list not store them , d and spam have id of one list same list

# # # NOTE:->d=copy.copy(spam) it means tha d have different id and it point a same list in different location , here copy is a module ..

# # '''


# # '''
# # #TODO DICTIONARY
# #  dictionary and list are same but have little difference 
# #  1. list are orderd and dictionary are  unorderd 
# #  2.list have a 1 item and acess by indexing list[1]
# #  3.dictionary have key:value pair and can acess like a list insteadt of indexing using key dict['key']
# #  # NOTE:-> dict.key() give key of dictionary and dic.values() give value of key in dictionary
# #  # NOTE:->dict.items() give key and value also ...


# #  # NOTE:->dict.get("hlo",0) it give a value of 'hlo' and if not exists in dict then give bydefault NONE but we pass 0 so it give 0 instead of None

# #  # NOTE:-> dict.setdefault("key",'value') is a shortcut of :->
# #     if key is not dict:
# #         dict['key']='value'
# # ex:->


# # l={
# #     '11th':200,
# #     '10th':300
# # }
# # print(l.setdefault('12th',800))
# # print(l)

# # '''
# # '''
# # #TODO nested dictionaries
# # # ex:->
# # friend={
# #     'deepak':{'iphone':2,'flat':5,'shoes':6},
# #     'hershit':{'iphone':4,'flat':1,'shoes':4},
# #     'aman':{'iphone':0,'flat':2,'shoes':10},
# #     'sahil':{'iphone':0,'flat':1,'shoes':1}
# # }

# # def totalbrought(dost,item):
# #     numitem=0
# #     for k,v in dost.items():
# #         numitem+=v.get(item,0)
# #     return numitem

# # print(totalbrought(friend,input("enter item:")))



# TODO DICTIONARY COMPREHENSION 
# # dicti={1:1,2:4,3:9}
# print({num:num**2 for num in range(1,11)})
# #if else in dict comp.
# # di={1:'odd',2:'even'}
# print({num:('even' if num%2==0 else 'odd') for num in range(1,11)})

# # '''

# # '''   
# # #TODO STRING

# # #STRING LITERAL
# # print("deepak 'ji' verma")#allow singlequote in double quote
# # print('deepak "ji" verma')#also allow double quote in single quotes
# # print("deepak "ji" verma")#syntax error
# # print('deepak 'ji' verma')#syntax error


# # TODO ESCAPE SEQUENCE
# # \':-> use to print ' single quote
# # \":->use to print double quote
# # \t:->use to print(a tab)
# # \n:->use to next  line
# # \\:->use to print single backword slash \

# # print("deepak \"ji\" verma")
# # '''
# # #RAW STRING
# # print(r"it is a mountain \\/\\/\\/\\/\//\"")
# # print(r"it is escape sequence \n \t \' \" ")

# # #multiline string in triple quote

# # '''
# #     deepak is a student of tulas and 
# #     doing study in bca department 

# # '''

# # '''

# # #STRING INDEXING 

# # # bydefault indexing start with zero 0 

# # #in and not in OPERATOR

# # print("ji" in "nehrujideepak")
# # print("ji" not in "nehru deepak")


# # #USEFUL STRING METHOD
# # stri='deepak'

# # stri.upper():->change in uppercase
# # stri.lower():->change in lowercase
# # stri.isupper():->give booleanvalue
# # stri.islower():->give booleanvalue


# # #useful isX() type method
# # isalpha():->return true if the string consists only of letters and isn't blank 
# # isalnum():->return true if the string consists only of letters and number and it isn't blank 
# # isdecimal():->return true if the string consists only of numeric character  and isn't blank 
# # isspace():->return true if the string consists only space ,tab newline  and isn't blank 
# # istittle():->return true if the string consists only of word that begin with an uppercase letter followed by only lowercase letters

# # '''



# # '''
# # # startswith() and endswith() methods

# # print("hello,world".startswith("hell"))
# # print("hello,world".endswith("rld"))

# # TODO join and split method 

# # print(','.join(['deepak','aman','kajal','hershit']))
# # '''join method convert the list of string in a single string 
# # and also seperated ',' and other symbol in a string 
# # '''
# # '''


# # print('deepak,aman,kajal,hershit,amit'.split(","))

# # #PARTITION METHOD
# # print("hlo my name is deepak".partition("name"))# it can devided by a string to three sub string .......





# # #rjust() , ljust() , center() method 

# # name='deepak'
# # print(name.rjust(50,'*'))
# # print(name.ljust(50,'*'))
# # print(name.center(50,'*'))


# # # lstrip(),rstrip(),strip()

# # print('  deepak  '.strip())
# # print('vermadeepakjiverma'.strip("verma"))

# # print('  deepak  '.rstrip())
# # print('  deepak  '.lstrip())

# # # ord() and chr() 
# # ord():-> to use convert character to intiger value
# # chr():-> to use convert the intiger to anhi unique code value 

# # print(ord('f'))
# # print(chr(ord('f')))
# # print(chr(65+32))



# # import pyperclip
# # # pyperclip.copy("my name is deepak ")


# # print(pyperclip.paste())



# # experiment:->>>>>>>>>>>>>
# # import pyperclip
# # while True:
# #     print(pyperclip.paste())

#TODO LAMBDA

# # a=lambda s: 'kutta hai tu ' if len(s)>5 else 'ab nahi hai kutta'
# # print(a('deepak ji'))


# # ex:->lambda 
# # a=lambda n:'even' if n%2==0 else 'odd'
# # print(a(8))


#TODO ARGS
# # def addTo(*args):  #acc. to convention u take args name variable after * operator
# #     t=0
# #     for i in args:
# #         t+=i

# #     return t

# # print(addTo(1,2,3,4,5))

# # def multi(*args):
# #     mu=1
# #     for i in args:
# #         mu*=i
# #     return mu
# # l=[1,2,3,4]
# # print(multi(*l))# it unpack the list 









# #TODO **kwargs

# #NOTE:->

# # def name(**kwargs):
# # #     print(kwargs)

# # # name(a='deepak',b='aman')

# # #NOTE:2-> unpacking kwargs
# # def di(**kwargs):
# #     print(kwargs)

# # ld={
# #     'a':'deepak',
# #     'b':'aman',
# #     'c':90
# # }

# # di(**ld)
# # ld={
# #     1:'deepak',
# #     2:'aman',
# #     3:'hershit'
# # }
# # print(ld)

# # #TODO EXERSICE
# # def takelist(l1,**kwargs):
#     # if kwargs.get('reverse')==True:
#     #     return [i[::-1].title() for i in l1]
#     # else:
#     #     return [i.title() for i  in l1]
# #     return [i[::-1].title() if kwargs.get('reverse')==True else i.title() for i in l1]


# # print(takelist(['deepak','aman','hershit'],reverse=True))        

# # # ex:->3 ,
# # l=[True,False,1,'deepak',2,3,2.4,'aman',5,'a',1.02,6,3,5]

# # def num_set(l1):
# #     # s=[]
# #     # for item in l1:
# #     #     if type(item)==int:
# #     #         s.append(item)
# #     # return s 
# #     return [item for item in l1 if type(item)==int]

# # print(num_set(l))

#TODO PARAMETER ORDER
# # #NOTE:->order of parameter in function 
# # PADK
# # P=norml parameter
# # A=*args
# # D=default parameter like name='unkonown'
# # K=**kwargs

#TODO CUSTOM MODULE

# # import dount# it find module in existing directory  if true otherwise find all os directory 

# # print(dount.add(1,5,4,7,8))
# # print(dount.mul(1,2,3,4))




# TODO EXERSICE :->CALENDER
# # import calendar
# # weeks=['mon','teu','wed','thu','fri','sat','sun']
# # a=input("enter date:(year/month/date):").split("/")
# # # print(a)
# # d=calendar.weekday(int(a[0]),int(a[1]),int(a[2]))

# # print(weeks[d])



    
#####################################################################################################################################
# #TODO pathlib                 *****************************************
# from pathlib import Path
# print(Path('deepak','aman','hlo'))#it will make the path according to operating system ......
# #NOTE:-> '/ ' to use join path in window ....
# from pathlib import Path

# # Setup a path first
# path = Path("hello.py")
# print(path)

# # To get the home directory of the
# # current user
# print(path.home())
# print(path.exists())


# # To check whether the path represents a path
# # to file
# print(path.is_file())
# # To check whether the path represents a path
# # to the directory
# print(path.is_dir())
# # To get the suffix of the path
# print(path.suffix)  # extension of the file

# # To get the the name of the file on which the path is setup
# # without the suffix
# print(path.stem)

# # The parent of the file
# # on which we set up the path object
# print(path.parent)

# #  absolute path for the file hello.py
# print(path.absolute())

# # ......................................................../

# import os
# os.makedirs('D:\\DEEPK')
from pathlib import Path
print(Path.cwd())
print(Path.absolute(Path.cwd())) 
##################################################################################################################################

