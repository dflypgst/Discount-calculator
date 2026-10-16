import tkinter as tk
from tkinter import messagebox

def count_discount():
    try:
        price = float(entry_price.get())
        discount = float(entry_discount.get())
        saving = price * (discount / 100)
        pay = price - saving

        label_result.config(text=f"You save: Rp{saving:,.2f}\nFinal Price: Rp{pay:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ooopss")


app = tk.Tk()
app.title("Discount")
app.geometry("250x250")


tk.Label(app, text="Price (Rp):").pack(pady=5)
entry_price = tk.Entry(app)
entry_price.pack()


tk.Label(app, text="Discount (%):").pack(pady=5)
entry_discount = tk.Entry(app)
entry_discount.pack()


tk.Button(app, text="Count", command=count_discount).pack(pady=15)


label_result = tk.Label(app, text="-", fg="green")
label_result.pack()

app.mainloop()