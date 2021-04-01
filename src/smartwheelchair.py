from HC_SR04 import HC_SR04_fair
from motor import Motor_fair
import time

class SmartWheelChair:
    def __init__(self):
        self.HC_SR04 = HC_SR04_fair(channel = 4)
        self.motor = Motor_fair()

    def is_obstacle_front(self, debug = False):
        data = self.HC_SR04.get_front()
        if debug:
            print(data)
        if min(data) <= 20 :
            return True
        else :
            return False

    def is_obstacle_near(self, debug = False):
        data = self.HC_SR04.get_front()
        if debug:
            print(data)
        if min(data) <= 50 :
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
    
    def close_serial(self):
        self.HC_SR04.close_serial()
        self.motor.close_serial()


    
    
    def run(self, only_option='', joystick = False, bluetooth = False, multi_tread = False, fastmode = False, debug = False):
        if type(only_option) == str: 
            if only_option == 'motor':
                self.motor.test()
                self.motor.run()
                
            if only_option == 'sonic':
                self.HC_SR04.test()
                self.HC_SR04.run(debug = debug)
            
            if only_option == 'sonicdebug':
                self.HC_SR04.test()
                self.HC_SR04.run(debug = True)

            if only_option == 'forward':
                self.HC_SR04.open_serial()
                forward_flag = False
                speed_flag = 0
                try:
                    while True:
                        if self.is_obstacle_front(debug = debug):
                            self.motor.stop()
                            forward_flag = False
                        # elif not forward_flag:
                        elif self.is_obstacle_near(debug = debug):
                            self.motor.set_speed(50)
                        else:
                            # self.motor.forward(fastmode = fastmode, debug = debug)
                            # self.motor.forward(fastmode = fastmode, debug = debug)
                            self.motor.accel(10)
                except KeyboardInterrupt:
                    self.motor.stop()
                    time.sleep(0.1)
                    self.motor.stop()
                    # self.close_serial()
            
            return
        
        try:
            self.HC_SR04.open_serial()
            while True:
                if debug:
                    print('Front :', self.HC_SR04.get_front(), 'Leftside :', self.HC_SR04.get_leftside(), 'Rightside :', self.HC_SR04.get_rightside())
                
                if not self.is_obstacle_near():
                    self.motor.accel(10)
                    if debug:
                        print('accel')
                    continue

                if self.is_obstacle_front():
                    self.motor.backward()
                    if debug:
                        print('back')
                
                elif self.is_obstacle_near() and self.is_obstacle_left():
                    self.motor.turn_right()
                    if debug:
                        print('right')
                
                elif self.is_obstacle_near() and self.is_obstacle_right():
                    self.motor.turn_left()
                    if debug:
                        print('left')
                
                else:
                    self.motor.forward(debug=debug)
                    if debug:
                        print('forward')
        except KeyboardInterrupt:
            self.motor.stop()
            self.close_serial()
            
