import sys
import sqlite3

Title="-:WELCOME TO DOUNTLESS DICTIONARY:-"
print(Title.center(len(Title)+100,"-"))

#connect sqlite to database and creat table
db=sqlite3.connect("Dictionary.db")
cur=db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS WORD_MEANING_DATA(ID INTEGER PRIMARY KEY AUTOINCREMENT,WORD TEXT,MEANING TEXT)")

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
 
        cur.execute("SELECT * FROM WORD_MEANING_DATA")
        print("No. Word")
        for i in cur.fetchall():
            print(f"{i[0]}.  {i[1]}")
          
    def addWord(self,word):
        '''add any word in dictionary'''
        #user input
        X=word
        if X:
            Y=input("Enter meaning:->")
            if Y:
                cur.execute("INSERT INTO WORD_MEANING_DATA(word,meaning) VALUES('"+X+"','"+Y+"')")
                confirm=input("Save:(y/n)")
                #save word and meaning
                if confirm.lower()=='y':
                    db.commit()
                    print("Added Sucessfully...")
                elif confirm.lower()=='n':
                    print("\t\t\tOk.......")
            else:
                print("You dont type anything...")
        else:
            print("You dont type anything..")
       
                
    def deletedictionary(self):
        #enter index of word for delete....
        try:
            INDEX=int(input("enter index number of word:->"))
            cur.execute("DELETE FROM WORD_MEANING_DATA WHERE ID=?",(INDEX, ))
            db.commit()
            print("\n\t\t\tDelete Successfully......")
        except ValueError:
            print("\t\t\tEnter only index number...".upper())

    def searchWord(self):
        '''search word and give meaning of that word'''
        cur.execute("SELECT * FROM WORD_MEANING_DATA")
        print("Word\tMeaning")
        #show word meaning
        for i in cur.fetchall():
            print(f"{i[0]}.{i[1]}")
        #enter word for search....
        try:
         i=int(input("enter index of word:->".upper()))
        except ValueError:
            print("Enter only index number...")
        
        cur.execute("SELECT * FROM WORD_MEANING_DATA")
        #print meaning of word.....
        for j in cur.fetchall():
            if j[0]==i:
                print(f"Meaning of {j[1]}:->{j[2]}")
            

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
                Dict.showDict()
                Dict.deletedictionary()
            elif ch==4:
                Dict.searchWord()
            elif ch==5:
                db.close()
                sys.exit()
            else:
                print("\n\t\t invalid number .. Enter Given choice No\n")
    except KeyboardInterrupt:
        db.close()
        sys.exit()