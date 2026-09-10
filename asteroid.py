import random

import pygame  # pyright: ignore[reportMissingImports]

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white", self.position , self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self,) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            rotated_vector1 = self.velocity.rotate(angle)
            rotated_vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x,self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x,self.position.y, new_radius)
            asteroid1.velocity = rotated_vector1 *1.2
            asteroid2.velocity = rotated_vector2 *1.2
