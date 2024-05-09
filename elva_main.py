from tkinter import *
#from func_lib import *
#import sys
#sys.path.append('~\UROP\UROP2023-Dmitir-Elva\lib')

#sys.path.insert(1, '.\UROP\UROP2023-Dmitir-Elva\lib')
#import func_lib

global e_username, e_password

root = Tk() #widgets
root.title('UROP')
#root.iconbitmap('nuslogo.ico')
root.geometry("800x500")

def lesson_choice(value, window):
    if value == 'Lesson 1':
        open_lesson_1_window()
    elif value == 'Lesson 2':
        open_lesson_2_window()
    elif value == 'Lesson 3':
        open_lesson_3_window()
    elif value == 'Lesson 4':
        open_lesson_4_window()
    else:
        lesson_choice_error_label = Label(window, text='Error when selecting lessons, please ask for assistance.')
        lesson_choice_error_label.place(x=50, y=300)    
    return

def confirm_button(value, window):
    lesson_choice(value, window)
    return

def check_quiz_answer(user_choice, correct_ans):
    if user_choice != correct_ans:
        return False
    else:
        return True

def open_lesson_1_window():
    lesson_1_window = Toplevel()
    lesson_1_window.title('Lesson 1 Kenemetics')
    #lesson_1_window.iconbitmap('nuslogo.ico')
    lesson_1_window.geometry('800x500')

    lesson_1_label1 = Label(lesson_1_window, text='Welcome to Lesson 1 Kinemetics!')
    lesson_1_label1.pack()

    lesson_1_label2 = Label(lesson_1_window, text='Quiz')
    lesson_1_label2.pack()

    lesson_1_label3 = Label(lesson_1_window, text='Question 1')
    lesson_1_label3.pack()

    OPTIONS = [
        ('Option 1', '1'),
        ('Option 2', '2')
        ('Option 3', '3')
    ]

    quiz_choice = StringVar()
    quiz_choice.set('')

    quiz_answer = '2'

    for choice, option in OPTIONS:
        Radiobutton(lesson_1_window, text=choice, variable=quiz_choice, value=option).pack() # fix position later

    submit_button = Button(lesson_1_window, text='Submit', command= lambda : check_quiz_answer(quiz_choice.get(), quiz_answer))
    submit_button.pack()
    return

def open_lesson_2_window():
    lesson_2_window = Toplevel()
    lesson_2_window.title('Lesson 2 Motion')
    #lesson_2_window.iconbitmap('nuslogo.ico')
    lesson_2_window.geometry('800x500')

    lesson_2_label1 = Label(lesson_2_window, text='Welcome to Lesson 2 Motion!')
    lesson_2_label1.place(x=25, y=25)
    return

def open_lesson_3_window():
    lesson_3_window = Toplevel()
    lesson_3_window.title('Lesson 3 Newton\'s Law')
    #lesson_3_window.iconbitmap('nuslogo.ico')
    lesson_3_window.geometry('800x500')

    lesson_3_label1 = Label(lesson_3_window, text='Welcome to Lesson 3 Newton\'s Law!')
    lesson_3_label1.place(x=25, y=25)
    return

def open_lesson_4_window():
    lesson_4_window = Toplevel()
    lesson_4_window.title('Lesson 4 Thermodynamics')
    #lesson_4_window.iconbitmap('nuslogo.ico')
    lesson_4_window.geometry('800x500')

    lesson_4_label1 = Label(lesson_4_window, text='Welcome to Lesson 4 Thermodynamics!')
    lesson_4_label1.place(x=25, y=25)
    return


def open_menu_window():
    menu_window = Toplevel()
    menu_window.title('Lesson menu')
    #menu_window.iconbitmap('nuslogo.ico')
    menu_window.geometry('800x500')

    menu_label1 = Label(menu_window, text='Please select your lesson')
    menu_label1.place(x=25, y=25)

    menu_exit_button = Button(menu_window, text='EXIT', command=menu_window.destroy)
    menu_exit_button.place(x=50, y=50)

    COURSE = [
    ('Lesson 1 Kinemetics', 'Lesson 1'),
    ('Lesson 2 Motion', 'Lesson 2'),
    ('Lesson 3 Newton\'s Law', 'Lesson 3'),
    ('Lesson 4 Thermodynamics', 'Lesson 4')]

    user_choice = StringVar()
    user_choice.set('Lesson 1 Kinemetics')

    for text, mode in COURSE:
        Radiobutton(menu_window, text=text, variable=user_choice, value=mode).pack() # fix position later
    
    def choicebutton_clicked(value):
        choicebutton_value_label = Label(menu_window, text=value)
        choicebutton_value_label.place(x=50, y=100)
    
    choice_button = Button(menu_window, text='Confirm', command= lambda : lesson_choice(user_choice.get(), menu_window)) # add quit menu window later
    choice_button.place(x=50, y=150)
    return

def main_window():
    main_label1 = Label(root, text='Physics learning tool for VI students')
    main_label1.place(x=30, y=30)

    main_label2 = Label(root, text='Project from NUS ECE department')
    main_label2.place(x=30, y=50)

    main_label_username = Label(root, text='Student name:')
    main_label_username.place(x=30, y=70)

    main_label_password = Label(root, text='Password:')
    main_label_password.place(x=30, y=90)

    e_username = Entry(root, width=30, fg='blue')
    e_username.place(x=140, y=70)
    e_password = Entry(root, width=30, fg='blue')
    e_password.place(x=140, y=90)

    main_login_button = Button(root, text='Login', padx=10, pady=10, bg='#33FFCA', fg='black', command=open_menu_window)
    main_login_button.place(x=100, y=110)

    main_exit_button = Button(root, text='EXIT', command=root.quit)
    main_exit_button.place(x=100, y=200)
    return


def get_data_login_button():
    mylabel = Label(root, text="Welcome to Physics, " + e_username.get() + "!")
    mylabel.grid(row=6, column=2)
    e_username.delete(0, END)
    return

main_window()
mainloop()