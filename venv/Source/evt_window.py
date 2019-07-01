import tkinter as tk
import os
import fileOperations as fOp
from PIL import Image, ImageTk


class EvtWindow:

    # in constructor are created start components
    def __init__(self):
        self.__root = tk.Tk()
        self.__lHeader = tk.Label(text="English Vocabulary Tester", bg="white", fg="black")
        self.__lHeader.config(font=("Courier", 25))
        self.__iFlag = ImageTk.PhotoImage(Image.open("flag.jpg"))
        self.__lFlag = tk.Label(self.__root, image=self.__iFlag)
        self.__bPlay = tk.Button(self.__root, text="Play", command=self.__start_game)
        self.__bPlay.config(font=("Courier", 20))
        self.__bAdd = tk.Button(self.__root, text="Add", command=self.__add_word)
        self.__bAdd.config(font=("Courier", 20))
        self.__grid_start_window()
        self.__root.tk.mainloop()

    # user pressed play and then has to choose file with vocabulary to be able to start game
    def __start_game(self):
        txt_files = fOp.traverse_directory()  # list of txt files with vocabulary
        self.__clear_start_window()

    # user pressed add and now has to choose file and put word
    def __add_word(self):
        txt_files = fOp.traverse_directory()  # list of txt files with vocabulary
        self.__clear_start_window()
        self.__bAddExisting = tk.Button(self.__root, text="Add to existing file", command=self.__txt_files_menu(txt_files))
        self.__bAddNew = tk.Button(self.__root, text="Add to new file")
        self.__bAddExisting.config(font=("Courier", 15))
        self.__bAddNew.config(font=("Courier", 15))
        self.__bAddExisting.grid(row=2, column=0, sticky="NSEW")
        self.__bAddNew.grid(row=2, column=1, sticky="NSEW")

    # this method places start components in window
    def __grid_start_window(self):
        self.__lHeader.grid(row=0, column=0, columnspan=2)
        self.__lFlag.grid(row=1, column=0, columnspan=2)
        self.__bPlay.grid(row=2, column=0, sticky="NSEW")
        self.__bAdd.grid(row=2, column=1, sticky="NSEW")

    # removing unnecessary components
    def __clear_start_window(self):
        self.__bPlay.grid_forget()
        self.__bAdd.grid_forget()

    # drop down menu with txt files
    def __txt_files_menu(self, txt_files):
        if txt_files is not None:
            default = tk.StringVar(self.__root)
            default.set(txt_files[0])
            drop_down = tk.OptionMenu(self.__root, default, txt_files)
            drop_down.grid(row=3, column=0, columnspan=2)

