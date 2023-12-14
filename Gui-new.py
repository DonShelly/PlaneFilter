import csv
import tkinter as tk

raw_plane_row_list = []
temp_filtered_plane_list = []

# make first empty window
window = tk.Tk()
window.title("Aircraft Filter")
window.geometry("500x360")
frm = tk.Frame(window, padx=10, pady=10)
frm.grid()

# initialise variables for options (tick box)
fw_var = tk.IntVar()
heli_var = tk.IntVar()
gyro_var = tk.IntVar()

light_var = tk.IntVar()
medium_var = tk.IntVar()
heavy_var = tk.IntVar()

i_var = tk.IntVar()
ii_var = tk.IntVar()
iii_var = tk.IntVar()

# populate list with csv rows(последовательность,ряд)
with open('MANUFACTURER.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

    # we iterate over reader(list) and populate plane_row_list with each row 
    for index, row in enumerate(reader):
        if index == 0:
            continue
        raw_plane_row_list.append(row)


# An operation to add a list of each filter to a master list
def add_filtered_planes_to_master_list(plane_list, filtered_plane_list):
    clean_list = []
    for plane in plane_list:
        clean_list.append(plane[0])
    filtered_plane_list.append(plane_list)


def join_and_dedupe_master_list(master_list):
    return set(master_list[0]) | set(master_list[1]) | set(master_list[2])


# define(explain) function
def filter_via_properties():
    filtered_plane_list = []

    # Clear the list box before populating it with filtered items
    list_box.delete(0, tk.END)

    fw_planes = filter(lambda plane: fw_var and "Fixed-wing" in plane, raw_plane_row_list)
    heli_planes = filter(lambda plane: heli_var.get() and "Helicopter" in plane, raw_plane_row_list)
    gyro_planes = filter(lambda plane: gyro_var.get() and "Gyrocopter" in plane, raw_plane_row_list)

    light_planes = filter(lambda plane: light_var and ("Light" in plane or "Light " in plane), raw_plane_row_list)
    heavy_planes = filter(lambda plane: heavy_var and ("Heavy" in plane or "Heavy " in plane), raw_plane_row_list)

    add_filtered_planes_to_master_list(list(fw_planes), filtered_plane_list)
    add_filtered_planes_to_master_list(list(heli_planes), filtered_plane_list)
    add_filtered_planes_to_master_list(list(gyro_planes), filtered_plane_list)

    join_and_dedupe_master_list(filtered_plane_list)

    # Populate the list box with the filtered items
    for index, plane_row in enumerate(filtered_plane_list):
        list_box.insert(index, plane_row)
    if (fw_var.get() or heli_var.get() or gyro_var) and (light_var or medium_var or heavy_var) and not (
            i_var.get() or ii_var.get() or iii_var.get()):
        list_box.insert(0, "Please select an option from each category")
    if len(list_box.get(0, tk.END)) == 0:
        list_box.insert(0, "No results")

    print("Added " + str(filtered_plane_list))


tk.Label(frm, text="Class", font='Helvetica 16 bold').grid(column=0, row=0, padx=10)

fw_check = tk.Checkbutton(frm, text="Fixed-wing", variable=fw_var, command=filter_via_properties)
heli_check = tk.Checkbutton(frm, text="Helicopter", variable=heli_var, command=filter_via_properties)
gc_check = tk.Checkbutton(frm, text="Gyrocopter", variable=gyro_var, command=filter_via_properties)

fw_check.grid(column=0, row=1, sticky="W")
heli_check.grid(column=0, row=2, sticky="W")
gc_check.grid(column=0, row=3, sticky="W")

tk.Label(frm, text="\n", height=1).grid(column=0, row=4)

tk.Label(frm, text="ICAO WTC", font='Helvetica 16 bold').grid(column=0, row=5, padx=10)

light_check = tk.Checkbutton(frm, text="Light", variable=light_var, command=filter_via_properties)
med_check = tk.Checkbutton(frm, text="Medium", variable=medium_var, command=filter_via_properties)
heavy_check = tk.Checkbutton(frm, text="Heavy", variable=heavy_var, command=filter_via_properties)

light_check.grid(column=0, row=6, sticky="W")
med_check.grid(column=0, row=7, sticky="W")
heavy_check.grid(column=0, row=8, sticky="W")

tk.Label(frm, text="\n", height=1).grid(column=0, row=9)

tk.Label(frm, text="SRS", font='Helvetica 16 bold').grid(column=0, row=10, padx=10)

srs_i = tk.Checkbutton(frm, text="I", variable=i_var, command=filter_via_properties)
srs_ii = tk.Checkbutton(frm, text="II", variable=ii_var, command=filter_via_properties)
srs_iii = tk.Checkbutton(frm, text="III", variable=iii_var, command=filter_via_properties)

srs_i.grid(column=0, row=11, sticky="W")
srs_ii.grid(column=0, row=12, sticky="W")
srs_iii.grid(column=0, row=13, sticky="W")

list_box = tk.Listbox(window, height=20, width=40, selectmode="multiple")

list_box.grid(column=1, row=0)

# Start the event loop.
window.mainloop()
