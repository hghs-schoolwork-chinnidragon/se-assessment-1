import pyglet, tkinter
pyglet.font.add_file('fonts/CherryBombOne-Regular.ttf')

root = tkinter.Tk()
MyLabel = tkinter.Label(root,text="test",font=("CherryBombOne-REgular.ttf",25))
MyLabel.pack()
root.mainloop()