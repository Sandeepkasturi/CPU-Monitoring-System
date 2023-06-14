import psutil
import tkinter as tk

# Custom color palette (dark green2 theme)
BG_COLOR = "#1D3324"
FG_COLOR = "#FFFFFF"
BUTTON_BG_COLOR = "#307B58"
BUTTON_FG_COLOR = "#FFFFFF"


def monitor_system():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    num_threads = psutil.cpu_count()
    
    cpu_label.config(text=f"CPU Utilization: {cpu_percent}%", fg=FG_COLOR, bg=BG_COLOR)
    memory_label.config(text=f"Memory Usage: {memory.percent}%", fg=FG_COLOR, bg=BG_COLOR)
    threads_label.config(text=f"Number of Threads: {num_threads}", fg=FG_COLOR, bg=BG_COLOR)


window = tk.Tk()
window.title("System Monitoring")
window.geometry("300x150")
window.configure(bg=BG_COLOR)

cpu_label = tk.Label(window, text="CPU Utilization: -", fg=FG_COLOR, bg=BG_COLOR)
memory_label = tk.Label(window, text="Memory Usage: -", fg=FG_COLOR, bg=BG_COLOR)
threads_label = tk.Label(window, text="Number of Threads: -", fg=FG_COLOR, bg=BG_COLOR)

cpu_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
memory_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
threads_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

update_button = tk.Button(window, text="Update", command=monitor_system, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR)
update_button.grid(row=3, column=0, padx=10, pady=10)

while True:
    monitor_system()
    window.update()
