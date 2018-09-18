from arcade import *
import random
import os

# Tutorial from: https://opensource.com/article/18/4/easy-2d-game-creation-python-and-arcade

# Constants
SPRITE_SCALING_PLAYER = 1
SPRITE_SCALING_COIN = .4
COIN_COUNT = 50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite tester")
        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        set_background_color(color.AMAZON)

    def setup(self):

        self.player_list = SpriteList()
        self.coin_list = SpriteList()

        self.score = 0

        self.player_sprite = Sprite("C:/Users/indomat64/Python Projects/ninja.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range (COIN_COUNT):

            coin = Sprite("C:/Users/indomat64/Python Projects/sushi.png", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.coin_list.append(coin)

    def on_draw(self):
        """Draw everything"""
        start_render()
        self.coin_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        draw_text(output, 10, 20, color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):

        self.coin_list.update()
        coins_hit_list = check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coins_hit_list:
            coin.kill()
            self.score += 1

def main():

    window = MyGame()
    window.setup()
    run()

if __name__ == "__main__":
    main()