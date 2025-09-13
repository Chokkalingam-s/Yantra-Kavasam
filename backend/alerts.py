import tkinter.messagebox as msg

def alert(event_type, details=""):
    """Trigger alert popup & log"""
    print(f"[ALERT] {event_type}: {details}")
    msg.showwarning("Vehicle Alert", f"{event_type}\n{details}")
