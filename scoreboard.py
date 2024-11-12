import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """A class to report scoring information"""
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()
        self.prep_high_score()

        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"

        # Make a label for score
        score_title = "SCORE:"
        self.score_title_image = self.font.render(
            score_title, True, self.text_color, self.settings.bg_color
        )
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Dispaly the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

        # Display the score text to the left of the score
        self.score_title_rect = self.score_title_image.get_rect()
        self.score_title_rect.right = self.score_rect.left - 10
        self.score_title_rect.top = 20

    def show_score(self):
        """Draw scores, level and ships to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.score_title_image, self.score_title_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.high_score_text_image, self.high_score_text_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.level_text_image, self.level_text_rect)
        
        # Draw the single ship icon and the count of ships
        self.screen.blit(self.ship_icon, self.ship_icon_rect)
        self.screen.blit(self.ship_count_image, self.ship_count_rect)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color
        )

        high_score_text = "HIGH SCORE:"
        self.high_score_text_image = self.font.render(
            high_score_text, True, self.text_color, self.settings.bg_color
        )

        # Position the high score text just to the left of the high score
        self.high_score_text_rect = self.high_score_text_image.get_rect()
        self.high_score_text_rect.left = self.screen_rect.left + 20
        self.high_score_text_rect.top = self.score_rect.top

                # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.high_score_text_rect.right + 10  
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color
        )

        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

        level_text = "LEVEL"
        self.level_text_image = self.font.render(
            level_text, True, self.text_color, self.settings.bg_color
        )

        self.level_text_rect = self.level_text_image.get_rect()
        self.level_text_rect.right = self.level_rect.left - 10
        self.level_text_rect.top = self.level_rect.top

    def prep_ships(self):
        """Display one ship icon, an 'x', and the number of ships left."""
        # Create the "x" and count text
        ship_count_text = f"X {self.stats.ships_left}"
        self.ship_count_image = self.font.render(
            ship_count_text, True, self.text_color, self.settings.bg_color
        )

        # Position the count text just to the right of the ship icon
        self.ship_count_rect = self.ship_count_image.get_rect()
        self.ship_count_rect.right = self.level_rect.right  # Small gap between icon and text
        self.ship_count_rect.y = self.level_rect.y + 40

        # Load and position a single ship icon near the top-right
        original_ship_icon = pygame.image.load('images/bg_ship.png')
        self.ship_icon = pygame.transform.scale(original_ship_icon, (30, 30))
        self.ship_icon_rect = self.ship_icon.get_rect()
        self.ship_icon_rect.right = self.ship_count_rect.left - 10 # Adjust position as needed
        self.ship_icon_rect.y = self.ship_count_rect.y

        