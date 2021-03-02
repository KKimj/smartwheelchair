# 기본 라이브러리
import time

# Arduino Uno 통신
from serial import Serial
# LiDar x4
import PyLidar3

# Depth D455
import pyrealsense2 as rs

# mpu 9250 통신
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250


# Arduino motor left
# Port 수정해야 됨
PORT_left = '/dev/ttyACM0'
Board_left = Serial(PORT_left, 115200, timeout = 3)

# Arduino motor right
# Port 수정해야 됨
PORT_right = '/dev/ttyACM1'
Board_right = Serial(PORT_right, 115200, timeout = 3)

# LiDar x4
PORT_x4 = '/dev/ydlidar'
X4 = PyLidar3.YdLidarX4(PORT_x4)

# SONIC2CAN
#
# /dev/serial0
# /dev/serial1
Sonic_PORT_left = '/dev/serial0'
# Sonic_left = Serial(Sonic_PORT_left, 115200, timeout = 3)

# /dev/ttyS0
# /dev/ttyAMA0
Sonic_PORT_right = '/dev/serial1'
# Sonic_right = Serial(Sonic_PORT_right, 115200, timeout = 3)

class HC_SR04:
    left_sensors = Serial('/dev/ttyUSB0', 115200, timeout = 3)
    right_sensors = Serial('/dev/ttyUSB1', 115200, timeout = 3)
    
    @staticmethod
    def getLeftSensors():
        return list(map(int, HC_SR04.left_sensors.readline().decode('utf-8').strip().split()))

    @staticmethod
    def getRightSensors():
        return list(map(int, HC_SR04.right_sensors.readline().decode('utf-8').strip().split()))
        
    @staticmethod
    def getFront():
        return HC_SR04.getLeftSensors()[:2] + HC_SR04.getRightSensors()[:2]
    
    @staticmethod
    def getLeftside():
        return HC_SR04.getLeftSensors()[2:]
    
    @staticmethod
    def getRightside():
        return HC_SR04.getRightSensors()[2:]
    



class SONIC2CAN:
    def __init__(self):
        self.serial_left = Serial('/dev/serial0', 115200, timeout = 3)
        self.serial_right = Serial('/dev/serial1', 115200, timeout = 3)

    def getData(self):
        command = ';06\r'
        
        self.serial_left.write(bytes(command.encode()))
        self.data_left = self.serial_left.readline()

        self.serial_right.write(bytes(command.encode()))
        self.data_right = self.serial_right.readline()




    def test(self):
        command = ';06\r'
        self.serial_left.write(bytes(command.encode()))
        line = self.serial_left.readline()
        print('left : '+line)

        self.serial_right.write(bytes(command.encode()))
        line = self.serial_right.readline()
        print('right : '+line)
        pass
    



class WheelChair:
    speed = 0

    def accelerate(self):
        if self.isObstacle_Front() == True:
            self.stop()
            return

        WheelChair.speed = WheelChair.speed + 200
        self.leftSpeed(WheelChair.speed)
        self.rightSpeed(WheelChair.speed)

    def leftSpeed(self, _speed):
        _speed = str(_speed)
        Board_left.write(bytes(_speed.encode()))
        time.sleep(0.3)

    def rightSpeed(self, _speed):
        _speed = str(_speed)
        Board_right.write(bytes(_speed.encode()))
        time.sleep(0.3)

    def stop(self):
        WheelChair.speed = 0
        self.leftSpeed(0)
        self.rightSpeed(0)
        

    def forward(self):
        if self.isObstacle_Front() == True:
            self.stop()
            return 

        WheelChair.speed = 1000
        self.leftSpeed(1000)
        self.rightSpeed(1000)
        

    def backward(self):
        WheelChair.speed = -1000
        self.leftSpeed(-1000)
        self.rightSpeed(-1000)

    def left(self):
        if self.isObstacle_Left() == True:
            self.stop()
            return

        self.leftSpeed(-1000)
        self.rightSpeed(1000)

    def right(self):
        if self.isObstacle_right() == True:
            self.stop()
            return
        
        self.leftSpeed(1000)
        self.rightSpeed(-1000)

    def isObstacle_Front(self):
        if min(HC_SR04.getFront()) <= 20 :
            return True
        else :
            return False

    def isObstacle_Left(self):
        if min(HC_SR04.getLeftside()) <= 20 :
            return True
        else :
            return False

    def isObstacle_right(self):
        if min(HC_SR04.getRightside()) <= 20 :
            return True
        else :
            return False
    

    def run(self):
        pass

    def test(self):
        while True:
            mode = int(input('0: Quit, 1 : Forward, 2: Backward, 3: Left, 4: Right, 5 : acclerate'))
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
                self.left()
                time.sleep(1)
                self.stop()
            if mode == 4:
                self.right()
                time.sleep(1)
                self.stop()
            
            if mode == 5:
                self.accelerate()
            


def main():
    wheelChair = WheelChair()
    wheelChair.test()

    # sonic2can = SONIC2CAN()
    # sonic2can.test()

    while True:
        wheelChair.run()

if __name__ == '__main__':
    main()
