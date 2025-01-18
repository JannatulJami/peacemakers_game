
#Jannatul Jami
#Period 1 and 2
# 1/17/2025
import simplegui
import random

#Teh width and teh ehight
width = 600
height = 600

# Room states
room1 = True 
room2 = False
room3 = False
frame = None

# Character variables
char_x = width // 2 
char_y = height - 100
char_health = 10
char_score = 0
twinkle_frame = 0

#To see if the game is over and if teh player won or loss
victory = False
game_over = False

# Inventory
char_inventory = []

# Asteroid variables (using lists instead of class)
asteroid_x = []  # List of x positions
asteroid_y = []  # List of y positions
asteroid_speed = []  # List of speeds
asteroid_size = []  # List of sizes

#To create the astroids
def create_asteroid():
    asteroid_x.append(random.randint(0, width))
    asteroid_y.append(0)
    asteroid_speed.append(random.randint(3, 7))
    asteroid_size.append(random.randint(10, 25))

 To change teh rooms based on the stats
def check_room_progression():
    global room1, room2, room3, char_score, victory, game_over
    
    if char_health <= 0:
        game_over = True
        return
        
    if char_score >= 70:
        victory = True
    elif char_score >= 50:
        room1 = False
        room2 = False
        room3 = True
    elif char_score >= 30:
        room1 = False
        room2 = True
        room3 = False

#To create astroids in room1 only
def spawn_asteroid():
    if room1 and random.random() < 0.03:  # 3% chance each frame
        create_asteroid()

def update_asteroids():
    global char_health
    
    # Update each asteroid
    for i in range(len(asteroid_y) - 1, -1, -1):
        asteroid_y[i] += asteroid_speed[i]
        
        # Check if asteroid is off screen
        if asteroid_y[i] > height:
            del asteroid_x[i]
            del asteroid_y[i]
            del asteroid_speed[i]
            del asteroid_size[i]
            continue
            
        # Check collision with player
        distance = ((asteroid_x[i] - char_x) ** 2 + (asteroid_y[i] - char_y) ** 2) ** 0.5
        if distance < (asteroid_size[i] + 15):
            char_health -= 5
            del asteroid_x[i]
            del asteroid_y[i]
            del asteroid_speed[i]
            del asteroid_size[i]
            check_room_progression()
#Room 1 drawing
def room1_drawing(canvas):
    canvas.draw_polygon([(0, 0), (width, 0), 
                        (width, height), (0, height)], 1, "white", "#AF958F")
    canvas.draw_polygon([(0, height), (0, 530), (width, 530), (width, height)], 1, "black", "#725E59")
    canvas.draw_polygon([(400, 200), (510, 200), (510, 530), (400, 530)], 1, "black", "#725E59")
    
    # Draw asteroids
    for i in range(len(asteroid_x)):
        canvas.draw_circle((asteroid_x[i], asteroid_y[i]), asteroid_size[i], 1, "gray", "brown")
#Room 2 drawing 
def room2_drawing(canvas):
    canvas.draw_polygon([(0, 0), (width, 0), 
                        (width, height), (0, height)], 1, "white", "#ebc4f0")
    canvas.draw_polygon([(0, height), (0, 530), (width, 530), (width, height)], 1, "black", "#735e50")
    canvas.draw_polygon([(300, 200), (510, 200), (510, 530), (300, 530)], 1, "black", "#dad2e3")
    for i in range(0, 200, 25):
        canvas.draw_polygon([(i + 305, 235), (i + 315, 235), (i + 315,  255), (i + 305,  255)], 1, "black", "#fffbd9")
        canvas.draw_polygon([(i + 305, 285), (i + 315, 285), (i + 315,  305), (i + 305,  305)], 1, "black", "#fffbd9")
        canvas.draw_polygon([(i + 305, 335), (i + 315, 335), (i + 315,  355), (i + 305,  355)], 1, "black", "#fffbd9")
        canvas.draw_polygon([(i + 305, 385), (i + 315, 385), (i + 315,  405), (i + 305,  405)], 1, "black", "#fffbd9")
        canvas.draw_polygon([(i + 305, 435), (i + 315, 435), (i + 315,  455), (i + 305,  455)], 1, "black", "#fffbd9")
        canvas.draw_polygon([(i + 305, 485), (i + 315, 485), (i + 315,  505), (i + 305,  505)], 1, "black", "#fffbd9")
#room3 drawing 
def room3_drawing(canvas):
    canvas.draw_polygon([(0, 0), (width, 0), 
                        (width, height), (0, height)], 1, "white", "#ffcde2")
    canvas.draw_polygon([(0, height), (0, 530), (width, 530), (width, height)], 1, "black", "#FFF5F3")
    canvas.draw_polygon([(300, 250), (510, 250), (510, 530), (300, 530)], 1, "black", "#c496a9")
    canvas.draw_circle((470, 100), 40, 1, "black", "#ff60a2")

 #to create everything about the game and put it all together and make it appear in teh frame
