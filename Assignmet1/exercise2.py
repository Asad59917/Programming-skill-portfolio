import tkinter as tk
import random
from PIL import ImageTk,Image

# for creating the main window
root = tk.Tk()
root.title("Alexa tell me a Joke")
root.geometry("400x500")
root.configure(background="#e5ebc5")


# to load jokes from a text file
def load_jokes():
    with open(r"C:\Users\User\Downloads\randomJokes.txt") as file:
        return [line.strip() for line in file if line.strip()] #for ignoring the empty lines

# to display a random joke
def tell_joke():
    joke = random.choice(jokes) # to pick random joke 
    setup, punchline = joke.split("?", 1) # for splitting the joke into two parts
    setup_label.config(text=f"Setup: {setup}?") # to diplay setup in setup label
    punchline_label.config(text="") #to leave space for punchline for later to display 
    global current_punchline
    current_punchline = punchline.strip() # to store the punchline globally
    show_button.config(state=tk.NORMAL) # to enabel the show punchline button

#to show the punchline
def show_punchline():
    punchline_label.config(text=f"Punchline: {current_punchline}")# to display the punchline
    show_button.config(state=tk.DISABLED) # to disable the punchline after showing the punchline



# Load jokes
jokes = load_jokes()# to load jokes from txt file
current_punchline = "" # for making punchline storage

# For making labels and buttons
setup_label = tk.Label(root, text="", fg='Red',bg='#e5ebc5', wraplength=300, font=("Helvetica", 14))
setup_label.pack(pady=20)

punchline_label = tk.Label(root, text="", fg='green',bg='#e5ebc5', wraplength=300, font=("Helvetica", 14))
punchline_label.pack(pady=20)

show_button = tk.Button(root, text="Show Punchline",fg='Black',bg='yellow',font=("Helvetica", 12) , command=show_punchline, state=tk.DISABLED)
show_button.pack(pady=10)

tell_button = tk.Button(root, text="Alexa tell me a Joke", fg='black',bg='light blue',font=("Helvetica", 12) , command=tell_joke)
tell_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", fg='white', bg='red',font=("Helvetica", 10), command=root.quit)
quit_button.pack(pady=10)

root.iconphoto(False, ImageTk.PhotoImage(file=r"C:\Users\User\OneDrive\python\Assignments\Assignmet1\clown.png"))

# Run the application
root.mainloop()