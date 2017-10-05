import arcade
import arcade.key
from models import World,Alien,Base
from random import randint
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
GRAVITY_CONSTANT = 750 #เดี๋ยวมาแก้ ความโน้มถ่วงให้เพิ่มตามเวลาที่เปลี่ยนไป 
                       #โดยสร้างตัวแปรเวลามาเก็บ
                       #แล้วมาคูนกับ gravity
MOVEMENT_CONSTANT = 5

class AlienWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width, height)
        self.background = None
        self.base_list = None 
        self.world = World(width,height) 
        self.alien_sprite = arcade.Sprite('images/alien1.png')
        self.base_sprite = arcade.Sprite('images/base_3.png')
        alien = Alien(self.world,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.delta_x = alien.delta_x
        self.delta_y = alien.delta_y
        
        #self.alien.set_position(400, 125) #alien position
        

    def setup(self):
        self.background = arcade.load_texture("images/space2.jpg")
        self.base_list = arcade.SpriteList()
        self.alien_sprite.center_x = self.world.alien.x
        self.alien_sprite.center_y = self.world.alien.y
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.alien_sprite.draw()
        self.base_sprite.draw()

    def update(self,delta):
        self.world.update(delta)
        self.alien_sprite.set_position(self.world.alien.x,self.world.alien.y)
        self.base_sprite.set_position(self.world.base.x,self.world.base.y)  
        self.world.alien.y -= self.delta_y*delta
        self.world.alien.x += self.delta_x
        #print(self.alien_sprite.center_y)
        #print(self.world.base.y)
        if(self.alien_sprite.center_y >= self.world.base.y-10.5 and self.alien_sprite.center_y <= self.world.base.y+50.5  and self.alien_sprite.center_x <= self.world.base.x+65 and self.alien_sprite.center_x >= self.world.base.x-65):
            self.delta_y = 0
        else:
            self.delta_y = GRAVITY_CONSTANT
        

    def on_key_press(self,key,modifiers):
        if(key == arcade.key.LEFT):
            self.delta_x = -MOVEMENT_CONSTANT
        if(key == arcade.key.RIGHT):
            self.delta_x = MOVEMENT_CONSTANT
    def on_key_release(self,key,modifiers):
        if(key == arcade.key.LEFT or key == arcade.key.RIGHT):
           self.delta_x = 0
       
def main():
    window = AlienWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()      
