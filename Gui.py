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
def filter_via_properties():
    if fw_var or heli_var or gyro_var or light_var or medium_var or heavy_var:
        filtered_plane_list.clear()

        for plane_row in plane_row_list:
            if fw_var.get():
                if "Fixed-wing" in plane_row:
                    filtered_plane_list.append(plane_row)
            if heli_var.get():
                if "Helicopter" in plane_row:
                    filtered_plane_list.append(plane_row)
            if gyro_var.get():
                if "Gyrocopter" in plane_row:
                    filtered_plane_list.append(plane_row)
            if light_var.get():
                if "Light" or "Light " in plane_row:
                    filtered_plane_list.append(plane_row)
            if medium_var.get():
                if "Medium" or "Medium " in plane_row:
                    filtered_plane_list.append(plane_row)
            if heavy_var.get():
                if "Heavy" or "Heavy" in plane_row:
                    filtered_plane_list.append(plane_row)

        for index, plane_row in enumerate(filtered_plane_list):
            list_box.insert(index, plane_row)
        print("added " + str(filtered_plane_list))
    # else:
    #     # create a copy of filtered_plane_list before iterating and modifying it
    #     # TODO: Get vehicle class items from plane row list
    #     copy_plane_row_list = list(plane_row_list)
    #     for plane_row in copy_plane_row_list:
    #         if prop_str in plane_row or prop_str + ' ' in plane_row:
    #             # filtered_plane_list.remove(plane_row)
    #             # convert plane_row to a tuple before finding the index
    #             plane_row_tuple = tuple(plane_row)
    #             idx = list_box.get(0, tk.END).index(plane_row_tuple)
    #             # delete the item at the found index
    #             list_box.delete(idx)
    #     print("removed " + prop_str)


tk.Label(frm, text="Class").grid(column=0, row=0)

fw_check = tk.Checkbutton(frm, text="Fixed-wing", variable=fw_var, command=filter_via_properties)
heli_check = tk.Checkbutton(frm, text="Helicopter", variable=heli_var, command=filter_via_properties)
gc_check = tk.Checkbutton(frm, text="Gyrocopter", variable=gyro_var, command=filter_via_properties)

fw_check.grid(column=0, row=1)
heli_check.grid(column=0, row=2)
gc_check.grid(column=0, row=3)

tk.Label(frm, text="ICAO WTC").grid(column=0, row=5)

light_check = tk.Checkbutton(frm, text="Light", variable=light_var, command=filter_via_properties)
med_check = tk.Checkbutton(frm, text="Medium", variable=medium_var, command=filter_via_properties)
heavy_check = tk.Checkbutton(frm, text="Heavy", variable=heavy_var, command=filter_via_properties)

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
