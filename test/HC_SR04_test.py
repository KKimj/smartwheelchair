import os
import sys
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src.HC_SR04 import HC_SR04_quad

if __name__ == '__main__':
    HC_SR04_quad.openSerial()
    for i in range(100):
        print(HC_SR04_quad.getTotalData())
        time.sleep(30)
    HC_SR04_quad.close()

