import argparse

from visualizer import Visualizer

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--level', type=int, nargs='?', default=0)
    parser.add_argument('-a', '--agent', action='store_const', const=0, default=1)
    args = parser.parse_args()

    mode = args.agent

    visualizer = Visualizer(mode, args.level)
