import pygame

brush_type = 0      # value range --> 0-3
brush_size = 5
brush_color = 'white'
eraser_size = 20
bg_color = (40,40,40)

class Canvas:
    def __init__(self, screen, brush_type: int=brush_type, brush_size: float=brush_size, \
                brush_color: tuple | str=brush_color, eraser_size: int=eraser_size, \
                bg_color: tuple | str=bg_color) -> None:
        self.brush_types = [0, 1, 2, 3]
        self.brush_type = brush_type
        self.brush_size = brush_size
        self.brush_color = brush_color
        self.eraser_size = eraser_size
        self.bg_color = bg_color
        self.screen = screen
        screen.fill(bg_color)

    def drawOnClick(self, mouse_buttons, x, y) -> None:
        self.rect = pygame.Rect(x, y, self.brush_size, self.brush_size)

        if mouse_buttons[0]:
            '''paint when left mouse button is clicked'''

            match self.brush_type:
                case 0:
                    # Circle
                    pygame.draw.circle(self.screen, self.brush_color, (x, y), self.brush_size)

                case 1:
                    # Rectangle
                    pygame.draw.rect(self.screen, self.brush_color, self.rect)

                case 2:
                    # Hollow circle
                    pygame.draw.circle(self.screen, self.brush_color, (x, y), self.brush_size, 1)

                case 3:
                    # Hollow rectangle
                    pygame.draw.rect(self.screen, self.brush_color, self.rect, 1)

                case _:
                    # Circle
                    pygame.draw.circle(self.screen, self.brush_color, (x, y), self.brush_size)

    def erase(self, mouse_buttons, x, y) -> None:
        '''Erase around the cursor on right click'''
        if mouse_buttons[2]:
            pygame.draw.circle(self.screen, self.bg_color, (x, y), self.eraser_size)
    
    def clearScreen(self, screen) -> None:
        screen.fill(self.bg_color)
