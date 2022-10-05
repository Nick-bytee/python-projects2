from email import message
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import tkinter
from tkinter import messagebox
from pytube import YouTube
from tkinter.ttk import *

root = Tk()
root.title('YT Video Downloader')
root.geometry('390x500')
root.resizable(False,False)
root.config(bg='#5A5A5A')
style = Style()
option_list = ["High Quality","Low Quality"]
value_inside = tkinter.StringVar(root)

value_inside.set("Select Quality")
dr_check = 0

def browse():
       download_dir = filedialog.askdirectory(
          initialdir="Your Directory Path", title = "Save Video"
       )
       dr_check = 1
       path_dir.set(download_dir)



def download():
     Ytlink = link.get()
     dwnldfolder = path_dir.get()
     getvideo = YouTube(Ytlink)
     if dr_check == 1 and link != ():
          if value_inside.get() == option_list[0]:
               videoStream = getvideo.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
               videoStream.download(dwnldfolder)
               messagebox.showinfo("Success", "Downloded in {}".format(dwnldfolder))
               print(videoStream)
          elif value_inside.get() == option_list[1]:
                    videoStream = getvideo.streams.first()
                    videoStream.download(dwnldfolder)
                    messagebox.showinfo("Success", "Downloded in {}".format(dwnldfolder))
          else:
               messagebox.showinfo("Error","Please Choose Quality")
     else:
          messagebox.showinfo("Error","Plaese Choose Path")

def download_audio():
     if dr_check == 1:
          Ytlink = link.get()
          dwnldfolder = path_dir.get()
          getvideo = YouTube(Ytlink)
          videoStream = getvideo.streams.filter(only_audio=True,file_extension='webm').desc().first()
          videoStream.download(dwnldfolder)
          messagebox.showinfo("Success", "Downloded in {}".format(dwnldfolder))
     else:
          messagebox.showinfo("Error","Plaese Choose Path")

style.configure('TButton', font =
               ('calibri', 15, 'bold'),
                    borderwidth = '2')

style.map('TButton', foreground = [('active', '!disabled', 'red')],
                     background = [('active', 'black')])

head = tk.Label(root, text=('Youtube Video Downloader'), font=("Times New Roman", "25", "bold"), bg= '#5A5A5A', fg='White').pack()

head2 = tk.Label(root, text=('By Nick'), font=("Times New Roman", "20", "italic"), bg='#5A5A5A', fg='Red').pack()

head3 = tk.Label(root, text=('Enter Your Link Below :'), font=("Times New Roman", "20"), bg= '#5A5A5A', fg='White').pack()

link = StringVar()
link_entry = tk.Entry(root, width=75, textvariable=link)
link_entry.place(x=0, y=130, height=35)

head4 = tk.Label(root, text='Choose Path', font=('Times New Roman', "20", "italic"), bg= "#5A5A5A", fg= "White")
head4.place(x = 125, y = 170)

browse_but= Button(root, text='Browse', command=browse)
browse_but.place(x=100, y=210, height=35, width=200)

path_dir = StringVar()
path_text = Entry(root, width=75, textvariable=path_dir)
path_text.place(x=0, y= 270, height= 35)

question_menu = tkinter.OptionMenu(root, value_inside, *option_list)
question_menu.place(x=100, y = 320, width=200, height=30)

dwnld_but= Button(root, text='Download Video', command=download)
dwnld_but.place(x=100, y=370, height=35, width=200)

dwnld_but2= Button(root, text='Download Audio Only', command=download_audio)
dwnld_but2.place(x=100, y=430, height=35, width=200)
root.mainloop()