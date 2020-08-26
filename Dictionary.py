from tkinter import *
from tkinter import messagebox
import json
from difflib import get_close_matches
import pyttsx3
#pip install pillow for jpg image

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id )

#To change the speed of voice
rate = engine.getProperty('rate')
engine.setProperty('rate',150)

def wordaudio():
      engine.say(enterwordentry.get())
      engine.runAndWait()

def meaningaudio():
      engine.say(textarea.get(1.0,END))
      engine.runAndWait()


def iexit():
      res = messagebox.askyesno('CONFIRM', 'Do You Want To Exit?')
      if res==True:
            root.destroy()
      else:
            pass
def clear():
      textarea.config(state=NORMAL)
      enterwordentry.delete(0,END)
      textarea.delete(1.0,END)
      textarea.config(state=DISABLED)

def search():
      data = json.load(open('data.json'))
      word = enterwordentry.get()
      word = word.lower()
      if word in data:
            meaning = data[word]
            textarea.config(state=NORMAL)
            textarea.delete(1.0,END)
            for item in meaning:
                  textarea.insert(END ,"-"+item+"\n\n")
            textarea.config(state=DISABLED)

      elif len(get_close_matches(word , data.keys()))>0:
            close_match = get_close_matches(word , data.keys() ,n=1 ,cutoff=0.7)[0]
            res = messagebox.askyesno('Confirm',"Did you mean  " +close_match+ ' instead?')
            if res==True:
                  meaning = data[close_match]
                  textarea.delete(1.0,END)
                  textarea.config(state=NORMAL)
                  for item in meaning:
                        textarea.insert(END ,"-"+item+"\n\n" )
                  textarea.config(state=DISABLED)
            else:
                  textarea.delete(1.0,END)
                  messagebox.showinfo('Information',"Word doesn't exist")
                  enterwordentry.delete(0,END)

      else:
            messagebox.showerror('Error' , "Word doesn't exist. Please check it.")

root = Tk()
root.geometry('1000x626+100+50')
root.title("Talking Dictionary")
root.resizable(0,0)

#Background Image
bg_image = PhotoImage(file='bg.png')
bg_label = Label(root , image = bg_image)
bg_label.place(x = 0 , y = 0)

#Text
enterwordlabel = Label(root , text='Enter The Word' , font = ('castellar',25,'bold'), fg='red',bg='whitesmoke')
enterwordlabel.place(x=530 , y=40)

#Input Box
enterwordentry = Entry(root , font = ('arial',23,'bold'),bd=8 , relief=GROOVE,justify=CENTER)
enterwordentry.place(x=530,y=100)
enterwordentry.focus_set()

#SearchBotton
searchimage = PhotoImage(file="search.png")
searchButton = Button(root,image=searchimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor = 'hand2',
                      command=search)
searchButton.place(x=628,y=160)

#MicButton
micimage = PhotoImage(file="mic.png")
micButton = Button(root,image=micimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor = 'hand2',
                   command=wordaudio)
micButton.place(x=710,y=163)

#Text
MeaningLabel = Label(root , text ="Meaning" , font = ('casteller',25 , 'bold') , fg='red',bg='whitesmoke')
MeaningLabel.place(x = 630 ,y=240)

#Text Output Area
textarea = Text(root,font=('arial',18,'bold') , height=8,width=30 , bd=8 , relief=GROOVE , wrap='word')
textarea.place(x = 510 , y=300)

#Audio Button
audioimage = PhotoImage(file="microphone.png")
audioButton = Button(root,image=audioimage , bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor = 'hand2',
                     command=meaningaudio)
audioButton.place(x=550,y=555)

#clear Button
clearimage = PhotoImage(file="clear.png")
clearButton = Button(root,image=clearimage , bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor = 'hand2',
                     command = clear)
clearButton.place(x=660,y=555)

#Exit Button
exitimage = PhotoImage(file="exit.png")
exitButton = Button(root,image=exitimage , bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor = 'hand2' , command=iexit)
exitButton.place(x=770,y=555)

root.mainloop()
