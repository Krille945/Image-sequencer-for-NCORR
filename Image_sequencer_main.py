import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
from datetime import datetime
import os 
import sys
import matlab.engine


HEIGHT = 700
WIDTH = 800

root = tk.Tk()
root.title("NCORR Image Sequencer")

canvas = tk.Canvas(root, height= HEIGHT, width= WIDTH, bg='#202020')
canvas.pack()

path_file =''
nm_files = 0
viddir= ''
dirName= ''
i = 0
framenumber = tk.IntVar()
framenumber2 = tk.IntVar()

eng = matlab.engine.start_matlab()

def open_folder():
    global viddir
    global nm_files
    global path_file

    path_file = filedialog.askopenfilename(title='Select file', filetypes=(("avi files", "*.avi"),("all files", "*.*")))
    entry_path = tk.Label(page, text = path_file)
    entry_path.place(relx=0.01, rely=0.07, relwidth=0.70,relheight=0.04)
    viddir = path_file

global script_path
script_path = os.path.dirname(__file__)

def start_sequensing():
    global dirName
    global length


    #defines path to the folder for the sequenced images
    dirName = path_file
    dirName = ".".join(dirName.split(".")[:-1])

    #writes dirName in a dir.txt allowing communication between matlab and python
    Folder_txt = (script_path+'\dir.txt')

    with open(Folder_txt, 'w') as file:
        file.writelines( dirName )
    
    try:
        #Creates folder for the images 
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")

    #openCV loads the video
    vid = cv2.VideoCapture(viddir)
    #defines counter
    i=0

    #determens the amount of frames and is usesd as stop function
    length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

    #sequences the video and names them according to the NCORR format
    while(vid.isOpened() and i <= length):
        ret, frame = vid.read(i)
        if ret == False:
            i+=1
            continue
        j = "0"
        k = len(str(i))
        cv2.imwrite(dirName+'/Frame_'+ (4-k)*j +str(i)+'.png',frame)
        i+=1
        if i == length:
            page3(canvas)
            break
    
def Open_ncorr():
        
    eng.open_ncorr_only(nargout=0)

def page3(root):
    global page
    global x
    global c
    global max_x

    page = tk.Frame(root, bg='#272727', bd=5)
    page.place(relx=0.52, rely=0.01, relwidth=0.47, relheight=0.98,)
    #display first
    changeimage(z=0,f=1)
    c = 0
    #display second image 
    max_x = length-1
    x = max_x
    changeimage(z=x,f=2)
    

    ImgDownButton2 = tk.Button(page, text = '<', command=changeimagedown, bg='#545454',fg='#ffffff')
    ImgDownButton2.place(relx=0.7, rely=0.47,relheight = 0.04)

    ImgUpButton = tk.Button(page, text = '>', command=changeimageup , bg='#545454',fg='#ffffff')
    ImgUpButton.place(relx=0.95, rely=0.47,relheight = 0.04)

    ImgDownButton2 = tk.Button(page, text = '<', command=changeimagedown2, bg='#545454',fg='#ffffff')
    ImgDownButton2.place(relx=0.7, rely=0.97,relheight = 0.04)

    ImgUpButton2 = tk.Button(page, text = '>', command=changeimageup2 , bg='#545454',fg='#ffffff')
    ImgUpButton2.place(relx=0.95, rely=0.97,relheight = 0.04)

    #1
    framenumber.set(0)
    frameview = tk.Entry(page, bg='#545454',fg='#ffffff', textvariable=framenumber)

    frameview.place(relx=0.76, rely=0.47, relheight = 0.04, relwidth= 0.18)
    frameview.bind('<Return>', lambda event, g=1: type2image(g))

    #2
    framenumber2.set(max_x)
    frameview2 = tk.Entry(page, bg='#545454',fg='#ffffff', width=4, textvariable=framenumber2)

    frameview2.place(relx=0.76, rely=0.97, relheight = 0.04, relwidth= 0.18)
    frameview2.bind('<Return>', lambda event, g=2: type2image(g))

