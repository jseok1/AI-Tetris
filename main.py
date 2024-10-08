import argparse

from renderer import Renderer

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-l", "--level", type=int, default=0, required=False, help="initial level")
  parser.add_argument(
    "-a",
    "--ai",
    action="store_const",
    const=0,
    default=1,
    help="run with an AI agent trained using reinforcement learning",
  )
  args = parser.parse_args()

  renderer = Renderer(args.ai, args.level)
