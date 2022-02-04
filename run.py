from Grid1DWorld import Grid1DWorld
from Grid2DWorld1 import Grid2DWorld1
from Grid2DWorld2 import Grid2DWorld2
from Agent import Agent

n_training = 1000

if __name__ == "__main__":
    print("RUNNING")
    # env = Grid1DWorld()
    # env = Grid2DWorld1()
    env = Grid2DWorld2()
    agent = Agent(env, autorun=False,
                  verbose=True,
                  plot_reward=True,
                  learning_rate=0.2,
                  discount_rate=0.9)

    for i in range(0,n_training):
        agent.do_episode()

    print("DONE TRAINING")
    print("Final average reward : {}".format(agent.average_reward))
    print("Trained policy:")
    print(agent.policy_table)