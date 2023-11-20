import turtle
import random
import tkinter as tk
from tkinter import messagebox
wn = turtle.Screen()
wn.bgcolor("green")
wn.bgpic(r"C:\Users\Kshitiz Trigunayat\OneDrive\Desktop\python\Python-project\bg.png")
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.num_trees_label = tk.Label(self)
        self.num_trees_label["text"] = "Number of Trees:"
        self.num_trees_label.pack(side="top")

        self.x_coordinate_label = tk.Label(self)
        self.x_coordinate_label["text"] = "X Coordinate:"
        self.x_coordinate_label.pack(side="top")

        self.y_coordinate_label = tk.Label(self)
        self.y_coordinate_label["text"] = "Y Coordinate:"
        self.y_coordinate_label.pack(side="top")

        # Entries
        self.num_trees_entry = tk.Entry(self)
        self.num_trees_entry.pack(side="top")

        self.x_coordinate_entry = tk.Entry(self)
        self.x_coordinate_entry.pack(side="top")

        self.y_coordinate_entry = tk.Entry(self)
        self.y_coordinate_entry.pack(side="top")

        # Button
        self.submit_button = tk.Button(self)
        self.submit_button["text"] = "Submit"
        self.submit_button["command"] = self.submit
        self.submit_button.pack(side="top")

    def submit(self):
        num_trees = int(self.num_trees_entry.get() or 0)
        x_coordinate = int(self.x_coordinate_entry.get() or 0)
        y_coordinate = int(self.y_coordinate_entry.get() or 0)

        # Display a message box with the inputs
        messagebox.showinfo("Submitted", f"Number of Trees: {num_trees}\nX Coordinate: {x_coordinate}\nY Coordinate: {y_coordinate}")

        # Create forest with turtle graphics
        
        
        presapling_x = x_coordinate -300
        presapling_y = y_coordinate
        presaplinggrp(num_trees, presapling_x, presapling_y)

        saplinggrp(num_trees, x_coordinate, y_coordinate)

        create_forestx = x_coordinate +300
        create_foresty = y_coordinate 
        create_forest(num_trees, create_forestx, create_foresty)



def tree(branch_len, t):
    angle = random.randint(22, 30)
    sf = random.uniform(0.6, 0.8)
    if branch_len < 10:
        t.color("green")
        t.width(8)
        t.shapesize(2.5)
        t.stamp()
        t.color("brown")
    else:
        t.width(5)
        t.forward(branch_len)
        t.left(angle)
        tree(branch_len*sf, t)
        t.right(2*angle)
        tree(branch_len*sf, t)
        t.left(angle)
        t.backward(branch_len)

def sapling(branch_len, t1):
    angle = random.randint(20, 28)
    sf = random.uniform(0.5, 0.7)
    if branch_len < 8:
        t1.color("green")
        t1.width(5)
        t1.shapesize(1)
        t1.stamp()
        t1.color("brown")
    else:
        t1.width(2)
        t1.forward(branch_len)
        t1.left(angle)
        sapling(branch_len*sf, t1)
        t1.right(2*angle)
        sapling(branch_len*sf, t1)
        t1.left(angle)
        t1.backward(branch_len)

def saplinggrp(num_sap, x, y):
    for _ in range(num_sap):
        sapling_turtle = turtle.Turtle()
        sapling_turtle.speed(100)
        sapling_turtle.left(90)
        sapling_turtle.color("brown")
        sapling_turtle.up()
        sapling_turtle.goto(x, y)
        sapling_turtle.down()
        sapling(100, sapling_turtle)
        x += 150

def presapling(branch_len, t2):
    angle = random.randint(15, 25)
    sf = random.uniform(0.4, 0.6)
    if branch_len < 5:
        t2.color("green")
        t2.width(1)
        t2.shapesize(1)
        t2.stamp()
        t2.color("brown")
    else:
        t2.width(2)
        t2.forward(branch_len)
        t2.left(angle)
        presapling(branch_len*sf, t2)
        t2.right(2*angle)
        presapling(branch_len*sf, t2)
        t2.left(angle)
        t2.backward(branch_len)

def presaplinggrp(num_sap, x, y):
    for _ in range(num_sap):
        presapling_turtle = turtle.Turtle()
        presapling_turtle.speed(100)
        presapling_turtle.left(90)
        presapling_turtle.color("brown")
        presapling_turtle.up()
        presapling_turtle.goto(x, y)
        presapling_turtle.down()
        presapling(100, presapling_turtle)
        x += 150

def create_forest(num_trees, x, y):
    for _ in range(num_trees):
        tree_turtle = turtle.Turtle()
        tree_turtle.speed(100)
        tree_turtle.left(90)
        tree_turtle.color("brown")
        tree_turtle.up()
        tree_turtle.goto(x, y)
        tree_turtle.down()
        tree(100, tree_turtle)
        x += 200

root = tk.Tk()
app = Application(master=root)
app.mainloop()
turtle.done()



