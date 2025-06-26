import tkinter as tk
import serial
import time

# Set your Arduino COM port here:
# ser = serial.Serial('COM4', 115200)
# time.sleep(2)  # Give time to Arduino to reset

def send_params():
    kp = kp_var.get()
    ki = ki_var.get()
    kd = kd_var.get()
    sp = sp_var.get()

    data = f"Kp={kp:.2f};Ki={ki:.2f};Kd={kd:.2f};SP={sp:.2f}\n"
    # ser.write(data.encode())
    print(data)

    print("Sent:", data.strip())

root = tk.Tk()
root.title("PID Tuning GUI")

kp_var = tk.DoubleVar(value=0.1)
ki_var = tk.DoubleVar(value=0.0)
kd_var = tk.DoubleVar(value=0.0)
sp_var = tk.DoubleVar(value=30.0)

def create_slider(label, var, from_, to_, row):
    tk.Label(root, text=label).grid(row=row, column=0, padx=3, pady=2)
    slider = tk.Scale(root, from_=from_, to=to_, resolution=0.1,
                      orient=tk.HORIZONTAL, variable=var, length=300,
                      command=lambda val: send_params())
    slider.grid(row=row, column=1, padx=10, pady=10)
    return slider

create_slider("Kp", kp_var, 0.0, 5.0, 0)
create_slider("Ki", ki_var, 0.0, 2.0, 1)
create_slider("Kd", kd_var, 0.0, 2.0, 2)
create_slider("SetPoint", sp_var, 0.0, 100.0, 3)

# tk.Button(root, text="Send to Arduino", command=send_params).grid(row=4, columnspan=2, pady=10)

root.mainloop()
