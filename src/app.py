import tkinter as tk
from tkinter import ttk, messagebox
from databaseAPI import get_all_members, add_member, delete_member
 
root = tk.Tk()
root.title("Gym Management System")
root.geometry("950x560")
 
tabs = ttk.Notebook(root)
tabs.pack(fill="both", expand=True, padx=10, pady=10)
 
# members tab
mem_tab = tk.Frame(tabs)
tabs.add(mem_tab, text="Members")
 
mem_cols = ("MemberID", "Name", "Email", "Phone", "DOB", "JoinDate", "PlanID", "Zipcode")
mem_tree = ttk.Treeview(mem_tab, columns=mem_cols, show="headings", height=11)
for col in mem_cols:
    mem_tree.heading(col, text=col)
    mem_tree.column(col, width=105)
mem_tree.pack(fill="both", expand=True, padx=5, pady=5)
 
def load_members():
    mem_tree.delete(*mem_tree.get_children())
    for row in get_all_members():
        mem_tree.insert("", "end", values=list(row.values()))
 
tk.Button(mem_tab, text="Refresh", command=load_members).pack(anchor="w", padx=5, pady=2)
 
add_frame = tk.LabelFrame(mem_tab, text="Add Member")
add_frame.pack(fill="x", padx=5, pady=4)
 
tk.Label(add_frame, text="ID").grid(row=0, column=0, padx=4, pady=3)
f_id = tk.StringVar()
tk.Entry(add_frame, textvariable=f_id, width=10).grid(row=0, column=1)
 
tk.Label(add_frame, text="Name").grid(row=0, column=2, padx=4)
f_name = tk.StringVar()
tk.Entry(add_frame, textvariable=f_name, width=16).grid(row=0, column=3)
 
tk.Label(add_frame, text="Email").grid(row=0, column=4, padx=4)
f_email = tk.StringVar()
tk.Entry(add_frame, textvariable=f_email, width=18).grid(row=0, column=5)
 
tk.Label(add_frame, text="Phone").grid(row=1, column=0, padx=4, pady=3)
f_phone = tk.StringVar()
tk.Entry(add_frame, textvariable=f_phone, width=14).grid(row=1, column=1)
 
tk.Label(add_frame, text="DOB").grid(row=1, column=2, padx=4)
f_dob = tk.StringVar()
tk.Entry(add_frame, textvariable=f_dob, width=12).grid(row=1, column=3)
 
tk.Label(add_frame, text="JoinDate").grid(row=1, column=4, padx=4)
f_join = tk.StringVar()
tk.Entry(add_frame, textvariable=f_join, width=12).grid(row=1, column=5)
 
tk.Label(add_frame, text="PlanID").grid(row=2, column=0, padx=4, pady=3)
f_plan = tk.StringVar()
tk.Entry(add_frame, textvariable=f_plan, width=8).grid(row=2, column=1)
 
tk.Label(add_frame, text="Zipcode").grid(row=2, column=2, padx=4)
f_zip = tk.StringVar()
tk.Entry(add_frame, textvariable=f_zip, width=10).grid(row=2, column=3)
 
def add_member_click():
    try:
        add_member(int(f_id.get()), f_name.get(), f_email.get(), f_phone.get(),
                   f_dob.get(), f_join.get(), int(f_plan.get()), f_zip.get())
        messagebox.showinfo("Done", "Member added.")
        load_members()
    except Exception as e:
        messagebox.showerror("Error", str(e))
 
def delete_member_click():
    sel = mem_tree.selection()
    if not sel:
        messagebox.showwarning("No selection", "Select a member first.")
        return
    mid = mem_tree.item(sel[0])["values"][0]
    if messagebox.askyesno("Confirm", f"Delete member {mid}?"):
        try:
            delete_member(int(mid))
            load_members()
        except Exception as e:
            messagebox.showerror("Error", str(e))
 
tk.Button(add_frame, text="Add Member", command=add_member_click).grid(row=3, column=0, columnspan=2, pady=5, padx=5)
tk.Button(add_frame, text="Delete Selected", command=delete_member_click).grid(row=3, column=2, columnspan=2, pady=5)
 
load_members()
root.mainloop()
 