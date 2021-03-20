import tkinter as tk
import math
import pickle
import os

root = tk.Tk()

result = 0  # The int result
str_result = ""  # The result in str
number = 0  # The number

# For float result
float_bool = 0
float_count = 0
temp_bool_float_div = 1

# For operations
calculatorOperation = 0
clear_display1 = 0
first_nr = 1

# For square root and 1/x
math_sqrt = 0
math_sqrt_result = 0
half_x_ = 0
half_x_result = 0

# Array for history
result_history = []

# The main display
display1 = tk.Label()
display2 = tk.Entry()

# History display
history_index = 0

# Save file path
save_path = ""
open_file = 0


class Window:
    # Window Config
    height = 550
    width = 550
    img = tk.PhotoImage(file='img/bg1.png')
    quit = tk.PhotoImage(file='img/x.png')
    history = tk.PhotoImage(file="img/his.png")


def calculation_equal():
    global display1, display2, number, str_result, result, calculatorOperation, clear_display1, first_nr, \
        temp_bool_float_div
    clear_display1 = 1
    if calculatorOperation == 1:
        first_nr = 1
        result += number
        str_result = str_result + str(number) + "="
        number = result
        result = 0
        display2.delete(0, tk.END)
        display2.insert(tk.END, number)
        calculatorOperation = 0
    elif calculatorOperation == 2:
        first_nr = 1
        result -= number
        str_result = str_result + str(number) + "="
        number = result
        result = 0
        display2.delete(0, tk.END)
        display2.insert(tk.END, number)
        calculatorOperation = 0
    elif calculatorOperation == 3:
        first_nr = 1
        result *= number
        str_result = str_result + str(number) + "="
        number = result
        result = 0
        display2.delete(0, tk.END)
        display2.insert(tk.END, number)
        calculatorOperation = 0
    elif calculatorOperation == 4:
        first_nr = 1
        result /= number
        result = result
        str_result = str_result + str(number) + "="
        number = result
        result = 0
        display2.delete(0, tk.END)
        display2.insert(tk.END, number)
        calculatorOperation = 0
    if len(result_history) == 5:
        result_history.pop(0)
    temp_bool_float_div = 1
    result_history.append(str_result + str(round(number, 3)))
    display1['text'] = str_result
    str_result = ""


def clear():
    global display1, display2, result, str_result, number, calculatorOperation, clear_display1, first_nr,\
        float_bool, float_count, temp_bool_float_div
    display1['text'] = ""
    display2.delete(0, tk.END)
    result = 0
    str_result = ""
    number = 0
    calculatorOperation = 0
    clear_display1 = 0
    first_nr = 1
    float_bool = 0
    float_count = 0
    temp_bool_float_div = 0


def clear_last_nr():
    global number, display2, result, float_bool, float_count, temp_bool_float_div
    if float_count > 0:
        if float_bool == 1 or float_bool == 2:
            number = float(str(number)[0:len(str(number)) - 1])
            float_count -= 1
            if float_count == 0:
                float_bool = 0
    else:
        number /= 10
        number = int(number)
    display2.delete(0, tk.END)
    display2.insert(tk.END, number)


def add_float():
    global number, display2, float_bool, temp_bool_float_div
    temp_bool_float_div = 1
    number /= 1
    display2.delete(0, tk.END)
    display2.insert(tk.END, number)
    float_bool = 1


