# imports
from turtle import *
import random, time

# constants
size=40      # number of elements in the list
width=20     # width of the bars in px

# status
status=0    # 0: sorted     1: shuffled     2: sorting

# create the list
list = []

# current comparison index
target=-1

# number of consecutive non-swaps
consecutive=0

# is the list sorted?
issorted=True

# maximum size to check
maxsize=size

# populate the list with numbers from 1 to size
for i in range(size):
    list.append(i+1)

# set bg color
bgcolor("black")

# set window title
title("Visual Bubble Sort")

# set window size
setup((size*width)+30, (size*width/2)+60)

# set delay
delay(0)
hideturtle()
tracer(0)

# rendering
def render():
    # clear the screen
    clear()

    # go to bottom right
    penup()
    goto(-(size*width/2), (-(size*width/2)/2))
    pendown()

    # draw the list
    for i in range(size):
        # draw the bar
        if i==target:
            color("red")
        elif issorted or i>=maxsize:
            color("green")
        else:
            color('white')
        begin_fill()
        forward(width)
        left(90)
        forward(list[i]*(width/2))
        left(90)
        forward(width)
        left(90)
        forward(list[i]*(width/2))
        left(90)
        end_fill()

        # move the turtle to the next bar
        forward(width)
    # draw to display
    update()

# shuffling
def shufflelist():
    global issorted, status, target
    issorted=False
    # shuffle the list
    random.shuffle(list)
    # set status
    status=1
    # set target
    target=0

def doshuffleorsort():
    global consecutive, status, target, maxsize, size
    # shuffle the list
    if status==0:
        shufflelist()
    # sort the list
    elif status==1:
        consecutive=0
        maxsize=size
        status=2

# keypresses
onkeypress(bye, "Escape")
onkeypress(doshuffleorsort, "space")
onkeypress(shufflelist, "Return")


# main loop
while True:
    if status==2:
        # swap the current target with the next element
        if list[target]>list[target+1]:
            temp=list[target]
            list[target]=list[target+1]
            list[target+1]=temp
            consecutive=0
        else:
            consecutive+=1
        target+=1
        # check if the list is sorted
        if maxsize<=1:
            status=0
            consecutive=0
            maxsize=size
            issorted=True
            target=-1
        # no point in checking the end since it's already sorted
        if target >= maxsize-1:
            target=0
            maxsize-=(consecutive+1)
            consecutive=0
    render()
    listen()

