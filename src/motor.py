from serial import Serial
from usbserial import USBSerial
import time


class Motor(USBSerial):
    def __init__(self, port, baudrate = 115200, timeout = 0.1, open = False):
        self._port = port
        self._baudrate = baudrate
        self._timeout = timeout
        self.serial = None
        if open:
            self.open_serial()
    
    # override
    def open_serial(self):
        self.serial = Serial(port = self._port, baudrate = self._baudrate, timeout = self._timeout, write_timeout=0.11)
    
    def reset_output_buffer(self):
        self.serial.reset_output_buffer()

    def stop(self):
        self.serial.write(0)
        



class Motor_fair:
    def __init__(self, port_left = '/dev/ttyACM0', port_right = '/dev/ttyACM1', baudrate = 115200, timeout = 0.1, open = True, is_reverse_left = False, is_reverse_right = True):
        self.left = Motor(port=port_left, baudrate=baudrate, timeout=timeout, open=open)
        self.right = Motor(port=port_right, baudrate=baudrate, timeout=timeout, open=open)
        self.speed = 0
        self.speed_left = 0
        self.speed_right = 0

        self.std_speed = 512
        
        self.is_reverse = [is_reverse_left, is_reverse_right]


    def open_serial(self):
        self.left.open_serial()
        self.right.open_serial()

    def close_serial(self):
        self.stop()
        time.sleep(1)
        self.left.close_serial()
        time.sleep(0.5)
        self.right.close_serial()

    def reset_output_buffer(self):
        self.left.reset_output_buffer()
        self.right.reset_output_buffer()
    
    def set_port(self, port_left, port_right, open=True):
        self.close_serial()
        self.left = Motor(port=port_left, baudrate=self.left.baudrate, timeout=self.left.timeout, open=open)
        self.right = Motor(port=port_right, baudrate=self.right.baudrate, timeout=self.right.timeout, open=open)
        self.open_serial()

    def flush(self):
        self.left.flush()
        self.right.flush()
        
    
    def switch(self):
        '''
        Swtich left to right, right to left
        '''
        tmp = self.left
        self.left = self.right
        self.right = tmp
        

    def set_speed(self, speed, debug = False):
        speed = int(speed)
        # if self.speed == speed:
        #     if debug:
        #         print('already speed : %d'%(self.speed))
        #     return
        self.speed = speed
        # self.reset_output_buffer()
        self.left.flush()
        self.right.flush()

        self.set_speed_right(speed)
        self.set_speed_left(speed)

        self.left.flush()
        self.right.flush()
        time.sleep(0.05)
        # self.left.flush()

        # self.right.flush()
    
    def set_speed_left(self, speed):
        self.speed_left = int(speed)
        
        if self.is_reverse[0]:
            speed *= -1
        # self.left.flush()
        # self.left.reset_output_buffer()
        self.left.write(speed)
        self.left.flush()


    def set_speed_right(self, speed):
        self.speed_right = int(speed)

        if self.is_reverse[1]:
            speed *= -1
        # self.right.flush()
        # self.right.reset_output_buffer()
        self.right.write(speed)
        self.right.flush()




    
    def accel(self, offset = 50):
        if self.speed < 150:
            self.set_speed(self.speed+offset)

    def stop(self, is_slowdown = False, close = False):
        while self.speed > 10 and is_slowdown:
            self.speed -= 10
            self.set_speed(self.speed)
        self.set_speed(0)
        if close:
            self.close_serial()
        
    
    def forward(self, speed = 200, fastmode = False, debug = False):
        '''
        recommend NOT to use fastmode option
        '''
        if fastmode:
            speed = 200
        if debug:
            print('forward')
            speed = self.std_speed
        self.set_speed(speed, debug)
        

    def backward(self, speed = -200, fastmode = False, debug = False):
        '''
        recommend NOT to use fastmode option
        '''
        if fastmode:
            speed = -200
        if debug:
            print('backward')
            speed = - self.std_speed
        self.set_speed(speed, debug)

    
    def turn_left(self, speed = 150, debug = False):
        if debug:
            print('turn left')
            speed = self.std_speed

        self.set_speed_left(-speed*0.3)
        self.set_speed_right(speed*0.3)

    
    def turn_right(self, speed = 150, debug = False):
        if debug:
            print('turn right')
            speed = self.std_speed
        self.set_speed_left(speed*0.3)
        self.set_speed_right(-speed*0.3)
    
    def run(self):
        while True:
            mode = int(input('0: Quit, 1 : Forward, 2: Backward, 3: Left, 4: Right, 5 : acclerate 6 : Swtich left/right'))
            if mode == 0:
                self.stop()
                self.close_serial()
                break

            if mode == 1:
                self.forward()
                time.sleep(3)
                self.stop()
            if mode == 2:
                self.backward()
                time.sleep(3)
                self.stop()
            if mode == 3:
                self.turn_left()
                time.sleep(3)
                self.stop()
            if mode == 4:
                self.turn_right()
                time.sleep(3)
                self.stop()
            
            if mode == 5:
                offset = int(input('Enter offset').strip())
                self.accel(offset)
                print('now speed : %d'%(self.speed))

            if mode == 6:
                self.stop()
                self.switch()
            
    def test(self):
        print('** check left **')
        self.left.test()
        print('** check left **')
        self.right.test()
