import tkinter as tk
from tkinter import ttk, messagebox

# Sample Player Data
database = {
    "Mike Trout": {
        "team": "Los Angeles Angels",
        "position": "CF",
        "age": 34,
        "Average Exit Velocity": 92.3,
        "Max Exit Velocity": 115.2,
        "Average Launch Angle": 14.5,
        "Hard Hit %": 45.6,
    },
    "Aaron Judge": {
        "team": "New York Yankees",
        "position": "RF",
        "age": 33,
        "Average Exit Velocity": 95.8,
        "Max Exit Velocity": 121.1,
        "Average Launch Angle": 16.4,
        "Hard Hit %": 50.2,
    },
    "Shohei Ohtani": {
        "team": "Los Angeles Angels",
        "position": "DH",
        "age": 31,
        "Average Exit Velocity": 93.5,
        "Max Exit Velocity": 118.0,
        "Average Launch Angle": 15.2,
        "Hard Hit %": 48.3,
    },
}

class MetricsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Baseball Metrics Search App")
        self.root.geometry("500x400")

        # Search label
        self.label = tk.Label(root, text="Search Player Name:", font=("Arial", 12))
        self.label.pack(pady=10)

        # Search entry
        self.search_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.search_entry.pack()
        self.search_entry.bind("<Return>", lambda e: self.search_player())

        # Search button
        self.search_button = tk.Button(root, text="Search", font=("Arial", 12), command=self.search_player)
        self.search_button.pack(pady=10)

        # Results frame
        self.results_frame = tk.Frame(root)
        self.results_frame.pack(pady=20, fill="both", expand=True)

        self.tree = ttk.Treeview(self.results_frame, columns=("Metric", "Value"), show="headings", height=8)
        self.tree.heading("Metric", text="Metric")
        self.tree.heading("Value", text="Value")
        self.tree.column("Metric", width=250)
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
            metrics = database[name]
            for metric, value in metrics.items():
                self.tree.insert("", "end", values=(metric, value))
        else:
            messagebox.showinfo("Not Found", f"No metrics found for {name}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MetricsApp(root)
    root.mainloop()