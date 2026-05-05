import tkinter as tk
from tkinter import ttk, messagebox
from databaseAPI import (
    get_all_members,
    add_member,
    delete_member,
    book_class,
    delete_booking,
    get_db_connection,
    record_payment,
    delete_payment,
)


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

# bookings tab
book_tab = tk.Frame(tabs)
tabs.add(book_tab, text="Bookings")

book_cols = ("BookingID", "MemberID", "ClassID", "BookingDate", "Status")
book_tree = ttk.Treeview(book_tab, columns=book_cols, show="headings", height=11)
for col in book_cols:
    book_tree.heading(col, text=col)
    book_tree.column(col, width=160)
book_tree.pack(fill="both", expand=True, padx=5, pady=5)

def load_bookings():
    book_tree.delete(*book_tree.get_children())
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Bookings")
    for row in cur.fetchall():
        book_tree.insert("", "end", values=list(row.values()))
    cur.close()
    conn.close()

tk.Button(book_tab, text="Refresh", command=load_bookings).pack(anchor="w", padx=5, pady=2)

bk_frame = tk.LabelFrame(book_tab, text="Book a Class")
bk_frame.pack(fill="x", padx=5, pady=4)

tk.Label(bk_frame, text="BookingID").grid(row=0, column=0, padx=4, pady=3)
bk_id = tk.StringVar()
tk.Entry(bk_frame, textvariable=bk_id, width=10).grid(row=0, column=1)

tk.Label(bk_frame, text="MemberID").grid(row=0, column=2, padx=4)
bk_mem = tk.StringVar()
tk.Entry(bk_frame, textvariable=bk_mem, width=10).grid(row=0, column=3)

tk.Label(bk_frame, text="ClassID").grid(row=0, column=4, padx=4)
bk_cls = tk.StringVar()
tk.Entry(bk_frame, textvariable=bk_cls, width=10).grid(row=0, column=5)

tk.Label(bk_frame, text="Date").grid(row=1, column=0, padx=4, pady=3)
bk_date = tk.StringVar()
tk.Entry(bk_frame, textvariable=bk_date, width=14).grid(row=1, column=1)

def book_class_click():
    try:
        book_class(int(bk_id.get()), int(bk_mem.get()), int(bk_cls.get()), bk_date.get())
        messagebox.showinfo("Done", "Booking added.")
        load_bookings()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_booking_click():
    sel = book_tree.selection()
    if not sel:
        messagebox.showwarning("No selection", "Select a booking first.")
        return
    bid = book_tree.item(sel[0])["values"][0]
    if messagebox.askyesno("Confirm", f"Delete booking {bid}?"):
        try:
            delete_booking(int(bid))
            load_bookings()
        except Exception as e:
            messagebox.showerror("Error", str(e))

tk.Button(bk_frame, text="Book Class", command=book_class_click).grid(row=2, column=0, columnspan=2, pady=5, padx=5)
tk.Button(bk_frame, text="Delete Selected", command=delete_booking_click).grid(row=2, column=2, columnspan=2, pady=5)

load_bookings()


# payments tab
pay_tab = tk.Frame(tabs)
tabs.add(pay_tab, text="Payments")

pay_cols = ("PaymentID", "MemberID", "Amount", "PayDate", "Method", "Status")
pay_tree = ttk.Treeview(pay_tab, columns=pay_cols, show="headings", height=11)
for col in pay_cols:
    pay_tree.heading(col, text=col)
    pay_tree.column(col, width=140)
pay_tree.pack(fill="both", expand=True, padx=5, pady=5)

def load_payments():
    pay_tree.delete(*pay_tree.get_children())
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Payments")
    for row in cursor.fetchall():
        pay_tree.insert("", "end", values=list(row.values()))
    cursor.close()
    conn.close()

tk.Button(pay_tab, text="Refresh", command=load_payments).pack(anchor="w", padx=5, pady=2)

pay_frame = tk.LabelFrame(pay_tab, text="Record Payment")
pay_frame.pack(fill="x", padx=5, pady=4)

tk.Label(pay_frame, text="PaymentID").grid(row=0, column=0, padx=4, pady=3)
py_id = tk.StringVar()
tk.Entry(pay_frame, textvariable=py_id, width=10).grid(row=0, column=1)

tk.Label(pay_frame, text="MemberID").grid(row=0, column=2, padx=4)
py_mem = tk.StringVar()
tk.Entry(pay_frame, textvariable=py_mem, width=10).grid(row=0, column=3)

tk.Label(pay_frame, text="Amount").grid(row=0, column=4, padx=4)
py_amt = tk.StringVar()
tk.Entry(pay_frame, textvariable=py_amt, width=10).grid(row=0, column=5)

tk.Label(pay_frame, text="Date").grid(row=1, column=0, padx=4, pady=3)
py_date = tk.StringVar()
tk.Entry(pay_frame, textvariable=py_date, width=14).grid(row=1, column=1)

tk.Label(pay_frame, text="Method").grid(row=1, column=2, padx=4)
py_method = tk.StringVar(value="Credit Card")
ttk.Combobox(pay_frame, textvariable=py_method,
            values=["Credit Card", "Debit Card", "Cash", "PayPal"],
            width=14, state="readonly").grid(row=1, column=3)

tk.Label(pay_frame, text="Status").grid(row=1, column=4, padx=4)
py_status = tk.StringVar(value="Paid")
ttk.Combobox(pay_frame, textvariable=py_status,
            values=["Paid", "Pending", "Overdue"],
            width=10, state="readonly").grid(row=1, column=5)

def add_payment_click():
    try:
        record_payment(int(py_id.get()), int(py_mem.get()), float(py_amt.get()),
        py_date.get(), py_method.get(), py_status.get())
        messagebox.showinfo("Done", f"Payment {py_id.get()} recorded.")
        load_payments()
    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Button(pay_frame, text="Record Payment", command=add_payment_click).grid(row=2, column=0, columnspan=2, pady=5, padx=5)

load_payments()
root.mainloop()
