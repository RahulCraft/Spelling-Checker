                     #Project 1.#


""" Project of Speling Checker using Python Code"""

from textblob import TextBlob

"""
TextBlob:- TextBlob is a module or Python Library
           that is very easy to use for processing text data.

Working Processing:
1) pip install TextBlob
2) import TextBlob
3) Logic:-

   obj=TextBlob("daataa")
   print(obj.correct())
"""
from tkinter import *


    

#def main_window():
scr = Tk()
scr.geometry("510x390")
scr.config(bg="blue")
scr.title("Spelling Checker")

def correct_spelling():
    get_data=e1.get()
    corr = TextBlob(get_data)
    data =corr.correct()
    e2.delete(0,END)
    e2.insert(0,data)

# make label for Incorrect Spelling and Correct Spelling text
Label1 = Label(scr,text="Incorrect Spelling",font=("Time New Roman",25,"bold"),
                   bg="blue",fg="white")
Label1.place(x=100,y=25,height=50,width=300)

# make Entry for label1 for input Incorrect Spelling text
e1 = Entry(scr,font=("Time New Roman",20,"bold"))
e1.place(x=50,y=80,height=50,width=400)

# make label for Incorrect Spelling and Correct Spelling text
Label2 = Label(scr,text="Correct Spelling",font=("Time New Roman",25,"bold"),
                   bg="Blue",fg="white")
Label2.place(x=100,y=225,height=50,width=300)

# make Entry for label2 for correct Spelling text
e2 = Entry(scr,font=("Time New Roman",20,"bold"))
e2.place(x=50,y=280,height=50,width=400)

# create button for Action for currect spelling 
button = Button(scr,text="Submit",font=("Time New Roman",20,"bold"),
                    bg="yellow",command=correct_spelling)
button.place(x=150,y=160,height=50,width=200)


scr.mainloop()


#main_window()
    
    
