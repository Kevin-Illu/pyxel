import pyxel


class App:
    def __init__(self) -> None:
        pyxel.init(160, 120)

        # load the tilemap resource
        pyxel.load("./my_resource.pyxres")

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        # Draw a single tile at the center of the screen
        # The parameters are:
        # 1. Screen X and Y coordinates (in pixels)
        screen_x, screen_y = 0, 0
        # 2. Tilemap layer
        tilemap_layer = 0
        # 3. Tilemap X and Y coordinates (in tiles)
        tilemap_x, tilemap_y = 0, 0
        # 4. Width and Height of the tile area to draw (in tiles)
        width, height = 8, 8
        pyxel.bltm(
            screen_x, screen_y, tilemap_layer, tilemap_x, tilemap_y, width, height
        )


App()
