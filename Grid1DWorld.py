from Environment import Environment


class Grid1DWorld(Environment):
    def __init__(self):
        super().__init__(width=7, height=1)
        self.make_cliff_tile_at(0,0)
        self.make_cliff_tile_at(0,6)
        self.make_start_tile_at(0,1)
        self.make_goal_tile_at(0,5)
        self.reset_state()