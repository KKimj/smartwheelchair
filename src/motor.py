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


class Motor_fair:
    def __init__(self, port_left = '/dev/ttyACM0', port_right = '/dev/ttyACM1', baudrate = 115200, timeout = 3, open = True, is_reverse_left = False, is_reverse_right = True):
        self.left = Motor(port=port_left, baudrate=baudrate, timeout=timeout, open=open)
        self.right = Motor(port=port_right, baudrate=baudrate, timeout=timeout, open=open)
        self.speed = 0
        self.speed_left = 0
        self.speed_right = 0
        
        self.is_reverse = [is_reverse_left, is_reverse_right]


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
        speed = int(speed)
        self.speed = speed
        self.set_speed_left(speed)
        self.set_speed_right(speed)
    
    def set_speed_left(self, speed):
        self.speed_left = int(speed)
        
        if self.is_reverse[0]:
            speed *= -1
        self.left.write(speed)
        time.sleep(0.5)

    def set_speed_right(self, speed):
        self.speed_right = int(speed)

        if self.is_reverse[1]:
            speed *= -1
        self.right.write(speed)
        time.sleep(0.5)



    
    def accel(self, offset = 50):
        self.set_speed(self.speed+offset)

    def stop(self, is_slowdown = False):
        while self.speed > 10 and is_slowdown:
            self.speed -= 10
            self.set_speed(self.speed)
        self.set_speed(0)
        
    
    def forward(self, speed = 50, fastmode = False):
        '''
        recommend NOT to use fastmode option
        '''
        if fastmode:
            speed = 100
        self.set_speed(speed)
        

    def backward(self, speed = -50, fastmode = False):
        '''
        recommend NOT to use fastmode option
        '''
        if fastmode:
            speed = -100
        self.set_speed(speed)

    
    def turn_left(self, speed = 100):
        self.set_speed_left(-speed)
        self.set_speed_right(speed)

    
    def turn_right(self, speed = 100):
        self.set_speed_left(speed)
        self.set_speed_right(-speed)
    
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
