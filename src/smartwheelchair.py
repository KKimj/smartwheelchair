from HC_SR04 import HC_SR04_fair
from motor import Motor_fair

class SmartWheelChair:
    def __init__(self):
        self.HC_SR04 = HC_SR04_fair(channel = 4)
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
        if type(only_option) == str: 
            if only_option == 'motor':
                self.motor.test()
                self.motor.run()
                
            if only_option == 'sonic':
                self.HC_SR04.test()
                self.HC_SR04.run()
            
            if only_option == 'sonicdebug':
                self.HC_SR04.test()
                self.HC_SR04.run(debug = True)
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
            
