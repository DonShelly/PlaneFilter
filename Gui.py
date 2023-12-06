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
                if (("I" in size or "I " in size) and i_var.get()) or \
                   (("II" in size or "II " in size) and ii_var.get()) or \
                   (("III" in size or "III " in size) and iii_var.get()):
                    # Append the row to the filtered list
                    filtered_plane_list.append(plane_row)

    # Populate the list box with the filtered items
    for index, plane_row in enumerate(filtered_plane_list):
        list_box.insert(index, plane_row)

    print("Added " + str(filtered_plane_list))



# Filter functions
# def filter_via_properties():
#     if fw_var or heli_var or gyro_var or light_var or medium_var or heavy_var:
#
#         filtered_plane_list.clear()
#         list_box.delete(0, tk.END)
#
#         for plane_row in plane_row_list:
#             if fw_var.get():
#                 if "Fixed-wing" in plane_row:
#                     filtered_plane_list.append(plane_row)
#             if heli_var.get():
#                 if "Helicopter" in plane_row:
#                     filtered_plane_list.append(plane_row)
#             if gyro_var.get():
#                 if "Gyrocopter" in plane_row:
#                     filtered_plane_list.append(plane_row)
#             if light_var.get():
#                 if ("Light" in plane_row or "Light " in plane_row) and plane_row not in filtered_plane_list:
#                     filtered_plane_list.append(plane_row)
#             if medium_var.get():
#                 if ("Medium" in plane_row or "Medium " in plane_row) and plane_row not in filtered_plane_list:
#                     filtered_plane_list.append(plane_row)
#             if heavy_var.get():
#                 if ("Heavy" in plane_row or "Heavy " in plane_row) and plane_row not in filtered_plane_list:
#                     filtered_plane_list.append(plane_row)
#
#         for index, plane_row in enumerate(filtered_plane_list):
#             list_box.insert(index, plane_row)
#         print("added " + str(filtered_plane_list))
#     else:
#         list_box.delete(0, tk.END)


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
