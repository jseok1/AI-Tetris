import argparse

import Visualizer

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--level', type=int, nargs='?', default=0)
    args = parser.parse_args()

    visualizer = Visualizer.Visualizer(args.level)
    visualizer.run_game()
