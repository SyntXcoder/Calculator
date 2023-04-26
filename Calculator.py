from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the display
        self.display = Entry(master, width=25, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        # Create the buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row, row_values in enumerate(buttons, start=1):
            for column, button_value in enumerate(row_values):
                button = Button(master, text=button_value, width=5, height=2, font=('Arial', 12))
                button.grid(row=row, column=column, padx=3, pady=3)
                button.bind('<Button-1>', self.handle_click)

        # Create the clear button
        clear_button = Button(master, text='C', width=5, height=2, font=('Arial', 12))
        clear_button.grid(row=5, column=1, padx=3, pady=3)
        clear_button.bind('<Button-1>', self.clear)

    def handle_click(self, event):
        button = event.widget
        text = button['text']

        if text == '=':
            # Evaluate the expression
            try:
                result = eval(self.display.get())
            except:
                result = 'Error'
            self.display.delete(0, END)
            self.display.insert(0, str(result))
        else:
            self.display.insert(END, text)

    def clear(self, event):
        self.display.delete(0, END)

root = Tk()
calculator = Calculator(root)
root.mainloop()
