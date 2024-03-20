import pygame
from canvas import Canvas
from menu_bar import Menu, Dropdown, Slider, Button
from file_handler import fileName

def main():
    WIDTH, HEIGHT = 1000, 700

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PyCanvas")
    canvas = Canvas(screen)

    clock = pygame.time.Clock()
    running = True

    # Initialize all the objects for menu bar
    menu = Menu(160, HEIGHT)
    brush_options = ["0", "1", "2", "3"]
    brush_size_slider = Slider("Brush Size", 15, 75, 130, 50)
    eraser_size_slider = Slider("Eraser Size", 15, 130, 130, 50)
    brush_type_dropdown = Dropdown("Brush Type", 15, 180, 130, 30, brush_options)

    # Initialize the buttons
    def buttons():        
        white_button = Button('white', 10, 340, 40, 30, 'color')
        blue_button = Button('blue', 60, 340, 40, 30, 'color')
        red_button = Button('red', 110, 340, 40, 30, 'color')
        yello_button = Button('yellow', 10, 380, 40, 30, 'color')
        green_button = Button('green', 60, 380, 40, 30, 'color')
        black_button = Button('black', 110, 380, 40, 30, 'color')
    
        clear_button = Button('gray', 40, 450, 60, 40, 'clear', 'Clear')

        buttons = [white_button, blue_button, red_button, yello_button, green_button, black_button, clear_button]
        return buttons

    buttons = buttons()
    menu_bar = False

    canvas.brush_size = brush_size_slider.calculateVal()
    canvas.eraser_size = eraser_size_slider.calculateVal()


    def renderButtons():
        for button in buttons:
            button.drawButton(screen)
            button.hoverEffect(screen, mouse_x, mouse_y)
            if button.text:
                button.renderText(screen)
        
    
    def buttonEvent():
        for button in buttons:
            if button.isClicked(mouse_x, mouse_y):
                if button.button_type == 'color':
                    canvas.brush_color = button.color
                elif button.button_type == 'clear':
                    canvas.clearScreen()

    def open_menu():
        menu.skeleton(screen)
        brush_type_dropdown.draw(screen, mouse_x, mouse_y)
        brush_size_slider.drawSlider(screen)
        eraser_size_slider.drawSlider(screen)
        renderButtons()

        if brush_size_slider.changed:
            canvas.brush_size = brush_size_slider.calculateVal()

        if eraser_size_slider.changed:
            canvas.eraser_size = eraser_size_slider.calculateVal()

    def menu_events():
        if event.type == pygame.MOUSEBUTTONDOWN:    # Assign the value from dropdown
            brush_type_dropdown.handle_event(event)
            if brush_type_dropdown.selected_option != None:
                canvas.brush_type = int(brush_type_dropdown.selected_option)

            buttonEvent()

        brush_size_slider.handleEvent(event, mouse_x, mouse_y)
        eraser_size_slider.handleEvent(event, mouse_x, mouse_y)

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_buttons = pygame.mouse.get_pressed()

            canvas_state = screen.copy()
            
            if not menu_bar:  
                canvas.drawOnClick(mouse_buttons, mouse_x, mouse_y)
                canvas.erase(mouse_buttons, mouse_x, mouse_y)

            elif not menu.rect.collidepoint(mouse_x, mouse_y):  # Check if drawing inside the menu
                canvas.drawOnClick(mouse_buttons, mouse_x, mouse_y)
                canvas.erase(mouse_buttons, mouse_x, mouse_y)

            if event.type == pygame.KEYDOWN:    # Reset the canvas when pressed R key
                if event.key == pygame.K_r:
                    canvas.clearScreen()

                if event.key == pygame.K_TAB:   # Open the menu when pressed TAB

                    if not menu_bar:
                        screen_under_menu = screen.subsurface((0, 0, menu.width, menu.height)).copy()
                    
                    menu_bar = not menu_bar

                    screen.blit(canvas_state, (0, 0))
                    screen.copy()

                    if not menu_bar:
                        screen.blit(screen_under_menu, (0, 0))

                if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:    # Save the image when pressed ctrl+s
                    pygame.image.save(screen, fileName("saved_images", 'png'))

            if menu_bar:
                menu_events()
                        
        if menu_bar:
            open_menu()

        pygame.display.update()

if __name__=='__main__':
    main()