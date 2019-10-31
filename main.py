import tkinter as tk
from PIL import ImageTk, Image
from pytube import YouTube
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import os

def getPlaylistLinks(url):
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page , 'html.parser')
    pl_videos = set()
    for a in soup.find_all('a'):
            if a.get('href').startswith('/watch'):
                pl_videos.add('https://youtube.com' + a.get('href').split('&')[0])
    print(pl_videos)

def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
        yt.download(path)

def enter():
    getPlaylistLinks(str(urlInput.get()))
    #downloadYouTube(str(urlInput.get()), "C:/Users/HASANTHA MALSHAN/Desktop")


root = tk.Tk()
root.title("dTube")

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

urlInput = tk.Entry(frame,font=40)
urlInput.place(y=50,relwidth=1,relheight=0.06)

urlInput_button = tk.Button(frame, text="Enter",bd=0,padx=20,pady=10, bg='#052978',fg="#ffffff",command=enter)
urlInput_button.place(x=150,y=90)


root.mainloop()









