import tkinter as tk
import tkinter.font as tkFont

# Reset the formula when 'C' is clicked
def clear() :
    formula.delete(0, tk.END)

# Calculate the formula when '=' is clicked
def answer() :
    try :
        output.config(text = str(eval(formula.get())))
        clear()
    except :
        output.config(text = "Error occurs.")

# Add a number or operator symbol into the formula
def click(buttonClicked) :
    if buttonClicked == '◀' :
        buttonClicked = '\b'
    temp = formula.get()
    formula.delete(0, tk.END)
    formula.insert(0, temp + buttonClicked)

# Set window object's properties
window = tk.Tk()
window.title("Tkinter Calculator")
# window.geometry("300x400")
window.resizable(False, False)

# Input formula
formula = tk.Entry(window)
font = tkFont.Font(size = 18)
formula.configure(font = font)
formula.grid(row = 0, column = 0, columnspan = 99, ipady = 10)

# Output the result
output = tk.Label(window, textvariable = "answer will be shown here", font = font)
output.grid(row = 1, column = 0, columnspan = 99, ipady = 10)

# Generate buttons
buttons = []
buttonText = [
    'C', '(', ')', '◀',
    '1', '2', '3', '/',
    '4', '5', '6', '*',
    '7', '8', '9', '-',
    '0', '.', '=', '+',
]
for i in range(len(buttonText)) :
    if i == 0 :                                                                                                         # 'C'
        buttons.append(tk.Button(window, text = buttonText[i], width = 8, height = 4, command = clear))
    elif i == 18 :                                                                                                      # '='
        buttons.append(tk.Button(window, text = buttonText[i], width = 8, height = 4, command = answer))
    else :
        buttons.append(tk.Button(window, text = buttonText[i], width = 8, height = 4, command = click(buttonText[i])))
    # print(i, buttons[i], buttonText[i])                                                                               # test : ok
    buttons[i].grid(row = 2 + int(i / 4), column = i % 4)

window.mainloop()