import pygame

size = width, height = 800, 600
black = 0, 0, 0
speed = [2, 2]

ball = pygame.image.load("graph/face1.png")
ballrect = ball.get_rect()

clock = pygame.time.Clock()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(size)

    do_exit = False
    
    while not do_exit:
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right  > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()

        clock.tick_busy_loop(50)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                do_exit = True

    




