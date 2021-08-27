import turtle
# import turtle as t 这样引用下面所有的turtle可更改为t


# 绝对坐标系：以窗口中心为原点的直角坐标系 海龟坐标系：海龟自身的朝向
# 设置窗体    宽度 高度 x   y   (相对于屏幕左上角的位置)
turtle.setup(650,350,300,200)
# 画笔抬起 这样移动时便不会产生图案
turtle.penup()
# 向朝向的相反方向直走 单位像素
turtle.fd(-250)
turtle.pendown()
# 修改画笔宽度
turtle.pensize(25)
# 修改画笔颜色
turtle.pencolor("purple")
# 绝对坐标系下改变海龟方向
turtle.seth(-40)
# 循环语句 for <变量> in range (<变量>) Case：for i in range (5) 即i的值从0到5
# Case: for i in range(M,N) That means, the value of i ranges from m to n-1
for i in range (4):
#circle(r,extent=None)根据半径r绘制角度extent的弧形 默认圆心在海龟左侧距离为r的位置 extent默认情况下绘制整圆
#若r为负数，则默认圆心在海龟右侧距离为r的绝对值的位置
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
# 画完后暂停一下
turtle.done()
