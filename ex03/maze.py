import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    root.geometry("1500x900")
    tori = tk.PhotoImage(file="fig/5.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=tori, tag="tori")
    root.mainloop()