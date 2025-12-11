import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Try to import matplotlib and its TkAgg backend; if missing, disable plotting features.
import importlib
import importlib.util

matplotlib = None
plt = None
FigureCanvasTkAgg = None
CAN_PLOT = False

# Check if matplotlib is available without a direct static import (avoids linter/resolver errors)
if importlib.util.find_spec("matplotlib") is not None:
    try:
        matplotlib = importlib.import_module("matplotlib")
        matplotlib.use("TkAgg")
        plt = importlib.import_module("matplotlib.pyplot")
        FigureCanvasTkAgg = importlib.import_module("matplotlib.backends.backend_tkagg").FigureCanvasTkAgg
        CAN_PLOT = True
    except Exception:
        CAN_PLOT = False
        plt = None
        FigureCanvasTkAgg = None

# Player metrics database
database = {
    "Mike Trout": {
        "Average Exit Velocity": 92.3,
        "Max Exit Velocity": 115.2,
        "Launch Angle Avg": 14.7
    },
    "Aaron Judge": {
        "Average Exit Velocity": 95.8,
        "Max Exit Velocity": 121.1,
        "Launch Angle Avg": 16.4
    },
    "Wyatt": {
        "Height (in)": 71.4, "Weight (lb)": 160, "GS (Right)": 141, "GS (Left)": 141,
        "RHB/LHB": "RHB", "Bat Name": "cat2 puck", "Exit Speed": 92.1, "Bat Speed": 68.175, "Launch Angle": 13.125
    },
    "Rigsby": {
        "Height (in)": 70.7, "Weight (lb)": 192, "GS (Right)": 129, "GS (Left)": 115,
        "RHB/LHB": "RHB", "Bat Name": "combat", "Exit Speed": 85.76, "Bat Speed": 68.2375, "Launch Angle": 13.67143
    },
    "Matt": {
        "Height (in)": 68.2, "Weight (lb)": 132, "GS (Right)": 117, "GS (Left)": 111,
        "RHB/LHB": "RHB", "Bat Name": "Atlas", "Exit Speed": 78.37142857, "Bat Speed": 60.3, "Launch Angle": 10.4
    },
    "Xavion": {
        "Height (in)": 64.2, "Weight (lb)": 129, "GS (Right)": 131, "GS (Left)": 102,
        "RHB/LHB": "RHB", "Bat Name": "voodoo", "Exit Speed": 75.26571429, "Bat Speed": 57.5375, "Launch Angle": 18.07143
    },
    "Avery (RHB)": {
        "Height (in)": 70.3, "Weight (lb)": 200, "GS (Right)": 82, "GS (Left)": 92,
        "RHB/LHB": "RHB", "Bat Name": "combat", "Exit Speed": 82.57142857, "Bat Speed": 65.5375, "Launch Angle": 7.666667
    },
    "Jaden": {
        "Height (in)": 72.0, "Weight (lb)": 200, "GS (Right)": 131, "GS (Left)": 114,
        "RHB/LHB": "RHB", "Bat Name": "Atlas", "Exit Speed": 77.92857143, "Bat Speed": 64.025, "Launch Angle": 10.24444
    },
    "Aiden": {
        "Height (in)": 68.1, "Weight (lb)": 154, "GS (Right)": 117, "GS (Left)": 130,
        "RHB/LHB": "RHB", "Bat Name": "combat", "Exit Speed": 81.76571429, "Bat Speed": 62.928571, "Launch Angle": 14.08333
    },
    "Zachary": {
        "Height (in)": 72.8, "Weight (lb)": 154, "GS (Right)": 131, "GS (Left)": 128,
        "RHB/LHB": "RHB", "Bat Name": "Atlas", "Exit Speed": 86.23333333, "Bat Speed": 65.157143, "Launch Angle": 19.6125
    },
    "Jaxen": {
        "Height (in)": 67.3, "Weight (lb)": 148, "GS (Right)": 81, "GS (Left)": 101,
        "RHB/LHB": "RHB", "Bat Name": "voodoo", "Exit Speed": 76.71428571, "Bat Speed": 60.9375, "Launch Angle": 15.08571
    },
    "Dawson": {
        "Height (in)": 66.1, "Weight (lb)": 124, "GS (Right)": 115, "GS (Left)": 117,
        "RHB/LHB": "RHB", "Bat Name": "voodoo", "Exit Speed": 80.0, "Bat Speed": 53.371429, "Launch Angle": 21.05714
    },
    "Benjamin": {
        "Height (in)": 72.5, "Weight (lb)": 161, "GS (Right)": 102, "GS (Left)": 106,
        "RHB/LHB": "RHB", "Bat Name": "icon", "Exit Speed": 81.21428571, "Bat Speed": 62.9, "Launch Angle": 23.44286
    },
    "Dallas": {
        "Height (in)": 69.8, "Weight (lb)": 175, "GS (Right)": 96, "GS (Left)": 99,
        "RHB/LHB": "RHB", "Bat Name": "icon", "Exit Speed": 72.22857143, "Bat Speed": 60.171429, "Launch Angle": 9.655556
    },
    "Caymin": {
        "Height (in)": 67.7, "Weight (lb)": 140, "GS (Right)": 103, "GS (Left)": 86,
        "RHB/LHB": "RHB", "Bat Name": "voodoo", "Exit Speed": 68.6, "Bat Speed": 55.4, "Launch Angle": 3.49
    },
    "Jenkins": {
        "Height (in)": 65.9, "Weight (lb)": 172, "GS (Right)": 90, "GS (Left)": 89,
        "RHB/LHB": "RHB", "Bat Name": "mavl flash", "Exit Speed": 77.15, "Bat Speed": 59.814286, "Launch Angle": 6.8
    },
    "Caleb": {
        "Height (in)": 67.0, "Weight (lb)": 111, "GS (Right)": 72, "GS (Left)": 61,
        "RHB/LHB": "RHB", "Bat Name": "exclle", "Exit Speed": 68.0, "Bat Speed": 51.8375, "Launch Angle": 12.34286
    },
    "Jackson": {
        "Height (in)": 66.7, "Weight (lb)": 117, "GS (Right)": 62, "GS (Left)": 60,
        "RHB/LHB": "RHB", "Bat Name": "voodoo", "Exit Speed": 58.78571429, "Bat Speed": 45.9125, "Launch Angle": 6.95
    },
    "Braylon": {
        "Height (in)": 67.6, "Weight (lb)": 130, "GS (Right)": 88, "GS (Left)": 86,
        "RHB/LHB": "RHB", "Bat Name": "dynasty", "Exit Speed": 61.87142857, "Bat Speed": 52.5125, "Launch Angle": 8.788889
    },
    "Cayden": {
        "Height (in)": 65.0, "Weight (lb)": 112, "GS (Right)": 71, "GS (Left)": 76,
        "RHB/LHB": "RHB", "Bat Name": "dynasty", "Exit Speed": 59.97142857, "Bat Speed": 44.82857, "Launch Angle": 12.65
    },
    "Owen": {
        "Height (in)": 71.3, "Weight (lb)": 245, "GS (Right)": 112, "GS (Left)": 115,
        "RHB/LHB": "RHB", "Bat Name": "combat", "Exit Speed": 77.41428571, "Bat Speed": 60.6125, "Launch Angle": 14.2
    },
    "Miller": {
        "Height (in)": 73.7, "Weight (lb)": 200, "GS (Right)": 118, "GS (Left)": 117,
        "RHB/LHB": "LHB", "Bat Name": "cat2 puck", "Exit Speed": 86.14285714, "Bat Speed": 66.385714, "Launch Angle": 19.51429
    },
    "Avery (LHB)": {
        "Height (in)": 69.6, "Weight (lb)": 260, "GS (Right)": 147, "GS (Left)": 132,
        "RHB/LHB": "LHB", "Bat Name": "icon", "Exit Speed": 83.21428571, "Bat Speed": 64.885714, "Launch Angle": 5.944444
    },
    "Carter": {
        "Height (in)": 66.6, "Weight (lb)": 200, "GS (Right)": 103, "GS (Left)": 109,
        "RHB/LHB": "LHB", "Bat Name": "omega", "Exit Speed": 73.91428571, "Bat Speed": 59.1125, "Launch Angle": 12.8875
    },
    "Tanner": {
        "Height (in)": 65.6, "Weight (lb)": 121, "GS (Right)": 89, "GS (Left)": 88,
        "RHB/LHB": "LHB", "Bat Name": "Atlas", "Exit Speed": 72.52857143, "Bat Speed": 58.485714, "Launch Angle": 24.35
    },
    "Ayden": {
        "Height (in)": 66.4, "Weight (lb)": 223, "GS (Right)": 94, "GS (Left)": 87,
        "RHB/LHB": "RHB", "Bat Name": "combat", "Exit Speed": 66.18571429, "Bat Speed": 51.157143, "Launch Angle": 24.725
    }
}

