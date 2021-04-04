import os
import sys
import time
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src import usbserial
from src.motor import Motor_fair


if __name__ == '__main__':
    mf = Motor_fair()    
    mf.open_serial()
    mf.left.write('y')
    mf.right.write('y')
    
    time.sleep(3)
    mf.close_serial()