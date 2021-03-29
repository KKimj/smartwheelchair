from serial import Serial
from usbserial import USBSerial
import time


class Motor(USBSerial):
    def __init__(self, port, baudrate = 115200, timeout = 3, open = False):
        self._port = port
        self._baudrate = baudrate
        self._timeout = timeout
        self.serial = None
        if open:
            self.open_serial()
    # TODO 

class Motor_fair:
    leftPort = '/dev/ttyACM0'
    rightPort = '/dev/ttyACM1'

    leftBoard = None
    rightBoard = None

    speed = 0
    def __init__(self, port_left = '/dev/ttyACM0', port_right = '/dev/ttyACM1', baudrate = 115200, timeout = 3, open = True):
        self.left = Motor(port=port_left, baudrate=baudrate, timeout=timeout, open=open)
        self.right = Motor(port=port_right, baudrate=baudrate, timeout=timeout, open=open)
        self.speed = 0
        self.speed_left = 0
        self.speed_right = 0


    def open_serial(self):
        self.left.open_serial()
        self.right.open_serial()

    def close_serial(self):
        self.left.close_serial()
        self.right.close_serial()
    
    def set_port(self, port_left, port_right, open=True):
        self.close_serial()
        self.left = Motor(port=port_left, baudrate=self.left.baudrate, timeout=self.left.timeout, open=open)
        self.right = Motor(port=port_right, baudrate=self.right.baudrate, timeout=self.right.timeout, open=open)
        self.open_serial()
        
    
    def switch(self):
        '''
        Swtich left to right, right to left
        '''
        tmp = self.left
        self.left = self.right
        self.right = tmp
        

    def set_speed(self, speed):
        if type(speed) is not type(str):
            speed = str(speed)
        self.left.write(speed)
        self.right.write(speed)
        self.speed = speed
        self.speed_left = speed
        self.speed_right = speed
        time.sleep(0.3)
    
    def set_speed_left(self, speed):
        if type(speed) is not type(str):
            speed = str(speed)
        self.left.write(speed)
        self.speed_left = speed
        time.sleep(0.3)

    def set_speed_right(self, speed):
        if type(speed) is not type(str):
            speed = str(speed)
        self.right.write(speed)
        self.speed_right = speed


    
    def accel(self, offset = 50):
        self.set_speed(self.speed+offset)

    def stop(self):
        while self.speed > 10:
            self.speed -= 10
            self.set_speed(self.speed)
            time.sleep(0.01)
        self.set_speed(0)
        
    
    def forward(self, speed = 100, is_highspeed = False):
        if is_highspeed:
            speed = 1000
        self.set_speed(speed)
        
        
    @staticmethod
    def backward(self, speed = -100, is_highspeed = False):
        if is_highspeed:
            speed = -1000
        self.set_speed(speed)

    
    def turn_left(self, speed = 100):
        self.set_speed_left(-speed)
        self.set_speed_right(speed)

    
    def turn_right(self, speed = 100):
        self.set_speed_left(speed)
        self.set_speed_right(-speed)
    

    def test(self):
        while True:
            mode = int(input('0: Quit, 1 : Forward, 2: Backward, 3: Left, 4: Right, 5 : acclerate 6 : Swtich left/right'))
            if mode == 0:
                break

            if mode == 1:
                self.forward()
                time.sleep(1)
                self.stop()
            if mode == 2:
                self.backward()
                time.sleep(1)
                self.stop()
            if mode == 3:
                self.turn_left()
                time.sleep(1)
                self.stop()
            if mode == 4:
                self.turn_right()
                time.sleep(1)
                self.stop()
            
            if mode == 5:
                self.accel()

            if mode == 6:
                self.switch()
            
