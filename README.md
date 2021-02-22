# smartwheelchair
smartwheelchair

## Getting Started
```
$ git clone https://github.com/KKimj/PerformanceFuzzer
```

### Prerequisites
```
$ sudo apt update && sudo apt upgrade
$ sudo apt install python3 python3-pip software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt install python3.5
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.5 1
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
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

$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
$ sudo apt update
$ sudo apt install ros-noetic-desktop-full
$ apt search ros-noetic
$ echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
$ sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
$ sudo apt install python3-rosdep

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
https://github.com/sparkfun/SparkFun_MPU-9250_Breakout_Arduino_Library

https://github.com/Motorbank/MAS001
