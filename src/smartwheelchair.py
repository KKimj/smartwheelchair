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
        if min(data) <= 25 :
            return True
        else :
            return False

    def is_obstacle_near(self, debug = False):
        data = self.HC_SR04.get_front()
        if debug:
            print(data)
        if min(data) <= 60 :
            return True
        else :
            return False

    
    def is_obstacle_left(self):
        if min(self.HC_SR04.get_leftside()) <= 30 :
            return True
        else :
            return False

    
    def is_obstacle_right(self):
        if min(self.HC_SR04.get_rightside()) <= 15 :
            return True
        else :
            return False

    def obstacle_status(self):
        # data = self.HC_SR04.get()

        # ret = []
        # ret.append(self.is_obstacle_front())
        # ret.append(self.is_obstacle_left())
        # ret.append(self.is_obstacle_right())

        ret = {
            'front' : self.is_obstacle_front(),
            'left' : self.is_obstacle_left(),
            'right' : self.is_obstacle_right(),
            'near' : self.is_obstacle_near(),
        }
        return ret
        

    
    def close_serial(self):
        self.HC_SR04.close_serial()
        self.motor.close_serial()


    
    
    def run(self, only_option='', joystick = False, bluetooth = False, multi_tread = False, fastmode = False, debug = False):
        if type(only_option) == str: 
            if only_option == 'motor':
                self.motor.open_serial()
                self.motor.test()
                self.motor.run()
                
            if only_option == 'sonic':
                self.HC_SR04.test()
                self.HC_SR04.run(debug = debug)
            
            if only_option == 'obstacle' or only_option == 'ob':
                self.HC_SR04.open_serial()
                while True:
                    obstacle_status = self.obstacle_status()
                    print('obstacle_status', obstacle_status)

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
                time_offset = 0.85
                obstacle_status = self.obstacle_status()
                if debug:
                    print('obstacle_status', obstacle_status)

                if obstacle_status['front']:
                    # break
                    if obstacle_status['left'] and obstacle_status['right']:
                        self.motor.backward(debug=debug)

                    elif obstacle_status['left']:
                        self.motor.turn_right(debug=debug)

                    
                    elif obstacle_status['right']:
                        self.motor.turn_left(debug=debug)
                    else:
                        self.motor.turn_left(debug=debug)

                
                elif obstacle_status['left']:
                    self.motor.turn_right(debug=debug)

                    
                elif obstacle_status['right']:
                    self.motor.turn_left(debug=debug)


                elif obstacle_status['near']:
                    self.motor.forward(speed = 150, debug=debug)


                
                # Safe from obstacle
                else:
                    self.motor.forward(debug=debug)
                
                time.sleep(time_offset)
                # self.motor.stop()
                # time.sleep(time_offset*2)

            self.motor.stop()
            time.sleep(1)
            self.motor.set_speed_left(0)
            time.sleep(1)
            self.motor.set_speed_right(0)
            time.sleep(1)
            
            
            self.motor.close_serial()
            time.sleep(1)
            self.HC_SR04.close_serial()

        except KeyboardInterrupt:
            self.motor.stop()
            time.sleep(1)
            self.motor.set_speed_left(0)
            time.sleep(1)
            self.motor.set_speed_right(0)
            time.sleep(1)
            
            
            self.motor.close_serial()
            time.sleep(1)
            self.HC_SR04.close_serial()
            
