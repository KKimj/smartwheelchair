# Dev

## CPU Architecture
* cpu architecture 
    * ```$ dpkg --print-architecture```
    ![cpu_arch_screen](https://raw.githubusercontent.com/KKimj/smartwheelchair/main/images/screenshots/screenshot3.png?raw=true "Title")

## Operating System

[18.04.05 LTS for arm64 raspi4](http://old-releases.ubuntu.com/releases/18.04.0/ubuntu-18.04.4-preinstalled-server-arm64+raspi4.img.xz)

- http://old-releases.ubuntu.com/releases/18.04.0/ubuntu-18.04.4-preinstalled-server-arm64+raspi4.img.xz

## Serial port

* ttyAMA[0-1] : Arduino Uno for Motor
* ttyUSB[0-3] : Wemos d1 for HC_SR04, Lidar X4
* Screenshot : RealSense D455
    * ![serial_port_screenshot](https://raw.githubusercontent.com/KKimj/smartwheelchair/main/images/screenshots/screenshot1.png?raw=true "Title")

## Raspi @ Ubuntu MATE, WIFI and SSH Setup
* raspi-config install & Wireless LAN & Locale Setup
* Setup ssh
    * ```$ sudo apt install openssh-server``` 
* Port-forwarding with WIFI router(=공유기)

## ROS install
* ```$ wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_kinetic.sh && chmod 755 ./install_ros_kinetic.sh && bash ./install_ros_kinetic.sh```
    * ![ros_install_complete](https://raw.githubusercontent.com/KKimj/smartwheelchair/main/images/screenshots/screenshot2.png?raw=true "Title")


## ROS test

## Wheelchair Control test
* Bluetooth
  * ```$ sudo apt-get install bluez libbluetooth-dev pi-bluetooth```
  * ```$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev```
  * ```$ sudo python3 -m pip install pybluez```
  

## HC-SR04 algorithm

## Lidar map

## Road condition sensing


## References
* https://github.com/robotpilot/ros-seminar/blob/master/03_ROS_%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD_%EA%B5%AC%EC%B6%95.pdf


```
$ sudo apt-get update

$ sudo apt-get upgrade

$ sudo apt-get install python-setuptools
$ sudo apt-get install build-essential python-dev

alias pip=pip3
alias python=python3
```