import pygame
import json


pygame.init()

def draw_face():

    screen = pygame.display.set_mode((1320, 960))
    clock = pygame.time.Clock()

    drawing = False
    radius = 3
    current_stroke = []
    strokes = []

    def draw_line(surface, color, points, radius):
        if len(points) > 1:
            pygame.draw.lines(surface, color, False, points, radius * 2)

    def redraw(surface):
        surface.fill("black")
        for stroke in strokes:
            draw_line(surface, "white", stroke, radius)

    def save_strokes(strokes, filename="docs/face.json"):
        with open(filename, "w") as f:
            json.dump(strokes, f)

    def load_strokes(filename="docs/face.json"):
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

                elif event.key == pygame.K_s and mods & pygame.KMOD_CTRL:
                    save_strokes(strokes)

                elif event.key == pygame.K_l and mods & pygame.KMOD_CTRL:
                    strokes = load_strokes()

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
            draw_line(screen, "white", current_stroke, radius)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

draw_face()