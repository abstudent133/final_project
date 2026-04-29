import pygame
import json

#screen.blit(text, (x, y))


pygame.init()

screen_x = 1320
screen_y = 960
font = pygame.font.SysFont("Arial", 12)
fullscreen = False

def draw_face():

    screen = pygame.display.set_mode((screen_x, screen_y))
    clock = pygame.time.Clock()

    drawing = False
    radius = 3
    current_stroke = []
    strokes = []
    stroke_color = "white"

    def draw_line(surface, color, points, radius):
        if len(points) > 1:
            pygame.draw.lines(surface, color, False, points, radius * 2)

    def redraw(surface):
        surface.fill("black")
        for stroke in strokes:
            draw_line(surface, stroke_color, stroke, radius)

    def save_strokes(strokes, filename = "docs/face.json"):
        with open(filename, "w") as f:
            json.dump(strokes, f)

    def load_strokes(filename = "docs/face.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                return [[tuple(point) for point in stroke] for stroke in data]
        except FileNotFoundError:
            print("No saved file found.")
            return []

    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                mods = pygame.key.get_mods()

                if event.key == pygame.K_z and mods & pygame.KMOD_CTRL:
                    if strokes:
                        strokes.pop()

                elif event.key == pygame.K_F11:
                    if fullscreen == False:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        fullscreen == True
                    elif fullscreen == True:
                        screen = pygame.display.set_mode((screen_x, screen_y))
                        fullscreen == False

                elif event.key == pygame.K_s and mods & pygame.KMOD_CTRL:
                    save_strokes(strokes)

                elif event.key == pygame.K_l and mods & pygame.KMOD_CTRL:
                    strokes = load_strokes()

                elif event.key == pygame.K_c and mods & pygame.KMOD_CTRL:
                    text = ""
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                            show_text = font.render(text, True, ("red"))
                            screen.blit(show_text, (screen_x / 2, screen_y / 2))
                        if event.key == pygame.K_RETURN:
                            pass
                        else:
                            text += event.unicode
                            show_text = font.render(text, True, ("red"))
                            screen.blit(show_text, (screen_x / 2, screen_y / 2))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                current_stroke = [event.pos]

            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                if current_stroke:
                    strokes.append(current_stroke)
                current_stroke = []

            elif event.type == pygame.MOUSEMOTION and drawing:
                current_stroke.append(event.pos)

        redraw(screen)

        if current_stroke:
            draw_line(screen, stroke_color, current_stroke, radius)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

draw_face()