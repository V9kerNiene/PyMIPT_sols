import turtle
turtle.speed('fastest')
turtle.penup()
turtle.setposition(-300, 0)
turtle.pendown()

patt = 'F'
tPatt = ''
h = 8 # recursion depth
pat = {'F':'-F++F-'}
l=8 # initial edge length


for i in range(h):
    for j in patt:
        if j in pat:
            tPatt += pat[j]
        else:
            tPatt += j
    patt, tPatt = tPatt, ''

for k in patt:
    if k == '-':
        turtle.left(45)
    elif k == '+':
        turtle.right(45)
    else:
        turtle.forward(l)

