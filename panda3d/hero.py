# напиши свій код тут
class Hero():
    def __init__(self):
        self.hero = loader.loadModel("Boeing707.egg")
        self.hero.setTexture(loader.loadTexture("BoeingTexture.tif"))
        #self.hero.setColor((0,0,0,1))
        self.hero.reparentTo(render)