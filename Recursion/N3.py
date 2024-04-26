import turtle
turtle.speed('fastest')
turtle.penup()
turtle.setposition(-300, 0) # initial position
turtle.pendown()
l = 8 # initial edge length
patt = 'F'
tPatt = ''
h = 4 # recursion depth
pat = {'F':'F-F+F-F'}

for i in range(h):
    for j in patt:
        if j in pat:
            tPatt += pat[j]
        else:
            tPatt += j
    patt, tPatt = tPatt, ''
for _ in range(3):
    for k in patt:
        if k == '+':
            turtle.right(120)
        elif k == '-':
            turtle.left(60)
        else:
            turtle.forward(l)
    turtle.right(120)
