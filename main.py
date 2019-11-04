import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image
from pytube import YouTube
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import os

root = tk.Tk()
root.title("dTube")

videoList = []

var = IntVar()
videotype = IntVar()
path = StringVar()


def getpath():
    path1 = filedialog.askdirectory()
    path.set(path1)
    urlInput_label = tk.Label(frame,text="Path > " + path.get(),bg="#041824",fg="#ffffff",font=("Courier", 10),wraplength=400)
    urlInput_label.place(y=440,relwidth=1,relheight=0.05)

def selection(value):
    videotype.set(value)
    if(value == 1):
        urlInput_label = tk.Label(frame,text="----------Video Details----------",bg="#041824",fg="#ffffff",font=("Courier", 10))
        urlInput_label.place(y=200,relwidth=1,relheight=0.07)
    elif(value == 2):
        urlInput_label = tk.Label(frame,text="--------PlayList Details--------",bg="#041824",fg="#ffffff",font=("Courier", 10))
        urlInput_label.place(y=200,relwidth=1,relheight=0.07)

def getPlaylistLinks(url):
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page , 'html.parser')
    for a in soup.find_all('a'):
            if a.get('href').startswith('/watch'):
                videoList.append('https://youtube.com' + a.get('href').split('&')[0])
    #print(videoList)

def downloadYouTube(videourl,downloadpath,name):
    # progress = Progressbar(frame,orient="horizontal",length=100,mode='determinate')
    # progress.place(y=450,relwidth=1,relheight=0.01)
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(downloadpath):
        os.makedirs(downloadpath)
    yt.download(downloadpath)
   

def enter():
    print(videoList)
    if(videotype.get() == 1):
        yt1 =  YouTube(urlInput.get())
        urlInput_label = tk.Label(frame,text=yt1.title,bg="#041824",fg="#ffffff",font=("Courier", 10),wraplength=400)
        urlInput_label.place(y=260,relwidth=1,relheight=0.2)
    elif(videotype.get() == 2):
        getPlaylistLinks(urlInput.get())
        urlInput_label = tk.Label(frame,text=len(videoList),bg="#041824",fg="#ffffff",font=("Courier", 10),wraplength=400)
        urlInput_label.place(y=260,relwidth=1,relheight=0.2)

def download():
    yt1 =  YouTube(urlInput.get())
    if(videotype.get() == 1):
        downloadYouTube(str(urlInput.get()),path.get(),yt1.title)
    elif(videotype.get() == 2):
        for l in videoList:
            yt1 =  YouTube(l)
            get_true = True
            while get_true:
                downloadYouTube(l,path.get(),yt1.title)
                

canvas = tk.Canvas(root, height=760, width=510,bg="#041824")
root.maxsize(500, 750)
root.minsize(500, 750) 
canvas.pack()

logo = Image.open("logo.png")
logo = logo.resize((300,150), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(logo)
logo_label = tk.Label(root,image=photoImg,bg="#041824")
logo_label.place(x=2,y=-230,relwidth=0.992,relheight=0.9)

frame = tk.Frame(root,bg="#041824")
frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.73,anchor='n')

urlInput_label = tk.Label(frame,text="Paste your URL here...",bg="#041824",fg="#ffffff",font=("Courier", 15))
urlInput_label.place(relwidth=1,relheight=0.07)

PlaylistRadio = tk.Radiobutton(frame,bg="#0c98f0",variable=var, value=2,text="Playlist",font=("Courier", 10),fg="#041824",borderwidth=0,command=lambda : selection(var.get()))
PlaylistRadio.place(x=210,y=57)

SingleRadio = tk.Radiobutton(frame,bg="#0c98f0", variable=var, value=1,text="Single video",font=("Courier", 10),fg="#041824",borderwidth=0,command=lambda : selection(var.get()))
SingleRadio.place(x=70,y=57)

urlInput = tk.Entry(frame,font=40)
urlInput.place(y=100,relwidth=1,relheight=0.06)

urlInput_button = tk.Button(frame, text="Enter",bd=0,padx=20,pady=10, bg='#052978',fg="#ffffff",command=enter)
urlInput_button.place(x=150,y=155)

urlInput_button = tk.Button(frame, text="Set Path",bd=0,padx=20,pady=10, bg='#052978',fg="#ffffff",command=getpath)
urlInput_button.place(x=85,y=500)

urlInput_button = tk.Button(frame, text="Download",bd=0,padx=20,pady=10, bg='#052978',fg="#ffffff",command=download)
urlInput_button.place(x=200,y=500)


root.mainloop()









