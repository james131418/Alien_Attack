import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(f_settings, screen, fighter, bullets):
    """Respond to event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, f_settings, screen, fighter, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, fighter)



def check_keydown_events(event, f_settings, screen, fighter, bullets):
    """respond to keypress"""
    if event.key == pygame.K_RIGHT:
        # Move the fighter to the right.
        fighter.move_right = True
    elif event.key == pygame.K_LEFT:
        # Move the fighter to the left.
        fighter.move_left = True
    elif event.key == pygame.K_UP:
        # Move up the fighter
        fighter.move_up = True
    elif event.key == pygame.K_DOWN:
        # Move down the fighter
        fighter.move_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(f_settings, screen, fighter, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def check_keyup_events(event, fighter):
    """respond to keyreleases"""
    if event.key == pygame.K_RIGHT:
        fighter.move_right = False
    elif event.key == pygame.K_LEFT:
        fighter.move_left = False
    elif event.key == pygame.K_UP:
        fighter.move_up = False
    elif event.key == pygame.K_DOWN:
        fighter.move_down = False

def screen_update(f_settings, screen, fighter, bullets, aliens):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(f_settings.screen_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    fighter.blitme()
    aliens.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets"""
    """Update bullets position"""
    bullets.update()

    """Get rid of bullets out of screen"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(f_settings, screen, fighter, bullets):
    """Fire a bullet if the limit is not reached"""
    """Create new bullets"""
    if len(bullets) <= f_settings.bullet_allowed:
        fired_bullet = Bullet(f_settings, screen, fighter)
        bullets.add(fired_bullet)

def create_fleet(f_settings, screen, aliens):
    """Create a full fleet of aliens"""
    """Create an alien and find the number of aliens in a row"""
    """Spaceing between aliens"""
    alien = Alien(f_settings, screen)
    alien_width = alien.rect.width
    availabe_space_x = f_settings.screen_width - 2 * alien_width
    number_aliens_x = availabe_space_x / (2 * alien_width)

    # Create the first row of aliens
    for alien_number in range(number_aliens_x):
        alien = Alien(f_settings, screen)
        alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)