from abc import ABC
import numpy as np
from tkinter import *


class Environment(ABC):
    tile_markers = {
        0: "land",
        1: "start",
        2: "goal",
        3: "cliff"
    }


    def __init__(self, width=4, height=4):
        self.window = None
        self.frame = None
        self.width = width
        self.height = height

        self.grid = np.zeros((height,width))
        self.starting_tile = (0,0)

        self.actor_loc = self.starting_tile
        self.reset_state()

    def grid_from_numpy(self, grid_array: np.ndarray):
        (self.height, self.width) = grid_array.shape
        self.grid = grid_array
        self.reset_state()

    def make_land_tile_at(self, row:int, col: int):
        if (row<self.height) and (col<self.width):
            self.grid[row, col] = 0

    def make_start_tile_at(self, row: int, col: int):
        if (row < self.height) and (col < self.width):
            self.grid[self.grid==1] = 0
            self.grid[row, col] = 1
            self.starting_tile = (row, col)

    def make_goal_tile_at(self, row: int, col: int):
        if (row < self.height) and (col < self.width):
            self.grid[self.grid == 2] = 0
            self.grid[row, col] = 2

    def make_cliff_tile_at(self, row: int, col: int):
        if (row<self.height) and (col<self.width):
            self.grid[row, col] = 3

    def reset_state(self):
        self.actor_loc = self.starting_tile

    def get_state(self):
        return {
            "row": self.actor_loc[0],
            "col": self.actor_loc[1],
            "tile": self.tile_markers[self.grid[self.actor_loc]]
        }

    def get_all_actions(self)->list[str]:
        # return list of all possible action in this environment
        # to be implemented by subclass
        return []

    def get_possible_action(self) -> list[str]:
        # return list of possible action given current state
        # to be implemented by subclass
        return []

    def perform_action(self, action: str):
        # manipulate state based on the action
        # to be implemented by subclass
        return

    def show_env(self):
        window_width = self.width*50
        window_height = self.height*50

        if self.window == None:
            self.window = Tk()
            self.window.geometry("{}x{}".format(window_height,window_width))
            self.window.title("Environment")

            self.frame = Frame(self.window)
            self.frame.pack(fill=BOTH, expand=1)

        for widget in self.frame.winfo_children():
            widget.destroy()

        canvas = Canvas(self.frame)
        for r in range(0,self.height):
            for c in range(0, self.width):
                top_left = (50 * r, 50*c)
                bottom_right = (50+50*r, 50+50*c)
                tile_type = self.grid[(r,c)]
                if tile_type==0:
                    color = "#fff"
                elif tile_type==1:
                    color = "#fa0"
                elif tile_type==2:
                    color = "#0fa"
                else:
                    color = "#666"
                canvas.create_rectangle(top_left[0],
                                        top_left[1],
                                        bottom_right[0],
                                        bottom_right[1],
                                        outline="#000",
                                        fill=color)

                if self.actor_loc==(r,c):
                    canvas.create_oval(top_left[0]+5,
                                       top_left[1]+5,
                                       bottom_right[0]-5,
                                       bottom_right[1]-5,
                                       outline="#000",
                                       fill="#8af")
        canvas.pack(fill=BOTH, expand=1)

