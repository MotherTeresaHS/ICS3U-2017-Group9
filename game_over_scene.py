from scene import *
import ui

from game_scene import *

class GameOverScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = '#55bcff', 
                                     parent = self, 
                                     size = self.size)

        self.restart_game_button = SpriteNode('./assets/sprites/restart_game.png',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 0.2)
    
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
        if self.restart_game_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
            
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
   
