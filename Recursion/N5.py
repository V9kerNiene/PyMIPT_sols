import turtle
turtle.speed('fastest')
turtle.penup()
turtle.setposition(-300, 0)
turtle.pendown()

patt = 'F'
tPatt = ''
h = 4 # recursion depth
l=8 # initial edge length
pat = {'F':'F+F-F-FF+F+F-F'}

for i in range(h):
    for j in patt:
        if j in pat:
            tPatt += pat[j]
        else:
            tPatt += j
    patt, tPatt = tPatt, ''

for k in patt:
    if k == '+':
        turtle.left(90)
    elif k == '-':
        turtle.right(90)
    else:
        turtle.forward(l)
