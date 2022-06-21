

import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました")
root = tk.Tk()
root.title("試運転")
root.geometry("500x200")

label = tk.Label(root,
                text="らべるを書いてみた件",
                font=("Ricty Diminished", 20) #フォント指定なくても大丈夫
                )           
label.pack()

button = tk.Button(root, text="押すな", command=button_click)
button.bind("<1>", button_click)
button.pack()

entry=tk.Entry(width=30)
entry.insert(tk.END, "owari")
entry.pack()

root.mainloop()