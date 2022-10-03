from tkinter import *
import speedtest

root = Tk()
root.title('Internet Speed Test')
root.geometry('360x500')
root.resizable(False,False)
root.config(bg = "black")

def speed():
    root = speedtest.Speedtest()
    root._secure
    root.get_servers()
    down = str(round(root.download() / (10**6))) +' mbps'
    upload = str(round(root.upload() / (10**6))) +' mbps'
    down_text.config(text=down)
    upload_text.config(text=upload)

test = Label(root, text = 'Internet Speed Test', font=("Times New Roman", "20", "bold"), bg = 'Black', fg = 'Green')
test.place(x=0, y=20, height= 50, width= 370)
test_down = Label(root, text = 'Download Speed', font=("Times New Roman", "20", ), bg = 'black', fg = 'white')
test_down.place(x=0, y=80, height= 50, width= 370)
down_text = Label(root, text = '00', font=("Times New Roman", "20", ), bg= 'black', fg = 'blue')
down_text.place(x=0, y=140, height= 50, width= 370)
test_upload = Label(root, text = 'Upload Speed', font = ('Times New Roman', "20", ), bg = 'black', fg = 'white')
test_upload.place(x = 0, y = 200, height=50, width=370)
upload_text = Label(root, text = '00', font=('Times New Roman', '20'), bg = 'black', fg = 'blue')
upload_text.place(x = 0, y = 260, width= 370)
test_button = Button(root, text= 'Go', font=('Times New Roman', '20'), command= speed, bg= 'black', fg = 'red')
test_button.place(x = 0, y = 320, width= 370)






















root.mainloop()

