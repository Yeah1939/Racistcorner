# напиши тут код основного вікна гри
from mapmanager import Mapmanager
from direct.showbase.ShowBase import ShowBase
from hero import Hero


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.maps = Mapmanager()
        self.maps.loadLand()
        self.hero = Hero()

game = Game()

game.run()