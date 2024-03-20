import pygame

pygame.init()

class Menu:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.color = (69, 69, 69)

    def skeleton(self, screen) -> None:
        '''Draw the main body of menu bar'''
        pygame.draw.rect(screen, self.color, (0, 0, self.width, self.height))
    

# Dropdown class was written by ChatGPT        
class Dropdown:
    def __init__(self, name: str, x: int, y: int, width: int, height: int, options: list, selected_option = None, color: str | tuple = 'gray') -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.name = name
        self.options = options
        self.selected_option = selected_option
        self.is_open = False
        self.font = pygame.font.Font(None, 32)
        self.color = color

    def draw(self, screen, mouse_x, mouse_y) -> None:
        pygame.draw.rect(screen, self.color, self.rect)
        
        # Hover effect for dropdown name
        if self.rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, (150, 150, 150), self.rect)
        
        # Border for dropdown
        pygame.draw.rect(screen, 'black', self.rect, 1)

        text = self.font.render(self.selected_option if self.selected_option else self.name, True, 'black')
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

        if self.is_open:
            for i, option in enumerate(self.options):
                option_rect = pygame.Rect(self.rect.x, self.rect.y + self.rect.height * (i + 1), self.rect.width, self.rect.height)

                # Hover effect for options
                if option_rect.collidepoint(mouse_x, mouse_y):
                    pygame.draw.rect(screen, (150, 150, 150), option_rect)
                
                else:
                    pygame.draw.rect(screen, self.color, option_rect)
                
                pygame.draw.rect(screen, (69, 69, 69), option_rect, 1)
                text = self.font.render(option, True, 'black')
                text_rect = text.get_rect(center=option_rect.center)
                screen.blit(text, text_rect)

    def handle_event(self, event) -> None:
            if self.rect.collidepoint(event.pos):
                self.is_open = not self.is_open
            if self.is_open:
                for i, option in enumerate(self.options):
                    option_rect = pygame.Rect(self.rect.x, self.rect.y + self.rect.height * (i + 1), self.rect.width, self.rect.height)
                    if option_rect.collidepoint(event.pos):
                        self.selected_option = option
                        self.is_open = False


class Slider:
    def __init__(self, name: str, x: int, y: int, width: int, range: int, color: str | tuple = 'gray') -> None:
        self.name = name
        self.range = range
        self.x = x
        self.y = y
        self.width = width
        self.current_pos = x
        self.rect = pygame.Rect(x, y, width, 50)
        self.mouse_hold = False
        self.end = x+width
        self.color = color

        pygame.init()
        self.font = pygame.font.Font(None, 28)
        self.calculateVal()
        self.changed = True

    def drawSlider(self, screen) -> None:
        slider_name = self.font.render(self.name, True, (255, 255, 255))
        screen.blit(slider_name, (self.x+10, self.y-30))

        pygame.draw.line(screen, 'white', (self.x, self.y), (self.end, self.y))

        self.pointer_rect = pygame.draw.circle(screen, 'white', (self.current_pos, self.y), 7)

    def calculateVal(self) -> int:
        value = (self.range/self.width)*self.current_pos
        if value < 1:
            value = 1
        
        return value

    def handleEvent(self, event, mouse_x, mouse_y) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.pointer_rect.collidepoint(mouse_x, mouse_y):
                self.mouse_hold = True

        if event.type == pygame.MOUSEBUTTONUP:
            self.mouse_hold = False
            self.changed = False

        if self.mouse_hold:
                dx = mouse_x-self.pointer_rect.x
                if mouse_x <= self.end and mouse_x > self.x-7:
                    self.current_pos += dx
                    self.calculateVal()
                    self.changed = True

    def hoverEffect(self, screen, mouse_x, mouse_y):
        if abs(self.current_pos-mouse_x) <= 7 and abs(self.y-mouse_y) <= 7:
            pygame.draw.circle(screen, ('white'), (self.current_pos, self.y), 8)

class Button:
    def __init__(self, color: str | tuple, x: int, y: int, width: int, height: int, button_type, text: str = None, border_color: str | tuple = (69, 69, 69)) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = color
        self.border_color = border_color
        self.button_type = button_type
        self.text = text
        self.font = pygame.font.Font(None, 28)
    
    def drawButton(self, screen) -> None:
        pygame.draw.rect(screen, self.color, self.rect)

    def hoverEffect(self, screen, mouse_x, mouse_y) -> None:
        if self.rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, self.border_color, self.rect, 1)
    
    def renderText(self, screen) -> None:
        button_text = self.font.render(self.text, True, 'black')
        text_rect = button_text.get_rect(center=self.rect.center)
        screen.blit(button_text, text_rect)
    
    def isClicked(self, mouse_x, mouse_y) -> bool:
        if self.rect.collidepoint(mouse_x, mouse_y):
            return True
        return False