def calculation(operation):
    global display2, number, str_result, result, calculatorOperation, clear_display1, first_nr, float_bool,\
        float_count, math_sqrt, math_sqrt_result, half_x_, half_x_result, temp_bool_float_div
    # Operation 1 = +
    # Operation 2 = -
    # Operation 3 = x
    # Operation 4 = /
    if first_nr == 1:
        result += number
        calculatorOperation = operation
        if math_sqrt == 1:
            str_result += "√(" + str(math_sqrt_result) + ")"
            math_sqrt = 0
        elif half_x_ == 1:
            str_result += "1/" + str(half_x_result) + ""
            half_x_ = 0
        else:
            str_result += str(number)

        if calculatorOperation == 1:
            str_result += "+"
        elif calculatorOperation == 2:
            str_result += "-"
        elif calculatorOperation == 3:
            str_result += "*"
        elif calculatorOperation == 4:
            str_result += "/"
        display1['text'] = str_result
        number = 0
        first_nr = 0
    else:
        display1['text'] = str_result
        if math_sqrt == 1:
            str_result += "√(" + str(number) + ")"
            math_sqrt = 0
        else:
            str_result += str(number)

        if operation == 1:
            str_result += "+"
        elif operation == 2:
            str_result += "-"
        elif operation == 3:
            str_result += "*"
        elif operation == 4:
            str_result += "/"

        if calculatorOperation == 1:
            result += number
        elif calculatorOperation == 2:
            result -= number
        elif calculatorOperation == 3:
            result *= number
        elif calculatorOperation == 4:
            result /= number

        display1['text'] = str_result
        calculatorOperation = operation
        number = 0

    float_bool = 0
    float_count = 0
    temp_bool_float_div = 1

    if clear_display1 == 1:
        clear_display1 = 0
        display1['text'] = ""
    display1['text'] = str_result
    display2.delete(0, tk.END)
    display2.insert(tk.END, number)


def sqrt():
    global display2, number, str_result, math_sqrt, math_sqrt_result
    math_sqrt_result = number
    number = math.sqrt(number)
    display1['text'] = str_result
    display2.delete(0, tk.END)
    display2.insert(tk.END, number)
    math_sqrt = 1


def half_x():
    global display2, number, str_result, half_x_result
    global half_x_
    half_x_result = number
    number = 1 / number
    display1['text'] = str_result
    display2.delete(0, tk.END)
    display2.insert(tk.END, number)
    half_x_ = 1


def add_nr(nr):
    global display2, number, float_bool, float_count
    # Checks if the number is higher than 25 the user cannot input more numbers
    if len(str(number)) >= 20:
        return
    if float_bool == 0:
        number = (number * 10) + nr
    else:
        float_count += 1
        if float_bool == 1:
            number = number + (nr / 10)
            float_bool = 2
        else:
            number = float(str(number) + str(nr))

    display2.delete(0, tk.END)
    display2.insert(tk.END, number)


def show_history():
    global display1, frame, result_history, result, str_result, number, delete_user_button
    result = 0
    str_result = ""
    number = 0
    frame.destroy()
    frame = tk.Frame(root, bd=10, bg="grey")
    frame['bg'] = '#666666'
    frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')

    display1 = tk.Label(frame, text="History", bg='#666666', font=("Arial", 20), fg="red")
    display1.place(relheight=0.1, relwidth=1, rely=0.05)

    delete_user_button = tk.Button(frame, bg='#f7f7f7', fg="black", borderwidth=0, command=lambda: delete_user(),
                                   text="DELETE")
    delete_user_button.place(relheight=0.15, relwidth=0.15, relx=0.85, rely=0.85)

    temp_string_label = ""
    for i in result_history:
        temp_string_label += i + "\n\n"
    content = tk.Label(frame, text=temp_string_label, bg='#666666', anchor='center', font=("Arial", 20), fg="white")
    content.place(relheight=0.85, relx=.5, rely=.6, anchor="center")


def delete_user():
    # Important variables are reset
    global result, str_result, number, calculatorOperation, clear_display1, first_nr, \
        float_bool, float_count, temp_bool_float_div, result_history
    result_history = []
    result = 0
    str_result = ""
    number = 0
    calculatorOperation = 0
    clear_display1 = 0
    first_nr = 1
    float_bool = 0
    float_count = 0
    temp_bool_float_div = 0

    # Variables based on save history are reset
    global save_path, history_index, save_path, open_file
    os.remove(save_path)
    login()
    history_index = 0
    save_path = ""
    open_file = 0


