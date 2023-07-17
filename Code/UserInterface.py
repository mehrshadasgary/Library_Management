#                                  Library management Project(Front)

# Import
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import BackEnd
import Dooz_Game

# ==================================Configure Setting====================================

window = Tk()
window.title('مدیریت کتابخانه')
window.geometry('710x500')
window.minsize(710, 500)
window.maxsize(710, 500)
window.resizable(height=False, width=False)
large_font = ("Arial", 20)

# baraye range  background #
# back_color = 'grey'
# window.configure(bg=back_color)

# baraye aks dar background #
img = PhotoImage(file="background.png")
label = Label(
    window,
    image=img
)
label.place(x=0, y=0)

# ===================================Labels==============================================

# Titel book Label
titel_Label = Label(window,
                    text='نام کتاب',
                    font=('arial', 11, 'bold'),
                    bg= 'black',
                    fg='white')

titel_Label.grid(row=0, column=8 ,
                 padx=3)

# Author book Label
author_Label = Label(window,
                     text='نویسنده',
                     font=('arial', 11, 'bold'),
                     bg='black',
                     fg='white')

author_Label.grid(row=0, column=6,
                  padx=2)

# Years book Label
years_Label = Label(window,
                    text='سال',
                    font=('arial', 12, 'bold'),
                    bg='black',
                    fg='white')

years_Label.grid(row=1, column=8,)

# ISBN book Label
isbn_Label = Label(window,
                   text='شابک',
                   font=('arial', 11, 'bold'),
                   bg='black',
                   fg='white'
                   )

isbn_Label.grid(row=1, column=6)

# ===================================Variables=============================================

# Titel Variable
titel_var = StringVar()

# Author Variable
author_var = StringVar()

# Years Variable
years_var = StringVar()

# ISBN Variable
isbn_var = StringVar()

# white color variable
color_w = 'white'

# ===================================Entries==============================================

# Titel book Entries
titel_Label_entry = Entry(window, textvariable=titel_var,
                           highlightbackground=color_w,
                           justify=RIGHT,
                           font=('arial', 10, 'bold'),
                           bg='#FFFF8C',
                           bd=4)
titel_Label_entry.grid(row=0, column=7)

# Author book Entries
author_Label_entry = Entry(window, textvariable=author_var,
                           highlightbackground=color_w,
                           justify=RIGHT,
                           font=('arial', 10, 'bold'),
                           bg='#FFFF8C',
                           bd=4)

author_Label_entry.grid(row=0, column=5)

# Years book Entries
years_Label_entry = Entry(window, textvariable=years_var,
                          highlightbackground=color_w,
                          font=('arial', 10, 'bold'),
                          bg='#FFFF8C',
                          bd=4,)

years_Label_entry.grid(row=1, column=7)

# ISBN book Entries
isbn_Label_entry = Entry(window, textvariable=isbn_var,
                         highlightbackground=color_w,
                         font=('arial', 10, 'bold'),
                         bg='#FFFF8C',
                         bd=4)

isbn_Label_entry.grid(row=1, column=5)

# ===================================List Box==============================================

#    لیست تمامی اطلاعات وارد شده ما
list = Listbox(window, width=50, height=27,
               highlightbackground=color_w)
list.grid(row=0, column=0,
          rowspan=9, columnspan=2,
          pady=25, padx=5)

# ===================================Scroll Bar=============================================

scroll = Scrollbar(window)
scroll.grid(row=0, column=1,
            rowspan=10, columnspan=6)

# connect scroll & List
list.configure(yscrollcommand=scroll.set)
scroll.configure(command=list.yview)


# =============================Functions for connect Backend==================================

# Delete item in box function
def delete_box():
    list.delete(0, END)


# por kardan box az data be soorat pishfarz
def fill_box(library):
    for book in library:
        list.insert(END, book, '---------------------------------------------')


# function rooydade select kardan
def event_get_selected(event):
    # global baraye estefade dar baqie function ha
    global selected_book

    if len(list.curselection()) > 0:
        # daryaft index list
        index = list.curselection()[0]
        selected_book = list.get(index)

        # darj etelat ba select kardan item
        # titel
        titel_Label_entry.delete(0, END)
        titel_Label_entry.insert(END, selected_book[1])

        # author
        author_Label_entry.delete(0, END)
        author_Label_entry.insert(END, selected_book[2])

        # years
        years_Label_entry.delete(0, END)
        years_Label_entry.insert(END, selected_book[3])

        # isbn
        isbn_Label_entry.delete(0, END)
        isbn_Label_entry.insert(END, selected_book[4])


