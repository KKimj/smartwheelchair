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
    def leftSpeed(self, speed):
        speed = str(speed)
        Board_left.write(bytes(speed.encode()))
        time.sleep(0.3)

    def rightSpeed(self, speed):
        speed = str(speed)
        Board_right.write(bytes(speed.encode()))
        time.sleep(0.3)

    def stop(self):
        self.leftSpeed(0)
        self.rightSpeed(0)
        

    def forward(self):
        self.leftSpeed(1000)
        self.rightSpeed(1000)
        

    def backward(self):
        self.leftSpeed(-1000)
        self.rightSpeed(-1000)

    def left(self):
        self.leftSpeed(-1000)
        self.rightSpeed(1000)

    def right(self):
        self.leftSpeed(1000)
        self.rightSpeed(-1000)

    def isObstacle(self):
        pass

    def run(self):
        pass

    def test(self):
        while True:
            mode = int(input('1 : Forward 2: Backward 3: Left 4: Right 5: Quit'))
            if mode == 1:
                self.forward()
                time.sleep(1)
                self.stop()
            if mode == 2:
                self.forward()
                time.sleep(1)
                self.stop()
            if mode == 3:
                self.forward()
                time.sleep(1)
                self.stop()
            if mode == 4:
                self.forward()
                time.sleep(1)
                self.stop()
            if mode == 5:
                break


def main():
    wheelChair = WheelChair()
    wheelChair.test()

    sonic2can = SONIC2CAN()
    sonic2can.test()

    while True:
        wheelChair.run()

if __name__ == '__main__':
    main()
