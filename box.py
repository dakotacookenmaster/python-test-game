import pygame

class Box:
    def __init__(self, surface, color, x, y, width, height, border=0):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border = border
        self.surface_width, self.surface_height = surface.get_size()

    def paint(self):
        pygame.draw.rect(self.surface, self.color, ((self.x, self.y), (self.width, self.height)), self.border)

    def tick(self):
        self.paint()

    def move_up(self, amount):
        if(self.y - amount > 0):
            self.y -= amount
        else:
            self.y = 0

    def move_down(self, amount):
        if(self.y + self.height + amount < self.surface_height):
            self.y += amount
        else:
            self.y = self.surface_height - self.height

    def move_right(self, amount):
        if(self.x + self.width + amount < self.surface_width):
            self.x += amount
        else:
            self.x = self.surface_width - self.width

    def move_left(self, amount):
        if(self.x - amount > 0):
            self.x -= amount
        else:
            self.x = 0


    