import tkinter as tk

window = tk.Tk()
window.title("Hello World")


def show_lightweight_planes(event):
    list_box.insert("200T Plane")
    list_box.insert("300T Plane")
    list_box.insert("100T Plane")
    list_box.insert("400T Plane")
    list_box.insert("500T Plane")
    window.destroy()


light_btn = tk.Button(text="Lightweight Plane")
light_btn.bind("", show_lightweight_planes)

list_box = tk.Listbox(window)


light_btn.pack()
list_box.pack()

# Start the event loop.
window.mainloop()