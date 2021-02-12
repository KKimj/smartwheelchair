BLDC 모터(70W 이상 고출력, 2개), 초음파센서( 2개 ), LiDar, IMU(=mpu9250) 사용한, 장애물 회피 스마트 휠체어

## Getting Started
```
$ git clone https://github.com/KKimj/smartwheelchair
$ python3 ./smartwheelchair/src/main.py
```

### Prerequisites
```
$ sudo apt update && sudo apt upgrade
$ sudo apt install python3 python3-pip software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt install python3.7
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
$ sudo update-alternatives --config python
$ sudo apt install python3-pip
$ pip3 install serial
$ pip3 install PyLidar3
$ pip3 install pyrealsense2
```

## Running the tests
```
$ python3 ./smartwheelchair/src/test/test.py
```

## Acknowledgments
