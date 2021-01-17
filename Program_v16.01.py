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


    #definere den path der skal bruges til resultaterne
    dirName = path_file
    dirName = ".".join(dirName.split(".")[:-1])

    #skriver dirName ud til et tekst dokument så den path kan læses i matlab
    Folder_txt = (script_path+'\dir.txt')

    with open(Folder_txt, 'w') as file:
        file.writelines( dirName )
    
    try:
        # opretter mappen og meddeler hvis mappen allerede eksistere 
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")

    #finder den første fil i data mappen


    #openCV åbner videoen
    vid = cv2.VideoCapture(viddir)
    #definere counter
    i=0

    #definere mængden af frames i videoen og bruges som en stop parameter
    length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

    #sekvensere videoen i enkelte frames og navngiver dem i ncorr formaten
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
    global max_x
    page = tk.Frame(root, bg='#272727', bd=5)
    page.place(relx=0.52, rely=0.01, relwidth=0.47, relheight=0.98,)

    #display  1 billede
    path_frame1 = (dirName + '/Frame_0000.png')
    load1=Image.open(path_frame1)
    render1 = ImageTk.PhotoImage(load1)
    img1 = tk.Label(page , image=render1)
    img1.image = render1
    img1.place(relx=0.01,rely=0.05, relwidth=0.98,relheight=0.40)

    Labelframe0000 = tk.Label(page, text = '#Frame0000', bd=0, bg='#272727', font=30, fg='#ffffff')
    Labelframe0000.place(relx=0.02, rely=0.01)

    #display varrierende billeder 
    max_x = length-1
    x = max_x
    changeimage(z=x)
    
    ImgDownButton = tk.Button(page, text = '<-', command=changeimagedown , bg='#545454',fg='#ffffff')
    ImgDownButton.place(relx=0.8, rely=0.97)

    ImgUpButton = tk.Button(page, text = '->', command=changeimageup , bg='#545454',fg='#ffffff')
    ImgUpButton.place(relx=0.90, rely=0.97)

def changeimage(z):
    dirName = path_file
    dirName = ".".join(dirName.split(".")[:-1])

    k = len(str(length))
    j = "0"
    path_frame2 = (dirName + '/Frame_'+ (4-k)*j + str(z) + ".png")

    load2=Image.open(path_frame2)
    
    render2 = ImageTk.PhotoImage(load2)

    img2 = tk.Label(page , image=render2)
    
    img2.image = render2

    img2.place(relx=0.01,rely=0.55, relwidth=0.98,relheight=0.40)

    Labelframe0000 = tk.Label(page, text = '#Frame_'+ (4-k)*j + str(z), bd=0, bg='#272727', font=30, fg='#ffffff')
    Labelframe0000.place(relx=0.02, rely=0.51)

def changeimagedown():
    x = x-1
    if x < 0:
     x=0

    changeimage(z=x)

def changeimageup():
    x= x+1
    if x > max_x:
        x=max_x

    changeimage(z=x)

def page1(root):
    global page
    page = tk.Frame(root, bg='#272727', bd=5)
    page.place(relx=0.01, rely=0.01, relwidth=0.5, relheight=0.98,)

    Label = tk.Label(page, text = 'NCORR Image sequencer', bd=0, bg='#272727', font=30, fg='#ffffff')
    Label.place(relx=0.02, rely=0.01)

    Button = tk.Button(page, text = 'NCORR data proccessing', command = changepage, bg='#545454',fg='#ffffff')
    Button.place(relx=0.6, rely=0.01)

    #vælgfiler
    button_selectfiles = tk.Button(page, text="choose files", font=10, command=open_folder, bg='#545454',fg='#ffffff')
    button_selectfiles.place(relx=0.72, rely=0.07,relheight=0.04)
    
    
    entry_path = tk.Label(page, font=40,)
    entry_path.place(relx=0.01, rely=0.07, relwidth=0.70,relheight=0.04)




    #navngiv sevensering

    #text_nm = tk.Text(page, height=2, bg='#a6a6a6', bd=0, font=40)
    #text_nm.insert(tk.INSERT, "Naming format")
    #text_nm.config(state="disabled")
    #text_nm.place(relx=0.01 , rely=0.14, relwidth=0.30,)

    #entry_navngivning = tk.Entry(page, font=40)
    #entry_navngivning.place(relx=0.31, rely=0.14, relwidth=0.25,)

    #text_nm1 = tk.Text(page, height=2, bg='#a6a6a6', bd=0, font=40)
    #text_nm1.insert(tk.INSERT, "_####.png")
    #text_nm1.config(state="disabled")
    #text_nm1.place(relx=0.56 , rely=0.14, relwidth=0.20,)

    #start sekvensering
    button_start_sek = tk.Button(page, text="start sequencing", font=40, command= start_sequensing, bg='#545454',fg='#ffffff')
    button_start_sek.place(relx=0.01, rely=0.14)

    #check boks

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