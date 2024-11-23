import tkinter as tk

# Define the Calculator class
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.result_var = tk.StringVar()
        
        # Create the result display
        self.result_display = tk.Entry(root, textvariable=self.result_var, font=('Arial', 20), bd=10, relief='sunken', width=15, justify='right')
        self.result_display.grid(row=0, column=0, columnspan=4)
        
        # Buttons layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            self.create_button(text, row, col)
        
    def create_button(self, text, row, col):
        """Create and place a button on the grid."""
        button = tk.Button(self.root, text=text, font=('Arial', 18), width=5, height=2, command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        """Handle button clicks."""
        current_text = self.result_var.get()
        
        if char == 'C':  # Clear the display
            self.result_var.set('')
        elif char == '=':  # Calculate the result
            try:
                result = str(eval(current_text))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            # Add the clicked button's value to the current text
            self.result_var.set(current_text + char)

# Create the main window
root = tk.Tk()
calculator = Calculator(root)

# Start the GUI loop
root.mainloop()
