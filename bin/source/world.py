import bloop

class World :

    def __init__(self, popSize, foodQuantity) :
        self.bloops = []
        self.food = []

        for i in range(popSize) :
            self.bloops.append(bloop.Bloop(random(0, width),random(0, height), bloop.DNA.DNA()))

        for i in range(foodQuantity) :
            self.food.append(PVector(random(0, width), random(0, height))) # Place random food particles

    def update(self) :
        for b in self.bloops :
            if b.isDead() :
                self.food.append(b.location)
                self.bloops.remove(b)
                continue

            b.update()
            b.edgeCollision()
            b.eat(self.food)

            child = b.reproduce()
            if child != None :
                self.bloops.append(child)

    def draw(self) :
        for b in self.bloops :
            b.draw()
            
        for f in self.food :
            noStroke()
            fill(0, 255, 0)
            ellipse(f.x, f.y, 10, 10)