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
$ sudo ln -sf /usr/bin/python3.7 /usr/bin/python3
$ sudo apt-get install ninja-build

$ wget http://www.cmake.org/files/v3.19/cmake-3.19.4.tar.gz
$ tar xpvf cmake-3.19.4.tar.gz cmake-3.19.4/
$ cd cmake-3.19.4/
$ ./bootstrap --system-curl
$ make -j6
$ echo 'export PATH=/home/$USER/cmake-3.19.4/bin/:$PATH' >> ~/.bashrc
$ source ~/.bashrc

$ git clone https://github.com/Microsoft/vcpkg.git
$ cd vcpkg
$ ./bootstrap-vcpkg.sh
$ ./vcpkg integrate install
$ ./vcpkg install realsense2
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
