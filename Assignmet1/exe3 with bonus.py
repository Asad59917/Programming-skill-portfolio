import os
import tkinter as tk
from tkinter import messagebox # for displaying pop-up msgs

# Main window
root = tk.Tk()
root.title("Student Management System")
root.resizable(False,False) # to disable window resizing

# function which loads student data from the file and calculate marks and grade
def load_student_data():
    students = [] #empty list to store student data
    with open(r"C:\Users\User\OneDrive\python\Assignments\Assignmet1\studentMarks.txt") as file:
        num_students = int(file.readline().strip()) #reads the first line of the students as number
        for line in file: # loops for each line in file
            parts = line.strip().split(',') # from splitting line by comma to get each part of data
            student_id = int(parts[0])# to get student id as number
            name = parts[1] # fro gettung students name 
            coursework_marks = list(map(int, parts[2:5]))# getting course marks as number
            exam_mark = int(parts[5]) #gets the exams marks
            total_coursework = sum(coursework_marks) # for getting sum of marks
            total_score = total_coursework + exam_mark #calculating the total marks
            percentage = (total_score / 160) * 100 # for converting marks into percentage
            grade = calculate_grade(percentage)  
            students.append({     # stores all the data in student rec
                'id': student_id,
                'name': name,
                'coursework': total_coursework,
                'exam': exam_mark,
                'total': total_score,
                'percentage': percentage,
                'grade': grade
            })
    return students, num_students

# Function to calculate grades based on percentage
def calculate_grade(percentage):
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

# Function to display all students result
def view_all_students():
    output_text.delete(1.0, tk.END) #For clearing the text area
    output_text.insert(tk.END, "All Student Records:\n\n") 
    for student in students:  # loop whihc goes throug each student rec
        display_student(student) # displays all the reccords
    avg_percentage = sum(s['percentage'] for s in students) / len(students) # get avg percentage
    output_text.insert(tk.END, f"\nTotal students: {len(students)}\n") # display total students
    output_text.insert(tk.END, f"Class average percentage: {avg_percentage:.2f}%\n") # Display class avg

# Function to print individual student record
def display_student(student):
    output_text.insert(tk.END, f"Name: {student['name']}, ID: {student['id']}\n")
    output_text.insert(tk.END, f"Coursework: {student['coursework']}, Exam: {student['exam']}\n")
    output_text.insert(tk.END, f"Total Score: {student['total']}, Percentage: {student['percentage']:.2f}%\n")
    output_text.insert(tk.END, f"Grade: {student['grade']}\n\n")

# Function to display single record
def view_individual_student():
    search_id = id_entry.get() # to get Students id from user
    try:
        search_id = int(search_id) # this checks if enter id is a number
        student = next((s for s in students if s['id'] == search_id), None) # this finds students with that id
        output_text.delete(1.0, tk.END) # To clear the area
        if student:
            display_student(student)
        else:
            output_text.insert(tk.END, "Student not found.\n") # for displaying msg if student is not found
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid student ID.") # for displaying erroe for wrong ID

# For displaying highest marks/grade
def show_highest_marks():
    highest_student = max(students, key=lambda s: s['total']) # this finds students with heighest marks
    output_text.delete(1.0, tk.END) # for clearing the text area
    output_text.insert(tk.END, "Student with Highest Score:\n\n")
    display_student(highest_student) # displays the heighest marks

# For displaying lowest marks/grade
def show_lowest_marks():
    lowest_student = min(students, key=lambda s: s['total']) # check for lowest marks
    output_text.delete(1.0, tk.END) #to clear the text area
    output_text.insert(tk.END, "Student with Lowest Score:\n\n")
    display_student(lowest_student) # display lowest score student

