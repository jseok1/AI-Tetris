import Visualizer
import Tetris

if __name__ == '__main__':
    visualizer = Visualizer.Visualizer(Tetris.Tetris(10, 20))
    visualizer.run_game()
