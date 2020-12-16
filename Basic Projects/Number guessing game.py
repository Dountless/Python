import random,sys
name='\tDOUNTLESS NUMBER GUESS GAME\t'
print(name.center(len(name)+110,"*"))

def oneMorePlay():
    decision=input("try one more?(y/n):->")
    if decision=='y':
        chanceGuess()
        return
    sys.exit()
def chanceGuess():
    global secrtNo
    secrtNo=random.randint(0,20)
    global chance
    chance=8
    global guesstake
    guesstake=0

chanceGuess()#creat chance and guessing number
while True:
    print("\t\t\t\t\t[%s chance %s guess]"%(chance,guesstake))
    chance-=1
    #user input
    try:
        userno=int(input("Guess the number between 0 to 20:->"))
        if userno<=20 and userno>=0:  #if number is between 0 to 20    
            #result
            if chance==0:
                print(f"\nNope! number is {secrtNo} ....You Lose!..")
                #asking one more play game
                oneMorePlay()
            elif userno>secrtNo:
                print("number is too high..")
            elif userno<secrtNo:
                print("number is too low.. ")
            else:
                print(f"you win! and you guess {guesstake} times")
                #asking one more play game
                oneMorePlay()
            guesstake+=1
        else:
            print("input number between 0 to 20 only ......")
    except KeyboardInterrupt:
        sys.exit()
    except ValueError:
        print("\n\t\t\t\t\t****only intiger number allows****\n")

    
