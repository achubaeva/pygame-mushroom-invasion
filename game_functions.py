import sys
import pygame
from bullet import Bullet
from mushroom import Mushroom

def get_number_mushrooms_x(settings, mushroom_width):
    '''Determine the number of mushrooms that fit in a row'''
    available_space_x = settings.screen_width - 2 * (mushroom_width)
    number_mushrooms_x = int(available_space_x / (2* mushroom_width))
    return number_mushrooms_x 

def create_mushroom(settings, screen, mushrooms, mushroom_number, row_number):
    '''Create a mushroom and place it in the row.'''
    mushroom = Mushroom(settings, screen)
    mushroom_width = mushroom.rect.width
    mushroom.x = mushroom_width + 2 * mushroom_width * mushroom_number
    mushroom.rect.x = mushroom.x
    
    mushroom.rect.y = mushroom.rect.height + 2 * mushroom.rect.height * row_number
    
    mushrooms.add(mushroom)


def check_keydown_events(event, settings, screen, snail, bullets):
    if event.key == pygame.K_RIGHT:
        # Move the snail to the right.
        snail.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the snail to the left.
        snail.moving_left = True
    elif event.key == pygame.K_UP:
        fire_bullet(settings, screen, snail, bullets)
    elif event.key == pygame.K_q:
            pygame. quit()
            sys.exit

def fire_bullet(settings, screen, snail, bullets):
    '''Fire a bullet if limit not reached yet.'''
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < settings.bullets_allowed:
            new_bullet = Bullet(settings, screen, snail)
            bullets.add(new_bullet)

def check_keyup_events(event, snail):
    if event.key == pygame.K_RIGHT:
        snail.moving_right = False
    elif event.key == pygame.K_LEFT:
        snail.moving_left = False

def check_events(settings, screen, snail, bullets):
    '''Respond to keypresses and mouse events.'''
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, snail, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, snail)
        

def update_screen(settings, screen, snail, mushrooms, bullets):
    """Update images on the screen and flip to new screen."""
    # Redraw the screen during each pass through the loop
    screen.fill(settings.bg_color)
    
    # Redraw all bullets behind snail and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    snail.blitme()
    mushrooms.draw(screen)
    # Make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    '''Update the position of bullets and get rid of old bullets.'''
    # update bullet positions.
    # Get rid of bullets that have dissappeared.
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)

def create_fleet(settings, screen, snail, mushrooms):
    '''Create fleet of mushrooms.'''
    # Create a mushroom and find the number of mushrooms in a row.
    # Spacing between each mushroom is equal to 1/2 mushroom width.
    mushroom = Mushroom(settings, screen)
    number_mushrooms_x = get_number_mushrooms_x(settings, mushroom.rect.width)
    number_rows = get_number_rows(settings, snail.rect.height, mushroom.rect.height)

    # Create the fleet of mushrooms.
    for row_number in range(number_rows):
        # Create the first row of mushrooms.
        for mushroom_number in range(number_mushrooms_x):
            # Create a mushroom and place it in the row
            create_mushroom(settings, screen, mushrooms, mushroom_number, row_number)

    

        

def get_number_rows(settings, snail_height, mushroom_height):
    '''Determine the number of rows of mushrooms that fit on the screen.'''
    available_space_y = (settings.screen_height - (3*mushroom_height)-snail_height)
    number_rows = int(available_space_y / (2*mushroom_height))
    return number_rows