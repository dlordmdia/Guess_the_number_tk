import random
import tkinter as tk


class GuessingGame:
    # Initialize UI
    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")
        # Set window size in the format 'WidthxHeight'
        master.geometry("400x170")

        self.reset_game()  # Generate number & reset 'guesses' counter.

        tk.Label(master, text="Guess a number between 1 and 100:").pack(pady=5)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        tk.Button(master, text="Guess", command=self.check_guess).pack(pady=5)

        self.result = tk.Label(master, text="")
        self.result.pack(pady=5)

        self.quit_button = tk.Button(
            master, text="Quit", command=master.quit).pack()

        # Check Guess on 'Enter' pressed
        root.bind('<Return>', self.check_guess)

        # Exit Game on 'Escape' pressed
        root.bind('<Escape>', lambda e: root.destroy())

    # Regenerates the random number and resets the 'guesses' counter
    def reset_game(self):
        self.number = random.randint(1, 100)
        self.guesses = 0

    def check_guess(self, event=None):
        # If textbox is empty
        if self.entry.get() == "":
            return  # Ignore

        self.guesses += 1
        # Get the text from the textbox and convert it to an integer
        guess = int(self.entry.get())

        # Check if guess matches with generated number
        if guess == self.number:
            message = f"Congratulations! You guessed the number in {self.guesses} guesses."
            self.reset_game()  # Reset the game

            # Wait for 3 seconds (3000ms), then clear the result text.
            self.result.after(3000, lambda: self.result.config(text=""))
        elif guess < self.number:
            message = "Too low! Guess again."
        else:
            message = "Too high! Guess again."
        self.result.config(text=message)
        self.entry.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
