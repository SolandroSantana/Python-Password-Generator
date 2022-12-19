import secrets
import string
import tkinter
from tkinter import *
from tkinter import ttk, messagebox


class PasswordGenerator:

    # Tela inicial
    def __init__(self, master):

        self.letters = None
        self.digits = None
        self.special_chars = None
        self.alphabet = ''
        self.pwd_lenght = None
        self.pwd = None

        self.vletter = IntVar()
        self.vnum = IntVar()
        self.vsimbol = IntVar()

        self.master = master

        self.lblpassword = Label(master=master, text='Password Generator', font=['arial', '24'])
        self.lblpassword.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        self.txtpassword = Entry(master=master, width=30, font=['arial', '16'])
        self.txtpassword.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.lblscale = Label(master=master, text='Quantidade de caracteres: ', font=['arial', '12'])
        self.lblscale.place(relx=0.28, rely=0.45, anchor=tkinter.CENTER)

        self.numofchar = Scale(master=master, orient='horizontal', to=20, length=100)
        self.numofchar.place(relx=0.65, rely=0.43, anchor=tkinter.CENTER)

        self.inpletters = Checkbutton(master=master, text='Incluir letras', variable=self.vletter, font=['arial', '12'])
        self.inpletters.place(relx=0.18, rely=0.55, anchor=tkinter.CENTER)

        self.inpnumbers = Checkbutton(master=master, text='Incluir números', variable=self.vnum, font=['arial', '12'])
        self.inpnumbers.place(relx=0.21, rely=0.6, anchor=tkinter.CENTER)

        self.inpsimbol = Checkbutton(master=master, text='Incluir simbolos', variable=self.vsimbol, font=['arial', '12'])
        self.inpsimbol.place(relx=0.21, rely=0.65, anchor=tkinter.CENTER)

        self.btngenerate = Button(master=master, text='Generate Password', command=self.generate_password)
        self.btngenerate.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    # Função que gera a senha
    def generate_password(self):
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.special_chars = string.punctuation

        if self.vletter.get() == 0 and self.vnum.get() == 0 and self.vsimbol.get() == 0:

            messagebox.showwarning("Warning!", "Inclua ao menos um caracter na senha!")

        else:

            if self.vletter.get() == 1:

                self.alphabet = self.letters

            if self.vnum.get() == 1:

                self.alphabet = self.digits

            if self.vsimbol.get() == 1:

                self.alphabet = self.special_chars

            if self.vletter.get() == 1 and self.vnum.get() == 1:

                self.alphabet = self.letters + self.digits

            if self.vletter.get() == 1 and self.vsimbol.get() == 1:

                self.alphabet = self.letters + self.special_chars

            if self.vnum.get() == 1 and self.vsimbol.get() == 1:

                self.alphabet = self.digits + self.special_chars

            if self.vletter.get() == 1 and self.vnum.get() == 1 and self.vsimbol.get() == 1:

                self.alphabet = self.letters + self.digits + self.special_chars

            self.pwd_lenght = self.numofchar.get()

            self.pwd = ''

            self.txtpassword.delete(0, tkinter.END)

            for i in range(self.pwd_lenght):
                self.pwd += ''. join(secrets.choice(self.alphabet))

            self.txtpassword.insert(0, self.pwd)


if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    root.geometry('400x400')
    root.title('Password Generator')
    password_generator = PasswordGenerator(root)
    root.mainloop()
