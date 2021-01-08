# TODO: adding bullets to wiki markup
import os,pyperclip
from csv import DictWriter
os.system("echo off | clip")#used to empty clipboard
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