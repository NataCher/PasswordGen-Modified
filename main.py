
try:
    from tkinter import *
except ImportError:
    from tkinter import *
import time
import pyperclip
from PasswordGen import RandPass
from tkinter import filedialog

#---Main
def pwGenerator(size=8):
    data = RandPass(size)
    new_password = data[0]
    pw_strength = data[1]
    pw_color = data[2]
    PASSWORD.set(new_password)
    label_strength.configure(foreground="white", background=pw_color, text=pw_strength, font=('Segoe UI', 10, 'bold'), bd=10, height=1, width=10)
    gui.clipboard_clear()
    gui.clipboard_append(new_password)
    gui.update()
    time.sleep(0.02)
    gui.update()
    gui.mainloop()

#---MainWindow
gui = Tk()
gui.title("Password Generator")
gui.config(bg ='#92E3C0') 
gui.title('Password Gen') 
width = 600
height = 342
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
gui.geometry("%dx%d+%d+%d" % (width, height, x, y))

#---Var
PASSWORD = StringVar()
PW_SIZE = IntVar()
e1 = Entry(gui, text=PW_SIZE)
PW_SIZE.set(8) # размер пароля и установка значения по умолчанию в 8

#---WindowFrame
Top = Frame(gui, width=width)

Top.pack(side=TOP)
Top.config(bg = '#92E3C0')

Form = Frame(gui, width=width, background="#1A1A1A",)
Form.pack(side=TOP)

Bot = Frame(gui, width=width)
Bot.pack(side=BOTTOM)

#---Label
label_password = Label(Form, font=('Bernard MT Condensed', 18), text="Password",foreground="white", background="#1A1A1A", bd=10)
label_password.grid(row=0, pady=10)
label_strength = Label(Form, font=('Bernard MT Condensedt', 10, 'bold'), foreground="white", background="white", text="Weak", bd=10, height=1, width=10)
label_strength.grid(row=0, column=3, pady=10, padx=10)
label_pw_size = Label(Form, font=('Bernard MT Condensed', 18), text="Size",foreground="white", background="#1A1A1A", bd=10)
label_pw_size.grid(row=2, pady=10)
label_instructions = Label(Bot, width=width, font=('Bookman old style', 12, 'bold'), text="Password Generated to your Clipboard!", foreground="white", background="#1A1A1A", bd=1, relief=SOLID)
label_instructions.pack(fill=X)

#---Button
password = Entry(Form, font=('Bookman old style', 18), textvariable=PASSWORD,foreground="white", background="#1A1A1A", bd=10) 
password.grid(row=0, column=1, columnspan=2)
pw_size = Scale(Form, from_=8, to=24, length=200,width=24,sliderlength=14, orient=HORIZONTAL, variable=PW_SIZE, foreground="white", background="#1A1A1A",  font=(16))
pw_size.grid(row=2, column=1, columnspan=2)

#---CopytoClip
def Copy_password(): #---функция для копирования значения пароля из переменной PASSWORD в буфер обмена.
     pyperclip.copy(PASSWORD.get()) 

def Save_password():
    password = PASSWORD.get()  # Получите пароль из переменной PASSWORD
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(password)

Button(Top, font=('Bookman old style', 15), text="COPY TO CLIPBOARD", foreground="white", background="#1A1A1A", command=Copy_password).pack(pady=5)

btn_generate = Button(Form, font=('Bookman old style', 12), text="Generate Now", width=20, command=lambda: pwGenerator(PW_SIZE))
btn_generate.grid(row=4, column=1, columnspan=2)

Button(Top, font=('Bookman old style', 15), text="SAVE", foreground="white", background="#1A1A1A", command=Save_password).pack(pady=5)

gui.resizable(False, False)

gui.mainloop()
