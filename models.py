import sqlite3
from tkinter import*

base = sqlite3.connect('phonebook.db')
cur = base.cursor()

def show_result(lst):
    text = ''
    for row in lst:
        text += f"ID:{row[0]}\nИмя:{row[1]}\nФамилия:{row[2]}\nНомера телефона:{row[3]}\nКомментарий:{row[4]}\n***************************************\n"
    return text
   
def new_id():
    with open('id.txt', 'r+') as f:
        id = int(f.read())
        id+=1
    with open('id.txt', 'w') as f:
        f.write(str(id))
    return str(id)

def show_all_result():
    show_window = Tk()
    show_window.geometry('300x500')
    show_window.title('Все результаты записи')
    cur.execute("SELECT * FROM users")
    result = show_result(cur.fetchall())
    print(result)
    show = Text(master=show_window)
    show.pack(fill=BOTH)
    show.insert('1.0', result)
    scrollbar = Scrollbar(master = show_window, orient='vertical', command=show.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    show['yscrollcommand'] =scrollbar.set
   
   

def add_result():
    def cancel():
        search_window.destroy()
    def confirm():
        name = name_entry.get()
        second_name = surname_entry.get()
        number = phone_entry.get()
        comment = comment_entry.get()
        cur.execute(""" INSERT INTO users(id,name,surname,number,comment) \
        VALUES(?,?,?,?,?);""",(new_id(), name, second_name, number, comment))
        base.commit()
        search_window.destroy()
   
    search_window  = Tk()
    search_window.geometry('400x200')
    search_window.title('Меню добаления записи')
    name_label = Label(master = search_window, text='Введите имя')
    name_entry = Entry(master=search_window)
    name_label.grid(column=0,row=0)
    name_entry.grid(column=1,row=0)
    surname_label = Label(master=search_window, text='Введите фамилию')
    surname_entry = Entry(master=search_window)
    surname_label.grid(column=0,row=1)
    surname_entry.grid(column=1,row=1)
    phone_label = Label(master=search_window, text="Введите номер телефона")
    phone_entry = Entry(master=search_window)
    phone_label.grid(column=0,row=2)
    phone_entry.grid(column=1,row=2)
    comment_label = Label(master=search_window, text="Введите комментарий")
    comment_entry = Entry(master=search_window)
    comment_label.grid(column=0, row=3)
    comment_entry.grid(column=1, row=3)   
    confirm_but = Button(master = search_window,text="Записать",command=confirm)
    cancel_but = Button(master = search_window,text="Отмена", command=cancel)
    confirm_but.grid(column=0, row=4)
    cancel_but.grid(column=1,row=4)
          
def search_result():
    def cancel():
        search_window.destroy()
    def confirm():
        sql_search_querry = """ SELECT * FROM users where """
        result = [['name=?',''], ['surname=?',''], ['number=?',''],['comment=?','']]
        data = []
        name = name_entry.get()
        result[0][1] = name
        second_name = surname_entry.get()
        result[1][1] = second_name
        number = phone_entry.get()
        result[2][1] = number
        comment = comment_entry.get()
        result[3][1] = comment
        for i in range(len(result)-1):
            if result[i][1] != '':
                sql_search_querry += result[i][0]
                data.append(result[i][1])
                sql_search_querry+= ' AND '
        sql_search_querry = sql_search_querry[:-5]
        data = tuple(data)
        cur.execute(sql_search_querry, data)
        result = cur.fetchall()
        print(result)
        if len(result) == 0:
            result = 'Записей не найдено!'
        else:
            result = show_result(result)
        show = Label(master=search_window, width=40, text=result,justify=LEFT)
        show.grid(column=0,row=5)
        print(result)        
        base.commit()
        
    search_window = Tk()
    search_window.geometry('500x500')
    search_window.title('Меню поиска записи')
    name_label = Label(master = search_window, text='Введите имя')
    name_entry = Entry(master=search_window)
    name_label.grid(column=0,row=0)
    name_entry.grid(column=1,row=0)
    surname_label = Label(master=search_window, text='Введите фамилию')
    surname_entry = Entry(master=search_window)
    surname_label.grid(column=0,row=1)
    surname_entry.grid(column=1,row=1)
    phone_label = Label(master=search_window, text="Введите номер телефона")
    phone_entry = Entry(master=search_window)
    phone_label.grid(column=0,row=2)
    phone_entry.grid(column=1,row=2)
    comment_label = Label(master=search_window, text="Введите комментарий")
    comment_entry = Entry(master=search_window)
    comment_label.grid(column=0, row=3)
    comment_entry.grid(column=1, row=3)
    confirm_but = Button(master = search_window,text="Поиск",command=confirm)
    cancel_but = Button(master = search_window,text="Отмена", command=cancel)
    confirm_but.grid(column=0, row=4)
    cancel_but.grid(column=1,row=4)   
   
