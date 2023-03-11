from tkinter import*
import models as mod


root = Tk()
root.title('Телефонный справочник')
root.geometry('500x400')


Show_Button = Button(text='Показать все записи', font=('Arial', 14), foreground='blue', command=mod.show_all_result)
Add_Button = Button(text='Добавить запись', font=('Arail', 14), foreground='blue', command=mod.add_result)
Search_Button = Button(text='Поиск записи', font=('Arial', 14), foreground='blue', command=mod.search_result)

Show_Button.place(x=150,y=100, width=200,height=50)
Add_Button.place(x=150, y=200, width=200,height=50)
Search_Button.place(x=150, y=300, width=200,height=50)


def finish():
    root.destroy()
    print('Завершение работы программы')



entry_label = Label(text='Телефонный справочник', font=('Arial', 16), foreground='blue')
icon = PhotoImage(file="tel_icon.png")
root.iconphoto(False,icon)





entry_label.pack()




root.protocol("WM_DELETE_WINDOW", finish)
root.mainloop()


