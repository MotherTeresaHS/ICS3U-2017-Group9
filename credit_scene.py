from scene import *
import ui

from main_menu_scene import *


class CreditScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        center_of_screen = self.size/2
        
        # add background color
        self.background = SpriteNode(position = self.size / 2,
                                     color = '#39b1ff',
                                     parent = self,
                                     size = self.size)
                                     
        self.start_label = LabelNode(text = 'Developed by Younes Elfeitori & Joe Pagliaro',
                                     font = ('Helvetica', 20),
                                     parent = self,
                                     position = self.size / 2)
                                     
        back_button_position = self.size
        back_button_position.x = 100
        back_button_position.y = back_button_position.y - 100
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       parent = self,
                                       position = back_button_position)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
   
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass

