# Asteroids Game

A classic Asteroids arcade game implemented in Python using Pygame.

## Description

This is a recreation of the classic Asteroids arcade game where you control a spaceship and must destroy asteroids while avoiding collisions. The game features:

- Player-controlled spaceship with rotation and thrust mechanics
- Randomly spawning asteroids of different sizes
- Shooting mechanics to destroy asteroids
- Collision detection between player, asteroids, and shots
- Asteroid splitting mechanics when destroyed

## Prerequisites

- Python 3.x
- Pygame 2.6.1

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

Run the game with:
```bash
python main.py
```

## Controls

- **Arrow Keys / WASD**: Rotate and move the spaceship
- **Spacebar**: Shoot
- **Close Window**: Quit the game

## Game Rules

- Destroy asteroids by shooting them
- Large asteroids split into smaller ones when hit
- Avoid colliding with asteroids - collision ends the game
- Asteroids continuously spawn from the edges of the screen

## Project Structure

- `main.py` - Main game loop and initialization
- `player.py` - Player spaceship class with movement and shooting
- `asteroid.py` - Asteroid class with movement and collision
- `asteroidfield.py` - Manages asteroid spawning and splitting
- `shot.py` - Bullet/projectile class
- `circleshape.py` - Base class for circular game objects
- `constants.py` - Game configuration constants

## Game Configuration

The game can be customized by modifying values in `constants.py`:

- Screen dimensions: 1280x720 pixels
- Player speed and turn rate
- Asteroid spawn rate and sizes
- Bullet speed and cooldown

## Features

- Smooth 60 FPS gameplay
- Vector-based movement and rotation
- Sprite group management for efficient collision detection
- Modular object-oriented design

## License

This project is open source and available under the MIT License.