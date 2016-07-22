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

def update_bullets(f_settings, screen, fighter, bullets, aliens):
    """Update position of bullets and get rid of old bullets"""
    """Update bullets position"""
    bullets.update()

    """Get rid of bullets out of screen"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(f_settings, screen, fighter, bullets, aliens)

def update_aliens(f_settings, aliens, fighter):
    """Check if the fleet is at the edge and update aliens position"""
    check_fleet_edges(f_settings, aliens)
    aliens.update(f_settings)

    #If aliens collide with fighter, end the game
    if pygame.sprite.spritecollideany(fighter, aliens):
        print "Fighter hit !!"

def fire_bullets(f_settings, screen, fighter, bullets):
    """Fire a bullet if the limit is not reached"""
    """Create new bullets"""
    if len(bullets) <= f_settings.bullet_allowed:
        fired_bullet = Bullet(f_settings, screen, fighter)
        bullets.add(fired_bullet)

def create_fleet(f_settings, screen, aliens, fighter):
    """Create a full fleet of aliens"""
    """Create an alien and find the number of aliens in a row"""
    """Spaceing between aliens"""
    alien = Alien(f_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    fighter_height = fighter.rect.height
    number_aliens_x = get_number_alien_x(f_settings, alien_width)
    number_alien_row = get_number_alien_row(f_settings, alien_height, fighter_height)

    # Create the fleet of aliens
    for row_number in range(number_alien_row):
        for alien_number in range(number_aliens_x):
            create_aliens(f_settings, screen, aliens, alien_number, row_number)


def get_number_alien_x(f_settings, alien_width):
    """Determine the number of aliens that fit in row"""
    availabe_space_x = f_settings.screen_width - 2 * alien_width
    number_aliens_x = availabe_space_x / (2 * alien_width)
    return number_aliens_x

def create_aliens(f_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row"""
    alien = Alien(f_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_alien_row(f_settings, alien_height, fighter_height):
    """Determine the number of row of aliens that fit in the screen"""
    available_space_y = f_settings.screen_height - fighter_height - 3 * alien_height
    number_rows = available_space_y / (2 * alien_height)
    return number_rows

def check_fleet_edges(f_settings, aliens):
    """Respond correctly when reach the edge"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(f_settings, aliens)
            break

def change_fleet_direction(f_settings, aliens):
    """Drop the entire fleet and change the fleet direction"""
    for alien in aliens.sprites():
        alien.rect.y += f_settings.fleet_drop_speed
    f_settings.fleet_direction *= -1

def check_bullet_alien_collision(f_settings, screen, fighter, bullets, aliens):
    # Check if bullets collide with aliens
    # If so, get rid of both
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # Repopulate the fleet of aliens
    if len(aliens) == 0:
        # Get rid of all bullets once aliens are all destroyed
        bullets.empty()
        # regenerate aliens
        create_fleet(f_settings, screen, aliens, fighter)