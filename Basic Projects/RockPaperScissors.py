''' ROCK ,PAPER, SCISSORS GAME '''

import random,time,sys
print('Dountless rockPaperScissor game'.center(200,'*'))
win=0
losses=0
tie=0
chance=9
gameover=False
while (not gameover):
    try:

        print(f"{tie} tie {chance} chance".center(100," "))

        computerChoice=random.choice(['r','p','s'])

        #user take
        while True:
            check=input("Enter (r)ock ,(p)aper,(s)cissors.....")
            if check=='r' or check=='p' or check=='s':
                userChoice=check
                break
            else:
                print("\ninvalid input\n")
        

        #user input section
        if userChoice=='r':
            print("Rock versus ")
        elif userChoice=='p':
            print("paper versus ")
        else:
            print("scissors  versus ")


        #computer input section
        if computerChoice=='r':
            print("Rock  ")
        elif computerChoice=='p':
            print("paper ")
        else:
            print("scissors ")


        #result section
        if userChoice==computerChoice:
            print('tie')
            tie+=1


        #win section
        elif userChoice=='r' and computerChoice=='s':
            print("you win!")
            win+=1
        elif userChoice=='p' and computerChoice=='r':
            print("you win!")
            win+=1
        elif userChoice=='s' and computerChoice=='p':
            print("you win!")
            win+=1


        # loss section
        elif userChoice=='r' and computerChoice=='p':
            print("you loss!")
            losses+=1
        elif userChoice=='p' and computerChoice=='s':
            print("you loss!")
            losses+=1

        elif userChoice=='s' and computerChoice=='r':
            print("you loss!")
            losses+=1


        #game over
        if chance==1:
            print("FINAL RESULT".center(200,"*"))
            print('wait..........')
            time.sleep(5)

            #get final result
            if win>losses:
                print("\n\t\t***CONGRATULATION***\n[YOU WIN!]\n".ljust(50," "))
                print(f"your  point{win}\t\tcomputer point{losses}")
            elif win==losses:
                print("\n\t\t\t\t\t****Draw****\t\t\t\n")
            else:
                print("\n\t\t****YOU LOSS!****\n".ljust(50," "))
                print(f"\n\t\tyour  point:{win}\t \tcomputer point:{losses}\n")
                
            #ask one more play 
            ask=input("you play again!..(y/n):")
            if ask=='y':
                win=0
                losses=0
                tie=0
                chance=10
            else:
                gameover=True
            
        chance-=1
    except KeyboardInterrupt:
        sys.exit()

    



        

    
    


    
    

