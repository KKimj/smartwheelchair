# smartwheelchair

BLDC 모터(70W 이상 고출력, 2개), 초음파센서( 2개 ), LiDar, IMU(=mpu9250) 사용한, 장애물 회피 스마트 휠체어

## Getting Started
```
$ git clone https://github.com/KKimj/smartwheelchair
$ cd smartwheelchair
$ sudo python3 ./src/main.py
```
## Usage
```
usage: main.py [-h] [--joystick] [--bluetooth] [--thread] [--testmode] [--fastmode] [--debugmode] [--only ONLY]

optional arguments:
  -h, --help            show this help message and exit
  --joystick, -joy      Control by joystick
  --bluetooth, -bt      Use Bluetooth Protocol for Controller
  --thread, -thread     Use Multithreading for input handling
  --testmode, -test     Test(=verbose) mode
  --fastmode, -fast     Usb fastmode
  --debugmode, -debug, --debug
                        Usb debug mode
  --only ONLY           Special option to test e.g. motor, sonic
```


### Prerequisites
```
$ sudo apt update && sudo apt upgrade
$ sudo apt install python3 python3-pip software-properties-common
$ sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
$ sudo apt install python3-rosdep


$ sudo apt install python3-pip
$ pip3 install serial

$ cd ~
$ git clone https://github.com/YDLIDAR/ydlidar_ros
$ git chectout master
$ catkin_make



$ git clone https://github.com/Microsoft/vcpkg.git
$ cd vcpkg
$ ./bootstrap-vcpkg.sh
$ ./vcpkg integrate install

$ export VCPKG_FORCE_SYSTEM_BINARIES=1
$ ./vcpkg install grpc

// $ ./vcpkg install realsense2

```

## Running the tests
```
# Test for Sonic data 
$ sudo python3 ./src/main.py --only sonic -debug

# Test for Motor
$ sudo python3 ./src/main.py --only motor -debug

```


## Acknowledgments
https://github.com/sparkfun/SparkFun_MPU-9250_Breakout_Arduino_Library

https://github.com/Motorbank/MAS001
