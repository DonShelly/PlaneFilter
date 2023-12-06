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
gyro_var = tk.IntVar()
light_var = tk.IntVar()
medium_var = tk.IntVar()
heavy_var = tk.IntVar()

# populate list with csv rows
with open('MANUFACTURER.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for index, row in enumerate(reader):
        if index == 0:
            continue
        plane_row_list.append(row)
    # print(plane_row_list)


# Filter functions
def filter_property(prop_str, property_var):
    print(property_var.get())
    if property_var.get() == 1:
        filtered_plane_list.clear()

        listbox_content = list_box.get(0, tk.END)

        for plane_row in plane_row_list:
            if plane_row not in listbox_content:
                if prop_str in plane_row or prop_str + ' ' in plane_row:
                    filtered_plane_list.append(plane_row)
        for index, plane_row in enumerate(filtered_plane_list):
            list_box.insert(index, plane_row)
        print("added " + str(filtered_plane_list))
    else:
        # create a copy of filtered_plane_list before iterating and modifying it
        # TODO: Get vehicle class items from plane row list
        copy_plane_row_list = list(plane_row_list)
        for plane_row in copy_plane_row_list:
            if prop_str in plane_row or prop_str + ' ' in plane_row:
                # filtered_plane_list.remove(plane_row)
                # convert plane_row to a tuple before finding the index
                plane_row_tuple = tuple(plane_row)
                idx = list_box.get(0, tk.END).index(plane_row_tuple)
                # delete the item at the found index
                list_box.delete(idx)
        print("removed " + prop_str)

def filter_fw():
    filter_property("Fixed-wing", fw_var)

def filter_heli():
    filter_property("Helicopter", heli_var)


def filter_gyro():
    filter_property("Gyrocopter", gyro_var)


def filter_light():
    filter_property("Light", light_var)


def filter_medium():
    filter_property("Medium", medium_var)


def filter_heavy():
    filter_property("Heavy", heavy_var)


def filter_(event):
    pass


def filter_(event):
    pass


def filter_(event):
    pass





tk.Label(frm, text="Class").grid(column=0, row=0)

fw_check = tk.Checkbutton(frm, text="Fixed-wing", variable=fw_var, command=filter_fw)
heli_check = tk.Checkbutton(frm, text="Helicopter", variable=heli_var, command=filter_heli)
gc_check = tk.Checkbutton(frm, text="Gyrocopter", variable=gyro_var, command=filter_gyro)

fw_check.grid(column=0, row=1)
heli_check.grid(column=0, row=2)
gc_check.grid(column=0, row=3)

tk.Label(frm, text="ICAO WTC").grid(column=0, row=5)

light_check = tk.Checkbutton(frm, text="Light", variable=light_var, command=filter_light)
med_check = tk.Checkbutton(frm, text="Medium", variable=medium_var, command=filter_medium)
heavy_check = tk.Checkbutton(frm, text="Heavy", variable=heavy_var, command=filter_heavy)

light_check.grid(column=0, row=6)
med_check.grid(column=0, row=7)
heavy_check.grid(column=0, row=8)


tk.Label(frm, text="SRS").grid(column=0, row=10)
tk.Checkbutton(frm, text="I").grid(column=0, row=11)
tk.Checkbutton(frm, text="II").grid(column=0, row=12)
tk.Checkbutton(frm, text="III").grid(column=0, row=13)

list_box = tk.Listbox(window)

list_box.grid(column=1, row=0)

# Start the event loop.
window.mainloop()
