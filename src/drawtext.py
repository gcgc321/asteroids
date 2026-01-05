
import pygame 


def draw_text(screen, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, "white")
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)