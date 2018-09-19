from arcade import *
import random
import os

# Tutorial from: https://opensource.com/article/18/4/easy-2d-game-creation-python-and-arcade

# Constants
SPRITE_SCALING_PLAYER = 1
SPRITE_SCALING_COIN = .5
COIN_COUNT = 50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(Window):

    def __init__(self):
        # Initialize
        #Parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite tester")

        #enables "python -m" to run the game
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        #Hides mouse cursor
        self.set_mouse_visible(False)

        set_background_color(color.AMAZON)

    def setup(self):
        #Setup for game and initialize variables

        #Sprite lists
        self.player_list = SpriteList()
        self.coin_list = SpriteList()

        #Score
        self.score = 0

        #Set up player
        self.player_sprite = Sprite("images/ninja.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        #Create coins randomly across screen
        for i in range (COIN_COUNT):

            coin = Sprite("images/sushi.png", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            #Keeping a list of all generated coins to check for collision
            self.coin_list.append(coin)

    def on_draw(self):
        # Draw all elements
        start_render()
        self.coin_list.draw()
        self.player_list.draw()

        #On screen text of player's score
        output = ("Score=%d" % self.score)
        draw_text(output, 10, 20, color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        #Center of player sprite will align with mouse
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):

        self.coin_list.update()
        coins_hit_list = check_for_collision_with_list(self.player_sprite, self.coin_list)

        #Loop through coins in list and check for collisions - delete and add to score if collided
        for coin in coins_hit_list:
            coin.kill()
            self.score += 1

def main():

    window = MyGame()
    window.setup()
    run()

if __name__ == "__main__":
    main()
