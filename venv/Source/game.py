import tkinter as tk


class Game:
    def __init__(self, words, root):
        self.__words = words    # list with vocabulary
        self.__number_words = len(words)//2  # number of words (divided by 2 cause they are in 2 languages)
        self.__root = root      # gui window
        self.__round = 1
        self.__points = 0       # correct answer +1 pt

        # tk inter objects
        self.__bConfirm = tk.Button(self.__root, text="Confirm")
        self.__bConfirm.grid(row=3, column=0, sticky="NSEW", columnspan=2)
        self.__lTranslation = tk.Label(text="Word to translate")
        self.__lTranslation.config(font=("Courier", 20))
        self.__lWordToTranslate = tk.Label()
        self.__lWordToTranslate.config(font=("Courier", 20))
        self.__lAnswer = tk.Label(text="Your answer")
        self.__lAnswer.config(font=("Courier", 20))
        self.__eAnswer = tk.Entry(self.__root)
        self.__lTranslation.grid(row=1, column=0)
        self.__lWordToTranslate.grid(row=1, column=1)
        self.__lAnswer.grid(row=2, column=0)
        self.__eAnswer.grid(row=2, column=1)

    def perform(self):
        # game
        for i in range(self.__number_words):
            print(i)