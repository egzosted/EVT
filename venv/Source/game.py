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
        self.__lLast = tk.Label()
        self.__lLast.grid(row=4, column=0, columnspan=2)
        self.__lLast.config(font=("Courier", 25))

    def perform(self):
        # game
        for i in range(self.__number_words):
            wait_var = tk.IntVar()
            self.__lWordToTranslate.config(text=self.__words[2*i+1])    # in every round we have to change word to ask
            self.__bConfirm.config(command=lambda: self.__update(i, wait_var))    # function update checks answer
            self.__bConfirm.wait_variable(wait_var)

    # function to check answer and end game
    def __update(self, i, wait):
        answer = self.__eAnswer.get()
        if answer == self.__words[2*i]:
            self.__points += 1
            self.__lLast.config(text="Correct")
        else:
            self.__lLast.config(text="Mistake")
        self.__eAnswer.delete(0, 'end')
        wait.set(1)
        if i == self.__number_words - 1:
            self.__summary()

    def __summary(self):
        self.__bConfirm.grid_forget()
        self.__lLast.grid_forget()
        self.__lTranslation.grid_forget()
        self.__lWordToTranslate.grid_forget()
        self.__lAnswer.grid_forget()
        self.__eAnswer.grid_forget()
        self.__lPoints = tk.Label(text=f'You scored {self.__points} points')
        self.__lPoints.config(font=("Courier", 20))
        self.__lPoints.grid(row=1, column=0, columnspan=2)