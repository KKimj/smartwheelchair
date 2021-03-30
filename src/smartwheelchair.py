from HC_SR04 import HC_SR04_fair
from motor import Motor_fair

class SmartWheelChair:
    def __init__(self):
        self.HC_SR04 = HC_SR04_fair()
        self.motor = Motor_fair()

    def is_obstacle_front(self):
        if min(self.HC_SR04.get_front()) <= 20 :
            return True
        else :
            return False

    
    def is_obstacle_left(self):
        if min(self.HC_SR04.get_leftside()) <= 20 :
            return True
        else :
            return False

    
    def is_obstacle_right(self):
        if min(self.HC_SR04.get_rightside()) <= 20 :
            return True
        else :
            return False
    
    
    def Run(self, only_option='', joystick = False, bluetooth = False, multi_tread = False):
        if only_option == 'motor':
            self.motor.test()
            self.motor.run()
            return
        
        if only_option == 'snoic':
            self.HC_SR04.test()
            
            return
        
        if len(only_option.strip()) is not 0:
            return
        
        while True:
            if self.is_obstacle_front():
                self.motor.stop()
            
            elif self.is_obstacle_left():
                self.motor.turn_right()
            
            elif self.is_obstacle_right():
                self.motor.turn_left()
            
            else:
                self.motor.forward()
            
