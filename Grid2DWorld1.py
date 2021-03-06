from Environment import Environment


class Grid2DWorld1(Environment):
    def __init__(self):
        super().__init__(width=7, height=3)
        self.make_cliff_tile_at(0,1)
        self.make_cliff_tile_at(0, 2)
        self.make_cliff_tile_at(0, 3)
        self.make_cliff_tile_at(0, 4)
        self.make_cliff_tile_at(0, 5)
        self.make_start_tile_at(0, 0)
        self.make_goal_tile_at(0, 6)
        self.reset_state()

    def get_all_actions(self) ->list[str]:
        return ["left", "right", "up", "down"]

    def get_possible_action(self) -> list[str]:
        possible_actions = []
        (row, col) = self.actor_loc
        if row > 0:
            possible_actions.append("up")
        if row < self.height - 1:
            possible_actions.append("down")

        if col > 0:
            possible_actions.append("left")
        if col < self.width - 1:
            possible_actions.append("right")

        return possible_actions

    def perform_action(self, action: str):
        (row, col) = self.actor_loc
        if action == "left":
            if col > 0:
                self.actor_loc = (row, col - 1)
            else:
                self.actor_loc = (row, 0)
        elif action == "right":
            if col < self.width-1:
                self.actor_loc = (row, col + 1)
            else:
                self.actor_loc = (row, self.width-1)
        elif action == "up":
            if row > 0:
                self.actor_loc = (row-1, col)
            else:
                self.actor_loc = (0, col)
        elif action == "down":
            if row < self.height-1:
                self.actor_loc = (row+1, col)
            else:
                self.actor_loc = (self.height-1, col)
        else:
            pass
