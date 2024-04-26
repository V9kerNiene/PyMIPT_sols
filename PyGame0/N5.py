import sys
import pygame

pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()

x = 70
y = 30
vx = 100
vy = 100

vx1 = -100
vy1 = -100
x1, y1 = 300, 300
while True:
    dt = clock.tick(50) / 1000.0
    k = 0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if x >= 980 or x <= 20:
        vx *= -1
    if y >= 480 or y <= 20:
        vy *= -1
    if x1 >= 980 or x1 <= 20:
        vx1 *= -1
    if y1 >= 480 or y1 <= 20:
        vy1 *= -1
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        vy += 5
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        vx += 5
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        vx -= 5
    if pygame.key.get_pressed()[pygame.K_UP]:
        vy -= 5
    if pygame.key.get_pressed()[pygame.K_s]:
        vy1 += 5
    if pygame.key.get_pressed()[pygame.K_d]:
        vx1 += 5
    if pygame.key.get_pressed()[pygame.K_a]:
        vx1 -= 5
    if pygame.key.get_pressed()[pygame.K_w]:
        vy1 -= 5
    vx -= vx * k
    vy -= vy * k
    vx1 -= vx1 * k
    vy1 -= vy1 * k
    k1 = 0.75
    spd = (vx ** 2 + vy ** 2) ** 0.5
    spd1 = (vx ** 2 + vy ** 2) ** 0.5
    v1 = pygame.math.Vector2(x, y)
    v2 = pygame.math.Vector2(x1, y1)
    if v1.distance_to(v2) < 38:
        nv = v2-v1
        m1 = pygame.math.Vector2(vx, vy).reflect(nv)
        m2 = pygame.math.Vector2(vx1, vy1).reflect(nv)
        vx, vy = m1.x, m1.y
        vx1, vy1 = m2.x, m2.y
    x += vx * dt
    y += vy * dt
    x1 += vx1 * dt
    y1 += vy1 * dt
    if spd < 100:
        clr = (255, 165, 0)
    elif spd < 200:
        clr = (150, 10, 50)
    else:
        clr = (0, 0, 255)
    if spd1 < 100:
        clr1 = (255, 165, 0)
    elif spd1 < 200:
        clr1 = (150, 10, 50)
    else:
        clr1 = (0, 0, 255)
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, clr, (int(x), int(y)), 20)
    pygame.draw.circle(screen, clr1, (int(x1), int(y1)), 20)

    pygame.display.flip()
