# напиши свій код тут
camera = "c"             #kebab remover
forward = "w"
backward = "s"
left = "a"
right = "d"
rotate_left = "arrow_left"
rotate_right = "arrow_right"
up = "q"
down = "e"
killniggers = "m"



class Hero():
    def __init__(self):
        self.cameraOn = True
        self.hero = loader.loadModel("Boeing707.egg")
        self.hero.setTexture(loader.loadTexture("BoeingTexture.tif"))
        #self.hero.setColor((0,0,0,1))
        self.hero.reparentTo(render)
        self.cameraBind()
        self.hero.setScale(0.025)
        self.accept_events()
    
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos((0,0,1.5))
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(pos[0],pos[1],pos[2])
        base.camera.reparentTto(render)
        base.enableMouse()
        self.cameraOn = False
    def cameraChange(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()
    def forward(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)
    def backward(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)
    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)
    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)

    def rotateLeft(self):
        self.hero.setH(self.hero.getH() + 5)
    def rotateRight(self):
        self.hero.setH(self.hero.getH() - 5)





    def accept_events(self):
        base.accept("c",self.cameraChange)

        base.accept(rotate_left,self.rotateLeft)
        base.accept(rotate_left + "-repeat",self.rotateLeft)
        base.accept(rotate_right,self.rotateRight)
        base.accept(rotate_right + "-repeat",self.rotateRight)
