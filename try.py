import tkinter
from tkinter import *

from settings import *  # Импортируем настройки
from tclass import * # Импорт класса Text_editor

app = tkinter.Tk() # Создаем окно нашего приложения
app.title(APP_NAME) # Указываем название нашего приложения
app.minsize(width=WIDTH, height=HEIGHT) # Минимальный размер экрана
app.maxsize(width=WIDTH, height=HEIGHT) # Максимальный размер экрана

text = tkinter.Text(app, width=WIDTH-50, height=HEIGHT, wrap="word") # Создали поле с текстом, виджет текста, скролл
scroll = Scrollbar(app, orient=VERTICAL, command=text.yview) # Создали скролл
scroll.pack(side="right", fill="y") # Разместили скролл
text.configure(yscrollcommand=scroll.set) # Связь текста со скроллом
text.pack() # Разместили поле с текстом

menuBar = tkinter.Menu(app)  # Создаём меню

editor = Text_editor(text)

app_menu = tkinter.Menu(menuBar) # Выпадающее меню у "Файл"
app_menu.add_command(label="Новый файл", command=editor.new_file)
app_menu.add_command(label="Открыть", command=editor.open_file)
app_menu.add_command(label="Сохранить", command=editor.save_file)
app_menu.add_command(label="Сохранить как", command=editor.save_as_file)

menuBar.add_cascade(label="Файл", menu=app_menu)
menuBar.add_cascade(label="Справка", command=editor.get_info)
menuBar.add_cascade(label="Выход", command=app.quit)

app.config(menu=menuBar) # Публикуем меню

app.mainloop() # Бесконечный цикл нашего приложения