
from tkinter import *
import qrcode
cp = Tk()
cp.title("QR Code Generator")
cp.geometry("700x350")
cp.config(bg='#ADD8E6')
# Frame to hold widgets
frame = Frame(cp, bg='#ADD8E6')
frame.pack(expand=True)
# Labels and Entries
Label(frame, text='Enter Text or URL:', font=('Arial Black', 14), bg='#ADD8E6').grid(row=0, column=0, sticky='w', padx=10, pady=10)
msg = Entry(frame, width=40)
msg.grid(row=0, column=1, padx=10)

Label(frame, text='Enter File Name:', font=('Arial Black', 14), bg='#ADD8E6').grid(row=1, column=0, sticky='w', padx=10, pady=10)
save_me = Entry(frame, width=40)
save_me.grid(row=1, column=1, padx=10)

# Functions
def generate():
    data = msg.get()
    filename = save_me.get()
    if data and filename:
        img = qrcode.make(data)
        img.save(filename)
        Label(cp, text='QR Code Saved!', bg='#ADD8E6', fg='black', font=('Arial Black', 10)).pack()

def show():
    data = msg.get()
    if data:
        img = qrcode.make(data)
        img.show()

# Buttons
Button(cp, text='Generate QR Code', bd=5, command=generate, width=20).pack(pady=10)
Button(cp, text='Show QR Code', bd=5, command=show, width=20).pack(pady=5)

cp.mainloop()
