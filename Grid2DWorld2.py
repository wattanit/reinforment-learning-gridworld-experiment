from Environment import Environment


class Grid2DWorld2(Environment):
    def __init__(self):
        super().__init__(width=6, height=6)
        self.make_start_tile_at(0, 0)
        self.make_goal_tile_at(5, 5)
        self.make_cliff_tile_at(0, 2)
        self.make_cliff_tile_at(1, 2)
        self.make_cliff_tile_at(2, 2)
        self.make_cliff_tile_at(4, 2)
        self.make_cliff_tile_at(4, 3)
        self.make_cliff_tile_at(4, 4)
        self.make_cliff_tile_at(3, 4)
        self.make_cliff_tile_at(5, 4)

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