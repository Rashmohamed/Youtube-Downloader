import tkinter as tk
import tkinter.ttk as tkk
from tkinter import filedialog
import yt_dlp
window = tk.Tk()
window.title("Youtube Downloader")

#functions

yt=yt_dlp.YoutubeDL()
def downloadLinks():
    list=textfield.get('1.0',tk.END).split('\n')
    yt.download(list)


DownloadPath=tk.StringVar()
textfield=tk.Text(window)
textfield.insert('end',"https://www.youtube.com/playlist?list=PLOspHqNVtKADOvJFNA2e5cp1FSdRcTO8S")
DownloadButton=tk.Button(window,command=downloadLinks,text="Download")
StopButton=tk.Button(window,text="Stop")
PathButton=tk.Button(window,text="مكان التنزيل",command=lambda:DownloadPath.set(filedialog.askdirectory()))
QuitButton=tk.Button(window,text="Close",command=lambda:window.quit())

#GUI
#PathButton.pack()
DownloadButton.pack()
StopButton.pack()
textfield.pack()
QuitButton.pack()
#DownloadProgressBar.pack()
window.mainloop()
