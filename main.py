import arcade
import random

INITIAL_WIDTH = 800
INITIAL_HEIGHT = 800

class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.BITTER_LIME
        self.screen_width = INITIAL_WIDTH
        self.screen_height = INITIAL_HEIGHT
        self.snake = [(0, 0), (0, 1), (0, 2)]
        self.apples = [(8, 8)]
        self.direction = 1 # 0 = down, 1 = right, 2 = up, 3 = left
        self.counter = 0
        self.score = 0
        self.game_over = False

    def reset(self):
        pass

    def on_draw(self):
        self.clear()


        arcade.draw_text("Snake Game", self.screen_width / 2, self.screen_height - 60, arcade.color.WHITE, font_size=30, anchor_x="center", font_name="Arial")
        arcade.draw_text("Score: " + str(self.score), self.screen_width / 2, self.screen_height - 100, arcade.color.WHITE, font_size=30, anchor_x="center", font_name="Arial")
        arcade.draw_lbwh_rectangle_outline(self.screen_width / 2 - 250, self.screen_height / 2 - 250, 500, 500, arcade.color.BLACK, 3)
        #15x15
        for y in range(15):
            for x in range(15):
                if((y % 2 == 0 and x % 2 == 0) or (y % 2 == 1 and x % 2 == 1)):
                    arcade.draw_lbwh_rectangle_filled(self.screen_width / 2 - 250 + x * (500 / 15), self.screen_height / 2 - 250 + y * (500 / 15), 500 / 15, 500 / 15, arcade.color.BITTER_LEMON)
                else:
                    arcade.draw_lbwh_rectangle_filled(self.screen_width / 2 - 250 + x * (500 / 15), self.screen_height / 2 - 250 + y * (500 / 15), 500 / 15, 500 / 15, arcade.color.BRIGHT_GREEN)

        for i in range(len(self.snake)):
            if(i == 0):
                arcade.draw_circle_filled(self.screen_width / 2 - 250 + (self.snake[i][0] + 0.5) * (500 / 15), self.screen_height / 2 - 250 + (self.snake[i][1] + 0.5) * (500 / 15), 500 / 15 / 3, arcade.color.BLACK)
            else:
                arcade.draw_circle_filled(self.screen_width / 2 - 250 + (self.snake[i][0] + 0.5) * (500 / 15), self.screen_height / 2 - 250 + (self.snake[i][1] + 0.5) * (500 / 15), 500 / 15 / 3, arcade.color.WHITE)

        for i in range(len(self.apples)):
            arcade.draw_circle_filled(self.screen_width / 2 - 250 + (self.apples[i][0] + 0.5) * (500 / 15), self.screen_height / 2 - 250 + (self.apples[i][1] + 0.5) * (500 / 15), 500 / 15 / 3, arcade.color.RED)

        if (self.game_over):
            arcade.draw_lbwh_rectangle_filled(0, 0, self.screen_width, self.screen_height, (0, 0, 0, 180))
            arcade.draw_text("Game Over", self.screen_width / 2, self.screen_height / 2, arcade.color.WHITE, font_size=30, anchor_x="center", font_name="Arial")
            arcade.draw_text("Score: " + str(self.score), self.screen_width / 2, self.screen_height / 2 - 50, arcade.color.WHITE, font_size=30, anchor_x="center", font_name="Arial")

    def on_update(self, delta_time):
        if (self.game_over):
            return

        self.counter += 1
        if (self.counter % 10 == 0):
            self.counter = 0
            self.move_snake()

        if (self.snake[0] in self.apples):
            self.apples.remove(self.snake[0])
            self.snake.append((self.snake[-1][0], self.snake[-1][1]))
            self.score += 1
            self.apples.append((random.randint(0, 14), random.randint(0, 14)))


    def move_snake(self):
        self.snake.pop(-1)
        if (self.direction == 0):
            self.snake.insert(0, (self.snake[0][0], self.snake[0][1] + 1))
        elif (self.direction == 1):
            self.snake.insert(0, (self.snake[0][0] + 1, self.snake[0][1]))
        elif (self.direction == 2):
            self.snake.insert(0, (self.snake[0][0], self.snake[0][1] - 1))
        elif (self.direction == 3):
            self.snake.insert(0, (self.snake[0][0] - 1, self.snake[0][1]))

        # check if snake is out of bounds
        if (self.snake[0][0] < 0 or self.snake[0][0] > 14 or self.snake[0][1] < 0 or self.snake[0][1] > 14):
            self.game_over = True

        # check if snake hits itself
        for i in range(1, len(self.snake)):
            if (self.snake[0] == self.snake[i]):
                self.game_over = True

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            if self.direction != 0 and self.direction != 2:
                self.direction = 0
                self.move_snake()
                self.counter = 0
        elif key == arcade.key.RIGHT:
            if self.direction != 1 and self.direction != 3:
                self.direction = 1
                self.move_snake()
                self.counter = 0
        elif key == arcade.key.DOWN:
            if self.direction != 2 and self.direction != 0:
                self.direction = 2
                self.move_snake()
                self.counter = 0
        elif key == arcade.key.LEFT:
            if self.direction != 3 and self.direction != 1:
                self.direction = 3
                self.move_snake()
                self.counter = 0


    def on_key_release(self, key, key_modifiers):

        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):

        pass

    def on_mouse_press(self, x, y, button, key_modifiers):

        pass

    def on_mouse_release(self, x, y, button, key_modifiers):

        pass

    def on_resize(self, width, height):
        """ This method is automatically called when the window is resized. """
        super().on_resize(width, height)
        self.screen_width = width
        self.screen_height = height



def main():
    window = arcade.Window(INITIAL_WIDTH, INITIAL_HEIGHT, "Snake Game", resizable=True) # starting coordinates = (0, 0)

    game = GameView()
    window.show_view(game)
    window.set_location(10, 40)
    arcade.run()



if __name__ == "__main__":
    main()
