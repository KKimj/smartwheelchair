from usbserial import USBSerial
import time

class HC_SR04(USBSerial):
    def __init__(self, port = '/dev/ttyUSB0', baudrate = 115200, timeout = 3, channel = 1, open = False):
        super().__init__(port=port, baudrate=baudrate, timeout=timeout, open=open)
        self.channel = channel
    

    def get(self, separator=' '):
        '''
        Getter to data from serial
        Must call OpenSerial() before to use this method
        '''
        self.serial.reset_input_buffer()
        ret = list(map(int, super().readline().strip().split(separator)))
        return ret

    def test(self):
        '''
        Print out Sensors data
        '''
        print('Test method of HC_SR04 Class')
        if self:
            super().test()
            if self.channel:
                print('Channel : %s'%(self.channel))

class HC_SR04_fair():
    def __init__(self, port_left = '/dev/ttyUSB0', port_right = '/dev/ttyUSB1', baudrate = 115200, timeout = 3, channel = 1, open = False):
        '''
        left : Left Sensors
        right : Right Sensors
        '''
        self.channel = channel

        self.left = HC_SR04(port = port_left, baudrate=baudrate, timeout=timeout, channel=channel, open=open)
        self.right = HC_SR04(port = port_right, baudrate=baudrate, timeout=timeout, channel=channel, open=open)
    
    def set_port(self, port_left, port_right, open = False):
        self.left.port = port_left
        self.right.port = port_right
        if open:
            self.open_serial()

    def open_serial(self):
        self.left.open_serial()
        time.sleep(0.1)
        self.right.open_serial()
        time.sleep(0.1)
    
    def close_serial(self):
        self.left.close_serial()
        time.sleep(0.1)
        self.right.close_serial()
        time.sleep(0.1)
    
    def switch(self):
        '''
        Swtich left to right, right to left
        '''
        tmp = self.left
        self.left = self.right
        self.right = tmp       
    
    def get(self, separator=' '):
        return self.left.get() + self.right.get()

    def get_left_sensors(self):
        return self.left.get()
    
    def get_right_sensors(self):
        return self.right.get()
    
    def get_front(self):
        '''
        Front Sensor are 1, 2, 3 ...
        '''
        return self.left.get()[:self.channel//2]+ self.right.get()[:self.channel//2]
    
    def get_leftside(self):
        '''
        Side sensors are ... 5 6 7 8
        '''
        return self.left.get()[self.channel//2-1:]
    
    def get_rightside(self):
        return self.right.get()[self.channel//2-1:]
    
    
    def test(self):
        '''
        Print out Sensors data
        '''
        print('* Test method of HC_SR04_fair')
        if self.left:
            print('** Left sensors')
            self.left.test()
        if self.right:
            print('** Right sensors')
            self.right.test()

    def test_left(self):
        '''
        check left sensors
        '''
        if not self.left.serial:
            if not self.left.open_serial():
                return
        while True:
            result = self.left.get()
            print(result)
            if min(result) < 10:
                print('Left : detect')
                break


    def test_right(self):
        '''
        check left sensors
        '''
        if not self.right.serial:
            if not self.right.open_serial():
                return
        while True:
            result = self.right.get()
            print(result)
            if min(result) < 10:
                print('Right : detect')
                break

    def test_direction(self):
        '''
        check sensors direction
        '''
        print('** check left **')
        self.test_left()
        print('** check right **')
        self.test_right()

    def run(self, debug = False):
        self.open_serial()
        while True:
            if not debug:
                print('left :', self.get_left_sensors(), 'right :', self.get_right_sensors())
            if debug:
                print('Front :', self.get_front(), 'Leftside :', self.get_leftside(), 'Rightside :', self.get_rightside())
