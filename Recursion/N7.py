import turtle
turtle.speed('fastest')
turtle.penup()
turtle.setposition(-300, 0)
turtle.pendown()

patt = 'FX'
tPatt = ''
pat = {'X': 'X+YF+', 'Y': '−FX−Y'}
l = 8 # initial edge length
h = 10 # recursion depth
for i in range(h):
    for j in patt:
        if j in pat:
            tPatt += pat[j]
        else:
            tPatt += j
    patt, tPatt = tPatt, ''

for k in patt:
    if k == 'F':
        turtle.forward(l)
    elif k == '+':
        turtle.right(90)
    elif k == '−':
        turtle.left(90)