def type2image(g):
    global x
    global c

    if g == 1:
        h=framenumber.get()

        changeimage(z=h,f=g)
        c=h
    elif g == 2:
        h=framenumber2.get()

        changeimage(z=h,f=g)
        x=h
    

def changeimage(z,f):
    global x

    dirName = path_file
    dirName = ".".join(dirName.split(".")[:-1])

    k = len(str(length))
    j = "0"
    path_frame = (dirName + '/Frame_'+ (4-k)*j + str(z) + ".png")

    load=Image.open(path_frame)
    
    render = ImageTk.PhotoImage(load)

    img = tk.Label(page , image=render)
    
    img.image = render


    Labelframe0000 = tk.Label(page, text = '#Frame_'+ (4-k)*j + str(z), bd=0, bg='#272727', font=30, fg='#ffffff')
    if f == 2:
        img.place(relx=0.01,rely=0.55, relwidth=0.98,relheight=0.40)
        Labelframe0000.place(relx=0.02, rely=0.97)
        framenumber2.set(z)
    else:
        img.place(relx=0.01,rely=0.05, relwidth=0.98,relheight=0.40)
        Labelframe0000.place(relx=0.02, rely=0.47)
        framenumber.set(z)
    
def changeimagedown():
    global c 
    c = c-1
    if c < 0:
     c=0

    changeimage(z=c, f=1)

def changeimageup():
    global c
    c= c+1
    if c > max_x:
        c=max_x

    changeimage(z=c,f=1)

def changeimagedown2():
    global x 
    x = x-1
    if x < 0:
     x=0

    changeimage(z=x, f=2)

def changeimageup2():
    global x
    x= x+1
    if x > max_x:
        x=max_x

    changeimage(z=x,f=2)

def page1(root):
    global page
    page = tk.Frame(root, bg='#272727', bd=5)
    page.place(relx=0.01, rely=0.01, relwidth=0.5, relheight=0.98,)

    Label = tk.Label(page, text = 'NCORR Image sequencer', bd=0, bg='#272727', font=30, fg='#ffffff')
    Label.place(relx=0.02, rely=0.01)

    Button = tk.Button(page, text = 'NCORR data proccessing', command = changepage, bg='#545454',fg='#ffffff')
    Button.place(relx=0.6, rely=0.01)

    #choose files
    button_selectfiles = tk.Button(page, text="choose files", font=10, command=open_folder, bg='#545454',fg='#ffffff')
    button_selectfiles.place(relx=0.72, rely=0.07,relheight=0.04)
    
    
    entry_path = tk.Label(page, font=40,)
    entry_path.place(relx=0.01, rely=0.07, relwidth=0.70,relheight=0.04)


    #starts sequensing
    button_start_sek = tk.Button(page, text="start sequencing", font=40, command= start_sequensing, bg='#545454',fg='#ffffff')
    button_start_sek.place(relx=0.01, rely=0.14)

    #check box
    c_ncorr= tk.Checkbutton(page, text="Do you wan't to continue working with this data in NCORR", bg='#272727',fg='#ffffff')
    c_ncorr.place(relx=0.01, rely=0.9)

    #start ncorr
    button_start_NCORR = tk.Button(page, text="open NCORR", font=40, bg='#545454',fg='#ffffff', command= Open_ncorr)
    button_start_NCORR.place(relx=0.01, rely=0.95)

def page2(root):
    page = tk.Frame(root, bg='#a6a6a6', bd=5)
    page.place(relx=0.01, rely=0.01, relwidth=0.5, relheight=0.98,)

    Label2 = tk.Label(page, text = 'This is page 2')
    Label2.place(relx=0.72, rely=0.01)

    Button2 = tk.Button(page, text = 'To page 1', command = changepage)
    Button2.place(relx=0.72, rely=0.05)

def changepage():
    global pagenum, canvas
    for widget in canvas.winfo_children():
        widget.destroy()
    if pagenum == 1:
        page2(canvas)
        pagenum = 2
    else:
        page1(canvas)
        pagenum = 1

pagenum = 1

page1(canvas)

root.mainloop()
