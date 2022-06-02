from tkinter import *
#from tkinter.ttk import *
import tkinter.font as tf
import functions as f
from time import sleep
from pygame import image

class GUI():
    def launch_game(root):
        root.destroy()
        sleep(0.1)
        f.main()
        
            
    def launch():
        font1= ("Impact",36,"bold")
        root=Tk()
        root.geometry('650x600+500+100')
        root.title("SPACE INVADERS LAUNCHER")
        #FRAMES 
        MAINFRAME = Frame(root)
        MAINFRAME.grid(column=1,row=1)
        MAINFRAME.configure(highlightthickness = 6,highlightbackground="red",bg= "black")
        FRAME1 = Frame(MAINFRAME).grid(column=1,row=1)
        FRAME2 = Frame(MAINFRAME).grid(column=1,row=5)
        
       # FRAME2.configure()
        #WIDGETS 
        title1 = Label (MAINFRAME,text="LAUNCHER FOR SPACE INVADERS",fg="yellow",bg="black")
        Canvas1 = Canvas(FRAME1,width=530,height=350,bg="black",highlightthickness=2)
        Canvas1.grid(column=1,row=2,sticky = SW)
        img_1= PhotoImage(file="asset2.png")
        img_2= PhotoImage(file="asset1.png")
        Canvas1.create_image(530,350,anchor=SE,image=img_1)
        Button1 = Button(FRAME2,text="Launch \n space invaders",bg="#01016b",fg="#fff705",height=100 , width= 300,highlightthickness=0 , image = img_2 , compound = LEFT , activebackground = "red",activeforeground = "cyan" , command= lambda : GUI.launch_game(root))
        Button1.grid(column=1,row=3,sticky="SW" , padx= 0 , pady= 10)
        title1.grid(column=1,row=1,pady=10)
        title1.configure(font=font1)
        root.configure(bg="black")
        root.mainloop()                
    #def main_menu():
GUI.launch()