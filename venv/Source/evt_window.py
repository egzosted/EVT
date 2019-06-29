import tkinter as tk
import os
import fileOperations as fop
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
        self.__bAdd = tk.Button(self.__root, text="Add")
        self.__bAdd.config(font=("Courier", 20))
        self.__grid_start_window()
        self.__root.tk.mainloop()

    # user entered play and then has to choose file with vocabulary to be able to start game
    def __start_game(self):
        txt_files = []  # list of files with vocabulary
        for dir_path, dir_names, file_names in os.walk(os.getcwd()):   # traversing through directory
            fop.get_files(dir_path, file_names, txt_files)
        print(txt_files)

    # this method places start components in window
    def __grid_start_window(self):
        self.__lHeader.grid(row=0, column=0, columnspan=2)
        self.__lFlag.grid(row=1, column=0, columnspan=2)
        self.__bPlay.grid(row=2, column=0, sticky="NSEW")
        self.__bAdd.grid(row=2, column=1, sticky="NSEW")

