import pyglet, tkinter
# pyglet.font.add_file('fonts/CherryBombOne-Regular.ttf')

# root = tkinter.Tk()
# MyLabel = tkinter.Label(root,text="test",font=("Cherry Bomb One",25))
# MyLabel.pack()
# root.mainloop()



# root = tk.Tk()
# root.title("System Font Test")

# # Print available fonts
# system_fonts = tk.font.families()
# print(f"Available fonts: {system_fonts}")

# # Use a nice system font that's guaranteed to be there
# label = tk.Label(root, text="Testing Font", font=("Arial", 25))
# label.pack(pady=20)

# root.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import font


def create_simple_font_browser():
    root = tk.Tk()
    root.title("System Font Browser")
    root.geometry("700x600")
    
    # Create frame with scrollbar
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)
    
    # Create canvas with scrollbar
    canvas = tk.Canvas(main_frame)
    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Pack scrollbar and canvas
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    
    # Create scrollable frame
    scrollable_frame = tk.Frame(canvas)
    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    
    # Configure scrolling
    def configure_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    
    scrollable_frame.bind("<Configure>", configure_scroll_region)
    
    # Get available fonts
    try:
        all_fonts = sorted(list(tk.font.families()))
        print(f"Found {len(all_fonts)} fonts")
    except Exception as e:
        print(f"Error getting fonts: {e}")
        all_fonts = ["Arial", "Helvetica", "Times"]
    
    # Add fonts to frame
    for i, font_name in enumerate(all_fonts):
        try:
            # Create frame for each font
            font_frame = tk.Frame(scrollable_frame)
            font_frame.pack(fill="x", pady=2)
            
            # Try to create a label with the font
            try:
                label = tk.Label(font_frame, 
                                text=font_name, 
                                font=(font_name, 14))
                label.pack(side="left", padx=10)
            except:
                label = tk.Label(font_frame, 
                                text=f"{font_name} (unable to display)", 
                                font=("Arial", 12))
                label.pack(side="left", padx=10)
        except Exception as e:
            print(f"Error with font {font_name}: {e}")
    
    # Make canvas expandable
    def on_canvas_configure(event):
        canvas.itemconfig(canvas_window, width=event.width)
    
    canvas.bind("<Configure>", on_canvas_configure)
    
    # Handle scrolling with mouse wheel on macOS
    def on_mousewheel(event):
        # Different handling for different platforms
        if event.num == 4:  # Linux scroll up
            canvas.yview_scroll(-1, "units")
        elif event.num == 5:  # Linux scroll down
            canvas.yview_scroll(1, "units")
        else:  # macOS/Windows
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    # Bind for different platforms
    canvas.bind_all("<MouseWheel>", on_mousewheel)  # Windows/macOS
    canvas.bind_all("<Button-4>", on_mousewheel)    # Linux scroll up
    canvas.bind_all("<Button-5>", on_mousewheel)    # Linux scroll down
    
    root.mainloop()

if __name__ == "__main__":
    create_simple_font_browser()