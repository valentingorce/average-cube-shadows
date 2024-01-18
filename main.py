import argparse
from tqdm import tqdm
from cube import Cube
from utils import random_rotat, projection_area


def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="A cube shadow area simulation")

    # Add arguments
    parser.add_argument("--n_runs", "-n", type=int, help="Number of runs to simulate")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values of arguments
    n_runs = args.n_runs

    c = Cube(1)

    S = 0
    for i in tqdm(range(n_runs)):
        rot = random_rotat()
        c.rotate(rot[0], "x")
        c.rotate(rot[1], "y")
        c.rotate(rot[2], "z")
        p = c.project("xy")
        S += projection_area(p)
    return S / n_runs


if __name__ == "__main__":
    print(main())
