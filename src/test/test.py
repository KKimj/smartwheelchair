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




# SONIC2CAN
#
# /dev/serial0
# /dev/serial1
Sonic_PORT_left = '/dev/serial0'
Sonic_left = Serial(Sonic_PORT_left, 115200, timeout = 3)

# /dev/ttyS0
# /dev/ttyAMA0
Sonic_PORT_right = '/dev/serial1'
Sonic_right = Serial(Sonic_PORT_right, 115200, timeout = 3)

## 위에 Serial 통신 포트 설정 부분을 SONIC2CAN class에 모두 포함시켜도 괜찮을 것 같다.
class SONIC2CAN:
    def test(self):
        data = ';06\n'
        Sonic_left.write(bytes(data.encode()))
        line = Sonic_left.readline()
        print(line)
        
Sonic_left_inst = SONIC2CAN()
Sonic_left_inst.test()




class WheelChair:
    def leftSpeed(self, speed):
        speed = str(speed)
        Board_left.write(bytes(speed.encode()))
        time.sleep(0.3)

    def rightSpeed(self, speed):
        speed = str(speed)
        Board_right.write(bytes(speed.encode()))
        time.sleep(0.3)


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

def main():
    wheelChair = WheelChair()
    while True:
        wheelChair.run()

if __name__ == '__main__':
    main()



# LiDar x4
PORT_x4 = '/dev/ydlidar'
X4 = PyLidar3.YdLidarX4(PORT_x4)

if(X4.Connect()):
    print(X4.GetDeviceInfo())
    gen = X4.StartScanning()
    #  {angle(0):distance, angle(2):distance,....................,angle(359):distance}
    t = time.time() # start time 
    while (time.time() - t) < 30: #scan for 30 seconds
        print(next(gen))
        time.sleep(0.5)
    X4.StopScanning()
    X4.Disconnect()
else:
    print("Error connecting to device")


# Depth D455
# Create a context object. This object owns the handles to all connected realsense devices
pipeline = rs.pipeline()
pipeline.start()

try:
    while True:
        # Create a pipeline object. This object configures the streaming camera and owns it's handle
        frames = pipeline.wait_for_frames()
        depth = frames.get_depth_frame()
        if not depth: continue

        # Print a simple text-based representation of the image, by breaking it into 10x20 pixel regions and approximating the coverage of pixels within one meter
        coverage = [0]*64
        for y in xrange(480):
            for x in xrange(640):
                dist = depth.get_distance(x, y)
                if 0 < dist and dist < 1:
                    coverage[x/10] += 1

            if y%20 is 19:
                line = ""
                for c in coverage:
                    line += " .:nhBXWW"[c/25]
                coverage = [0]*64
                print(line)

finally:
    pipeline.stop()

#MPU9250
mpu9250 = MPU9250(
    address_ak=AK8963_ADDRESS, 
    address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
    address_mpu_slave=None, 
    bus=1,
    gfs=GFS_1000, 
    afs=AFS_8G, 
    mfs=AK8963_BIT_16, 
    mode=AK8963_MODE_C100HZ)

mpu9250.configure() # Apply the settings to the registers.

while True:

    print("|.....MPU9250 in 0x68 Address.....|")
    print("Accelerometer", mpu9250.readAccelerometerMaster())
    print("Gyroscope", mpu9250.readGyroscopeMaster())
    print("Magnetometer", mpu9250.readMagnetometerMaster())
    print("Temperature", mpu9250.readTemperatureMaster())
    print("\n")

    time.sleep(1)

