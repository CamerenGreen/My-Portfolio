
import tkinter as tk
from datetime import timedelta

class DualStopwatchApp:
    # Initial Application construction
    def __init__(self, master):
        self.master = master
        self.master.title("Interval Timer")

        self.intro_label = tk.Label(master, text="Welcome to The Interval Timer!", font=('Times', 24))
        self.intro_label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start_timers)
        self.start_button.pack(pady=10)

        self.global_timer_value = tk.StringVar()
        self.interval_timer_value = tk.StringVar()

        self.global_timer_label = tk.Label(master, text="Global Timer:", font=('Times', 24))
        self.global_timer_label.pack(pady=10)
        self.global_timer_display = tk.Label(master, textvariable=self.global_timer_value, font=('Times', 36, 'bold'))
        self.global_timer_display.pack(pady=10)

        self.interval_timer_label = tk.Label(master, text="Interval Timer:", font=('Times', 24))
        self.interval_timer_label.pack(pady=10)
        self.interval_timer_display = tk.Label(master, textvariable=self.interval_timer_value, font=('Times', 36, 'bold'))
        self.interval_timer_display.pack(pady=10)

        self.message_label = tk.Label(master, text="", font=('Times', 14), fg='red')
        self.message_label.pack(pady=10)

        self.global_timer = timedelta()              # Global timer: 0 seconds
        self.interval_timer = timedelta(seconds=10)  # Initial interval timer: 10 seconds
        self.is_running = False

    def start_timers(self):
        if not self.is_running:
            self.is_running = True
            self.intro_label.pack_forget()
            self.start_button.pack_forget()
            self.update_timers()

    # Update both global and interval timers
    def update_timers(self):
        if self.is_running:
            self.global_timer += timedelta(seconds=1)
            self.global_timer_value.set(str(self.global_timer).split(".")[0])  # Display without ms

            self.interval_timer -= timedelta(seconds=1)
            self.interval_timer_value.set(str(self.interval_timer).split(".")[0])  # Display without ms

            if self.interval_timer == timedelta():
                self.reset_interval_timer()
                self.show_move_message()

            self.master.after(1000, self.update_timers)  # Update every second (1000 ms)

    # Change interval timer time based on global timer time
    def reset_interval_timer(self):
        if 0 <= self.global_timer.seconds < 20:
            self.interval_timer = timedelta(seconds=10)
            self.message_label.config(text="*Interval Changed!*")
        elif 20 <= self.global_timer.seconds < 360:
            self.interval_timer = timedelta(seconds=6)
            self.message_label.config(text="*Interval Changed!*")
        elif 360 <= self.global_timer.seconds < 450:
            self.interval_timer = timedelta(seconds=3)
            self.message_label.config(text="*Interval Changed!*")
        elif 450 <= self.global_timer.seconds < 540:
            self.interval_timer = timedelta(seconds=2)
            self.message_label.config(text="*Final Interval Change!*")
        else:
            self.is_running = False


    # When interval timer has reached 0, movement opprotunity happens
    def show_move_message(self):
        if self.global_timer.seconds != 20 and self.global_timer.seconds != 360 and self.global_timer.seconds != 450 and self.global_timer.seconds != 540:
            self.message_label.config(text="*Interval Reset!*")
            self.master.after(1000, self.clear_message)  # Clear message after a second (1000 ms)
        

    def clear_message(self):
        self.message_label.config(text="")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DualStopwatchApp(root)
    root.mainloop()
