from tkinter import *

root=Tk()
root.title("Driving License")

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

# Create all the labels required to be displayed
label_id = Label(root, text="Driving License ID:")
label_name = Label(root, text="Name:")
label_dob = Label(root, text="Date of Birth:")
label_pin = Label(root, text="Pincode:")
label_address = Label(root, text="Address:")
label_vehicle_type = Label(root, text="Vehicle Types:")

# Define the function
def update_labels():
    # Defining variables
    driving_license_id = 19827198349
    print(type(driving_license_id))

    name = "Winnie the Pooh"
    print(type(name))

    dob = "01/01/2000"
    print(type(dob))

    pincode = 451478
    print(type(pincode))

    address = "Disney Land, Hong Kong"
    print(type(address))

    vehicle_types = ["Two", "Four"]
    print(type(vehicle_types))
    
    label_id.config(text="" + str(driving_license_id))
    label_name.config(text="" + name)
    label_dob.config(text="" + dob)
    label_pin.config(text="" + str(pincode))
    label_address.config(text="" + address)
    label_vehicle_type.config(text="" + ", ".join(vehicle_types))
    
    
button1 = Button(root, text="Show my Driving License", command=update_labels)

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()

# tkinter basic template end statement
root.mainloop()