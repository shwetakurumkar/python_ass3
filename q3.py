import tkinter as tk

def change_bg_color(color):
    root.config(bg=color)

root = tk.Tk()
root.title("Background Color Changer")
root.geometry("400x300")

menu_bar = tk.Menu(root)

color_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Colors", menu=color_menu)

color_menu.add_command(label="Red", command=lambda: change_bg_color("red"))
color_menu.add_command(label="Green", command=lambda: change_bg_color("green"))
color_menu.add_command(label="Blue", command=lambda: change_bg_color("blue"))
color_menu.add_command(label="Yellow", command=lambda: change_bg_color("yellow"))
color_menu.add_command(label="White", command=lambda: change_bg_color("white"))
color_menu.add_command(label="Gray", command=lambda: change_bg_color("gray"))

root.config(menu=menu_bar)
root.mainloop()