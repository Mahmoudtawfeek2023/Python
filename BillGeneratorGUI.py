import tkinter as tk
from tkinter import messagebox
import os
import datetime
from fpdf import FPDF

class Bill:
    def __init__(self, customer_name, items, prices):
        self.customer_name = customer_name
        self.items = items
        self.prices = prices

    def get_total(self):
        # calculate the total price of all items
        total = sum(self.prices)
        return total

    def to_string(self):
        # create a string representation of the bill
        items_string = "\n".join([f"{item}: {price}" for item, price in zip(self.items, self.prices)])
        total_string = f"\nTotal: {self.get_total()}"

        return f"Customer Name: {self.customer_name}\n\nItems:\n{items_string}\n{total_string}"

    def to_pdf(self, filename):
        # create a new PDF object
        pdf = FPDF()
        pdf.add_page()

        # set the font for the bill
        pdf.set_font("Arial", size=12)

        # add the customer name to the PDF
        pdf.cell(0, 10, f"Customer Name: {self.customer_name}", ln=1)

        # add the table header
        pdf.cell(60, 10, "Item", border=1)
        pdf.cell(50, 10, "Price", border=1, ln=1)

        # add the items and prices to the table
        for item, price in zip(self.items, self.prices):
            pdf.cell(60, 10, str(item), border=1)
            pdf.cell(50, 10, str(price), border=1, ln=1)

        # add the total price to the PDF
        pdf.cell(0, 10, f"Total: {self.get_total()}", ln=1)

        # create a folder with the current date if it doesn't exist
        folder_name = datetime.datetime.now().strftime("%Y-%m-%d")
        os.makedirs(folder_name, exist_ok=True)

        # save the PDF to a file in the folder with the customer name
        pdf.output(os.path.join(folder_name, filename))

class BillGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Bill Generator")

        # set the window size and position it in the center of the screen
        window_width = 400
        window_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # create the customer name entry
        tk.Label(self.root, text="Customer Name").grid(row=0, column=0, padx=10, pady=10)
        self.customer_name_entry = tk.Entry(self.root)
        self.customer_name_entry.grid(row=0, column=1)

        # create the item name and price entries
        tk.Label(self.root, text="Item Name").grid(row=1, column=0, padx=10, pady=10)
        self.item_name_entry = tk.Entry(self.root)
        self.item_name_entry.grid(row=1, column=1)
        tk.Label(self.root, text="Price").grid(row=2, column=0, padx=10, pady=10)
        self.price_entry = tk.Entry(self.root)
        self.price_entry.grid(row=2, column=1)

        # create the add item button
        self.add_item_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_item_button.grid(row=3, column=0, padx=10, pady=10)

        # create the generate bill button
        self.generate_bill_button = tk.Button(self.root, text="Generate Bill", command=self.generate_bill)
        self.generate_bill_button.grid(row=3, column=1, padx=10, pady=10)

        # create the item listbox
        tk.Label(self.root, text="Items").grid(row=4, column=0, padx=10, pady=10)
        self.item_listbox = tk.Listbox(self.root)
        self.item_listbox.grid(row=4, column=1)

        # create the total price label
        tk.Label(self.root, text="Total Price").grid(row=5, column=0, padx=10, pady=10)
        self.total_price_label = tk.Label(self.root, text="")
        self.total_price_label.grid(row=5, column=1)

        # initialize the items and prices lists
        self.items = []
        self.prices = []

    def add_item(self):
        # get the item name and price from the entries
        item = self.item_name_entry.get()
        price = self.price_entry.get()

        # validate the inputs
        if not item or not price:
            messagebox.showerror("Error", "Item name and price cannot be empty.")
            return
        try:
            price = float(price)
        except ValueError:
            messagebox.showerror("Error", "Price must be a number.")
            return

        # add the item and price to the lists
        self.items.append(item)
        self.prices.append(price)

        # add the item to the listbox
        self.item_listbox.insert(tk.END, f"{item}: {price}")

        # clear the entries
        self.item_name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

        # update the total price label
        total_price = sum(self.prices)
        self.total_price_label.config(text=f"{total_price:.2f}")

    def generate_bill(self):
        # get the customer name from the entry
        customer_name = self.customer_name_entry.get()

        # validate the input
        if not customer_name:
            messagebox.showerror("Error", "Customer name cannot be empty.")
            return

        # create a new bill object
        bill = Bill(customer_name, self.items, self.prices)

        # create a filename for the PDF based on the customer name
        filename = f"{customer_name}.pdf"

        # save the bill to a PDF file
        bill.to_pdf(filename)

        # show a message box with the success message
        messagebox.showinfo("Success", f"Bill for {customer_name} saved to {filename}.")

        # clear the entries and lists
        self.customer_name_entry.delete(0, tk.END)
        self.item_name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.item_listbox.delete(0, tk.END)
        self.total_price_label.config(text="")
        self.items = []
        self.prices = []

if __name__ == "__main__":
    root = tk.Tk()
    app = BillGenerator(root)
    root.mainloop()
