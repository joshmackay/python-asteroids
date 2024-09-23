from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += (self.velocity * dt)

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      random_angle = random.uniform(20, 50)
      vec1 = self.velocity.rotate(random_angle)
      vec2 = self.velocity.rotate(-random_angle)
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
      new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
      new_ast_1.velocity = vec1 * 1.2
      new_ast_2.velocity = vec2 * 1.2