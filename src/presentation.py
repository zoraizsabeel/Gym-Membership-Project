import tkinter as tk
from tkinter import messagebox, ttk
import databaseAPI as api  # This connects the Presentation Layer to the Application Layer

class GymApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GMMS - Gym Membership Management")
        self.root.geometry("600x400")

        # --- Search/View Section ---
        tk.Label(root, text="Member Management", font=("Arial", 16, "bold")).pack(pady=10)
        
        self.btn_view = tk.Button(root, text="Refresh Member List", command=self.load_members)
        self.btn_view.pack(pady=5)

        # Treeview to display data
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Email", "Plan"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Plan", text="Plan ID")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20)

        # --- Add Member Section ---
        tk.Label(root, text="Add New Member (Simple Form)", font=("Arial", 12)).pack(pady=10)
        
        self.entry_name = tk.Entry(root)
        self.entry_name.insert(0, "Full Name")
        self.entry_name.pack()

        self.btn_add = tk.Button(root, text="Register Member", command=self.submit_member)
        self.btn_add.pack(pady=5)

    def load_members(self):
        """Calls the API to fetch data and updates the GUI table."""
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Call Application Layer
        members = api.get_all_members() 
        for m in members:
            self.tree.insert("", tk.END, values=(m['MemberID'], m['Name'], m['Email'], m['PlanID']))

    def submit_member(self):
        """Takes GUI input and sends it to the database via the API."""
        name = self.entry_name.get()
        
        # Hardcoding some values for the 'simple' prototype test
        # In the final version, Affanuddin will add entry boxes for all these
        test_id = 999 
        test_email = f"{name.lower().replace(' ', '.')}@test.com"
        test_phone = "555-0000"
        test_dob = "1990-01-01"
        test_join = "2026-05-05"
        test_plan = 1
        test_zip = "95112"

        # Call Application Layer logic
        result = api.add_member(test_id, name, test_email, test_phone, test_dob, test_join, test_plan, test_zip)
        
        messagebox.showinfo("Result", result)
        self.load_members()

if __name__ == "__main__":
    root = tk.Tk()
    app = GymApp(root)
    root.mainloop()