def history_button():
    global history_index, delete_user_button
    # History_index - 0 => null
    # History_index - 1 => show calculator
    # History_index - 2 => show history
    if history_index == 1:
        display()
        history_index = 2
        print("destroy")
    else:
        show_history()
        history_index = 1


def login():
    global display1, display2, frame, result_history, open_file, frame
    frame.destroy()
    frame = tk.Frame(root, bd=10, bg="grey")
    frame['bg'] = '#666666'
    frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.5, anchor='n')

    display1 = tk.Label(frame, text="Enter you name", bg='#666666', font=("Arial", 20), fg="white")
    display1.place(relheight=0.1, relwidth=1, rely=0.2)

    display2 = tk.Entry(frame, text="", font=("Arial", 16), bg="grey", fg="white", borderwidth=0)
    display2['bg'] = '#b0acac'
    display2.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.8)

    reg_button = tk.Button(frame, text="SUBMIT", font=("Arial", 14), bg="grey", fg="white", borderwidth=0,
                           command=lambda: click())
    reg_button['bg'] = '#b0acac'
    reg_button.place(relx=0.34, rely=0.6, relheight=0.1, relwidth=0.3)

    def click():
        global result_history, save_path, open_file
        path = "data/" + str(display2.get()).lower() + ".txt"
        if os.path.exists(path):
            save_path = path
            f = open(path, 'rb')
            if os.path.getsize(path) > 0:
                result_history = pickle.load(f)
            f.close()
            display()
        else:
            f = open(path, 'wb')
            save_path = path
            pickle.dump([], f)
            f.close()
            display()
        open_file = 1


def close():
    global open_file
    if open_file == 0:
        quit()
    global result_history, save_path
    f = open(save_path, 'wb')
    pickle.dump(result_history, f)
    f.close()
    quit()


