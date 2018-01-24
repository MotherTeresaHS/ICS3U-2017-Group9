# Created by: younes elfeitori
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main game.

from scene import *
import ui
import sound
from numpy import random
from game_over_scene import *
from main_menu_scene import *
#from copy import deepcopy
#counter = 0


class GameScene(Scene):
    def  setup(self):
        # this method is called, when user moves to this scene
        
        # updated to not use deepcopy
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.score_position = Vector2()
        self.up_button_down = False
        self.down_button_down = False
        self.fish_move_speed = 20
        self.scuba_diver = []
        self.scuba_diver_attack_rate = 1.5
        self.scuba_diver_attack_speed = 12
        self.counter = 0
        self.life_bar_position = Vector2()
        # add background color
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.background = SpriteNode('./assets/sprites/background.png',
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
                                     
        self.fish_position = Vector2()
        self.fish_position.x = 100
        self.fish_position.y = 400
        self.fish = SpriteNode('./assets/sprites/fishy.png',
                                    parent = self,
                                    position = self.fish_position,
                                    scale = 0.19)
                                       
        up_button_position = Vector2()
        up_button_position.x = 100
        up_button_position.y = 300
        self.up_button = SpriteNode('./assets/sprites/up_button.png',
                                      parent = self,
                                      position = up_button_position,
                                      alpha = 0.6,
                                      scale = 0.2)
                                       
        down_button_position = Vector2()
        down_button_position.x = 100
        down_button_position.y = 100
        self.down_button = SpriteNode('./assets/sprites/down_button.png',
                                       parent = self,
                                       position = down_button_position,
                                       alpha = 0.6,
                                       scale = 0.2)
        self.score_position.x = 400
        self.score_position.y = self.size_of_screen_y - 50
        self.score_label = LabelNode(text = 'Score: 0',
                                     font = ('Helvetica', 40),
                                     parent = self,
                                     position = self.score_position)
                                     
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        #global counter
        # move fish if button down
        if (self.up_button_down == True) and (self.fish.position.y < self.size_of_screen_y - 100):
            fishMove = Action.move_by(0.0, 
                                           self.fish_move_speed,
                                           0.1)
            self.fish.run_action(fishMove)
        
        if (self.down_button_down == True) and (self.fish.position.y > 100):
            fishMove = Action.move_by(0.0, 
                                           -1*self.fish_move_speed, 
                                           0.1)
            self.fish.run_action(fishMove)
        
            
               
               
                 
               
        # every update, randomly check if a new scuba diver should be created
        scuba_diver_create_chance = random.randint(1, 100)
        if scuba_diver_create_chance <= self.scuba_diver_attack_rate:
            self.add_scuba_diver()
        
        # check every update if an scuba diver is off screen
        for scuba_diver in self.scuba_diver:
            if scuba_diver.position.x < 50:
                scuba_diver.remove_from_parent()
                self.scuba_diver.remove(scuba_diver)
                # you might want to end the game, or take points away
                self.counter = self.counter + 1
        else:
            pass
        
        # check every update to see shark touches the fish
        if len(self.scuba_diver) > 1:
            for scuba_diver_hit in self.scuba_diver:
                if scuba_diver_hit.frame.intersects(self.fish.frame):
                    self.fish.remove_from_parent()
                    scuba_diver_hit.remove_from_parent()
                    self.scuba_diver.remove(scuba_diver_hit)
                    sound.play_effect('8ve:8ve-tap-crisp')
                    self.dismiss_modal_scene()

            else:
             pass
        self.score_label.text = 'score:' + str(self.counter)
        
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        # check if up or down button is down
        if self.up_button.frame.contains_point(touch.location):
            self.up_button_down = True
        
        if self.down_button.frame.contains_point(touch.location):
            self.down_button_down = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
            # if I removed my finger, then no matter what fish
            #    should not be moving any more
            self.up_button_down = False
            self.down_button_down = False
    
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
        # when the user hits the fire button
      
        
        
    def add_scuba_diver(self):
        # add a new scuba to come down
        
        
        scuba_diver_start_position = Vector2()
        scuba_diver_start_position.x = self.size_of_screen_x + 100
        scuba_diver_start_position.y = random.randint(100, 
                                         self.size_of_screen_y - 100)
       
        scuba_diver_end_position = Vector2()
        scuba_diver_end_position.x = -100
        scuba_diver_end_position.y = random.randint(100, 
                                        self.size_of_screen_y - 100)
        
        self.scuba_diver.append(SpriteNode('./assets/sprites/scuba_diver.png',
                             position = scuba_diver_start_position,
                             parent = self,
                             scale = 0.4))
                   
        scuba_diverMoveAction = Action.move_to(scuba_diver_end_position.x, 
                                         scuba_diver_end_position.y, 
                                         self.scuba_diver_attack_speed,
                                         TIMING_SINODIAL)
        self.scuba_diver[len(self.scuba_diver)-1].run_action(scuba_diverMoveAction)
