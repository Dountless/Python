# #TODO PRIME NUMBER

# #  n=int(input("enter a number to check is prime or not"))
# # if n>1:
# #     for i in range(2,n):
# #         if(n%i==0):
# #             print("no. is not a prime")
# #             break
# #     else:
# #         print("number is a prime")

# #TODO RANGE OF PRIME NUMBER
# # n1,n2=input("enter to number by comma seperated:>").split(",")
# # for number in range(int(n1),int(n2)+1):
# #     if number>1:
# #         for j in range(2,number):
# #             if number%j==0:
# #                 break
# #         else:
# #             print(number)


# #TODO FACTORIAL OF A NUMBER

# # no=int(input("enter a number:->"))
# # factorial=1
# # for i in range(1,no+1):
# #     if no==0:
# #         factorial=1
# #     else:

# #         factorial*=i

# # print(factorial)

# # TODO MATRICES 
# # [[1,2],[4,2]]
# # ROW=int(input("enter a number of ROW:->"))
# # COLOUMN=int(input("enter a number of COLOUMN:->"))
# # print(f"enter {ROW*COLOUMN} element in matrices:->")
# # Matrices=[]
# # for i in range(ROW):
# #     a=[]
# #     for i in range(COLOUMN):
# #         a.append(int(input()))
# #     Matrices.append(a)

# # for i in range(ROW):
# #     for j in range(COLOUMN):
# #         print(Matrices[i][j],end=" ")
# #     print()


# #TODO palindrome number
# # n=input("enter a number")
# # if n==n[::-1]:
# #     print("number is palindrome")
# # else: 
# #     print("not a palindrome")


# #TODO Armstrome number
# # n=input("enter a number:->")
# # x=0
# # for i in n:
# #     x=x+int(i)**3
# # if x==int(n):  
# #     print(f"{n} is a armstrome number")

# #NOTE:->What are the benefits of using python?
#         the benifits of using python are that it is simple and easy,
#         portable,extensible,build-in data structure and it is an open source .
#         Most important is that python comes with lots of libraries.

# # NOTE:->What is PEP 8?
#         PEP 8 is a coding cconvention,a set of recommendation,about how to write 
#         your python code more readable.
        
#                 Naming Styles
#         The table below outlines some of the common naming styles in Python code and when you should use them:

#         Type	Naming Convention	Examples
#         Function	Use a lowercase word or words. Separate words by underscores to improve readability.	function, my_function

#         Variable	Use a lowercase single letter, word, or words. Separate words with underscores to improve readability.	x, var, my_variable

#         Class	Start each word with a capital letter. Do not separate words with underscores. This style is called camel case.	Model, MyClass

#         Method	Use a lowercase word or words. Separate words with underscores to improve readability.	class_method, method

#         Constant	Use an uppercase single letter, word, or words. Separate words with underscores to improve readability.	CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT

#         Module	Use a short, lowercase word or words. Separate words with underscores to improve readability.	module.py, my_module.py

#         Package	Use a short, lowercase word or words. Do not separate words with underscores.	package, mypackage


# #NOTE:->How memory is manage in python?
#     Python memory is manage by python private heap space. ALL python object 
#     and datastructure are located in private heap. the programmer does not 
#     have an access to this private heap and interpreter takes care of this python
#     private heap.the allocation of python heap space for python object is done by 
#     python memory manager.The core API give access to some tools for the programmer
#     to code .python also have a built-in garbage collector,which recycle all 
#     the unused memory and frees the memory and makes it available to heap spaces.
    


# # # TODO automatic copy-paste projet
# import sys,pyperclip
# text={
#         'deepak':'this is a devops engineer',
#         'aman':'this is a software dovoloper'
# }

# if len(sys.argv)<2:
#         print("use :python auto.py [keypharse]-copy pharase text");
#         sys.exit()
# key=sys.argv[1]#enter one argument only
# if key in text:
#         pyperclip.copy(text[key])
#         print("copy sucessful")
# else:
#         print("there is no text")


# TODO: adding bullets to wiki markup
import os,pyperclip
from csv import DictWriter
# os.system("echo off | clip")
t=pyperclip.paste()
index=0
while True:
        t=pyperclip.paste()
        if t!="":
                lines=t.split("\n")
                # for i in range(1):
                #         lines[i]=f"{index}:-> "+lines[i]
                with open("copylist.txt",'a',newline="") as f:
                        f=DictWriter(f,fieldnames=['S.No','lines'],delimiter="-")
                        if os.stat("copylist.txt").st_size==0:
                                f.writeheader()
                        f.writerow({
                                'S.No':index,
                                'lines':str(lines[0])
                        })
                        print("copy and paste successfuly..")
                        os.system("echo off | clip")#used to blank the clipboard
                        index+=1
                       

                
                
                

        




        