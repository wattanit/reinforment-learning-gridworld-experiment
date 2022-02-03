from Environment import *
from Grid1DWorld import Grid1DWorld
from Agent import Agent

n_training = 10

if __name__ == "__main__":
    print("RUNNING")
    env = Grid1DWorld()
    agent = Agent(env, autorun=False, verbose=True, learning_rate=0.2, discount_rate=0.9)

    for i in range(0,n_training):
        agent.do_episode()

    print("DONE TRAINING")
    print("Final average reward : {}".format(agent.average_reward))
    print("Trained policy:")
    print(agent.policy_table)