import tkinter
from tkinter import *
from pytube import YouTube
# tk innter to Display
window=tkinter.Tk()
window.title('YOUTUBE VIDEOS DOWNLOADER')
window.geometry('500x500')
#Widget main label
heading=tkinter.Label(window,text="welcome to youtube downloader",fg='blue',bg='yellow',font=("arial,Bold",20))
heading.grid(column=10,row=1)
#label 2
heading1=tkinter.Label(window,text="enter the Url",fg='blue',font=("arial,Bold",20))
heading1.grid(column=10,row=2)
#label2
entryurl=tkinter.Entry(window,width=30,fg='blue',font=(30))
entryurl.grid(column=10,row=3)
#output channel display
heading2=tkinter.Label(window,text="",fg='green',font=("arial,Bold",12))
heading2.grid(column=10,row=4)
heading3=tkinter.Label(window,text="",fg='green',font=("arial,Bold",12))
heading3.grid(column=10,row=5)
heading4=tkinter.Label(window,text="",fg='green',font=("arial,Bold",12))
heading4.grid(column=10,row=6)
def downloading():
    url = entryurl.get()
    my_video = YouTube(url)
    #get Video Title
    print(my_video.title)
    heading2.configure(text="title of video:-"+my_video.title)
    print("********************Tumbnail Image***********************")
    #get Thumbnail Image
    heading3.configure(text="video thumal:-"+my_video.thumbnail_url)

    print("********************Download video*************************")
    #get all the stream resolution for the 
    #for stream in my_video.streams:
        #print(stream)

    #set stream resolution
    my_video = my_video.streams.get_highest_resolution()

    #or
    #my_video = my_video.streams.first()

    #Download video
    my_video.download()
    heading4.configure(text="video downloaded check your file")

bt=tkinter.Button(window,text='Download',fg='blue',bg='yellow', width=20,command=downloading)
bt.grid(column=10,row=10)
window.mainloop()
