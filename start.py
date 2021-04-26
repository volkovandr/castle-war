import pygame

size = width, height = 800, 600
black = 0, 0, 0
speed = [2, 2]

ball = pygame.image.load("graph/face1.png")
ballrect = ball.get_rect()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(size)

    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

    clock = pygame.time.Clock()

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

        clock.tick_busy_loop(30)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                do_exit = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    do_exit = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] < ballrect.left:
                    speed[0] = speed[0] - 1
                elif event.pos[0] > ballrect.right:
                    speed[0] = speed[0] + 1
                if event.pos[1] < ballrect.top:
                    speed[1] = speed[1] - 1
                elif event.pos[1] > ballrect.bottom:
                    speed[1] = speed[1] + 1
    




