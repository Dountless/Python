import sys,os
from csv import DictReader,DictWriter

Title="-:WELCOME TO DOUNTLESS DICTIONARY:-"
print(Title.center(len(Title)+100,"-"))

class Dictionary:

    def Template(self,i):
        '''show the menue of dictionary'''
        #show options
        print("".center(150,"-"))
        print("\n [show dictionary_words:->1] [add dictionary:->2]  [delete dictionary:->3] \
            [search_word:->4] [quit dictionary:->5]")
        print("".center(150,"-"))
        #check user is correct or not 
        try:
            return int(input("Enter number for choice:->"))
        except ValueError:
            print("\n\t\t\t\t-----YOU DON'T TYPE ANY Choice Number------\t\n")

    def showDict(self):
        '''show the word of dictionary'''
        try:

            with open('dict.csv','r') as f:
                #object..iterator
                show_dict=DictReader(f)
                #check dict is empty or not
                if os.stat('dict.csv').st_size==0:
                    # styl to print message
                    x='Dictionary is Empty'
                    print(x.center(len(x)+100,"-"))
                else:
                    print("Word is :->",end="")
                    for i in show_dict:
                        print(i['Word'],end=",")
        except FileNotFoundError:
            print("\nDictionary is empty .....\n")
        return 1

            
    def addWord(self,word):
        '''add any word in dictionary'''
        #open file
        with open('dict.csv','a',newline="") as f:
            add_word=DictWriter(f,fieldnames=['Word','Meaning'])
            #check dict is empty or not
            if os.stat("dict.csv").st_size==0:
                add_word.writeheader()
                #add word to dictionary
            if word=="":
                print("\n\t\t\t\t-----YOU DON'T TYPE ANY WORD------\t\n")
            add_word.writerow({
                    'Word':word,
                    'Meaning':input(f"Enter meaning of {word}:->").lower()
                    })
            print("\n\t\t\t\tAdded Successfully...")
            
                
    def deletedictionary(self):
        '''delete whole word ,meaning in dictionary'''
        #open dictionary
        with open("dict.csv",'w') as f:
            pass

    def searchWord(self,word):
        '''search word and give meaning of that word'''
        #open dictionary
        with open("dict.csv") as f:
            mix_dict=DictReader(f)
            for i in mix_dict:
                if word in i.values():
                    print(f"Meaning is:-> {i.get('Meaning')}\n")
                    break
            else:
                print("\n\t\tNOT FOUND !")
    


if __name__=="__main__":
    
    try:

        while True:
            #user choice number
            Dict=Dictionary()
            ch=Dict.Template(input("\n\n\t\t\t\t\t\t\t\t\t\tpress Enter...\n\n\n\n"))

            if ch==1:
                Dict.showDict()
            elif ch==2:
                Dict.addWord(input("Enter word:"))
            elif ch==3:
                Dict.deletedictionary()
                print("\n\t\t\tDelete Successfully......")
            elif ch==4:
                if Dict.showDict()==None:
                    continue
                Dict.searchWord(input("\nEnter word:"))
            elif ch==5:
                sys.exit()
            else:
                print("\n\t\t invalid number .. Enter Given choice No\n")
    except KeyboardInterrupt:
        sys.exit()