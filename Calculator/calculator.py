import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
width, height = 400, 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Calculator")

# Colors and Fonts
gray = (128, 128, 128)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
Font = pygame.font.SysFont(None, 44)

# Button Grid
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
]

text = ""

def draw_buttons():
    button_w = width // 4
    button_h = (height - height // 6) // 4  # Area below the text box divided by 4

    for row in range(4):
        for col in range(4):
            x = col * button_w
            y = height // 6 + row * button_h
            pygame.draw.rect(screen, white, (x, y, button_w, button_h))
            pygame.draw.rect(screen, black, (x, y, button_w, button_h), 2)
            text_surface = Font.render(buttons[row][col], True, black)
            text_rect = text_surface.get_rect(center=(x + button_w // 2, y + button_h // 2))
            screen.blit(text_surface, text_rect)

def get_button(pos):
    x, y = pos
    if y < height // 6:
        return None
    button_w = width // 4
    button_h = (height - height // 6) // 4
    row = (y - height // 6) // button_h
    col = x // button_w
    if 0 <= row < 4 and 0 <= col < 4:
        return buttons[int(row)][int(col)]
    return None

def draw_text():
    pygame.draw.rect(screen, gray, (0, 0, width, height // 6))
    text_surface = Font.render(text, True, red)
    text_rect = text_surface.get_rect(center=(width // 2, height // 12))
    screen.blit(text_surface, text_rect)

# Main Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            btn = get_button(pygame.mouse.get_pos())
            if btn:
                if btn == "C":
                    text = ""
                elif btn == "=":
                    try:
                        text = str(eval(text))
                    except:
                        text = "Error"
                else:
                    text += btn

    screen.fill(white)
    draw_text()
    draw_buttons()
    pygame.display.update()

pygame.quit()
