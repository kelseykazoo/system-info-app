import platform
import psutil
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("System Info")
root.configure(bg="#344e41")

style = ttk.Style()
style.theme_use("clam")

style.configure("Custom.TLabel",
                background="#3a5a40",
                foreground="#a3b18a",
                font=("Helvetica", 14))

style.configure("Title.TLabel",
                background="#3a5a40",
                foreground="#a3b18a",
                font=("Helvetica", 20, "bold"))

style.configure("Refresh.TButton",
                background="#3a5a40",
                foreground="#a3b18a",
                font=("Helvetica", 14))

title = ttk.Label(root, text="💻 System Info", style="Title.TLabel")
title.pack(pady=10)

label_os_name = ttk.Label(root, style="Custom.TLabel")
label_os_name.pack(pady=3)

label_os_version = ttk.Label(root, style="Custom.TLabel")
label_os_version.pack(pady=3)

label_disk_info = ttk.Label(root, style="Custom.TLabel")
label_disk_info.pack(pady=3)

def update_info():
    os_name = platform.system()
    os_version = platform.version()
    usage = psutil.disk_usage('/System/Volumes/Data')
    total_gb = round(usage.total / (1024 ** 3), 1)
    used_gb = round(usage.used / (1024 ** 3), 1)
    disk_info = f"Disk Usage: {used_gb} GB used out of {total_gb} GB ({usage.percent}%)"
    label_os_name.config(text=" OS Name: " + os_name)
    label_os_version.config(text=" OS Version: " + os_version)
    label_disk_info.config(text=disk_info)

refresh_button = ttk.Button(root, text="🔄 Refresh", command=update_info, style="Refresh.TButton")
refresh_button.pack(pady=10)

update_info()
root.mainloop()
