# Summary of the Obstacle Dodge Game
# Game Title: Obstacle Dodge Game

# Overview:
The Obstacle Dodge Game is a simple yet engaging arcade-style game built using Python and the Pygame library. Players control a car that must maneuver left and right to avoid falling obstacles from the top of the screen. The objective is to dodge these obstacles for as long as possible, while accumulating points for each successfully avoided obstacle.
# GamePlay Mechanics :
# Controls: 
Players use the left and right arrow keys to move the car horizontally across the bottom of the screen.
# Obstacles: 
Obstacles appear at random horizontal positions at the top of the screen and descend towards the player's car. If the car collides with an obstacle, the game ends.
# Scoring System: 
Players earn points each time an obstacle is successfully dodged. The score is displayed at the top left corner of the screen.
# Game Over: 
When a collision occurs, a "Game Over" message is displayed along with the final score for a brief period before the game closes.
# Visuals:
The game features a simple graphical interface with a white background, a blue car, and red obstacles. The score is displayed in blue text.

# Technical Details:
The game is implemented using Pygame, which handles graphics rendering, event management, and sound playback.
The main loop continuously checks for user input, updates the positions of the car and obstacles, and redraws the screen.

# Objective:
The primary goal is to achieve the highest score possible by dodging obstacles for as long as you can without colliding with them.

This game serves as a great introduction to game development with Python and can be further expanded with additional features like multiple obstacle types, levels of difficulty, or power-ups to enhance gameplay.
