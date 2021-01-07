
import sys
#ask user to play or not
def OneMorePlay():
    while True:

        check=input("You want to play again!(Y/N):->")
        if check=='Y' or check=='y':
            return
        elif check=='N' or check=='n':
            sys.exit()
        else:
            print("only type Y or N")

#print data for user
def printDetail():
    while True:
        print("Enter name:->>>>")
        p1=input("Player 1:->")
        p2=input("Player 2:->")
        #check alphabate or not
        if all((p1.isalpha(),p2.isalpha()))==True:
            player[0]=p1
            player[1]=p2
            print(f"{player[0]} use X \n{player[1]} use O \n press s for play")
            print(" 1 | 2 | 3 ")
            print("___|___|___")
            print(" 4 | 5 | 6 ")
            print("___|___|___")
            print(" 7 | 8 | 9 ")
            print("   |   |   ")
            
            #for start a game permision
            while True:
                flag=input("start game:(s):->")
                if flag=='s' or flag=='S':
                    return flag
                else:
                    print("Enter s for start game:-...")
        else:
            print("\nEnter name only alphabate form... ")
        
#draw table while playing
def drawTable(a):
    print(a[1],'  |  ',a[2],'| ',a[3],"\t\t"," 1 | 2 | 3 ")
    print("____|_____|____")
    print(a[4],'  |  ',a[5],'| ',a[6],"\t\t"," 4 | 5 | 6 ")
    print("____|_____|____")
    print(a[7],'  |  ',a[8],'| ',a[9],"\t\t"," 7 | 8 | 9 ")
    print("    |     |   ")

#check winn or not
def checkWinner(v):
    for i in winner_conditions:
            if (pos[i[0]],pos[i[1]],pos[i[2]])==(v,v,v) :
                return 'Winner'


#start game
def startGame():
    turn=0#for first player
    for i in range(9):
        if turn%2==0:#chenge value 1,0
            
            # check X or not
            while True: 
                v=input(f"{player[0]} your turn:->").upper()#take X
                if v=='X':
                    try:
                        p=int(input("enter position"))#take position
                        pos[p]=v#assign X in board
                        drawTable(pos)
                        w=checkWinner(v)#check win or not
                        if w=='Winner':
                            print(f"{player[0]} You win..Congratulation..")
                            OneMorePlay()
                            return
                        else:
                                turn=1
                                break
                    except ValueError:
                        print("\nEnter intiger number for positions...")
                else:
                    print("\nEnter X only...")
            
        else:
            # check O or not
            while True:
                v=input(f"{player[1]} your turn:->").upper()#take O
                if v=='O':
                    try:
                        p=int(input("enter position"))#take position
                        pos[p]=v#assign O in board
                        drawTable(pos)
                        w=checkWinner(v)#check win or not
                        if w=='Winner':
                            print(f"{player[1]} You win..Congratulation..")
                            OneMorePlay()
                            return
                        else:
                            turn=0
                            break 
                    except ValueError:
                        print("\nEnter intiger number for positions...")
                        
                else:
                       print("\nEnter O only...")      


if __name__ == "__main__":
    while True:
        player=["",""]
        pos=[" "," "," "," "," "," "," "," "," "," "]
        winner_conditions=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(3,5,7),(1,5,9)]
        flag=printDetail()
        if flag=='s' or flag=='S':
            try:
                startGame()
            except KeyboardInterrupt:
                sys.exit()
        


