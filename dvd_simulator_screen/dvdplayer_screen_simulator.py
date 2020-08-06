import sys, pygame,random
pygame.init()

size = width, height = 1024, 720
speed = [1, 1]
white = 255, 255, 255

screen = pygame.display.set_mode(size)


ball_black = pygame.image.load("dvd.png")
ball_red = pygame.image.load("red.png")
ball_yellow = pygame.image.load("yellow.png")
ball_blue = pygame.image.load("blue.png")
#ball = ball_black

#ballrect = ball.get_rect()
n = 0
def color(n):
    n = n%4
    if n == 0:
        ball = ball_black
    if n == 1:
        ball = ball_red
    if n == 2:
        ball = ball_yellow
    if n == 3:
        ball = ball_blue
    return ball

ball = color(n)

ballrect = ball.get_rect()
    
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        n = n+1
        ball = color(n)
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        n = n+1
        ball = color(n)
        speed[1] = -speed[1]
  

    screen.fill(white)
    screen.blit(ball, ballrect)
    pygame.display.flip()

