grid_rows = 2
grid_cols = 2
ball_diameter = 50
goal_size = 100
background_img = None 

player_x = 0
player_y = 0
face_animation_frame = 0
player_scale = 2.0  # Adjust the scale factor as needed

ball_x = 0
ball_y = 0
ball_speed_y = 10  # Vertical speed for bouncing effect
gravity = 0.1  # Gravity to simulate a bouncing effect

bouncing = False  # Flag to indicate whether the ball should bounce

def setup():
    size(800, 500)  # Adjust the size based on your preferences
    global background_img
    background_img = loadImage("download (6).jpeg")
    global ball_speed_x, ball_speed_y
    ball_speed_x = 0
    ball_speed_y = 0

def draw():
    global ball_x, ball_y, ball_speed_y, bouncing

    background(200, 200, 200)  # Fill the background with a light gray color (adjust as needed)

    cell_width = width // grid_cols
    cell_height = height // grid_rows
    # Draw grid lines
    for i in range(1, grid_cols):
        line(i * cell_width, 0, i * cell_width, height)
    for j in range(1, grid_rows):
        line(0, j * cell_height, width, j * cell_height)

    # Draw shapes and images in each portion
    draw_goal(0, 0, cell_width, cell_height)  # Top-left portion for the goal with a green background

    # Add other shapes or details for the other portions as needed
  # Fixed ball in the third section

    # Draw cartoonish football player and ball in the second portion with the same background as the first portion
    draw_football_player_with_ball1(cell_width, 0, cell_width, cell_height, background_img)

    # Draw the same design in the third portion
    draw_football_player_with_ball2(0, cell_height, cell_width, cell_height, background_img)

    # Draw celebration only in the fourth portion
    if cell_width < mouseX < 2*cell_width and cell_height < mouseY < height:
        winning_celebration(cell_width, cell_height, cell_width, cell_height, background_img)

def draw_goal(x, y, width, height):
    # Draw green background for the goal portion
    fill(0, 255, 0)
    rect(x, y, width, height)

    # Draw a background image
    image(background_img, x, y, width, height)
    draw_fixed_ball(x + width / 2, y + height / 2+100)

def draw_fixed_ball(x, y):
    global ball_x, ball_y, ball_speed_y

    ball_x = x
    ball_y = y

    fill(255, 165, 0)  # Light orange color for the ball
    ellipse(ball_x, ball_y, ball_diameter, ball_diameter)

    # Reset vertical speed when the ball is at the bottom
    if ball_y >= height - ball_diameter / 2:
        ball_speed_y = 0

def draw_bouncing_ball(x, y):
    global ball_x, ball_y, ball_speed_y, gravity

    fill(255, 165, 0)  # Light orange color for the ball
    ellipse(x, y, ball_diameter, ball_diameter)

    # Move the ball upward vertically
    ball_y -= 2  # Adjust the value to control the vertical speed

    # Update ball position and simulate bouncing effect
    ball_speed_y += gravity

    # Bounce when the ball reaches the top
    if ball_y <= 0:
        ball_speed_y *= -0.9  # Elasticity factor for the bounce
        ball_y = 0
        
def draw_football_player_with_ball1(x, y, width, height, bg_img):
    global player_x, player_y, face_animation_frame

    # Fixed position for the football player and ball in the second portion
    ball_x = x + width / 2
    ball_y = y + height - ball_diameter / 2

    # Draw background image
    image(bg_img, x, y, width, height)

    # Draw ball
    if bouncing:
        draw_bouncing_ball(ball_x, ball_y)  # Draw bouncing ball in the second portion
    else:
        draw_fixed_ball(ball_x, ball_y)  # Draw fixed ball in the second portion

    # Draw football player with cartoonish features
    pushMatrix()
    translate(ball_x + 50, ball_y - 50)
    scale(player_scale)  # Scale the entire drawing

    # Draw football player with cartoonish features
    fill(255, 224, 189)  # Light orange color for the shirt
    draw_jersey(0, -40, 20, 40)  # Jersey
    fill(255, 224, 189)  # Light skin color for the face
    ellipse(0, -50, 20, 20)  # Head

    # Draw arms
    stroke(0)  # Black color for the arms
    strokeWeight(1)
    line(-5, -30, -20, -20)  # Left arm
    line(5, -30, 20, -20)  # Right arm

    # Draw legs
    line(-5, 0, -10, 30)  # Left leg
    line(5, 0, 10, 30)  # Right leg

    # Draw football player face with animation
    draw_player_face(0, -50, face_animation_frame)
    face_animation_frame += 0.1  # Increase this value to adjust the animation speed
    popMatrix()        