# Function to add a student
def add_student_window():
    def add_student():
        try:
            student_id = int(id_entry_add.get()) # to get the student id and convert it into integer
            name = name_entry.get() # to get name
            coursework_marks = list(map(int, coursework_entry.get().split(',')))  #to get coursework marks as integer list 
            exam_mark = int(exam_entry.get()) # To get marks as integers
            total_coursework = sum(coursework_marks) #Calculate the total of course marks
            total_score = total_coursework + exam_mark # calculate total marks
            percentage = (total_score / 160) * 100 # get percentage
            grade = calculate_grade(percentage)
            students.append({   # for adding new student record in the list 
                'id': student_id,
                'name': name,
                'coursework': total_coursework,
                'exam': exam_mark,
                'total': total_score,
                'percentage': percentage,
                'grade': grade
            })
            messagebox.showinfo("Success", "Student added successfully!") # display success msg
            add_window.destroy() # for closinng the window for making output neat and clean
        except Exception as e:  
            messagebox.showerror("Input Error", str(e)) # for showing error if input is not valid

    add_window = tk.Toplevel(root) # new window for adding student
    add_window.title("Add Student")
    # labels and entry for id namw course work marks etc
    tk.Label(add_window, text="Student ID:").grid(row=0, column=0)
    id_entry_add = tk.Entry(add_window)
    id_entry_add.grid(row=0, column=1)

    tk.Label(add_window, text="Name:").grid(row=1, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=1, column=1)

    tk.Label(add_window, text="Coursework Marks (comma separated):").grid(row=2, column=0)
    coursework_entry = tk.Entry(add_window)
    coursework_entry.grid(row=2, column=1)

    tk.Label(add_window, text="Exam Mark:").grid(row=3, column=0)
    exam_entry = tk.Entry(add_window)
    exam_entry.grid(row=3, column=1)

    add_button = tk.Button(add_window, text="Add Student", command=add_student)
    add_button.grid(row=4, columnspan=2)

# Function to delete a student
def delete_student_window():
    def delete_student():
        try:
            student_id = int(id_entry_delete.get()) # get students id for deleting 
            global students
            students = [s for s in students if s['id'] != student_id]  # for removing student with that ID
            messagebox.showinfo("Success", "Student deleted successfully!") # display success msgs
            delete_window.destroy() # to close window
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid student ID.") # it will display the error is the user input incorrect error
    
    delete_window = tk.Toplevel(root) # for creating new window for deleting students record
    delete_window.title("Delete Student")
    
    tk.Label(delete_window, text="Student ID:").grid(row=0, column=0)
    id_entry_delete = tk.Entry(delete_window)
    id_entry_delete.grid(row=0, column=1)

    delete_button = tk.Button(delete_window, text="Delete Student", command=delete_student)
    delete_button.grid(row=1, columnspan=2)

# Function to update a student
def update_student_window():
    def update_student():
        try:
            student_id = int(id_entry_update.get()) # gets user input for it and convert it to integers
            student = next((s for s in students if s['id'] == student_id), None) # finds the student with entered id
            if student:
                student['name'] = name_entry_update.get() or student['name'] # update name if provided
                coursework_marks = list(map(int, coursework_entry_update.get().split(','))) # new cource marks 
                student['coursework'] = sum(coursework_marks) if coursework_marks else student['coursework']
                student['exam'] = int(exam_entry_update.get()) if exam_entry_update.get() else student['exam']
                total_coursework = student['coursework'] # calculate total coursemarks
                total_score = total_coursework + student['exam'] # calculate the sum of marks
                percentage = (total_score / 160) * 100 # new persentage
                student['percentage'] = percentage
                student['total'] = total_score
                student['grade'] = calculate_grade(percentage) # change the grade according to new percentage
                messagebox.showinfo("Success", "Student updated successfully!") # display msg of success
                update_window.destroy() # close window
            else:
                messagebox.showerror("Error", "Student not found.") # display error when no student is found 
        except Exception as e:
            messagebox.showerror("Input Error", str(e)) # shows error if the input is invalid

    update_window = tk.Toplevel(root) # new window for updating record
    update_window.title("Update Student")

    tk.Label(update_window, text="Student ID:").grid(row=0, column=0)
    id_entry_update = tk.Entry(update_window)
    id_entry_update.grid(row=0, column=1)

