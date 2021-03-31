import argparse
from smartwheelchair import SmartWheelChair


def main(args):
    print('SmartWheelChair now running...')
    if args.testmode:
        print(args)
    SmartWheelChair().Run(only_option = args.only, joystick = args.joystick, bluetooth = args.bluetooth, multi_tread = args.thread, fastmode= args.fastmode)


def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--joystick', '-joy', help='Control by joystick', action="store_true")
    parser.add_argument('--bluetooth', '-bt', help='Use Bluetooth Protocol for Controller', action="store_true")
    parser.add_argument('--testmode', '-test', help='Test(=verbose) mode', action="store_true")
    parser.add_argument('--thread', '-thread', help='Use Multithreading for input handling', action="store_true")
    parser.add_argument('--fastmode', '-fast', help='Usb fastmode', action="store_true")
    
    # parser.add_argument('--onlymotor', '-motor', help='Without sensor handling', action="store_true")
    # parser.add_argument('--onlyutralsonic', '-sonic', help='Without sensor handling', action="store_true")
    
    parser.add_argument('--only', help='Special option to test e.g. motor, snoic')
    
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_arguments()
    main(args)