# motasel kardan (bind)  rooydad Select be list
list.bind("<<ListboxSelect>>", event_get_selected)


# Command for view (Connect backend)
def view_command():
    # baraye inke view tekrar nashe
    delete_box()
    library = BackEnd.view_db()
    # for book in library:
    # baraye ezafe kardan be box list
    # list.insert(END, book)
    fill_box(library)


# Command for search (Connect backend)
def search_command():
    delete_box()
    library = BackEnd.search_db(titel_var.get(),
                                author_var.get(),
                                years_var.get(),
                                isbn_var.get())
    for book in library:
        list.insert(END, book)


# Command for add (Connect backend)
def add_command():
    BackEnd.add_db(titel_var.get(),
                   author_var.get(),
                   years_var.get(),
                   isbn_var.get())
    # baraye neshoon dadan khodkar box
    # berooz resani khodkar box
    view_command()


# Command for edit (Connect backend)
def edit_command():
    BackEnd.edit_db(selected_book[0],
                    titel_var.get(),
                    author_var.get(),
                    years_var.get(),
                    isbn_var.get())
    # baraye neshoon dadan khodkar box
    # berooz resani khodkar box
    view_command()


# Command for delete (Connect backend)
def delete_command():
    # selected_book = event_get_selected([])
    BackEnd.delete_db(selected_book[0])
    # baraye neshoon dadan khodkar box
    # berooz resani khodkar box
    view_command()


# function gereftan taeid baraye bastan barname
def quite():
    quite = messagebox.askyesno('خروج از برنامه', 'آیا میخواهید خارج شوید؟')
    if quite:
        window.destroy()


# Command for closs (Connect backend)
def close_command():
    # taedie gereftan baraye khorooj az barname
    quite()


# ===================================Buttons==============================================

# Button for View items
view_btn = Button(window, text='نمایش همه',
                  width=12,
                  command=lambda: view_command(),
                  font=('arial', 11, 'bold'),
                  bd=4,
                  fg='black',
                  bg='#FF83FA')

view_btn.grid(row=2, column=5,
              columnspan=5)

# Button for search items
search_btn = Button(window, text='جست و جو',
                    width=12,
                    command=lambda: search_command(),
                    font=('arial', 11, 'bold'),
                    bd=4,
                    fg='black',
                    bg='#FF83FA')

search_btn.grid(row=3, column=5,
                columnspan=5)

# Button for add new item
add_btn = Button(window, text='اضافه کردن',
                 width=12,
                 command=lambda: add_command(),
                 font=('arial', 11, 'bold'),
                 bd=4,
                 fg='black',
                 bg='#FF83FA')

add_btn.grid(row=4, column=5,
             columnspan=5)

# Button for edit item
edit_btn = Button(window, text='ویرایش کردن',
                  width=12,
                  command=lambda: edit_command(),
                  font=('arial', 11, 'bold'),
                  bd=4,
                  fg='black',
                  bg='#FF83FA')

edit_btn.grid(row=5, column=5,
              columnspan=5)

# Button for delete item
delete_btn = Button(window, text='حذف کردن',
                    width=12,
                    command=lambda: delete_command(),
                    font=('arial', 11, 'bold'),
                    bd=4,
                    fg='black',
                    bg='#FF83FA')

delete_btn.grid(row=6, column=5,
                columnspan=5)

# Button for close app
close_btn = Button(window, text='خروج',
                   width=12,
                   command=lambda: close_command(),
                   font=('arial', 11, 'bold'),
                   bd=4,
                   fg='black',
                   bg='#FF83FA')

close_btn.grid(row=7, column=5,
               columnspan=5)


def game_run():
    Dooz_Game.game()


btn_game = Button(window, text='بیکارم \U0001F600',
                  width=5,
                  command=lambda: game_run(),
                  font=('arial', 9, 'bold'),
                  bd=4,
                  fg='white',
                  bg='red')

btn_game.grid(row=8, column=8,
              columnspan=5)

# baraye namaeysh data haye daroon database dar box
# vaghti barname baz shavad
view_command()

window.mainloop()
