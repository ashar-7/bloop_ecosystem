import bloop
import world

# java -jar processing_py/processing-py.jar bloop/ecosystem.py

World = None

def setup() :
    global World;
    size(600, 600)

    World = world.World(20, 50)

def draw() :
    background(51)

    World.update()
    World.draw()