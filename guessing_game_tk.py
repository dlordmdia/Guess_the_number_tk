import random
import tkinter as tk

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")
        
        self.number = random.randint(1, 100)
        self.guesses = 0
        
        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.button = tk.Button(master, text="Guess", command=self.check_guess)
        self.button.pack()
        
        self.result = tk.Label(master, text="")
        self.result.pack()
        
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()
        
    def check_guess(self):
        self.guesses += 1
        guess = int(self.entry.get())
        if guess == self.number:
            message = f"Congratulations! You guessed the number in {self.guesses} guesses."
        elif guess < self.number:
            message = "Too low! Guess again."
        else:
            message = "Too high! Guess again."
        self.result.config(text=message)
        self.entry.delete(0, tk.END)

root = tk.Tk()
game = GuessingGame(root)
root.mainloop()
