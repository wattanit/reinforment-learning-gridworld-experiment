from Environment import Environment


class Grid1DWorld(Environment):
    def __init__(self):
        super().__init__(width=7, height=1)
        self.make_cliff_tile_at(0, 0)
        self.make_cliff_tile_at(0, 6)
        self.make_start_tile_at(0, 1)
        self.make_goal_tile_at(0, 5)
        self.reset_state()

    def get_possible_action(self) -> list[str]:
        # return list of possible action given current state
        # to be implemented by subclass
        possible_actions = []
        (row, col) = self.actor_loc
        if col > 0:
            possible_actions.append("left")
        if col < self.width-1:
            possible_actions.append("right")
        return possible_actions

    def perform_action(self, action: str):
        # manipulate state based on the action
        # to be implemented by subclass
        if action == "left":
            (row, col) = self.actor_loc
            if col > 0:
                self.actor_loc = (row, col-1)
            else:
                self.actor_loc = (row, 0)
        elif action == "right":
            (row, col) = self.actor_loc
            if col < self.width-1:
                self.actor_loc = (row, col+1)
            else:
                self.actor_loc = (row, self.width-1)
        else:
            pass
