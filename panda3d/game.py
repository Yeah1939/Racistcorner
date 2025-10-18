# напиши тут код основного вікна гри
from mapmanager import Mapmanager
from direct.showbase.ShowBase import ShowBase


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.maps = Mapmanager()

game = Game()
game.maps.addBlock((0,0,0))
game.run()