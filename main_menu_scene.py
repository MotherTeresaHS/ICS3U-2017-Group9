# Created by: younes elfeitori
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui

from game_scene import *
from help_scene import *
from credit_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background color
        self.background = SpriteNode('./assets/sprites/background.png',
        	                           position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
                                     
        self.start_button = SpriteNode('./assets/sprites/start.png',
                                       parent = self,
                                       position = (self.size.x / 2, self.size.y / 2 - 200),
                                       scale = 0.7)
                                       
        help_button_position = self.size/2
        help_button_position.y = help_button_position.y - 190
        help_button_position.x = help_button_position.x + 350
        self.help_button = SpriteNode('./assets/sprites/help.png',
                                       parent = self,
                                       position = help_button_position,
                                       scale = 0.4)
                                       
        credit_button_position = self.size/2
        credit_button_position.y = credit_button_position.y - 190
        credit_button_position.x = credit_button_position.x - 350
        self.credit_button = SpriteNode('./assets/sprites/credits.png',
                                       parent = self,
                                       position = credit_button_position,
                                       scale = 0.4)
                                       
        logo_position = self.size/2
        logo_position.y = logo_position.y - 5
        logo_position.x = logo_position.x - 5
        self.logo_position = SpriteNode('./assets/sprites/logo.png',
                                       parent = self,
                                       position = logo_position,
                                       alpha = 2.0,
                                       scale = 1.5)
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
        if self.start_button.frame.contains_point(touch.location):
            sound.play_effect('8ve:8ve-beep-timber')
            self.present_modal_scene(GameScene())
            
        # if start button is pressed, goto game scene
        if self.help_button.frame.contains_point(touch.location):
            sound.play_effect('8ve:8ve-beep-timber')
            self.present_modal_scene(HelpScene())
    
        if self.credit_button.frame.contains_point(touch.location):
            sound.play_effect('8ve:8ve-beep-timber')
            self.present_modal_scene(CreditScene())
    
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
    
