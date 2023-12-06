import csv
import tkinter as tk


# Filter functions
def filter_fixed_wing(event):
    pass

def filter_(event):
    pass

def filter_(event):
    pass

def filter_(event):
    pass

def filter_(event):
    pass

def filter_(event):
    pass

def filter_(event):
    pass

def filter_(event):
    pass

def filter_(event):
    pass


window = tk.Tk()
window.title("Runway Checker")

frm = tk.Frame(window, padx=10, pady=10)
frm.grid()

tk.Label(frm, text="Class").grid(column=0, row=0)

fw_check = tk.Checkbutton(frm, text="Fixed-wing")
h_check = tk.Checkbutton(frm, text="Helicopter")
gc_check = tk.Checkbutton(frm, text="Gyro-copter")

fw_check.grid(column=0, row=1)
fw_check.bind('<Button-1>', filter_fixed_wing)
h_check.grid(column=0, row=2)
gc_check.grid(column=0, row=3)

tk.Label(frm, text="ICAO WTC").grid(column=0, row=5)

light_check = tk.Checkbutton(frm, text="Light").grid(column=0, row=6)
med_check = tk.Checkbutton(frm, text="Medium").grid(column=0, row=7)
heavy_check = tk.Checkbutton(frm, text="Heavy").grid(column=0, row=8)

tk.Label(frm, text="SRS").grid(column=0, row=10)
tk.Checkbutton(frm, text="I").grid(column=0, row=11)
tk.Checkbutton(frm, text="II").grid(column=0, row=12)
tk.Checkbutton(frm, text="III").grid(column=0, row=13)

list_box = tk.Listbox(window)

list_box.grid(column=1, row=0)

with open('MANUFACTURER.csv') as csv_file:
    reader = csv.reader(csv_file)
    for index, row in enumerate(reader):
        list_box.insert(index, ''.join(row[0]))


def show_lightweight_planes(event):
    list_box.insert("200T Plane")
    list_box.insert("300T Plane")
    list_box.insert("100T Plane")
    list_box.insert("400T Plane")
    list_box.insert("500T Plane")


# Start the event loop.
window.mainloop()
