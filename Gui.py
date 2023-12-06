import csv
import tkinter as tk

plane_row_list = []
filtered_plane_list = []
temp_filtered_plane_list = []


window = tk.Tk()
window.title("Runway Checker")
frm = tk.Frame(window, padx=10, pady=10)
frm.grid()

fw_var = tk.IntVar()
heli_var = tk.IntVar()

# populate list with csv rows
with open('MANUFACTURER.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for index, row in enumerate(reader):
        if index == 0:
            continue
        plane_row_list.append(row)
    # print(plane_row_list)


# Filter functions
def filter_class(class_str, class_var):
    print(class_var.get())
    if class_var.get() == 1:
        for plane_row in plane_row_list:
            if class_str in plane_row:
                filtered_plane_list.append(plane_row)
        for index, plane_row in enumerate(filtered_plane_list):
            list_box.insert(index, plane_row)
        print("added " + str(filtered_plane_list))
        # plane_row_list.clear()
        filtered_plane_list.clear()
    else:
        # create a copy of filtered_plane_list before iterating and modifying it
        copy_filtered_plane_list = list(filtered_plane_list)
        for plane_row in copy_filtered_plane_list:
            if class_str in plane_row:
                filtered_plane_list.remove(plane_row)
                # convert plane_row to a tuple before finding the index
                plane_row_tuple = tuple(plane_row)
                idx = list_box.get(0, tk.END).index(plane_row_tuple)
                # delete the item at the found index
                list_box.delete(idx)
        print("removed " + class_str)

def filter_fw():
    filter_class("Fixed-wing", fw_var)

def filter_heli():
    filter_class("Helicopter", heli_var)


def filter_gyro():
    filter_class("Gyro-copter")


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





tk.Label(frm, text="Class").grid(column=0, row=0)

fw_check = tk.Checkbutton(frm, text="Fixed-wing", variable=fw_var, command=filter_fw)
heli_check = tk.Checkbutton(frm, text="Helicopter", variable=heli_var, command=filter_heli)
gc_check = tk.Checkbutton(frm, text="Gyro-copter")

fw_check.grid(column=0, row=1)
heli_check.grid(column=0, row=2)
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
