import turtle
turtle.speed('fastest')
turtle.penup()
turtle.setposition(-300, 0)
turtle.pendown()


h = 4 # recursion depth
l=1000 # inital length
l1=l
for y in range(h):
    turtle.width(1)
    p=0
    patt = 'A'
    tPatt = ''
    pat = {'A': 'ABA', 'B': 'BBB'} # {'F':'F+F-F-FF+F+F-F'}
    l1 *= 1/3
    for i in range(y):
        for j in patt:
            if j in pat:
                tPatt += pat[j]
            else:
                tPatt += j
        patt, tPatt = tPatt, ''
    for k in patt:
        if k == 'A':
            turtle.pendown()
            turtle.forward(l1)
            p+=1
        elif k == 'B':
            turtle.penup()
            turtle.forward(l1)
            p+=1
    turtle.penup()
    turtle.backward(l1*p)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.pendown()
a=input()
