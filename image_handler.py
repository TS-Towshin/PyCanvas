import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Merge Images Example")

# Load the images
image1 = pygame.image.load("image1.png").convert_alpha()
image2 = pygame.image.load("image2.png").convert_alpha()

# Function to merge two images with a specific portion from each
def merge_images(image1, image2, portion_rect1, portion_rect2):
    merged_image = pygame.Surface((portion_rect1.width, portion_rect1.height), pygame.SRCALPHA)
    merged_image.blit(image1, (0, 0), portion_rect1)
    merged_image.blit(image2, (0, 0), portion_rect2)
    return merged_image

# Main loop
running = True

while running:
    screen.fill((255, 255, 255))  # Clear the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Define the portions of each image to be merged
    portion_rect1 = pygame.Rect(0, 0, 150, screen_height)
    portion_rect2 = pygame.Rect(150, 0, 850, screen_height)

    # Merge the images
    merged_image = merge_images(image1, image2, portion_rect1, portion_rect2)

    # Blit the merged image onto the screen
    screen.blit(merged_image, (0, 0))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