def draw(canvas):
    global twinkle_frame
    
    if game_over:
        canvas.draw_text("Game Over!", (width//2 - 100, height//2), 50, "red")
        canvas.draw_text("Press 'R' to restart", (width//2 - 80, height//2 + 50), 30, "white")
        return
        
    if victory:
        canvas.draw_text("You Win!", (width//2 - 70, height//2), 50, "green")
        return
    
    if room1:
        room1_drawing(canvas)
        spawn_asteroid()
        update_asteroids()
    elif room2:
        room2_drawing(canvas)
    elif room3:
        room3_drawing(canvas)
    
    # Draw character
    canvas.draw_circle((char_x, char_y), 15, 2, "#da9cb6", "#d8a9de")
    
    # Draw stats
    canvas.draw_text("Health: " + str(char_health), (10, 20), 20, "white")
    canvas.draw_text("Score: " + str(char_score), (10, 50), 20, "white")
    
    # Draw inventory
    canvas.draw_text("Inventory:", (10, 80), 20, "white")
    y_offset = 100
    for item in char_inventory:
        canvas.draw_text("- " + item, (10, y_offset), 20, "white")
        y_offset += 20

        #To use the keys to move the game
def keydown(key):
    global char_x, char_y, game_over, char_health, char_score
    global room1, room2, room3, asteroid_x, asteroid_y, asteroid_speed, asteroid_size
    
    if game_over and key == simplegui.KEY_MAP['r']:
            # Reset game
            char_health = 10
            char_score = 0
            char_x = width // 2
            char_y = height - 100
            # To create astroids 
            asteroid_x = []
            asteroid_y = []
            asteroid_speed = []
            asteroid_size = []
            #To click on differnet rooms
            room1 = True
            room2 = False
            room3 = False
            game_over = False
            return
    # To see if the player wins or no
    if victory or game_over:
        return
    #To use thje keys to move the character   
    if key == simplegui.KEY_MAP["up"] and char_y > 15:
        char_y -= 10
    elif key == simplegui.KEY_MAP["down"] and char_y < height - 15:
        char_y += 10
    elif key == simplegui.KEY_MAP["left"] and char_x > 15:
        char_x -= 10
    elif key == simplegui.KEY_MAP["right"] and char_x < width - 15:
        char_x += 10
#To see if a certain item is already in teh inventory and if nit it will be added
def add_item(item):
    if item not in char_inventory:
        char_inventory.append(item)
        print("Added " + item + " to inventory!")

#To increase teh score 
def increase_score(amount):
    global char_score
    char_score += amount
    check_room_progression()
#to be able to use the health poition if you find it
def use_item(item):
    global char_health
    if item == "Health Potion!":
        if item in char_inventory:
            char_health += 15
            char_inventory.remove(item)
            print("You used a Health Potion and restored 10 health!")
        else:
            print("You don't have a health potion")
#To find something radnom that either increases or decreases your points
def explore_room():
    global char_health, char_score
    
    #To see if you ended the game yet
    if victory or game_over:
        return
    #to find something random based on a random number
    #This will either increase or decrease your score
    event = random.randint(1, 6)
    if event == 1:
        add_item("Health Potion!")
        print("Found a Health Potion!")
    elif event == 2:
        print("Found treasure! +10 points!")
        increase_score(10)
    elif event == 3:
        print("Defeated an enemy! +15 points!")
        increase_score(15)
    elif event == 4:
        print("Found a gem! +5 points!")
        increase_score(5)
    elif event == 5:
        if char_health > 0:
            char_health -= 5
            print("Took damage! -5 health!")
    
    check_room_progression()
#To use itek in the health potion    
def use_health_potion():
    use_item("Health Potion!")
#The room 1 button function    
def toggle_room1():
    global room1, room2, room3
    room1 = True
    room2 = False
    room3 = False
    
#The room 2 button function
def toggle_room2():
    global room1, room2, room3
    room1 = False
    room2 = True
    room3 = False
#The room 3 button function
def toggle_room3():
    global room1, room2, room3
    room1 = False
    room2 = False
    room3 = True
#To create the buttons and the game appear
def create_frame():
    global frame
    frame = simplegui.create_frame("Final project", width, height)
    frame.set_draw_handler(draw)
    frame.set_keydown_handler(keydown)
    frame.add_button("1st room", toggle_room1, 150)
    frame.add_button("2nd room", toggle_room2, 150)
    frame.add_button("3rd room", toggle_room3, 150)
    frame.add_button("Use Health Potion", use_health_potion, 150)
    frame.add_button("Explore Room", explore_room, 150)
    frame.start()

create_frame()

