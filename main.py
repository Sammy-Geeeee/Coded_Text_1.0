# Text Encoding Program

# This program is to take a string of text and then make it all different so it can't be read
# Then there will a decoding section to ensure that it can be reversed and read as per normal again

from tkinter import *
from tkinter.ttk import *
from functions import *
import pyperclip


# Program Functions
def encrypt_apply():
    text_input = str(entry_decrypted.get())
    keys = [int(chosen_key_1.get()), int(chosen_key_2.get()), int(chosen_key_3.get()), int(chosen_key_4.get())]

    text_output = encrypt(text_input, keys)
    entry_encrypted.delete(0, END)
    entry_encrypted.insert(0, text_output)


def decrypt_apply():
    text_input = str(entry_encrypted.get())
    keys = [int(chosen_key_1.get()), int(chosen_key_2.get()), int(chosen_key_3.get()), int(chosen_key_4.get())]

    text_output = decrypt(text_input, keys)
    entry_decrypted.delete(0, END)
    entry_decrypted.insert(0, text_output)


def de_copy_text():
    de_text = entry_decrypted.get()
    pyperclip.copy(de_text)


def de_paste_text():
    clipboard_text = pyperclip.paste()
    entry_decrypted.delete(0, END)
    entry_decrypted.insert(0, clipboard_text)


def en_copy_text():
    en_text = entry_encrypted.get()
    pyperclip.copy(en_text)


def en_paste_text():
    clipboard_text = pyperclip.paste()
    entry_encrypted.delete(0, END)
    entry_encrypted.insert(0, clipboard_text)


# Universal Variables
int_padding = 2

optionmenu_ext_padding_x = (10, 5)
optionmenu_ext_padding_y = 5

label_width = 10
label_ext_padding = (15, 5)

entry_width = 150
entry_ext_padding = 10

button_width = 10
button_ext_padding = 10

# Creating Main Window
window = Tk()
window.title('Text Cryptographer')
window.geometry('800x250')

# Creating all the main elements
frame_keys = Frame(master=window)  # Frames for each section
frame_decrypted = Frame(master=window)
frame_buttons = Frame(master=window)
frame_encrypted = Frame(master=window)

frame_keys.pack(expand=1, fill=BOTH)  # Packing in each frame
frame_decrypted.pack(expand=1, fill=BOTH)
frame_buttons.pack(expand=1, fill=BOTH)
frame_encrypted.pack(expand=1, fill=BOTH)

# Key frame widgets
chosen_key_1 = StringVar()  # To create StringVars for all the key options
chosen_key_2 = StringVar()
chosen_key_3 = StringVar()
chosen_key_4 = StringVar()

key_options = list(range(1, 51))  # To make the list of options for each key
frame_keys.columnconfigure([1, 2, 3, 4], weight=1)  # To change the layout of each column

label_key = Label(master=frame_keys, width=label_width, text='Keys')  # Creates all the widgets
option_key_1 = OptionMenu(frame_keys, chosen_key_1, key_options[0], *key_options)
option_key_2 = OptionMenu(frame_keys, chosen_key_2, key_options[0], *key_options)
option_key_3 = OptionMenu(frame_keys, chosen_key_3, key_options[0], *key_options)
option_key_4 = OptionMenu(frame_keys, chosen_key_4, key_options[0], *key_options)

label_key.grid(row=0, column=0, sticky=W+E, ipadx=int_padding, ipady=int_padding, padx=label_ext_padding, pady=label_ext_padding)  # Positions all the widgets
option_key_1.grid(row=0, column=1, sticky=W+E, ipadx=int_padding, ipady=int_padding, padx=optionmenu_ext_padding_x, pady=optionmenu_ext_padding_y)
option_key_2.grid(row=0, column=2, sticky=W+E, ipadx=int_padding, ipady=int_padding, padx=optionmenu_ext_padding_x, pady=optionmenu_ext_padding_y)
option_key_3.grid(row=0, column=3, sticky=W+E, ipadx=int_padding, ipady=int_padding, padx=optionmenu_ext_padding_x, pady=optionmenu_ext_padding_y)
option_key_4.grid(row=0, column=4, sticky=W+E, ipadx=int_padding, ipady=int_padding, padx=optionmenu_ext_padding_x, pady=optionmenu_ext_padding_y)

# Decryption frame widgets
frame_decrypted.columnconfigure(1, weight=1)  # To change the layout of each column

label_input = Label(master=frame_decrypted, width=label_width, text='Decrypted')  # Creates all the widgets
entry_decrypted = Entry(master=frame_decrypted, width=entry_width)
button_de_copy = Button(master=frame_decrypted, command=de_copy_text, text='Copy', width=button_width)
button_de_paste = Button(master=frame_decrypted, command=de_paste_text, text='Paste', width=button_width)

label_input.grid(row=0, column=0, ipadx=int_padding, ipady=int_padding, padx=label_ext_padding, pady=label_ext_padding)  # Positions all the widgets
entry_decrypted.grid(row=0, column=1, ipadx=int_padding, ipady=int_padding, padx=entry_ext_padding, pady=entry_ext_padding)
button_de_copy.grid(row=0, column=2, ipadx=int_padding, ipady=int_padding, padx=button_ext_padding, pady=button_ext_padding)
button_de_paste.grid(row=0, column=3, ipadx=int_padding, ipady=int_padding, padx=button_ext_padding, pady=button_ext_padding)

# Button frame widgets
frame_buttons.columnconfigure([0, 1], weight=1)

button_encrypt = Button(master=frame_buttons, command=encrypt_apply, text='Encrypt', width=button_width)
button_decrypt = Button(master=frame_buttons, command=decrypt_apply, text='Decrypt', width=button_width)

button_encrypt.grid(row=0, column=0, sticky=EW, ipadx=int_padding, ipady=int_padding, padx=button_ext_padding, pady=button_ext_padding)
button_decrypt.grid(row=0, column=1, sticky=EW, ipadx=int_padding, ipady=int_padding, padx=button_ext_padding, pady=button_ext_padding)

# Encryption frame widgets
frame_encrypted.columnconfigure(1, weight=1)  # To change the layout of each column

label_output = Label(master=frame_encrypted, width=label_width, text='Encrypted')  # Creates all the widgets
entry_encrypted = Entry(master=frame_encrypted, width=entry_width)
button_en_copy = Button(master=frame_encrypted, command=en_copy_text, text='Copy', width=button_width)
button_en_paste = Button(master=frame_encrypted, command=en_paste_text, text='Paste', width=button_width)

label_output.grid(row=0, column=0, ipadx=int_padding, ipady=int_padding, padx=label_ext_padding, pady=label_ext_padding)  # Positions all the widgets
entry_encrypted.grid(row=0, column=1, ipadx=int_padding, ipady=int_padding, padx=entry_ext_padding, pady=entry_ext_padding)
button_en_copy.grid(row=0, column=2, ipadx=int_padding, ipady=int_padding, padx=button_ext_padding, pady=button_ext_padding)
button_en_paste.grid(row=0, column=3, ipadx=int_padding, ipady=int_padding, padx=button_ext_padding, pady=button_ext_padding)

window.mainloop()

# End - 16/03/2021

# FUTURE WORK OR FURTHER ITERATIONS
# Make the entry fields into text fields so that lots of text can be entered into them
# Will have to change the functions somehow to view the newline \n key as a character
# As per previous works, use classes to simplify the creation of all the tkinter widgets?
