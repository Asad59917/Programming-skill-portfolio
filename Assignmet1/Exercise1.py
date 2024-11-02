import tkinter as tk 
from tkinter import simpledialog, messagebox # for importing dialogue box and msg modules
import random

def display_menu(): #function to display the main menu
    Root = tk.Tk() # for creating the main window
    Root.title("Math Quiz") # For giving the title to the window


# Function to start the quiz and select mode
    def start_quiz(Mode): 
        Root.destroy() # i used this for closing window to make the output more clean
        quiz_window(Mode) # for opening the quiz window

# Creating labels and buttons for different levels
    tk.Label(Root, text="Select mode", font=("Helvetica", 16), fg= 'blue').pack(pady=10)
    tk.Button(Root, text="1. Easy", fg= 'black', bg= 'green',command=lambda: start_quiz("easy")).pack(pady=5)
    tk.Button(Root, text="2. Medium", fg= 'black', bg= 'yellow', command=lambda: start_quiz("Medium")).pack(pady=5)
    tk.Button(Root, text="3. Hard",fg= 'black', bg= 'red', command=lambda: start_quiz("Hard")).pack(pady=5)

    Root.mainloop() # To run the loop

def random_int(Mode): # funtion to get random integers according the dificulty mode choice
    if Mode == "easy":
        return random.randint(0, 9) # for easy mode questions will come betmen 0-9
    elif Mode == "Medium":
        return random.randint(10, 99) # for medium mode questions will come between 10-99
    elif Mode == "Hard":
        return random.randint(1000, 9999) #For hard mode questions will come from 1000-9999

def decide_operation(): 
    return random.choice(['+', '-']) # for randomly giving questions between addition and subtraction

def display_questions(Mode):
    num1 = random_int(Mode) # for getting first number 
    num2 = random_int(Mode) # for getting second number
    operation = decide_operation() # for getting random operations
    
    question = f"{num1} {operation} {num2} = ?" # for format of question
    correct_answer = eval(f"{num1} {operation} {num2}") # for calcuating the ans
    return question, correct_answer

def is_correct(user_answer, correct_answer): # this function will check of ans is correct
    return user_answer == correct_answer

def display_results(score): # funtion to display result 
    result_window = tk.Tk()
    result_window.title("Quiz Results")
    
    rank = "F"
    if score >= 90:
        rank = "A+"
    elif score >= 80:
        rank = "A"
    elif score >= 70:
        rank = "B"
    elif score >= 60:
        rank = "C"
    elif score >= 50:
        rank = "D"

#labels to display rand and marks
    tk.Label(result_window, text=f"Your final score: {score}/100", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(result_window, text=f"Rank: {rank}", font=("Helvetica", 16)).pack(pady=10)
    

# for playagain / restart quiz
    tk.Button(result_window, text="Play Again", command=lambda: [result_window.destroy(), display_menu()]).pack(pady=5)
    
    result_window.mainloop()


# function for running the quiz based o user selection mode
def quiz_window(Mode):
    score = 0 # counting score
    for _ in range(10): #loop for 10 questions
        question, correct_answer = display_questions(Mode) # for getting questions and answer
        user_answer = None # fro initializing users answer

# For allowing upto 3 attemps per question
        for attempt in range(3):
            user_answer = simpledialog.askinteger("Question", question) # answer prompt
            if user_answer is None:
                return  # exits the quiz if user selects cancel
            if is_correct(user_answer, correct_answer): # for checking if answer is true
                score += 10 if attempt == 0 else 5 # user will get full points on first try and half on other tries
                break
            else:
                messagebox.showerror("Incorrect", "Try again!")# this will display error for incorrect answer

    display_results(score) # to result after quiz is finished

# Start the program
if __name__ == "__main__":
    display_menu()