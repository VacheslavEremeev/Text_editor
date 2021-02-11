import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename  # Функции открыть файл и сохранить как
from tkinter.messagebox import showerror # Вывод всех ошибок
from tkinter import messagebox # Показ всех уведомлений 
import codecs

from settings import *  # Импортируем настройки

class Text_editor():
    def __init__(self, text):
        self.file_name = tkinter.NONE
        self.text = text

    def new_file(self):
        self.file_name = "Безымянный"
        self.text.delete("1.0", tkinter.END) # Удаляем старый текст в редакторе

    def open_file(self):
        name = askopenfilename() #Открываем для чтения
        if name is None: # Если файл пустой прекращаем выполнение метода
            return
        with codecs.open(name, encoding="utf-8") as inp:
            data = inp.read() # Запоминаем информацию из открытого файла
            self.text.delete("1.0", tkinter.END) # Удаляем существующий в редакторе текст
            self.text.insert("1.0", data) # Вставляем в редактор текст из открытого файла

    def save_file(self):
        data = self.text.get("1.0", tkinter.END) # Сохраняет набранный текст в переменной
        with open(self.file_name, "w", encoding="utf-8") as output: 
            output.write(data) # Сохраняем в открытый файл
            output.close() # Закрываем файл

    def save_as_file(self):
        output = asksaveasfilename() # Выводим окно Сохранить как mode="w", defaultextension="txt"
        data = self.text.get("1.0", tkinter.END) # Считываем всё что есть в поле, сохраняем набранный текст
        try:
            with open(output+".txt", "w", encoding="utf-8") as file:  #output.write(data.rstrip())
                file.write(data.rstrip())
        except Exception:
            showerror(title="Ошибка!", message="Ошибка при сохранении файла")

    def get_info(self):
        messagebox.showinfo("Справка", "Информация о приложении")