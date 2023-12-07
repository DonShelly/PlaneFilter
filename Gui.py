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

i_var = tk.IntVar()
ii_var = tk.IntVar()
iii_var = tk.IntVar()

# populate list with csv rows
with open('MANUFACTURER.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for index, row in enumerate(reader):
        if index == 0:
            continue
        plane_row_list.append(row)
    # print(plane_row_list)


def filter_via_properties():
    # Initialize the filtered list inside the function to avoid unexpected behavior
    filtered_plane_list = []

    # Clear the list box before populating it with filtered items
    list_box.delete(0, tk.END)

    for plane_row in plane_row_list:
        aircraft_type = plane_row[1]  # Assuming the aircraft type is at index 0 in the row
        weight = plane_row[2]  # Assuming the weight is at index 1 in the row
        size = plane_row[3]  # Assuming the size is at index 2 in the row

        # Check if any aircraft type checkbox is selected
        if (fw_var.get() and "Fixed-wing" in aircraft_type) or \
                (heli_var.get() and "Helicopter" in aircraft_type) or \
                (gyro_var.get() and "Gyrocopter" in aircraft_type):
            # Check for weight filters only if the corresponding type checkbox is selected
            if (light_var.get() and ("Light" in weight or "Light " in weight)) or \
                    (medium_var.get() and ("Medium" in weight or "Medium " in weight)) or \
                    (heavy_var.get() and ("Heavy" in weight or "Heavy " in weight)):
                # Check for size filters only if the corresponding type checkbox is selected
                if ((("I" in size or "I " in size) and i_var.get()) and not ("II" in size or "III" in size)) or \
                        ((("II" in size or "II " in size) and ii_var.get()) and not ("III" in size) and not ("I" in size)) or \
                        (("III" in size or "III " in size) and iii_var.get()):
                    # Append the row to the filtered list
                    filtered_plane_list.append(plane_row)
                elif not (("I" in size or "I " in size) and i_var.get()) and not (("II" in size or "II " in size) and ii_var.get()):
                    filtered_plane_list.append(plane_row)

    # Populate the list box with the filtered items
    for index, plane_row in enumerate(filtered_plane_list):
        list_box.insert(index, plane_row)
    if (fw_var.get() or heli_var.get() or gyro_var) and (light_var or medium_var or heavy_var) and not (
            i_var.get() or ii_var.get() or iii_var.get()):
        list_box.insert(0, "Please select all options")
    if len(list_box.get(0, tk.END)) == 0:
        list_box.insert(0, "No results")

    print("Added " + str(filtered_plane_list))


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
srs_i = tk.Checkbutton(frm, text="I", variable=i_var, command=filter_via_properties)
srs_ii = tk.Checkbutton(frm, text="II", variable=ii_var, command=filter_via_properties)
srs_iii = tk.Checkbutton(frm, text="III", variable=iii_var, command=filter_via_properties)

srs_i.grid(column=0, row=11)
srs_ii.grid(column=0, row=12)
srs_iii.grid(column=0, row=13)

list_box = tk.Listbox(window)

list_box.grid(column=1, row=0)

# Start the event loop.
window.mainloop()
