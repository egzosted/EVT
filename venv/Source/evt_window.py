import tkinter as tk
import tkinter.messagebox as tkm
import fileOperations as fOp
import game as gm
from PIL import Image, ImageTk

PLAY = 0
ADD = 1


class EvtWindow:

    def __init__(self):
        """
            in constructor are created start components:
            - label with header
            - image with flag
            - button to start playing game and button to add file with vocabulary
        """
        self.__root = tk.Tk()
        self.__lHeader = tk.Label(text="English Vocabulary Tester", bg="white", fg="black")
        self.__lHeader.config(font=("Courier", 25))
        self.__iFlag = ImageTk.PhotoImage(Image.open("flag.jpg"))
        self.__lFlag = tk.Label(self.__root, image=self.__iFlag)
        self.__bPlay = tk.Button(self.__root, text="Play", command=self.__start_game)
        self.__bPlay.config(font=("Courier", 20))
        self.__bAdd = tk.Button(self.__root, text="Add", command=self.__add_word)
        self.__bAdd.config(font=("Courier", 20))

        # confirm button (will be used later)
        self.__bConfirm = tk.Button(self.__root, text="Confirm")
        self.__bConfirm.config(font=("Courier", 15))

        self.__grid_start_window()
        self.__root.tk.mainloop()

    def __start_game(self):
        """
            user pressed play and then has to choose file with vocabulary to be able to start game
        """
        txt_files = fOp.traverse_directory()  # list of txt files with vocabulary
        self.__txt_files_menu(txt_files, PLAY)
        self.__clear_start_window()

    # user chose file with vocabulary
    def __game(self):
        file_name = self.__default.get()
        self.__lFlag.grid_forget()
        self.__lDrop_down.grid_forget()
        self.__drop_down.grid_forget()
        self.__bConfirm.grid_forget()
        # getting list of words from txt_file(translation is also here)
        words = fOp.get_words(file_name)
        game = gm.Game(words, self.__root)  # creating new object of game
        game.perform()    # this method performs game in game object

    # user pressed add and now has to choose file and put word
    def __add_word(self):
        txt_files = fOp.traverse_directory()  # list of txt files with vocabulary
        self.__clear_start_window()
        self.__bAddExisting = tk.Button(
            self.__root, text="Add to existing file", command=lambda: self.__txt_files_menu(txt_files, ADD))
        self.__bAddNew = tk.Button(self.__root, text="Add to new file", command=self.__get_name)
        self.__bAddExisting.config(font=("Courier", 15))
        self.__bAddNew.config(font=("Courier", 15))
        self.__bAddExisting.grid(row=2, column=0, sticky="NSEW")
        self.__bAddNew.grid(row=2, column=1, sticky="NSEW")

    def __grid_start_window(self):
        """
            this method places start components in window
        """
        self.__lHeader.grid(row=0, column=0, columnspan=2)
        self.__lFlag.grid(row=1, column=0, columnspan=2)
        self.__bPlay.grid(row=2, column=0, sticky="NSEW")
        self.__bAdd.grid(row=2, column=1, sticky="NSEW")

    def __clear_start_window(self):
        """
        removing unnecessary components
        """
        self.__bPlay.grid_forget()
        self.__bAdd.grid_forget()

    # drop down menu with txt files
    def __txt_files_menu(self, txt_files, mode):
        # adding button not necessary
        if mode == ADD:
            self.__bAddExisting.grid_forget()
            self.__bAddNew.grid_forget()
        if txt_files is not None:
            # label with instruction
            self.__lDrop_down = tk.Label(text="Choose file")
            self.__lDrop_down.grid(row=2, column=0)
            # drop_down menu
            self.__default = tk.StringVar(self.__root)
            self.__default.set(txt_files[0])
            self.__drop_down = tk.OptionMenu(self.__root, self.__default, *txt_files)
            self.__drop_down.grid(row=2, column=1)
            if mode == ADD:
                self.__bConfirm.config(command=lambda: self.__add_to_file("drop_down"))
            if mode == PLAY:
                self.__bConfirm.config(command=self.__game)
            self.__bConfirm.grid(row=3, column=0, columnspan=2)
        else:
            tkm.showerror("Error", "Files not found")
            self.__bPlay.grid(row=2, column=0, sticky="NSEW")
            self.__bAdd.grid(row=2, column=1, sticky="NSEW")

    # name of new file with vocabulary
    def __get_name(self):
        self.__bAddExisting.grid_forget()
        self.__bAddNew.grid_forget()
        # label with instruction
        self.__lNewFile = tk.Label(text="Enter name of file")
        self.__lNewFile.grid(row=2, column=0)
        # entry with new name of file
        self.__eNewFile = tk.Entry(self.__root)
        self.__eNewFile.grid(row=2, column=1)
        self.__bConfirm.config(command=lambda: self.__add_to_file("entry"))
        self.__bConfirm.grid(row=3, column=0, columnspan=2)

    # final addition
    def __add_to_file(self, name_source):
        if name_source == "drop_down":
            file_name = self.__default.get()
            self.__lDrop_down.grid_forget()
            self.__drop_down.grid_forget()
            self.__bConfirm.grid_forget()

        if name_source == "entry":
            file_name = self.__eNewFile.get()
            self.__lNewFile.grid_forget()
            self.__eNewFile.grid_forget()

        self.__lNewWord = tk.Label(text="Enter word")
        self.__lTranslation = tk.Label(text="Enter translation")
        self.__eNewWord = tk.Entry(self.__root)
        self.__eTranslation = tk.Entry(self.__root)
        self.__lNewWord.grid(row=2, column=0)
        self.__eNewWord.grid(row=2, column=1)
        self.__lTranslation.grid(row=3, column=0)
        self.__eTranslation.grid(row=3, column=1)
        self.__bConfirm.config(command=lambda: self.__put_in_file(file_name))
        self.__bConfirm.grid(row=4, column=0, columnspan=2)

    # add word to file
    def __put_in_file(self, file_name):
        self.__word = self.__eNewWord.get()
        self.__translation = self.__eTranslation.get()
        with open(file_name, 'a+') as f:
            f.write(self.__word)
            f.write("\n")
            f.write(self.__translation)
            f.write("\n")
        self.__finish_add()

    # after finishing word addition we can back to start window
    def __finish_add(self):
        self.__lNewWord.grid_forget()
        self.__lTranslation.grid_forget()
        self.__eNewWord.grid_forget()
        self.__eTranslation.grid_forget()
        self.__bConfirm.grid_forget()
        self.__grid_start_window()
