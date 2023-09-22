import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def check_duplicates():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])

    if not file_path:
        messagebox.showinfo("Info", "No file selected.")
        return

    df = pd.read_excel(file_path)

    duplicates_found = False

    for column in df.columns:
        column_values = df[column]
        duplicate_indices = column_values[column_values.duplicated()].index.tolist()

        if duplicate_indices:
            duplicates_found = True
            message = f"Duplicate values found in column '{column}':\n"
            for index in duplicate_indices:
                message += f"Duplicate value '{column_values.iloc[index]}' at position {index + 2}\n"
            messagebox.showinfo("Duplicate Values Found", message)

    if not duplicates_found:
        messagebox.showinfo("No Duplicates", "No duplicate values found in any column.")


root = tk.Tk()
root.title("Check Excel File for Duplicates")
check_button = tk.Button(root, text="Select Excel File and Check for Duplicates", command=check_duplicates)
check_button.pack(padx=20, pady=20)

root.mainloop()
