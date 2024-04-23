import pygame
import pygame.freetype

class Info:
    def __init__(self, info, x, y, width, height):
        self.info = info
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        pygame.freetype.init()
        self.font = pygame.freetype.SysFont("Arial", 20)
    
    def draw(self, screen):
        outline_rect = pygame.Rect(self.x - 2, self.y - 2, self.width + 4, self.height + 4)
        background_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Draw outline and background
        pygame.draw.rect(screen, (0, 0, 0), outline_rect)
        pygame.draw.rect(screen, (255, 255, 255), background_rect)

        # Split text into multiple lines to fit within the box
        lines = self.wrap_text(self.info, self.width - 10)

        # Render each line of text surface
        text_surfaces = []
        for line in lines:
            text_surface, _ = self.font.render(line, (0, 0, 0))  # Render text in black color
            text_surfaces.append(text_surface)

        # Calculate total height of all text lines
        total_height = sum(text_surface.get_height() for text_surface in text_surfaces)

        # Calculate starting y position to center the text vertically within the box
        text_y = self.y + (self.height - total_height) // 2

        # Blit text surfaces onto the screen
        for text_surface in text_surfaces:
            # Calculate text position to center it horizontally within the box
            text_x = self.x + (self.width - text_surface.get_width()) // 2
            screen.blit(text_surface, (text_x, text_y))
            # Update y position for the next line
            text_y += text_surface.get_height()  # Move down by the height of the current line

    def wrap_text(self, text, max_width):
        """Wrap text into multiple lines to fit within the given width."""
        words = text.split()
        lines = []
        current_line = ""
        for word in words:
            # Check if adding the word exceeds the max width
            if self.font.get_rect(current_line + " " + word).width <= max_width:
                # Add the word to the current line
                if current_line:
                    current_line += " "
                current_line += word
            else:
                # Start a new line with the word
                lines.append(current_line)
                current_line = word
        # Add the last line
        lines.append(current_line)
        return lines