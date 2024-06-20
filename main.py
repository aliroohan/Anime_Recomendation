import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk

df = pd.read_csv('anime-dataset-2023.csv')

print(df.columns)
types = df['Type'].unique()
types = list(types)
types.remove("UNKNOWN")
print(types)

rating = df['Rating'].unique()
rating = list(rating)
rating.remove("UNKNOWN")
print(rating)

source = df['Source'].unique()
source = list(source)
source.remove("Unknown")
print(source)

df.sort_values('Score', ascending=False, inplace=True)
df = df[["Name", 'Genres']]
genere = df['Genres'].unique()
genere = list(genere)
genere.remove("UNKNOWN")
genere = [i.split(",") for i in genere]
genre = list(set([j.strip() for i in genere for j in i]))



genre.sort()
print(genre)

# print(df.head())
# print(df.shape)

def on_button_click():
    print("Option 1:", combo1.get())
    print("Option 2:", combo2.get())
    print("Option 3:", combo3.get())
    print("Option 4:", combo4.get())


root = tk.Tk()
root.title("Tkinter Drop-down Example")
root.geometry("300x300")

# Define the options for the drop-down menus
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Create the drop-down menus
label1 = tk.Label(root, text="Select Type:", width=20)
label1.pack(pady=5)
combo1 = ttk.Combobox(root, values=types, width=30)
combo1.set("Select an option")
combo1.pack(pady=5)

label2 = tk.Label(root, text="Select Rating:", width=20)
label2.pack(pady=5)
combo2 = ttk.Combobox(root, values=rating, width=30)
combo2.set("Select an option")
combo2.pack(pady=5)

label3 = tk.Label(root, text="Select Source:", width=20)
label3.pack(pady=5)
combo3 = ttk.Combobox(root, values=source, width=30)
combo3.set("Select an option")
combo3.pack(pady=5)

label4 = tk.Label(root, text="Select Genre:", width=20)
label4.pack(pady=5)
combo4 = ttk.Combobox(root, values=genre, width=30)
combo4.set("Select an option")
combo4.pack(pady=5)

# Create the button
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=20)

# Run the application
root.mainloop()