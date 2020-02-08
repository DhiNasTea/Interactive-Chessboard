import pygame
import parametres as p


settings = p.Settings()
def show_rule(screen, piece):
    """Show the rule of the piece that was't moved correctly."""
    name_file = "images_2/" + piece + '_regles.png'
    rule = pygame.image.load(name_file).convert_alpha()
    rect = rule.get_rect()
    rect.centerx, rect.top = settings.rules_centerx, settings.rules_topy
    screen.blit(rule, rect)


