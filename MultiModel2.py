import tkinter as tk
from tkinter import messagebox
from googletrans import Translator, LANGUAGES


def translate():
    message = text_box.get("1.0", tk.END).strip()
    target_language = language_var.get()

    if not message:
        messagebox.showwarning(
            "Input Error", "Please Enter English Words To Translate."
        )
        return

    if target_language not in LANGUAGES:
        messagebox.showerror(
            "Translation Error",
            "Invalid Language Code Selected. Please Select Valid Language Code.",
        )
        return

    translator = Translator()
    try:
        translated_message = translator.translate(message, dest=target_language).text
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Translated :- " + translated_message)
        output_box.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))


def clear_output():
    text_box.delete("1.0", tk.END)
    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    output_box.config(state=tk.DISABLED)


def show_about():
    messagebox.showinfo(
        "About", "English To Hindi-Gujarati Translator\nVersion 1.0\nDeveloped By A&J"
    )


def show_help():
    messagebox.showinfo(
        "Help",
        "Enter English Words, Select Target Tanguage, Then Click ‘Translate’ To Get The Translation.",
    )


root = tk.Tk()
root.title("English To Hindi-Gujarati Translator Developed By A&J")
root.geometry("1920x1080")
root.configure(bg="#343f71")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)
help_menu.add_command(label="Help", command=show_help)

title_label = tk.Label(
    root,
    text="English To Hindi-Gujarati Translator",
    font=("Arial", 30, "bold"),
    bg="#343f71",
    fg="#ffffff",
)
title_label.pack(pady=20)

input_label = tk.Label(
    root, text="Enter English Text:", font=("Arial", 20), bg="#343f71", fg="#ff9900"
)
input_label.pack(pady=10)

text_box = tk.Text(
    root, height=7, width=50, font=("Courier", 15), bg="#37475a", fg="#ffffff"
)
text_box.pack(pady=10)

language_var = tk.StringVar(value="hi")
radio_hi = tk.Radiobutton(
    root,
    text="Hindi    ",
    variable=language_var,
    value="hi",
    font=("Arial", 15),
    bg="#343f71",
    fg="#ffffff",
    selectcolor="#e74c3c",
)
radio_hi.pack(pady=5)
radio_gu = tk.Radiobutton(
    root,
    text="Gujarati",
    variable=language_var,
    value="gu",
    font=("Arial", 15),
    bg="#343f71",
    fg="#ffffff",
    selectcolor="#e74c3c",
)
radio_gu.pack(pady=5)

button_frame = tk.Frame(root, bg="#343f71")
button_frame.pack(pady=20)

translate_button = tk.Button(
    button_frame,
    text="Translate",
    command=translate,
    font=("Arial", 15),
    bg="#009500",
    fg="#ffffff",
    activebackground="#3498db",
    activeforeground="#000000",
)
translate_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_output,
    font=("Arial", 15),
    bg="#e74c3c",
    fg="#ffffff",
    activebackground="#3498db",
    activeforeground="#000000",
)
clear_button.pack(side=tk.LEFT, padx=10)

output_box = tk.Text(
    root,
    height=7,
    width=50,
    font=("Courier", 15),
    bg="#37475a",
    fg="#ffffff",
    state=tk.DISABLED,
)
output_box.pack(pady=10)

footer_label = tk.Label(
    root, text="Developed By A&J", font=("Arial", 15), bg="#343f71", fg="#ffea00"
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()
