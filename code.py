import turtle
import random
wn = turtle.Screen()
wn.colormode = "255"
wn.bgpic(r"C:\Users\Kshitiz Trigunayat\OneDrive\Desktop\python\Python-project\bg.png")
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
    t1 = turtle.Turtle()
    t1.speed(100)
    t1.left(90)
    t1.color("brown")
    t1.up()
    t1.backward(200)
    t1.down()
    t1.penup()
    for _ in range(num_sap):
        t1.penup()
        t1.goto(x, y)
        t1.pendown()
        sapling(100, t1)
        x += 100
        y += 70
        x -= 100
        y -= 70

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
    t2 = turtle.Turtle()
    t2.speed(100)
    t2.left(90)
    t2.color("brown")
    t2.up()
    t2.backward(200)
    t2.down()
    t2.penup()
    for _ in range(num_sap):
        t2.penup()
        t2.goto(x, y)
        t2.pendown()
        presapling(100, t2)
        x += 100
        y += 70
        x -= 100
        y -= 70


    
def create_forest(num_trees, x, y):
    t = turtle.Turtle()
    t.speed(100)
    t.left(90)
    t.color("brown")
    t.up()
    t.backward(200)
    t.down()
    t.penup()
    for _ in range(num_trees):
        t.penup()
        t.goto(x, y)
        t.pendown()
        tree(100, t)
        x += 100
        y += 70
        x -= 100
        y -= 70

presaplinggrp(1, -350, -265) or saplinggrp(1, -420, -185) or create_forest(1,-350,-85)
presaplinggrp(1, -250, -265) or saplinggrp(1, -320, -185) or create_forest(1,-250,-85) 
presaplinggrp(1, -150, -265) or saplinggrp(1, -220, -185) or create_forest(1, -150, -85) 
presaplinggrp(1, -50, -265) or saplinggrp(1, -120, -185) or create_forest(1, -50, -85)
presaplinggrp(1, +50, -265) or saplinggrp(1, -20, -185) or create_forest(1, +50, -85)
presaplinggrp(1, +150, -265) or saplinggrp(1, +80, -185) or create_forest(1, +150, -85)
presaplinggrp(1, +250, -265) or saplinggrp(1, +180, -185) or create_forest(1, +250, -85)
presaplinggrp(1, +350, -265) or saplinggrp(1, +280, -185) or create_forest(1, +350, -85)
presaplinggrp(1, +450, -265) or saplinggrp(1, +380, -185) or create_forest(1, +450, -85)


turtle.done()




turtle.done()
