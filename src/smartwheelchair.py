from HC_SR04 import HC_SR04_fair
from motor import Motor_fair
import time
import threading

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
        # sonic_data = self.HC_SR04.get()

        # ret = []
        # ret.append(self.is_obstacle_front())
        # ret.append(self.is_obstacle_left())
        # ret.append(self.is_obstacle_right())
        
        # front = 

        ret = {
            'front' : self.is_obstacle_front(),
            'left' : self.is_obstacle_left(),
            'right' : self.is_obstacle_right(),
            'near' : self.is_obstacle_near(),
        }
        # return ret, sonic_data
        return ret
        

    
    def close_serial(self):
        self.HC_SR04.close_serial()
        self.motor.close_serial()

    def print_out(self):
        pass

    def input_handler(self):
        tmp_command = None

        while True:
            # stdscr.clear()
            # stdscr.move(0, 0)
            # stdscr.refresh()
            c = self.stdscr.getch()
            if c == -1:
                continue
            c = chr(c)

            if c == 'w':
                tmp_command = 'forward'
            elif c == 'a':
                tmp_command = 'turn_left'
            elif c == 's':
                tmp_command = 'stop'
            elif c == 'd':
                tmp_command = 'turn_right'
            elif c == 'x':
                tmp_command = 'backward'
            elif c == 'q':
                tmp_command = 'quit'
            else:
                continue

            with self.command_lock:
                self.command = tmp_command
                time.sleep(1)
            
            
            if self.command == 'quit':
                # curses.endwin()
                break
            
            # time.sleep(1)
    
    def motor_handler(self):
        prev_command = None
        while True:
            while not self.command:
                time.sleep(0.01)

            if prev_command == self.command:
                continue

            # with command_lock:
            #   pass
            stdscr.clear()
            stdscr.move(0, 0)
            stdscr.refresh()
            # print(command, end="motor_handler\n")

            
            prev_command = self.command
            
            if self.command == 'quit':
                    # curses.endwin()
                    # time.sleep(0.1)
                    self.motor.stop()
                    time.sleep(2)
                    break
                # command = None
            # time.sleep(1)
            elif self.command == 'forward':
                self.motor.forward()
            elif self.command == 'turn_left':
                self.motor.turn_left()
            elif self.command == 'turn_right':
                self.motor.turn_right()
            elif self.command == 'backward':
                self.motor.backward()
    
    def obstacle_handler(self):
        while True:
            obstacle_status = self.obstacle_status()

            if True:
                # print('obstacle_status', obstacle_status)
                pass

            if obstacle_status['front']:
                # break
                if obstacle_status['left'] and obstacle_status['right']:
                    tmp_command = 'backward'

                elif obstacle_status['left']:
                    tmp_command = 'turn_right'

                
                elif obstacle_status['right']:
                    tmp_command = 'turn_left'

                else:
                    tmp_command = 'turn_left'

            elif obstacle_status['left']:
                tmp_command = 'turn_right'

                
            elif obstacle_status['right']:
                tmp_command = 'turn_left'


            elif obstacle_status['near']:
                tmp_command = 'forward'

            # Safe from obstacle
            else:
                tmp_command = 'forward'

            with self.command_lock:
                self.command = tmp_command
                tmp_command = None
            # time.sleep(0.1)
            if self.command == 'quit':
                    break

    def _run(self, debug, data = False):
        try:
            if data:
                start_time = time.time()
                data_file = open('logdata_'+time.ctime()+'.txt', mode='wt', encoding='utf-8')
                data_file.write('Time\tL1\tL2\tL3\tL4\tR1\tR2\tR3\tR4\tLRPM\tRRPM\tMotion\n')
            self.HC_SR04.open_serial()
            while True:
                time_offset = 0.0
                tmp_command = None
                obstacle_status = self.obstacle_status()
                
                if obstacle_status['front']:
                    # break
                    if obstacle_status['left'] and obstacle_status['right']:
                        self.motor.backward(debug=debug)
                        tmp_command = 'backward'

                    elif obstacle_status['left']:
                        self.motor.turn_right(debug=debug)
                        tmp_command = 'right'

                    
                    elif obstacle_status['right']:
                        self.motor.turn_left(debug=debug)
                        tmp_command = 'left'
                    else:
                        self.motor.turn_left(debug=debug)
                        tmp_command = 'left'

                
                elif obstacle_status['left']:
                    self.motor.turn_right(debug=debug)
                    tmp_command = 'right'

                    
                elif obstacle_status['right']:
                    self.motor.turn_left(debug=debug)
                    tmp_command = 'left'


                elif obstacle_status['near']:
                    self.motor.forward(speed = 150, debug=debug)
                    tmp_command = 'forward'


                
                # Safe from obstacle
                else:
                    self.motor.forward(debug=debug)
                    tmp_command = 'forward'
                

                if debug:
                    print('obstacle_status', obstacle_status)

                if data:
                    data_file.write('%.3f\t'%(time.time()-start_time))
                    sonic_data = self.HC_SR04.get()
                    for data in sonic_data:
                        data_file.write('%d\t'%(data))
                    data_file.write('%d\t'%(self.motor.speed_left))
                    data_file.write('%d\t'%(self.motor.speed_right))
                    data_file.write(tmp_command+'\n')


                    


                time.sleep(time_offset)
                # self.motor.stop()
                # time.sleep(time_offset*2)

            self.motor.stop()
            time.sleep(1)
            self.motor.set_speed_left(0)
            time.sleep(1)
            self.motor.set_speed_right(0)
            time.sleep(1)
            
            
            if data:
                data_file.close()
            
            self.motor.close_serial()
            time.sleep(1)
            self.HC_SR04.close_serial()


        except KeyboardInterrupt:
            self.motor.flush()
            self.motor.stop()
            self.motor.flush()
            # time.sleep(1)
            # self.motor.set_speed_left(0)
            # time.sleep(1)
            # self.motor.set_speed_right(0)
            time.sleep(1)
            
            
            if data:
                data_file.close()
            
            self.motor.close_serial()
            time.sleep(1)
            self.HC_SR04.close_serial()

    def onlyoption_run(self, only_option, debug):
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
    
    def multi_tread_run(self):
        input_thread = threading.Thread(target=self.input_handler, args=())
        input_thread.daemon = True 

        motor_thread = threading.Thread(target=self.motor_handler, args=())
        motor_thread.daemon = True
        
        obstacle_thread = threading.Thread(target=self.obstacle_handler, args=())
        obstacle_thread.daemon = True

        self.command = None
        self.command_lock = threading._allocate_lock()

        self.stdscr = curses.initscr()
        self.stdscr.nodelay(1)

        input_thread.start()
        obstacle_thread.start()
        motor_thread.start()

        while True:
            try:
                if self.command == 'quit':
                    break
            except KeyboardInterrupt:
                self.curses.endwin()
                print("### End ###")
                break
    
    def run(self, only_option='', joystick = False, bluetooth = False, multi_tread = False, fastmode = False, debug = False, data = False):
        if type(only_option) == str: 
            self.onlyoption_run(only_option = only_option, debug = debug)
        else:
            self._run(debug = debug, data = data)
        
        

        
        
            
