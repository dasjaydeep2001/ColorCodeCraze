import tkinter as tk 
from tkinter import *
import random
import tkinter.messagebox














def check():
    global n, answer,ch1,ch2,ch3,ch4,correct
    cnt=0
    cnt=(ch1.get()==answer[0])+(ch2.get()==answer[1])+(ch3.get()==answer[2])+(ch4.get()==answer[3])
    chances=n.get()
    print(ch1.get(),",",ch2.get(),",",ch3.get(),",",ch4.get())
    print(cnt)
    if(chances>0):
        if(cnt==0):
            correct.set(0)
        elif(cnt==1):
            correct.set(1)
        elif(cnt==2):
            correct.set(2)
        elif(cnt==3):
            correct.set(3)
        elif(cnt==4):
            n=0
            tkinter.messagebox.showinfo("Congratulations, you have guessed it right !")
            return
        chances-=1
        n.set(chances)

    else:
        chances-=1
        print(n.get())
        if(chances<=0):
            l=['red','blue','green','yellow']
            ans=l[answer[0]-1]+","+l[answer[1]-1]+","+l[answer[2]-1]+","+l[answer[3]-1]
            tkinter.messagebox.showinfo("The correct answer is "+ans+".Beter luck next time")
            return
        n.set(chances)

        return 0
    















    def startGame():
        global n,answer,ch1,ch2,ch3,ch4,correct
        wn=Tk()
        wn.title("JD Mastermind Game")
        wn.geometry('700x500')
        wn.config(bg='SlateGray1')
        n=IntVar(wn)
        n.set(5)
        correct=IntVar(wn)
        correct.set(0)
        ch1=IntVar(wn)
        ch2=IntVar(wn)
        ch3=IntVar(wn)
        ch4=IntVar(wn)
        answer=[]
        for i in range(0,4):
            answer.append(random.randint(1,4))
            print(answer)
            #Getting the input of word from the user
            Label(wn,text='please make your choice',bg='SlateGray1',font=('caliber',10,'normal'),anchor="e",justify=LEFT).grid(row=3,column=1,pady=20)
            red1=Radiobutton(wn,text="Red",value=1,bg='SlateGray1',fg='red',variable=ch1,font=('caliber',12,'normal')).grid(row=4,coloum=1,padx=20,sticky=W,pady=10)
            blue1=Radiobutton(wn,text="Blue",value=2,bg='SlateGray1',fg='blue',variable=ch1,font=('caliber',12,'normal')).grid(row=4,coloum=2,sticky=W,pady=10)
            green1=Radiobutton(wn,text="Green",value=3,bg='SlateGray1',fg='green',variable=ch1,font=('caliber',12,'normal')).grid(row=4,coloum=3,padx=80,sticky=W,pady=10)
            
            
            








            red2=Radiobutton(wn,text="Red",value=1,bg='SlateGray1',fg='red',variable=ch2,font=('caliber',12,'normal')).grid(row=5,coloum=1,padx=20,sticky=W,pady=10)
            blue2=Radiobutton(wn,text="Blue",value=2,bg='SlateGray1',fg='blue',variable=ch2,font=('caliber',12,'normal')).grid(row=5,coloum=2,sticky=W,pady=10)
            green2=Radiobutton(wn,text="Green",value=3,bg='SlateGray1',fg='green',variable=ch2,font=('caliber',12,'normal')).grid(row=5,coloum=3,padx=80,sticky=W,pady=10)
            yellow2=Radiobutton(wn,text="Yellow",value=4,bg='SlateGray1',fg='yellow',variable=ch2,font=('caliber',12,'normal')).grid(row=5,coloum=4,padx=20,sticky=W,pady=10)



            red3=Radiobutton(wn,text="Red",value=1,bg='SlateGray1',fg='red',variable=ch3,font=('caliber',12,'normal')).grid(row=6,coloum=1,padx=20,sticky=W,pady=10)
            blue3=Radiobutton(wn,text="Blue",value=2,bg='SlateGray1',fg='blue',variable=ch3,font=('caliber',12,'normal')).grid(row=6,coloum=2,sticky=W,pady=10)
            green3=Radiobutton(wn,text="Green",value=3,bg='SlateGray1',fg='green',variable=ch3,font=('caliber',12,'normal')).grid(row=6,coloum=3,padx=80,sticky=W,pady=10)
            yellow3=Radiobutton(wn,text="Yellow",value=4,bg='SlateGray1',fg='yellow',variable=ch3,font=('caliber',12,'normal')).grid(row=6,coloum=4,padx=20,sticky=W,pady=10)



            red4=Radiobutton(wn,text="Red",value=1,bg='SlateGray1',fg='red',variable=ch4,font=('caliber',12,'normal')).grid(row=7,coloum=1,padx=20,sticky=W,pady=10)
            blue4=Radiobutton(wn,text="Blue",value=2,bg='SlateGray1',fg='blue',variable=ch4,font=('caliber',12,'normal')).grid(row=7,coloum=2,sticky=W,pady=10)
            green4=Radiobutton(wn,text="Green",value=3,bg='SlateGray1',fg='green',variable=ch4,font=('caliber',12,'normal')).grid(row=7,coloum=3,padx=80,sticky=W,pady=10)
            yellow4=Radiobutton(wn,text="Yellow",value=4,bg='SlateGray1',fg='yellow',variable=ch4,font=('caliber',12,'normal')).grid(row=7,coloum=4,padx=20,sticky=W,pady=10)

            Label(wn,text='No of chances left',bg='SlateGray1',font=('calibre',12,'normal'),anchor="e",justify=LEFT)
            Label(wn,textvariable=n,bg='SlateGray1',font=('calibre',12,'normal'),anchor="e",justify=LEFT)
            Label(wn,text='No of correct choices',bg='SlateGray1',font=('calibre',12,'normal'),anchor="e",justify=LEFT)
            #Button to do the spell check
            Label(wn,textvariable=correct,bg='SlateGray1',font=('calibre',12,'normal'),anchor="e",justify=LEFT)   

            Button(wn,text="Check",bg='SlateGray4',font=('calibre',13),command=check).grid(row=11,colummn=3)   

            #Runs the window till it is closed by the user
            wn.mainloop()  


            #Createing the window
            wn=Tk()
            wn.title("Mastermind Game")
            wn.geometry('500x300')
            wn.config(bg='SlateGray1')
            answer=[]
            #creating the variables to get the word and set the correct word 
            n=IntVar(wn)
            correct=IntVar(wn)
            n.set(5)
            correct.set(0)
            ch1=IntVar(wn)
            ch2=IntVar(wn)
            ch3=IntVar(wn)
            ch4=IntVar(wn)
            Label(wn,text='Please make your choice',bg='SlateGray1',font=('calibre',20,'normal'),anchor="e",justify=LEFT).place(x=100,y=20)
            Button(wn,text="start Game",bg='SlateGray4',font=('calibre',13),command=startGame).place(x=180,y=100)

            wn.mainloop()
