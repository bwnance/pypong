import pygame
import math

pygame.init()

screen = pygame.display.set_mode([800,800])
height, width = pygame.display.get_surface().get_size()
running = True
i = 0
c = 0
lpd = 0
rpd = 0
ball_size = 10
ball_pos = [400,400]
starting_dx = -5
b_dx = starting_dx
b_dy = 0
left_paddle = pygame.Rect(0, height/2 - 30, 15,75)
right_paddle = pygame.Rect(width - 15, height/2 - 30, 15,75)
won = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        lpd = -7
    if keys[pygame.K_s]:
        lpd = 7
    if keys[pygame.K_UP]:
        rpd = -7
    if keys[pygame.K_DOWN]:
        rpd = 7                 
    if c < 1000:
        c += 1
        continue
    else:
        c = 0
    if left_paddle.y + left_paddle.height + lpd >= height or left_paddle.y + lpd <= 0:
        lpd = 0
    if right_paddle.y + right_paddle.height + rpd >= height or right_paddle.y + rpd <= 0:
        rpd = 0
    left_paddle = left_paddle.move(0, lpd)
    right_paddle = right_paddle.move(0, rpd)

    screen.fill((0,0,0))



    bx, by = ball_pos


    ball_pos_height_top = by - ball_size
    ball_pos_height_bottom = by + ball_size
    ball_pos_width_left = bx - ball_size
    ball_pos_width_right = bx + ball_size

    left_paddle_top = left_paddle.y
    left_paddle_bottom = left_paddle.y + left_paddle.height
    left_paddle_x = left_paddle.x + left_paddle.width
    
    right_paddle_top = right_paddle.y
    right_paddle_bottom = right_paddle.y + right_paddle.height
    right_paddle_x = right_paddle.x

    if (ball_pos_width_left <= left_paddle_x and ball_pos_height_top >= left_paddle_top - ball_size and ball_pos_height_bottom <= left_paddle_bottom + ball_size):
        b_dx *= -1
        b_dy = b_dy if lpd == 0 else b_dy + lpd
    if (ball_pos_width_right > right_paddle_x and ball_pos_height_top >= right_paddle_top - ball_size and ball_pos_height_bottom <= right_paddle_bottom + ball_size):
        b_dx *= -1
        b_dy = b_dy if rpd == 0 else b_dy + rpd

    if bx + ball_size >= width or bx - ball_size <= 0:
       won = True
    if by + ball_size >= height or by - ball_size <= 0:
        b_dy = b_dy * -1

    
    if b_dy > 10:
        b_dy = 10
    bx = bx+b_dx
    by = by+b_dy
    ball_pos = [bx,by]
    lpd = 0
    rpd = 0


    if won:
        ball_pos = [400,400]
        starting_dx *= -1
        b_dx = starting_dx
        b_dy = 0
        won = False
        left_paddle.y = height/2 - 30
        right_paddle.y = height/2 - 30

    

    pygame.draw.circle(screen, (255, 255, 255), ball_pos, ball_size)
    pygame.draw.rect(screen, (255, 255, 255), left_paddle)
    pygame.draw.rect(screen, (255, 255, 255), right_paddle)
    pygame.display.flip()
pygame.quit()