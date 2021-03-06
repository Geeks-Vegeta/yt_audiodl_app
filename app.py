
from __future__ import unicode_literals
from tkinter import *
from tkinter.ttk import Progressbar
import threading,time
from threading import Thread
from PIL import ImageTk
from PIL import *
import tkinter.messagebox
import youtube_dl


#workon venv

class Youtubes:
    def __init__(self,root):
        self.root=root
        self.root.title("Youtube mp3 Downloader")
        self.root.geometry("500x300")
        self.root.resizable(0,0)
        self.root.iconbitmap("abyou.ico")




        urls=StringVar()



        def on_enter1(e):
            Down_but['background']="black"
            Down_but['foreground']="cyan"  
        def on_leave1(e):
            Down_but['background']="SystemButtonFace"
            Down_but['foreground']="SystemButtonText"

            

        def on_enter2(e):
            Clear_but['background']="black"
            Clear_but['foreground']="cyan"  
        def on_leave2(e):
            Clear_but['background']="SystemButtonFace"
            Clear_but['foreground']="SystemButtonText"
            


        def on_enter3(e):
            Down_but_audio['background']="black"
            Down_but_audio['foreground']="cyan"  
        def on_leave3(e):
            Down_but_audio['background']="SystemButtonFace"
            Down_but_audio['foreground']="SystemButtonText"







        def reset():
            Lab.config(text="It has been reset")
            self.root.update()
            urls.set("")
            self.root.update()
            Lab.config(text="Paste Your url")



            

        def Download_mp3():
            if urls.get=="":
                tkinter.messagebox.askretrycancel("INFORMATION","Network Error/Something went wrong")

            else:
 
                try:
                    prg.start(10)
                    Lab.config(text="Downloading")
                    #self.root.update()                    
                    url = urls.get()
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    }
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:  
                        ydl.download(['{}'.format(urls.get())])

                    prg.stop()
                    Lab.config(text="video downloaded succssfully")

                except:
                    tkinter.messagebox.askretrycancel("Info","Network Error/Something went wrong")


        def  thread_mp3():
            t1=threading.Thread(target=Download_mp3)
            t1.start()






        
      


        







        #frame ===========================
        MainFrame=Frame(self.root,width=500,height=300,bg="gray77")
        MainFrame.place(x=0,y=0)
        

        self.original1 = Image.open (r"img\unnamed.png")
        resized1 = self.original1.resize((540, 270),Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(resized1)
        bglab1=Label(MainFrame,image=self.image1).place(x=0,y=0)

        #MainLableFrame=LabelFrame(MainFrame,text="Enter Your Video Url",font=("times new roman",14,"bold"),width=499,height=300,fg="red")
        #MainLableFrame.place(x=1,y=0)

        Lab=Label(MainFrame,text="Paste your url",font=("times new roman",12,"bold"),
                  fg="cyan",bg="black")
        Lab.place(x=200,y=30)
        

        url_label=Label(MainFrame,text="URL :",font=('times new roman',12,'bold'),
                        fg="cyan",bg="black")
        url_label.place(x=50,y=80)
        

        url_field=Entry(MainFrame,width=40,textvariable=urls,font=('times new roman',12,'bold'),
                        bg="steelblue",relief=RIDGE,bd=4)
        url_field.place(x=120,y=80)



        Down_but=Button(MainFrame,text="Download audio",font=('times new roman',12,'bold'),
                        command=thread_mp3,width=15,
                        relief=RIDGE,bd=3,
                        cursor="hand2")        
        Down_but.place(x=20,y=200)
        Down_but.bind("<Enter>",on_enter1)
        Down_but.bind("<Leave>",on_leave1)
        

       


        Clear_but=Button(MainFrame,text="Clear",width=15,font=('times new roman',12,'bold'),
                         relief=RIDGE,bd=3,cursor="hand2",command=reset)
        
        Clear_but.place(x=335,y=200)
        Clear_but.bind("<Enter>",on_enter2)
        Clear_but.bind("<Leave>",on_leave2)
        


        prg=Progressbar(MainFrame,length=500,orient=HORIZONTAL,mode='indeterminate')
        prg.place(x=0,y=275)
        


if __name__ == "__main__":
    root=Tk()
    app=Youtubes(root)
    root.mainloop()
