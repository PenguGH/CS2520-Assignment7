CS2520 Assignment 7
This is a group project with the team members Carter Phung, Justin Chung, and Shawn Arlantico.

Our primary roles were
Manager - Carter Phung
Coder - Justin Chung
Tester - Shawn Arlantico

However, due to the time constraints, we each contributed to the project by coding some tasks as well.

We have refactored this project as well as implemented the following new features.
1. Implement various types of projectiles. 
Carter Phung has realized this task by having the shell projectile change size randomly each time it is shot from the cannon by using the change_size function which randomly chooses a radius length in a range of numbers.

2. Develop several target types with different movement patterns.
Shawn Arlantico has realized this task by having the targets use a bullseye apperance as well as having the targets move in different directions. The targets also vary in size. Some targets are stationary and others have varying movement patterns.

3. Transform the cannon into a moving tank.
Carter Phung has realized this task by implementing a wasd character controller that allows the player to freely move and control the tank.

4. Create "bombs" that will be dropped by targets onto the cannon.
Justin Chung has realized this by having the targets drop bombs periodically onto the cannon.

5. Implement multiple cannons that can shoot at each other.
Justin Chung has realized this by having blue cannons that are moving around that shoot projectiles periodically.

We have also reorganized the code and files and they are now in modules. Check the components folder to see how we used modular programming to seperate each major component into their own python file with their own classes. We seperated cannon, enemy_cannon, game_object, my_colors, score_table, settings, and target into their own files.

How to use this program.
Run the main.py python file in order to use this program.
Use the wasd keys to control the character, press down and hold the left mouse key to charge up projectiles, press down the left mouse key to shoot projectiles.
The goal of the game is to try to get the highest total score that you can.