# labels and entry for updating records

    tk.Label(update_window, text="New Name:").grid(row=1, column=0)
    name_entry_update = tk.Entry(update_window)
    name_entry_update.grid(row=1, column=1)

    tk.Label(update_window, text="New Coursework Marks (comma separated):").grid(row=2, column=0)
    coursework_entry_update = tk.Entry(update_window)
    coursework_entry_update.grid(row=2, column=1)

    tk.Label(update_window, text="New Exam Mark:").grid(row=3, column=0)
    exam_entry_update = tk.Entry(update_window)
    exam_entry_update.grid(row=3, column=1)

    update_button = tk.Button(update_window, text="Update Student", command=update_student)
    update_button.grid(row=4, columnspan=2)

# Function to sort students
def sort_students_window():
    def sort_students():
        if sort_var.get() == "Ascending": # this will check is ascending is selected
            students.sort(key=lambda s: s['total']) # it will sorrt by total marks in ascending order
        elif sort_var.get() == "Descending": # this will check is Descending is selected
            students.sort(key=lambda s: s['total'], reverse=True)# it will sorrt by total marks in Descending order
        messagebox.showinfo("Success", "Students sorted successfully!") # shows msg of success
        sort_window.destroy() # close window

    sort_window = tk.Toplevel(root)
    sort_window.title("Sort Students")

    sort_var = tk.StringVar(value="Ascending") # for setting the default order to ascending
    tk.Label(sort_window, text="Sort By:").grid(row=0, column=0)
    tk.Radiobutton(sort_window, text="Ascending", variable=sort_var, value="Ascending").grid(row=1, column=0)
    tk.Radiobutton(sort_window, text="Descending", variable=sort_var, value="Descending").grid(row=1, column=1)

    sort_button = tk.Button(sort_window, text="Sort", command=sort_students)
    sort_button.grid(row=2, columnspan=2)

students, num_students = load_student_data()


frame = tk.Frame(root) 
frame.pack(pady=10)

# creating buttons for view all students adn searsh, add, delete, update,sort, exit

View_all_btn = tk.Button(frame, text="View All Students", bg='#ffe5b0', command=view_all_students)
View_all_btn.grid(row=0, column=0, padx=5, pady=5)

individual_search = tk.Label(frame, text="Student ID:")
individual_search.grid(row=1, column=0)
id_entry = tk.Entry(frame, width=10, bg='#d7f5f4')
id_entry.grid(row=1, column=1, padx=5)
individual_search_btn = tk.Button(frame, text="View Individual", bg='#b0edff', command=view_individual_student)
individual_search_btn.grid(row=1, column=2, padx=5)

highest_button = tk.Button(frame, text="Highest Marks", bg='#8bf098', command=show_highest_marks)
highest_button.grid(row=2, column=0, padx=5, pady=5)

lowest_button = tk.Button(frame, text="Lowest Marks", bg='#ff8282', command=show_lowest_marks)
lowest_button.grid(row=2, column=1, padx=5, pady=5)

add_button = tk.Button(frame, text="Add Student",bg='#e8fff1' , command=add_student_window)
add_button.grid(row=3, column=0, padx=5, pady=5)

delete_button = tk.Button(frame, text="Delete Student", bg='#ff3636', fg='white' , command=delete_student_window)
delete_button.grid(row=3, column=1, padx=5, pady=5)

update_button = tk.Button(frame, text="Update Student", bg='#e8d1ff' , command=update_student_window)
update_button.grid(row=3, column=2, padx=5, pady=5)

sort_button = tk.Button(frame, text="Sort Students", bg='#87b5ff' , command=sort_students_window)
sort_button.grid(row=2, column=2, columnspan=3, pady=5)

exit_button = tk.Button(frame, text="Exit", command=root.quit)
exit_button.grid(row=5, columnspan=3, pady=5)

output_text = tk.Text(root, width=50, height=20, bg='#ffedde')
output_text.pack(pady=10)

root.mainloop()
