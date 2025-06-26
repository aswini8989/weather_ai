import tkinter as tk
from main import auto_update_today, export_csv

def run_auto_update():
    auto_update_today()

def run_export():
    export_csv()

app = tk.Tk()
app.title("My Weather Button App")

tk.Label(app, text="🌤️ Weather Logger", font=("Arial", 16)).pack(pady=10)
tk.Button(app, text="Auto Update Today", command=run_auto_update, width=25).pack(pady=5)
tk.Button(app, text="Export to CSV", command=run_export, width=25).pack(pady=5)
tk.Button(app, text="Close", command=app.quit, width=25).pack(pady=20)

app.mainloop()
