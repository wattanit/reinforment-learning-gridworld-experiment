from Environment import *
from Grid1DWorld import Grid1DWorld
import numpy as np

if __name__ == "__main__":
    print("RUNNING")
    # example_grid = np.array([[3,3,3,3,3],
    #                          [3,1,0,0,3],
    #                          [3,0,0,0,3],
    #                          [3,0,0,2,3],
    #                          [3,3,3,3,3]])
    env = Grid1DWorld()
    print(env.grid)
    env.show_env()
    input("ctrl+c to exit")