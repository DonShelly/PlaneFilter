import csv
import tkinter as tk

plane_row_list = []
displayed_planes = []

# populate list with csv rows
with open('MANUFACTURER.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for index, row in enumerate(reader):
        if index == 0:
            continue
        plane_row_list.append(', '.join(row))
    print(plane_row_list)


# Filter functions
def filter_fixed_wing():
    print(fw_var.get())
    if fw_var.get() == 0:
        # remove fixed wing

        for plane_model in displayed_planes:
            if plane_model.contains("Fixed-wing"):
                displayed_planes.remove(plane_model)
                idx = list_box.get(0, tk.END).index(plane_model)
                list_box.delete(idx)
    else:
        for plane_row in plane_row_list:
            if plane_row.contains("Fixed-wing"):
                displayed_planes.append(plane_row)
        for index, displayed_plane in enumerate(displayed_planes):
            list_box.insert(index, displayed_plane)



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

fw_var = tk.IntVar()

tk.Label(frm, text="Class").grid(column=0, row=0)

fw_check = tk.Checkbutton(
    frm, text="Fixed-wing", variable=fw_var, command=filter_fixed_wing
)
h_check = tk.Checkbutton(frm, text="Helicopter")
gc_check = tk.Checkbutton(frm, text="Gyro-copter")

fw_check.grid(column=0, row=1)
# fw_check.bind('<Button-1>', filter_fixed_wing)
h_check.grid(column=0, row=2)
gc_check.grid(column=0, row=3)

tk.Label(frm, text="ICAO WTC").grid(column=0, row=5)

# light_check = tk.Checkbutton(frm, text="Light").grid(column=0, row=6)
# med_check = tk.Checkbutton(frm, text="Medium").grid(column=0, row=7)
# heavy_check = tk.Checkbutton(frm, text="Heavy").grid(column=0, row=8)

tk.Label(frm, text="SRS").grid(column=0, row=10)
tk.Checkbutton(frm, text="I").grid(column=0, row=11)
tk.Checkbutton(frm, text="II").grid(column=0, row=12)
tk.Checkbutton(frm, text="III").grid(column=0, row=13)

list_box = tk.Listbox(window)

list_box.grid(column=1, row=0)

# Start the event loop.
window.mainloop()