def display():
    global display1, display2, button_history, frame
    frame.destroy()

    button_history = tk.Button(bg='#f7f7f7', fg="white", borderwidth=0, command=lambda: history_button(),
                               image=windows.history)
    button_history.place(relheight=0.1, relwidth=0.1, relx=0.9)

    frame = tk.Frame(root, bd=10, bg="grey")
    frame['bg'] = '#666666'
    frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')

    display1 = tk.Label(frame, text="", bg='#666666', anchor='w', font=("Arial", 16), fg="white")
    display1.place(relx=0.05, relheight=0.05, relwidth=1)

    display2 = tk.Entry(frame, text="", font=("Arial", 25), borderwidth=0, highlightthickness=0, bg="grey", fg="white")
    display2['bg'] = '#666666'
    display2.place(relx=0.05, rely=0.07, relheight=0.1, relwidth=1)

    # First row of the buttons
    button_c = tk.Button(frame, text='C', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                         fg="white", command=lambda: clear())
    button_c.place(relx=0.05, rely=0.2, relheight=0.14, relwidth=0.2)

    button_1x = tk.Button(frame, text='1/x', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                          fg="white", command=lambda: half_x())
    button_1x.place(relx=0.28, rely=0.2, relheight=0.14, relwidth=0.2)

    button_sqrt2 = tk.Button(frame, text='√(x)', borderwidth=0, highlightthickness=0, bg='#454545',
                             font=("Arial", 12), fg="white", command=lambda: sqrt())
    button_sqrt2.place(relx=0.52, rely=0.2, relheight=0.14, relwidth=0.2)

    button_delete = tk.Button(frame, text='<', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                              fg="white", command=lambda: clear_last_nr())
    button_delete.place(relx=0.75, rely=0.2, relheight=0.14, relwidth=0.2)

    # Second row of the buttons
    button_7 = tk.Button(frame, text='7', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                         fg="white", command=lambda: add_nr(7))
    button_7.place(relx=0.05, rely=0.36, relheight=0.14, relwidth=0.2)

    button_8 = tk.Button(frame, text='8', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                         fg="white", command=lambda: add_nr(8))
    button_8.place(relx=0.28, rely=0.36, relheight=0.14, relwidth=0.2)

    button_9 = tk.Button(frame, text='9', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                         fg="white", command=lambda: add_nr(9))
    button_9.place(relx=0.52, rely=0.36, relheight=0.14, relwidth=0.2)

    button_div = tk.Button(frame, text='/', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                           fg="white", command=lambda: calculation(4))
    button_div.place(relx=0.75, rely=0.36, relheight=0.14, relwidth=0.2)

    # Third row of the buttons
    button_4 = tk.Button(frame, text='4', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                         fg="white", command=lambda: add_nr(4))
    button_4.place(relx=0.05, rely=0.52, relheight=0.14, relwidth=0.2)

    button_5 = tk.Button(frame, text='5', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                         fg="white", command=lambda: add_nr(5))
    button_5.place(relx=0.28, rely=0.52, relheight=0.14, relwidth=0.2)

    button_6 = tk.Button(frame, text='6', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                         fg="white", command=lambda: add_nr(6))
    button_6.place(relx=0.52, rely=0.52, relheight=0.14, relwidth=0.2)

    button_x = tk.Button(frame, text='x', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                         fg="white", command=lambda: calculation(3))
    button_x.place(relx=0.75, rely=0.52, relheight=0.14, relwidth=0.2)

    # Forth row of the buttons
    button_1 = tk.Button(frame, text='1', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                         fg="white", command=lambda: add_nr(1))
    button_1.place(relx=0.05, rely=0.68, relheight=0.14, relwidth=0.2)

    button_2 = tk.Button(frame, text='2', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                         fg="white", command=lambda: add_nr(2))
    button_2.place(relx=0.28, rely=0.68, relheight=0.14, relwidth=0.2)

    button_3 = tk.Button(frame, text='3', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                         fg="white", command=lambda: add_nr(3))
    button_3.place(relx=0.52, rely=0.68, relheight=0.14, relwidth=0.2)

    button_minus = tk.Button(frame, text='-', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                             fg="white", command=lambda: calculation(2))
    button_minus.place(relx=0.75, rely=0.68, relheight=0.14, relwidth=0.2)

    # Fifth row of the buttons
    button_0 = tk.Button(frame, text='0', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                         fg="white", command=lambda: add_nr(0))
    button_0.place(relx=0.05, rely=0.84, relheight=0.14, relwidth=0.2)

    button_dot = tk.Button(frame, text='.', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                           fg="white", command=lambda: add_float())
    button_dot.place(relx=0.28, rely=0.84, relheight=0.14, relwidth=0.2)

    button_equal = tk.Button(frame, text='=', borderwidth=0, highlightthickness=0, bg='#0b97e3', font=("Arial", 12),
                             fg="white", command=lambda: calculation_equal())
    button_equal.place(relx=0.52, rely=0.84, relheight=0.14, relwidth=0.2)

    button_plus = tk.Button(frame, text='+', borderwidth=0, highlightthickness=0, bg='#454545', font=("Arial", 12),
                            fg="white", command=lambda: calculation(1))
    button_plus.place(relx=0.75, rely=0.84, relheight=0.14, relwidth=0.2)


# Configuring the window
windows = Window()
root.title("Calculator")
root.geometry("%dx%d" % (windows.width, windows.height))
root.resizable(False, False)

# Background of the window
background_label = tk.Label(root, image=windows.img)
background_label.place(relwidth=1, relheight=1)

# Main buttons
button_quit = tk.Button(bg='#f7f7f7', fg="white", borderwidth=0, command=lambda: close(), image=windows.quit)
button_quit.place(relheight=0.1, relwidth=0.1)

button_history = tk.Button
frame = tk.Frame()
delete_user_button = tk.Button

login()

root.mainloop()
