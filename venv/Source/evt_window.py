import tkinter as tk
from PIL import Image, ImageTk


class EvtWindow:
    def __init__(self):
        self.__root = tk.Tk()
        self.__lHeader = tk.Label(text="English Vocabulary Tester", bg="white", fg="black")
        self.__lHeader.config(font=("Courier", 25))
        self.__lHeader.grid(row=0, column=0, columnspan=2)
        self.__iFlag = ImageTk.PhotoImage(Image.open("flag.jpg"))
        self.__lFlag = tk.Label(self.__root, image=self.__iFlag)
        self.__lFlag.grid(row=1, column=0, columnspan=2)
        self.__bPlay = tk.Button(self.__root, text="Play")
        self.__bPlay.config(font=("Courier", 20))
        self.__bAdd = tk.Button(self.__root, text="Add")
        self.__bAdd.config(font=("Courier", 20))
        self.__bPlay.grid(row=2, column=0, sticky="NSEW")
        self.__bAdd.grid(row=2, column=1, sticky="NSEW")
        self.__root.tk.mainloop()