from objects.game import Game
from pygame import Surface, font, init, surface
init()
class Text(Game):
    fonts = {
        "xl": font.Font("assets/font/font.ttf", 50),
        "l": font.Font("assets/font/font.ttf", 40),
        "m": font.Font("assets/font/font.ttf", 30),
        "s": font.Font("assets/font/font.ttf", 20),
        "xs": font.Font("assets/font/font.ttf", 10),
    }

    def __init__(self, message, **kwargs):
        super().__init__()
        try:
            kwargs["display"]
        except:
            kwargs["display"] = True
        self.text = Text.fonts[kwargs["size"]].render(
            message, True, kwargs["fg"], kwargs["bg"]
        )
        self.text.set_colorkey((0, 0, 0, 0))
        if kwargs["align"] == "top-left":
            pos = (0, 0)
        elif kwargs["align"] == "top-center":
            pos = (Game.resolution[0]/2 - self.text.get_width()/2, 0)
        elif kwargs["align"] == "top-right":
            pos = (Game.resolution[0] - self.text.get_width(), 0)
        elif kwargs["align"] == "mid-left":
            pos = (0, Game.resolution[1]/2 - self.text.get_height()/2)
        elif kwargs["align"] == "mid-center":
            pos = (Game.resolution[0]/2 - self.text.get_width()/2,
                   Game.resolution[1]/2 - self.text.get_height()/2)
        elif kwargs["align"] == "mid-right":
            pos = (Game.resolution[0] - self.text.get_width(),
                   Game.resolution[1]/2 - self.text.get_height()/2)
        elif kwargs["align"] == "bottom-left":
            pos = (0, Game.resolution[1] - self.text.get_height())
        elif kwargs["align"] == "bottom-center":
            pos = (Game.resolution[0]/2 - self.text.get_width() /
                   2, Game.resolution[1] - self.text.get_height())
        elif kwargs["align"] == "bottom-right":
            pos = (Game.resolution[0] - self.text.get_width(),
                   Game.resolution[1] - self.text.get_height())
        else:
            pos = kwargs["align"]
        self.x, self.y = pos
        if kwargs["display"]:
            Game.surface.blit(self.text, pos)
