import tkinter as tk

root = tk.Tk()

# Create three labels with images
rayquaza_image = tk.PhotoImage(file="rayquaza.png")
rayquaza_label = tk.Label(root, image=rayquaza_image)
groudon_image = tk.PhotoImage(file="groudon.png")
groudon_label = tk.Label(root, image=groudon_image)
kyogre_image = tk.PhotoImage(file="kyogre.png")
kyogre_label = tk.Label(root, image=kyogre_image)

# Add labels to grid
rayquaza_label.grid(row=0, column=0, padx=10, pady=10)
groudon_label.grid(row=0, column=1, padx=10, pady=10)
kyogre_label.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()







