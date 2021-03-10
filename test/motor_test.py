import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import src.motor


if __name__ == '__main__':
    Motor.openSerial()
    Motor.Test()
    Motor.close()