def draw_football_player_with_ball2(x, y, width, height, bg_img):
    global face_animation_frame, ball_x, ball_y, ball_speed_y, gravity

    # Fixed position for the football player and ball in the third portion
    ball_x = x + width / 2
    ball_y = y + height - ball_diameter / 2

    # Draw background image
    image(bg_img, x, y, width, height)
    
        #football_player()
        # Draw football player with cartoonish features
    pushMatrix()
    translate(ball_x + 50, ball_y - 50)
    scale(player_scale)  # Scale the entire drawing

    # Draw football player with cartoonish features
    fill(255, 224, 189)  # Light orange color for the shirt
    draw_jersey(0, -40, 20, 40)  # Jersey
    fill(255, 224, 189)  # Light skin color for the face
    ellipse(0, -50, 20, 20)  # Head

    # Draw arms with animation
    stroke(0)  # Black color for the arms
    strokeWeight(1)

    line(-5, -30, -20, -20)  # Left arm
    line(5, -30, 20, -20)  # Right arm

    # Draw legs with animation
    left_leg_angle = sin(face_animation_frame) * 30  # Adjust the angle for the kicking animation
    line(-5, 0, -10, 30)  # Left leg
    line(-10, 30, -10, 30 + left_leg_angle)  # Animate kicking motion

    # Draw right leg (fixed for now)
    line(5, 0, 10, 30)  # Right leg

    # Draw football player face with animation
    draw_player_face(0, -50, face_animation_frame)
    face_animation_frame += 0.1  # Increase this value to adjust the animation speed
    popMatrix()
  

    # Update ball position and simulate bouncing effect
    ball_y -= ball_speed_y  # Change the sign to move the ball upwards
    ball_speed_y +=gravity

    # Bounce when the ball reaches the top
    if ball_y <= y + height/1.3:
        ball_speed_y *=-0.9  # Elasticity factor for the bounce
        ball_y = y + height/1.3
        

    # Constrain ball movement to the third portion
    ball_x = constrain(ball_x, x, x + width)

    # Draw ball
    fill(255, 165, 0)  # Light orange color for the ball
    ellipse(ball_x, ball_y, ball_diameter, ball_diameter)
    
def draw_player_face(x, y, frame):
    # Simple animation for facial features (eyes and mouth)
    eye_size = 5
    mouth_size = 6

    fill(255, 224, 189)  # Light skin color for the face

    # Blinking effect for the eyes
    if frameCount % 50 == 0:  # Change the divisor to adjust blink frequency
        ellipse(x - 5, y - 2, eye_size, eye_size)  # Left eye
        ellipse(x + 5, y - 2, eye_size, eye_size)  # Right eye
    else:
        ellipse(x - 5, y - 2, 0, 0)  # Left eye (closed)
        ellipse(x + 5, y - 2, 0, 0)  # Right eye (closed)

    # Animated mouth position
    mouth_y = y + sin(frame) * 0.8
    fill(255, 0, 0)  # Red color for the mouth
    arc(x, mouth_y, mouth_size, mouth_size, 0, PI)  # Mouth

def draw_jersey(x, y, width, height):
    # Custom shape for the jersey
    beginShape()
    vertex(x - width / 2, y)  # Top-left
    vertex(x + width / 2, y)  # Top-right
    vertex(x + width / 2 - 5, y + height)  # Bottom-right with a slight curve
    vertex(x - width / 2 + 5, y + height)  # Bottom-left with a slight curve
    endShape(CLOSE)

def mouseClicked():
    global ball_y
    cell_width = width // grid_cols

    # Check if the mouse is pressed inside the football in the third portion
    if cell_width < mouseX < 2*cell_width  and cell_height < mouseY < height:
        # Move the football towards the goal
        ball_y -= ball_speed

        # Check if the football reaches the goal
        if ball_y < 0:
            print("Goal!")
            reset_ball()
            
            
    
def winning_celebration(x, y, width, height, bg_img):
    global player_x, player_y, face_animation_frame

    # Fixed position for the football player and ball in the second portion
    ball_x = x + width / 2
    ball_y = y + height - ball_diameter / 2
    image(bg_img, x, y, width, height)

    pushMatrix()
    translate(ball_x + 50, ball_y - 50)
    scale(player_scale)  # Scale the entire drawing

    # Draw football player with cartoonish features
    fill(255, 224, 189)  # Light orange color for the shirt
    draw_jersey(0, -40, 20, 40)  # Jersey
    fill(255, 224, 189)  # Light skin color for the face
    ellipse(0, -50, 20, 20)  # Head

    # Draw arms with animation
    stroke(0)  # Black color for the arms
    strokeWeight(1)

    # Animate raising one arm
    left_arm_angle = sin(face_animation_frame) * 30  # Adjust the angle for the animation
    right_arm_angle = sin(face_animation_frame) * 30 # Keep the other arm down

    line(-5, -30, -20, -20 + left_arm_angle)  # Left arm
    line(5, -30, 20, -20 + right_arm_angle)  # Right arm
    line(-5, 0, -10, 30)  # Left leg
    line(5, 0, 10, 30)  # Right leg


    # Draw eyes with a happy expression
    eye_size = 5
    fill(255)  # White color for the eyes
    ellipse(-5, -52, eye_size, eye_size)  # Left eye
    ellipse(5, -52, eye_size, eye_size)  # Right eye
    

    # Draw a smiling mouth
    mouth_size = 8
    #fill(255, 0, 0)  # Red color for the mouth
    arc(0, -48, mouth_size, mouth_size, 0.2, 3.1 - 0.2)  # Smiling mouth

    popMatrix()

    # Draw cheering crowd
    crowd_color = color(random(255), random(255), random(255))  # Yellow color for the crowd

    for _ in range(30):
        crowd_x = random(x, x + width)
        crowd_y = random(y, y + height)
        size = random(5, 15)

        fill(crowd_color)
        ellipse(crowd_x, crowd_y, size, size)

    # Text
    fill(0, 0, 0)  # Green color for the text
    textFont(createFont("Arial", 20,True))  # Arial, bold, 20pt font

    # Text
    textAlign(CENTER, CENTER)
    text("You Scored a Goal!", x + width / 2, y + height / 2-100)
