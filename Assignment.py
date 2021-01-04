#TODO PRIME NUMBER

#  n=int(input("enter a number to check is prime or not"))
# if n>1:
#     for i in range(2,n):
#         if(n%i==0):
#             print("no. is not a prime")
#             break
#     else:
#         print("number is a prime")

#TODO RANGE OF PRIME NUMBER
# n1,n2=input("enter to number by comma seperated:>").split(",")
# for number in range(int(n1),int(n2)+1):
#     if number>1:
#         for j in range(2,number):
#             if number%j==0:
#                 break
#         else:
#             print(number)


#TODO FACTORIAL OF A NUMBER

# no=int(input("enter a number:->"))
# factorial=1
# for i in range(1,no+1):
#     if no==0:
#         factorial=1
#     else:

#         factorial*=i

# print(factorial)

# TODO MATRICES 
# [[1,2],[4,2]]
# ROW=int(input("enter a number of ROW:->"))
# COLOUMN=int(input("enter a number of COLOUMN:->"))
# print(f"enter {ROW*COLOUMN} element in matrices:->")
# Matrices=[]
# for i in range(ROW):
#     a=[]
#     for i in range(COLOUMN):
#         a.append(int(input()))
#     Matrices.append(a)

# for i in range(ROW):
#     for j in range(COLOUMN):
#         print(Matrices[i][j],end=" ")
#     print()


#TODO palindrome number
# n=input("enter a number")
# if n==n[::-1]:
#     print("number is palindrome")
# else: 
#     print("not a palindrome")


#TODO Armstrome number
n=input("enter a number:->")
x=0
for i in n:
    x=x+int(i)**3
if x==int(n):
    print(f"{n} is a armstrome number")
