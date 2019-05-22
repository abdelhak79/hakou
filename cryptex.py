import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import pyperclip


class CIPHER:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Cryptex')
        self.root.resizable(False, False)
        self.create_widget()
        style = ttk.Style()
        style.configure('TLabel', background='light grey')
        style.configure('TButton', background='light grey')
        style.configure('TRadiobutton', background='light grey')
        self.root.configure(background='light grey')

    def show_text(self):
        translated = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'

        for symbol in self.text.get():
            if symbol in letters:
                num = letters.find(symbol)
                if self.radio_but.get() == 0:
                    num = num + int(self.code.get())
                elif self.radio_but.get() == 1:
                    num = num - int(self.code.get())

                if num >= len(letters):
                    num = num - len(letters)
                elif num < 0:
                    num = num + len(letters)
                translated = translated + letters[num]

            else:
                translated = translated + symbol

        value = translated
        self.scr.insert(tk.INSERT, value + '\n')

        pyperclip.copy(translated)

    def _delete(self):
        self.scr.delete(1.0, tk.END)

    def create_widget(self):
        ttk.Label(self.root, text='Enter Your Message: ').grid(row=0, column=0, padx=10, pady=10)
        self.text = tk.StringVar()
        enter_text = ttk.Entry(self.root, width=36, textvariable=self.text, font=('Arial', 14))
        enter_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        enter_text.focus()

        self.radio_but = tk.IntVar()
        self.radio_but.set(3)
        type_msg = ['Encrypt', 'Decrypt']
        for col in range(2):
            btns = ttk.Radiobutton(self.root, text=type_msg[col], variable=self.radio_but, value=col)
            btns.grid(row=2, column=col, padx=10, pady=10)

        self.code = tk.StringVar()
        chosen_code = ttk.Combobox(self.root, width=7, textvariable=self.code, state='readonly')
        chosen_code.grid(row=2, column=2, padx=10, pady=10)
        chosen_code['value'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
        chosen_code.current(0)

        scroll_w = 36
        scroll_h = 9
        self.scr = scrolledtext.ScrolledText(self.root, width=scroll_w, height=scroll_h,
                                             wrap=tk.WORD, font=('Arial', 14))
        self.scr.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        self.encrypt = ttk.Button(self.root, text='Encrypt', command=self.show_text)
        self.encrypt.grid(row=4, column=1, padx=10, pady=10)

        self.delete = ttk.Button(self.root, text='Delete', command=self._delete)
        self.delete.grid(row=4, column=2, padx=10, pady=10)

        for child in self.root.winfo_children():
            child.grid_configure(sticky=tk.W)


crypt = CIPHER()
crypt.root.mainloop()
