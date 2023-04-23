## TEXT EDITOR

import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_colour():
    color = colorchooser.askcolor()
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(),size_box.get()))

def new_file():
    window.title('Untitled')
    text_area.delete(1.0, END)
    
def open_file():
    file = askopenfilename(defaultextension='.txt',
                                          file=(("All files","*.*"),
                                               ("Text files",".txt")))
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0,END)
        file_o = open(file,'r')
        text_area.insert(1.0,file_o.read())

    except Exception:
        print('Error','Couldnt read the file!!')

    finally:
        file.close()
        
def save_file():
    file = asksaveasfilename(initialfile='untitled.txt',
                             defaultextension='.txt',
                             filetypes=(('All files','*.*'),('Text files','.txt'))
                             )
    if file is None:
        return
    
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file,'w')
            file.write(text_area.get(1.0,END))

        except Exception:
            print('Error',"couldn't save the file !!!")    

        finally:
            file.close()

def cut():
    text_area.event_generate('<<Cut>>')

def copy():
    text_area.event_generate('<<Copy>>')

def paste():
    text_area.event_generate('<<Paste>>')

def about():
    showinfo('About this program.','This is a simple text editor created by using GUI tkinter.')

def quit():
    window.destroy()

window = Tk()
# window_height = 500
# window_width = 500
# window.title('Text Editor')
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

window.geometry('800x600')

font_name = StringVar(window)
font_name.set('Arial')

font_size = StringVar(window)
font_size.set('25')

text_area = Text(window,font=(font_name.get(),font_size.get()))
text_area.grid(sticky=N+E+S+W)

scrollbar = Scrollbar(text_area)
scrollbar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scrollbar.set)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0,weight=1)



frame = Frame(window)
frame.grid()

button = Button(frame,text="Color",command=change_colour)
button.grid(row=0,column=0)

font_box = OptionMenu(frame, font_name, *font.families(),command=change_font)
font_box.grid(row=0,column=1)

size_box = Spinbox(frame, from_=1,to=100,textvariable=font_size,command=change_font)
size_box.grid(row=0, column=2)


menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label='New',command=new_file)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)


edit_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_separator()
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_separator()
edit_menu.add_command(label="Paste",command=paste)

help_menu = Menu(menubar ,tearoff=0)
menubar.add_cascade(label='Help',menu=help_menu)
help_menu.add_command(label='About',command=about)



window.mainloop()