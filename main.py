import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0


  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updateable, drawable)
  AsteroidField.containers = updateable
  asteroid_field = AsteroidField()

  Player.containers = (updateable, drawable)
  player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT / 2)

  Shot.containers = (shots, updateable, drawable)

  while(1):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    screen.fill("black")

    for item in updateable:
      item.update(dt)
    
    for item in asteroids:
      if player.has_colided(item):
        print("Game over!")
        exit()
      for shot in shots:
        if item.has_colided(shot):
          item.split()
          shot.kill()

    for item in drawable:
      item.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()