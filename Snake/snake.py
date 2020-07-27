import tkinter as tk
from PIL import Image, ImageTk
from random import randint

MOVE_INCREMENT = 20
MOVERS_PER_SECOND = 15
GAME_SPEED = 1000 // MOVERS_PER_SECOND

class Snake(tk.Canvas): # Snake class inherits from Canvas
    def __init__(self) -> None:
        super().__init__(width=600, height=620, background='black', highlightthickness=0)  # Super classes initialize method.
                                                                                           # highlightthickness is 0 to avoid borders around canvas
        
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]   # (x, y): One piece of the snakes body. Pixels separated by 20px
        self.food_position = self.set_new_food_position() # (x, y): Starting food position
        self.score = 0
        self.direction = "Right"
        self.bind_all("<Key>", self.on_key_press)

        self.load_assets()
        self.create_objects()
        
        self.after(GAME_SPEED, self.perform_actions)

    def load_assets(self) -> None: # Imports images into project
        try:
            self.snake_body_image = Image.open("./assets/snake.png")        # Opens up snake.png image and creates a PhotoImage
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)       

            self.food_image = Image.open("./assets/food.png")
            self.food = ImageTk.PhotoImage(self.food_image)
        except IOError as error:
            print(error)
            window.destroy()

    def create_objects(self) -> None:
        """
        Places the objects onto the canvas given the locations in self.snake_position.
        """
        self.create_text(
            45, 12, text=f"Score: {self.score}", tag="score", fill="#fff", font=("TkDefaultFont", 14)
        )

        for x_pos, y_pos in self.snake_positions: # Will create 3 instances of the image
            self.create_image(x_pos, y_pos, image=self.snake_body, tag="snake") # Tag allows us to find the images in the canvas

        self.create_image(self.food_position[0], self.food_position[1], image=self.food, tag="food") # Creates food
        self.create_rectangle(7, 27, 593, 613, outline="#FF0000") # Creating boundaries

    def move_snake(self):
        head_x_pos, head_y_pos = self.snake_positions[0]
        new_head_pos = ""

        if self.direction == "Left":
            new_head_pos = (head_x_pos - MOVE_INCREMENT, head_y_pos)
        elif self.direction == "Right":
            new_head_pos = (head_x_pos + MOVE_INCREMENT, head_y_pos)
        elif self.direction == "Down":
            new_head_pos = (head_x_pos, head_y_pos + MOVE_INCREMENT)
        elif self.direction == "Up":
            new_head_pos = (head_x_pos, head_y_pos - MOVE_INCREMENT)
        
        self.snake_positions = [new_head_pos] + self.snake_positions[:-1] # Cuts off the last position to make it look like the snake is moving

        for seg, pos in zip(self.find_withtag("snake"), self.snake_positions): # Moves the snake
            self.coords(seg, pos)

    def perform_actions(self):
        if self.check_collisions(): # If true, game stops and snake stops moving
            self.end_game()
            return

        self.check_food_collision()
        self.move_snake()
        self.after(GAME_SPEED, self.perform_actions)

    def check_collisions(self):
        head_x_pos, head_y_pos = self.snake_positions[0]
        return (
            head_x_pos in (0, 600)      # Crashes into right/left boundaries
            or head_y_pos in (20, 620)  # Crashes into top/bottom boundaries
            or (head_x_pos, head_y_pos) in self.snake_positions[1:] # Crashes into itself
        )

    def on_key_press(self, event):
        new_direction = event.keysym
        
        all_directions = ("Up", "Down", "Left", "Right")
        opposites = ({"Down", "Up"}, {"Right", "Left"})

        if new_direction in all_directions and {new_direction, self.direction} not in opposites:
            self.direction = new_direction
        
    def check_food_collision(self):
        if self.snake_positions[0] == self.food_position:
            self.score += 1
            self.snake_positions.append(self.snake_positions[-1])

            self.create_image(
                *self.snake_positions[-1], image=self.snake_body, tag="snake"
            )
            self.food_position = self.set_new_food_position()
            self.coords(self.find_withtag("food"), self.food_position)

            score = self.find_withtag("score")
            self.itemconfigure(score, text=f"Score: {self.score}", tag="score")

    def set_new_food_position(self):
        while True:
            x_pos = randint(1, 29) * MOVE_INCREMENT
            y_pos = randint(3, 30) * MOVE_INCREMENT
            food_position = (x_pos, y_pos)

            if food_position not in self.snake_positions:
                return food_position

    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game Over! You Scored {self.score}!",
            fill="#00ffff",
            font=("TkDefaultFont", 24)
        )

window = tk.Tk()                # Creates application window
window.title("Snake")           # Changes windows title to "Snake" from "tk"
window.resizable(False, False)  # Restricts resizing the window (x_axis, y_axis)

board = Snake()     # Creating the canvas class
board.pack()        # Putting board into the window done with the pack method.

window.mainloop()   # Main Game Loop