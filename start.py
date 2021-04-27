import pygame
import sprites
import graph

speed = [2, 2]

factrect = sprites.face.get_rect()

if __name__ == "__main__":
    pygame.init()
    graph.init()

    clock = pygame.time.Clock()

    do_exit = False
    
    while not do_exit:
        factrect = factrect.move(speed)
        if factrect.left < 0 or factrect.right  > graph.width:
            speed[0] = -speed[0]
        if factrect.top < 0 or factrect.bottom > graph.height:
            speed[1] = -speed[1]

        graph.clear()
        graph.screen.blit(sprites.face, factrect)
        graph.flip()
        

        clock.tick_busy_loop(30)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                do_exit = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    do_exit = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] < factrect.left:
                    speed[0] = speed[0] - 1
                elif event.pos[0] > factrect.right:
                    speed[0] = speed[0] + 1
                if event.pos[1] < factrect.top:
                    speed[1] = speed[1] - 1
                elif event.pos[1] > factrect.bottom:
                    speed[1] = speed[1] + 1
    




