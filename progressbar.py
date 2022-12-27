import tkinter as tk
from tkinter import ttk

class ProgressBar:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x60')
        self.root.title('Loading... / กำลังโหลด')
        self.root.grid()
        self.init_components()

    def init_components(self):
        pb = ttk.Progressbar(self.root, orient='horizontal', mode='indeterminate', length=580)
        pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        pb.start()
        pb.after(10000, lambda: pb.stop())
        self.root.after(10001, lambda: self.root.quit())
        self.root.after(10002, lambda: self.attention())

    def attention(self):
        pb = ttk.Label(self.root, text='Click "x" to read the result / กด "x" เพื่ออ่านผล')
        pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

    def run(self):
        self.root.mainloop()
