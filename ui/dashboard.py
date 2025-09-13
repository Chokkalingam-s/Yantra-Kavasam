import tkinter as tk
from backend.alerts import alert
from backend.gps_logic import check_geofence
from backend.speed_logic import check_speed

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("IoT Vehicle Tracking Simulation")
        self.root.geometry("600x400")

        # Speed control
        self.speed_var = tk.IntVar(value=0)
        tk.Label(root, text="Speed (km/h):").pack()
        self.speed_slider = tk.Scale(root, from_=0, to=200,
                                     orient="horizontal",
                                     variable=self.speed_var,
                                     command=self.check_speed_event)
        self.speed_slider.pack()

        # Geofence rectangle
        self.canvas = tk.Canvas(root, width=400, height=200, bg="lightgrey")
        self.canvas.pack(pady=20)
        self.rect = self.canvas.create_rectangle(100, 50, 300, 150, outline="blue")
        self.car = self.canvas.create_oval(180, 90, 220, 130, fill="red")

        # Move car with mouse
        self.canvas.bind("<Motion>", self.track_position)

        # Harsh Braking Button
        tk.Button(root, text="Simulate Harsh Braking",
                  command=lambda: alert("Harsh Braking")).pack()

    def track_position(self, event):
        """Track mouse as vehicle"""
        self.canvas.coords(self.car, event.x-20, event.y-20, event.x+20, event.y+20)
        bounds = (100, 300, 50, 150)
        if check_geofence(event.x, event.y, bounds):
            alert("Geofence Breach", f"Car moved outside allowed zone at {event.x},{event.y}")

    def check_speed_event(self, event=None):
        speed = self.speed_var.get()
        if check_speed(speed):
            alert("Overspeeding", f"Vehicle at {speed} km/h")

def run_dashboard():
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()

if __name__ == "__main__":
    run_dashboard()
