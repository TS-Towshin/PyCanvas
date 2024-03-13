import pygame

size = (1000, 700)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("PyCanvas")

class Canvas:
    def __init__(self, brush_type: int=1, brush_size: int=10, brush_color='white' , eraser_size: int = 20, bg_color = 'black') -> None:
        self.brush_types = ['circle', 'rectangle', 'hollow_circle', 'hollow_rectangle']
        self.brush_type = brush_type    # value range --> 0-3
        self.brush_size = brush_size
        self.brush_color = brush_color
        self.eraser_size = eraser_size
        self.bg_color = bg_color

    def drawOnClick(self):
        if mouse_buttons[0]:
            '''paint when left mouse button is clicked'''

            match self.brush_types[self.brush_type]:
                case 'circle':
                    pygame.draw.circle(screen, self.brush_color, (x, y), self.brush_size)

                case 'rectangle':
                    pygame.draw.rect(screen, self.brush_color, (x, y, self.brush_size, self.brush_size))

                case 'hollow_circle':
                    pygame.draw.circle(screen, self.brush_color, (x, y), self.brush_size, 1)

                case 'hollow_rectangle':
                    pygame.draw.rect(screen, self.brush_color, (x, y, self.brush_size, self.brush_size), 1)
    
    def erase(self):
        '''Erase around the cursor on right click'''
        if mouse_buttons[2]:
            pygame.draw.circle(screen, self.bg_color, (x, y), self.eraser_size)
    
    def clearScreen(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill(self.bg_color)

clock = pygame.time.Clock()
running = True

canvas = Canvas()

while running:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        x, y = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        canvas.drawOnClick()
        canvas.erase()
        canvas.clearScreen()

    pygame.display.update()
