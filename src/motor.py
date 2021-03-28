from serial import Serial
import time

class _SerialDevice:
    def __init__(self, port, baudrate, timeout = 3, open = False):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial = None
        if open:
            self.open_serial()
    
    def open_serial(self):
        if not self.serial:
            self.close_serial()
        self.serial = Serial(self.port, self.baudrate, self.timeout)

    def close_serial(self):
        if self.serial:
            self.serial.close()
        self.serial = None

    def write(self, message):
        if self.serial:
            if type(message) is not str:
                message = str(message)
            self.serial.write(bytes(message.encode()))
    
    def readline(self):
        if self.serial:
            return self.serial.readline().decode('utf-8').strip()

class Motor:
    pass

class Motor_:
    leftPort = '/dev/ttyACM0'
    rightPort = '/dev/ttyACM1'

    leftBoard = None
    rightBoard = None

    speed = 0
    
    @staticmethod
    def setSerialPort(leftPort = '/dev/ttyACM0', rightPort = '/dev/ttyACM1'):
        Motor.CloseSerial()

        Motor.leftPort = leftPort
        Motor.rightPort = rightPort

        Motor.OpenSerial()

    @staticmethod
    def OpenSerial():    
        Motor.leftBoard = Serial(Motor.leftPort, 115200, timeout = 3)
        Motor.rightBoard = Serial(Motor.rightPort, 115200, timeout = 3)

    @staticmethod
    def CloseSerial():   
        Motor.leftBoard.close()
        Motor.rightBoard.close()

    @staticmethod
    def Switch():
        Motor.setSerialPort(leftPort=Motor.rightPort, rightPort=Motor.leftPort)
    
        

    @staticmethod
    def setLeftSpeed(_speed):
        _speed = str(_speed)
        Motor.leftBoard.write(bytes(_speed.encode()))
        time.sleep(0.3)

    @staticmethod
    def setRightSpeed(_speed):
        _speed = str(_speed)
        Motor.rightBoard.write(bytes(_speed.encode()))
        time.sleep(0.3)

    @staticmethod
    def Accelerate():
        Motor.speed = Motor.speed + 200
        Motor.setLeftSpeed(Motor.speed)
        Motor.setRightSpeed(Motor.speed)

    @staticmethod
    def Stop():
        Motor.speed = 0
        Motor.setLeftSpeed(0)
        Motor.setRightSpeed(0)
        
    @staticmethod
    def Forward(isHighSpeed = False):
        Motor.speed = 100
        Motor.setLeftSpeed(Motor.speed)
        Motor.setRightSpeed(Motor.speed)

        if isHighSpeed:
            Motor.speed = 1000
            Motor.setLeftSpeed(Motor.speed)
            Motor.setRightSpeed(Motor.speed)
        
        
    @staticmethod
    def Backward():
        Motor.speed = -1000
        Motor.setLeftSpeed(-1000)
        Motor.setRightSpeed(-1000)

    @staticmethod
    def TurnLeft():
        Motor.setLeftSpeed(-1000)
        Motor.setRightSpeed(1000)

    @staticmethod
    def TurnRight():
        Motor.setLeftSpeed(1000)
        Motor.setRightSpeed(-1000)
    
    @staticmethod
    def Test():
        while True:
            mode = int(input('0: Quit, 1 : Forward, 2: Backward, 3: Left, 4: Right, 5 : acclerate 6 : Swtich left/right'))
            if mode == 0:
                break

            if mode == 1:
                Motor.Forward()
                time.sleep(1)
                Motor.Stop()
            if mode == 2:
                Motor.Backward()
                time.sleep(1)
                Motor.Stop()
            if mode == 3:
                Motor.TurnLeft()
                time.sleep(1)
                Motor.Stop()
            if mode == 4:
                Motor.TurnRight()
                time.sleep(1)
                Motor.Stop()
            
            if mode == 5:
                Motor.Accelerate()

            if mode == 6:
                Motor.Switch()
            
            
