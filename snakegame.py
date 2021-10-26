import pygame
import random

pygame.init()

# GAME COLORS
green = pygame.Color("#00D32D")
red = pygame.Color("#D3002E")
black = pygame.Color(0, 0, 0)

dis = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Eric's Snake Game")

# Game Properties
game_speed = 15
block_increments = 10

clock = pygame.time.Clock()

text_font = pygame.font.SysFont("comic sans", 30)


def snake(block_increments, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, green, [x[0], x[1], block_increments, block_increments])


def messaging(msg, color):
    mesg = text_font.render(msg, True, red)
    dis.blit(mesg, [90, 500/2])


def loopGame():
    game_over = False
    game_close = False

    x1 = 300
    y1 = 300
    x1_change = 0
    y1_change = 0

    snake_List = []
    length_Of_Snake = 1

    food_x = round(random.randrange(0, 490) / 10) * 10
    food_y = round(random.randrange(0, 490) / 10) * 10

    while not game_over:

        while game_close == True:
            dis.fill(black)
            messaging("""You Lost   Play Again- C  Quit - Q""", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        loopGame()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_increments
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_increments
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -block_increments
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = block_increments

        if x1 >= 500 or x1 < 0 or y1 >= 500 or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [food_x, food_y, 10, 10])
        head = []
        head.append(x1)
        head.append(y1)
        snake_List.append(head)
        if len(snake_List) > length_Of_Snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == head:
                game_close = True

        snake(block_increments, snake_List)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, 490)/10)*10
            food_y = round(random.randrange(0, 490)/10)*10
            length_Of_Snake += 1



        clock.tick(game_speed)

    pygame.quit()
    quit()

loopGame()