class LoginWindow:
    def __init__(self, root, on_success):
        # use a Toplevel so we keep one root for the whole app
        self.parent = root
        self.on_success = on_success
        self.win = tk.Toplevel(self.parent)
        self.win.title("Login")
        self.win.transient(self.parent)
        self.win.grab_set()

        tk.Label(self.win, text="Username").pack(pady=5)
        self.username = tk.Entry(self.win)
        self.username.pack()

        tk.Label(self.win, text="Password").pack(pady=5)
        self.password = tk.Entry(self.win, show="*")
        self.password.pack()

        tk.Button(self.win, text="Login", command=self.login).pack(pady=10)

    def login(self):
        user = self.username.get()
        pwd = self.password.get()

        if user in USERS and USERS[user] == pwd:
            messagebox.showinfo("Success", "Login Successful!")
            self.win.destroy()
            self.on_success()
        else:
            messagebox.showerror("Error", "Invalid credentials")

class MetricsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Baseball Metrics App")
        self.root.geometry("650x550")
        graph_btn = tk.Button(root, text="Graph Player Metrics", command=self.graph_player)
        if not CAN_PLOT:
            graph_btn.config(state=tk.DISABLED)
            # optional: inform user how to enable plotting
            graph_btn.bind("<Enter>", lambda e: messagebox.showinfo("Unavailable", "matplotlib not installed. Run: pip install matplotlib"))
        graph_btn.pack(pady=5)
        tk.Label(root, text="Search Player Name:", font=("Arial", 12)).pack(pady=10)
        self.search_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.search_entry.pack()

        tk.Button(root, text="Search", command=self.search_player).pack(pady=5)
        tk.Button(root, text="Add New Player", command=self.add_player).pack(pady=5)
        tk.Button(root, text="Edit Player", command=self.edit_player).pack(pady=5)
        tk.Button(root, text="Export Metrics", command=self.export_metrics).pack(pady=5)
        tk.Button(root, text="Import Metrics", command=self.import_metrics).pack(pady=5)

        self.results_frame = tk.Frame(root)
        self.results_frame.pack(pady=20, fill="both", expand=True)

        self.tree = ttk.Treeview(self.results_frame, columns=("Metric", "Value"), show="headings", height=8)
        self.tree.heading("Metric", text="Metric")
        self.tree.heading("Value", text="Value")
        self.tree.column("Metric", width=350)
        self.tree.column("Value", width=200)
        self.tree.pack(fill="both", expand=True)

    def search_player(self):
        name = self.search_entry.get().strip()
        # Clear previous results
        for item in self.tree.get_children():
            self.tree.delete(item)

        if not name:
            messagebox.showinfo("Input Required", "Please enter a player name.")
            return

        if name in database:
            for metric, value in database[name].items():
                self.tree.insert("", "end", values=(metric, value))
        else:
            messagebox.showinfo("Not Found", f"No metrics found for {name}.")

    def add_player(self):
        name = simpledialog.askstring("Player Name", "Enter player's name:")
        if not name:
            return

        metrics = {}
        metrics_list = ["Average Exit Velocity", "Max Exit Velocity", "Launch Angle Avg"]

        for metric in metrics_list:
            value = simpledialog.askfloat(metric, f"Enter {metric}:")
            if value is None:
                return
            metrics[metric] = value

        database[name] = metrics
        messagebox.showinfo("Success", f"{name} added successfully!")

    def edit_player(self):
        # Prompt for the player to edit
        name = simpledialog.askstring("Edit Player", "Enter player's name to edit:")
        if not name:
            return

        if name not in database:
            messagebox.showerror("Error", "Player not found.")
            return

        metrics = database[name]
        # Ask which metric to edit from existing keys
        metric = simpledialog.askstring("Select Metric", f"Which metric to edit? Options: {', '.join(metrics.keys())}")
        if not metric:
            return
        if metric not in metrics:
            messagebox.showerror("Error", f"Metric '{metric}' not found for {name}.")
            return

        # Ask for the new numeric value
        value = simpledialog.askfloat("New Value", f"Enter new value for {metric} (current: {metrics[metric]}):")
        if value is None:
            return

        database[name][metric] = value
        messagebox.showinfo("Updated", f"{name}'s {metric} updated to {value}.")

    def graph_player(self):
        if not CAN_PLOT:
            messagebox.showerror("Unavailable", "Plotting requires matplotlib. Install it with: pip install matplotlib")
            return

        name = self.search_entry.get().strip()
        if not name:
            messagebox.showinfo("Input Required", "Please enter a player name to graph.")
            return

        if name not in database:
            messagebox.showerror("Error", "Player not found.")
            return

        metrics = database[name]
        labels = list(metrics.keys())
        values = list(metrics.values())

        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.bar(labels, values)
        ax.set_title(f"Metrics for {name}")
        ax.set_ylabel("Value")
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, rotation=45, ha="right")

        graph_window = tk.Toplevel(self.root)
        graph_window.title(f"Graph - {name}")
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def export_metrics(self):
        import json
        try:
            with open("metrics_export.json", "w") as f:
                json.dump(database, f, indent=4)
            messagebox.showinfo("Exported", "Metrics exported to metrics_export.json")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def import_metrics(self):
        import json
        try:
            with open("metrics_export.json", "r") as f:
                data = json.load(f)
                database.update(data)
            messagebox.showinfo("Imported", "Metrics imported successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    import sys
    print("Python executable:", sys.executable)
    try:
        import tkinter as _tk
        print("Tkinter available, Tk version:", _tk.TkVersion)
    except Exception as e:
        print("Tkinter import failed:", repr(e))

    print("CAN_PLOT:", CAN_PLOT)

    root = tk.Tk()
    MetricsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()