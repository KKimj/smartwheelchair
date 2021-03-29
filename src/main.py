import argparse
from smartwheelchair import SmartWheelChair


def main(args):
    print('SmartWheelChair now running...')
    if args.testmode:
        print(args)
    SmartWheelChair().Run(is_multithreading = args.thread, is_only_motor = args.onlymotor)


def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--joystick', '-joy', help='Control by joystick', action="store_true")
    parser.add_argument('--bluetooth', '-bt', help='Use Bluetooth Protocol for Controller', action="store_true")
    parser.add_argument('--testmode', '-test', help='Test mode', action="store_true")
    parser.add_argument('--thread', '-thread', help='Use Multithreading for input handling', action="store_true")
    parser.add_argument('--onlymotor', '-omotor', help='Without sensor handling', action="store_true")
    
    
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_arguments()
    main(args)

