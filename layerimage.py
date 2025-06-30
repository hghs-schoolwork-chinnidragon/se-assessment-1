import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
crimson = tk.PhotoImage(file="images/crimson.png")
chair = tk.PhotoImage(file="images/chair.png")
print(crimson.width()/2, crimson.height()/2)
# crimson = crimson.resize((517, 600))

whatver = tk.Label(window, image=crimson)
# chair = chair.resize(chair.width/2, chair.height/2)

# canvas = tk.Canvas(window, width=crimson.width)
# canvas.place(x=0, y=0)
# canvas.create_image(0, 0, anchor="nw", image=crimson)
# canvas.place(x=0, y=0)
# canvas.create_image(0, 0, anchor="nw", image=chair)
# canvas.place(x=0, y=0)
window.mainloop()