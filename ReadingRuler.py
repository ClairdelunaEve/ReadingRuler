import tkinter

root = tkinter.Tk()
root.title("Reading Ruler")
root.wm_attributes("-transparent", True)
root.attributes("-topmost", True)
root.geometry("+300+300")

c = tkinter.Canvas(root, bg="systemTransparent", highlightthickness=0, width=300, height=300)
rect_head = c.create_rectangle(0, 0, 300, 50, fill='#86A697', width=0)
rect_foot = c.create_rectangle(0, 0, 300, 300, fill='#86A697', width=0)
c.pack(fill=tkinter.BOTH, expand=True)

def change_rect(event):
    w = root.winfo_width()
    h = root.winfo_height()
    c.coords(rect_head, 0, 0, w, 50)
    c.coords(rect_foot, 0, h/2, w,h)

root.bind('<Configure>', change_rect)

root.mainloop()
