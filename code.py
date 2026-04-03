import pygame

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

pygame.display.set_caption('ESCAPE')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((960,720))

bg = pygame.image.load('nền.png').convert_alpha()
bg = pygame.transform.scale2x(bg)

mouse = pygame.image.load('player.png').convert_alpha()
mouse = pygame.transform.scale(mouse,(50,50))
mouse = pygame.transform.rotate(mouse,0)                      #hướng

pygame.mouse.set_visible(False)

music = pygame.mixer.Sound('nhạc nền.mp3')
time_music = 0
music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg,(0,0))
    
    clock.tick(50)
    time_music += 0.02
    if time_music >= 229 :
        time_music = 0
        music.play()

    toa_do_mouse = pygame.mouse.get_pos()
    mouse_x = toa_do_mouse[0]
    mouse_y = toa_do_mouse[1]
    screen.blit(mouse,(mouse_x,mouse_y))

    pygame.display.update()

pygame.quit()
# fasdfsadf
