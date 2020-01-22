from tkinter import *
import tkinter.messagebox
import speech_recognition as sr
import webbrowser

def voiceCon(): #will call this when the button is clicked
        r = sr.Recognizer()
        with sr.Microphone() as source:  #this code uses the mic.
            print("Speak Anything :")
            audio = r.listen(source) #this code saves the word that was given from the user (speech) to "text"
            text = r.recognize_google(audio)
        
            print("You said : {}".format(text))

            if text == "Google" or text == "google": 
                url = "http://www.google.com"
                webbrowser.open(url) 
                #text = "" #must be initialized, since the text saves the previous speech to text
               
            
            if text == "webtoon" or text == "Webtoon":
                url = "https://comic.naver.com/webtoon/list.nhn?titleId=670143&weekday=wed"
                webbrowser.open(url) 
                #text = "" 
            

            if text == "Naver" or text == "naver":
                url = "http://www.naver.com"
                webbrowser.open(url)
                #text = "" 
            
            if text == 'youtube' or text == 'Youtube':
                url = "http://www.youtube.com"
                webbrowser.open(url)
                #text = ""

            if text =='github' or text =='Github':
                url = "https://github.com/RelaxDanny?tab=repositories"
                webbrowser.open(url)
                #text = "" 

            else:
                repeat = 1 #if nothing is asked, exit.
                #text = ""

def explain():
    tkinter.messagebox.showinfo('Shortcut words','Naver, Google, Webtoon, Youtube, or Github')
    answer = tkinter.messagebox.askquestion('!!','Do you Understand?')
    if answer == 'yes':
        tkinter.messagebox.showinfo('!', 'Thanks')

def main():
    root = Tk()

    canvas = Canvas(root, width = 200, height = 100)
    canvas.pack()

# - - - - - - Inside the line - - - - - - - #
  #  blackLine = canvas.create_line(0, 2, 200, 2)

    background = PhotoImage(file="back.png") # cd github
    label = Label(root, image=background)
    label.pack()

 #   greenLine = canvas.create_line(0, 100, 200, 100, fill = "green")
# - - - - - - Inside the line - - - - - - - #


# - - - - - - Menu - - - - - - #
    menu = Menu(root)
    root.config(menu=menu) #this code makes a menu label 

    subMenu = Menu(menu, tearoff = 0)  #First Menu at the top-left // remove  "------" using tearoff = 0
    menu.add_cascade(label="Examples", menu=subMenu)
    subMenu.add_command(label="what kind of shortcuts...", command=explain)
    subMenu.add_separator() #this creates a line between the submenu
    subMenu.add_command(label="Exit", command=exit)

# - - - - - - - - - - - - - -#
    voiceButton = Button(root, text = "rxDanny", command = voiceCon)
    voiceButton.pack(side=LEFT)
    quitButton = Button(root, text = "Exit", command = quit)
    quitButton.pack(side=RIGHT)


    root.mainloop() 

main()