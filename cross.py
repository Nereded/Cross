import pygame


def draw_diagonal(screen, color, start, end, width):
    pygame.draw.line(screen, color, start, end, width)


def main():
    try:
        width, height = map(int, input().split())
    except ValueError:
        print("Неправильный формат ввода")
        return
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Крест")
    line_color = (255, 255, 255)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        draw_diagonal(screen, line_color, (0, 0), (width, height), 5)
        draw_diagonal(screen, line_color, (0, height), (width, 0), 5)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
