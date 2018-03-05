import DNA

class Bloop :

    def __init__(self, x, y, dna) :
        self.location = PVector(x, y)
        self.dna = dna

        self.size = map(self.dna.gene, 0, 1, 20, 80)
        self.maxSpeed = map(self.dna.gene, 0, 1, 15, 0)

        # Vars for perlin noise
        self.xOff = random(0, 100)
        self.yOff = random(0, 100)

        self.health = 100

    def update(self) :
        # Calculate
        vx = map(noise(self.xOff),0,1,-self.maxSpeed,self.maxSpeed)
        vy = map(noise(self.yOff),0,1,-self.maxSpeed,self.maxSpeed)

        velocity = PVector(vx,vy)
        self.xOff += 0.01
        self.yOff += 0.01

        self.location += velocity

    def draw(self) :
        ellipseMode(CENTER)
        stroke(0)
        fill(255, 255, 255, map(self.health, 0, 100, 0, 255))
        ellipse(self.location.x, self.location.y, self.size, self.size)

        self.health -= 0.5

    def edgeCollision(self) :
        if self.location.x - (self.size / 2) > width :
            self.location.x = 0
        elif self.location.x + (self.size / 2) < 0 :
            self.location.x = width
        if self.location.y - (self.size / 2) > height :
            self.location.y = 0
        elif self.location.y + (self.size / 2) < 0 :
            self.location.y = height

    def isDead(self) :
        if self.health <= 0 :
            return True
        
        return False

    def eat(self, food) :
        for f in food :
            if self.location.dist(f) < self.size / 2 :
                self.health += 100
                food.remove(f)

    def reproduce(self) :
        if random(1) < 0.0001 :
            childDNA = DNA.DNA()
            childDNA.gene = self.dna.gene
            child = Bloop(self.location.x, self.location.y, childDNA)

            return child

        return None