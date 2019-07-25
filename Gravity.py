import pygame , time
win = pygame.display.set_mode((800,800))


print("Press space to make the ball bounce. Click the ball to resert it")


x = 400
y = 200
run = True
bouncing = False
falling = False
clicked = False
height = 9
speed = -6
a = 0
t = 0
r = 0

while run:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if clicked == False:
                t, r = event.pos
            
                
        if event.type == pygame.MOUSEBUTTONUP:
            if clicked == True:
                x = 400
                y = 200
                bouncing = False
                falling = False     #resets everything when the ball is clicked
                clicked = False
                a = 0
                height = 9
                t = 0
                r = 0

    l,o = pygame.mouse.get_pos()   

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        if falling == False and bouncing == False and y != 776:
            falling = True
    if falling == True:
        y += (speed ** 2) /0.5
        if y >= 770:
            falling = False #this is the code for when the ball initially starts falling
            bouncing = True
        
    
    if bouncing == True:
        if height >= -9 + a:
            neg = 1
            if height < 0:
                neg = -1
            y -= (height ** 2) /0.5 * neg   #this is the code to make the ball bounce
            height -= 1
        else:
            a += 1
            if 9 - a < 0:
                bouncing = False
            else:
                height = 9 - a
            
    if clicked == True:
        circle = pygame.draw.circle(win, (255,0,255),(int(l),int(o)), 20)
        
    win.fill((255,255,255))
    if clicked == False:
        circle = pygame.draw.circle(win, (255,0,255),(int(x),int(y)), 20)
    if clicked == True:
        circle = pygame.draw.circle(win, (255,0,255),(int(l),int(o)), 20)
        t = 0
        r = 0
    marker = pygame.draw.rect(win,(255,0,255), (t,r,1,1))
    if circle.colliderect(marker) == True:
        clicked = True
    pygame.display.update()
    

    
