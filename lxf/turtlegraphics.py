# turtle graphics

# for turtle functions:
# https://www.jianshu.com/p/7bdb648e91a7

# 导入turtle包的所有内容:
from turtle import *
"""
# 设置笔刷宽度:
width(4)

# 前进:
forward(200) # unit = distance
# first forward is toward the right

# 右转90度:
right(90) # unit = degrees

# 笔刷颜色:
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()
"""



"""
def drawStar(x, y):
    width(2)
    speed(0)
    pu() # space between stars
    goto(x, y) # go to the beginning of the next star
    pd() # draw, leave color
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

for x in range(0, 250, 50):
    drawStar(x, 0)

done()
"""

# 使用递归，可以绘制出非常复杂的图形。例如，下面的代码可以绘制一棵分型树：


"""
from turtle import *

# 设置色彩模式是RGB:
colormode(255)

speed(0)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

speed("fastest") # speed(0)

draw_tree(l, 4)

done()
"""