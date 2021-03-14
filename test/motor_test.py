import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src.motor import Motor


if __name__ == '__main__':
    Motor.openSerial()
    Motor.Test()
    Motor.closeSerial()
