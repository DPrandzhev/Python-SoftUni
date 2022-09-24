import tkinter as tk

root = tk.Tk()

root.geometry("500x800")
root.title("STS Calculator")

label = tk.Label(root, text="Sky STS Calculator", font=('Arial', 20))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, font=("Arial", 16))
textbox.pack()

class MySTS:

    def __init__(self):
        self.root = tk.Tk()


    self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

root.mainloop()
