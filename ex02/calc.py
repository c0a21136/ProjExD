
import tkinter as tk
import tkinter.messagebox as tkm

def main():
    def button_click(event):
        btn = event.widget
        txt = btn["text"] #四則演算を追加します
        if txt == "+":
            entry.insert(tk.END, "+")
        elif txt == "-":
            entry. insert(tk.END,"-")
        elif txt == "/":
            entry. insert(tk.END,"/")
        elif txt == "*":
            entry. insert(tk.END,"*")
        elif txt == "=":
            formula = entry.get()
            result = eval(formula)
            entry.delete(0, tk.END)
            entry.insert(tk.END, int(result))
        else:
            entry.insert(tk.END, int(txt))


        


    root = tk.Tk()
    root.title("計算機")
    root.geometry("380x580")

    entry = tk.Entry(justify="right",
                    width=10,
                    font=("Times New Roman", 40)
                    )
    entry.grid(row=0, column=0, columnspan=3)

    r = 1
    c = 0
    for i in range(9, -1, -1):

        button = tk.Button(root, 
                        width=4,
                        height=2,
                        text = i,
                        font=("Times New Roman", 30)
                        )
        if (i%3==0):
            r += 1
            c = 0
        else:
             c += 1
        button.grid(row=r, column=c)
        button.bind("<1>", button_click)
    #プラスボタンの追加
    plus_button = tk.Button(root,
                        width=4,
                        height=2,
                        text="+",
                        font=("Times New Roman", 30)
                        )
    plus_button.grid(row=5, column=1)
    plus_button.bind("<1>", button_click)
    #マイナスボタンの追加
    minus_button = tk.Button(root,
                        width=4,
                        height=2,
                        text="-",
                        font=("Times New Roman", 30)
                        )
    minus_button.grid(row=2, column=3)
    minus_button.bind("<1>", button_click)
    #×ボタンのついか
    k_button = tk.Button(root,
                        width=4,
                        height=2,
                        text="*",
                        font=("Times New Roman", 30)
                        )
    k_button.grid(row=3, column=3)
    k_button.bind("<1>", button_click)
    #÷ボタンの追加
    w_button = tk.Button(root,
                        width=4,
                        height=2,
                        text="/",
                        font=("Times New Roman", 30)
                        )
    w_button.grid(row=4, column=3)
    w_button.bind("<1>", button_click)
    #イコールボタンの追加
    equal_button = tk.Button(root,
                        width=4,
                        height=2,
                        text="=",
                        font=("Times New Roman", 30)
                        )
    equal_button.grid(row=5, column=2)
    equal_button.bind("<1>", button_click)

    root.mainloop()
if __name__=="__main__":
    main()