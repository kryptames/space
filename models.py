import arcade.key

DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
 
DIR_OFFSET = { DIR_UP: (0,1),
               DIR_RIGHT: (1,0),
               DIR_DOWN: (0,-1),
               DIR_LEFT: (-1,0) }

class Snake:
    MOVE_WAIT = 0.2
    BLOCK_SIZE = 16
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.wait_time = 0
        self.direction = DIR_RIGHT
 
    def update(self, delta):
        self.wait_time += delta
 
        if self.wait_time < Snake.MOVE_WAIT:
            return
 
        self.x += DIR_OFFSET[self.direction][0]*self.BLOCK_SIZE
        self.y += DIR_OFFSET[self.direction][1]*self.BLOCK_SIZE
        
        self.wait_time = 0
 
 
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.snake = Snake(self, width // 2, height // 2)
        
    def update(self, delta):
            self.snake.update(delta)        

    def on_key_press(self, key, key_modifiers):
        #self.direction = DIR_UP*(key==arcade.key.UP) + DIR_DOWN*(key==arcade.key.DOWN) + DIR_LEFT*(key==arcade.key.LEFT) + DIR_RIGHT*(key==arcade.key.RIGHT)
        if key == arcade.key.W:
            self.direction = DIR_UP
        elif key == arcade.key.S:
            self.direction = DIR_DOWN
        elif key == arcade.key.A:
            self.direction = DIR_LEFT 
        elif key == arcade.key.D:
            self.direction = DIR_RIGHT 
                    
    
        
    