import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
# crimson = tk.PhotoImage(file="images/crimson.png")
# chair = tk.PhotoImage(file="images/chair.png")
# print(crimson.width()/2, crimson.height()/2)
# crimson = crimson.resize((517, 600))

crimson = Image.open("images/crimson.png")
crimson = crimson.resize((517, 600))
chair = Image.open("images/chair.png")
chair = chair.resize((517, 600))
crimson.paste(chair, (0, 0), chair)


crimson =  ImageTk.PhotoImage(crimson)
test = tk.Label(window, image=crimson)
test.pack()
# hair = tk.Label(window, image=chair)
# hair.pack(padx=0,pady=0)
# chair = chair.resize(chair.width/2, chair.height/2)

# canvas = tk.Canvas(window, width=crimson.width)
# canvas.place(x=0, y=0)
# canvas.create_image(0, 0, anchor="nw", image=crimson)
# canvas.place(x=0, y=0)
# canvas.create_image(0, 0, anchor="nw", image=chair)
# canvas.place(x=0, y=0)
window.mainloop()