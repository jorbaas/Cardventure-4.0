import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Button Example")

font = pygame.font.SysFont(None, 30)
button_surf = pygame.Surface((100, 50))
button_rect = button_surf.get_rect(center=(screen_width // 2, screen_height // 2))
button_text = font.render("Quit", True, BLACK)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos)):
            running = False

    button_surf.fill(WHITE)
    pygame.draw.rect(button_surf, BLACK, button_rect, 2)
    button_surf.blit(button_text, (15, 15))

    screen.fill(WHITE)
    screen.blit(button_surf, button_rect)
    pygame.display.update()

pygame.quit()
