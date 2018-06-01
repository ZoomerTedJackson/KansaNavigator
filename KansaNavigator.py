import csv
import os
import time
import codecs
import platform
from Tkinter import *
from ttk import *

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
		
		
list_of_files = []
list_of_filenames = []
computer_name_size = len(platform.node())
for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    for filename in filenames:
        if filename.endswith('.csv'):
			list_of_files.append(dirpath + "\\" + filename)
			list_of_filenames.append(" " + filename[computer_name_size+1:-4] + " ")

def stopProg(e):
    root.destroy()
	
root=Tk()
root.title("Kansa Navigator")
notebook = Notebook(root)


list_of_frames = []

for (file) in list_of_files:
	csv_file_path = file
	f = Frame(notebook)
	list_of_frames.append(f)

for b in range(len(list_of_frames)):
	notebook.add(list_of_frames[b], text=list_of_filenames[b])
	list_of_rows = []
	yscrollcommand = Scrollbar(list_of_frames[b])
	xscrollbar = Scrollbar(list_of_frames[b], orient=HORIZONTAL)
	yscrollcommand.pack(side="right", fill=Y)
	xscrollbar.pack(side="bottom", fill=X)
	textL = Text(list_of_frames[b], wrap=NONE)
	with codecs.open(list_of_files[b], 'rb', "utf-16") as csvfile:
		spamreader = csv.DictReader(csvfile)
		for row in spamreader:
			textL.insert(1.0,row)
			textL.insert(1.0,"\n---\n")
	yscrollcommand.config(command=textL.yview)	
	xscrollbar.config(command=textL.xview)
	textL.pack(side="left", fill="both", expand=True)
	notebook.pack()
	

app=FullScreenApp(root)
root.mainloop()