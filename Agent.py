import numpy as np
import time
import random
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from Environment import Environment

class Agent:
    reward = {
        'land': -1,
        'start': -1,
        'cliff': -200,
        'goal': 200
    }

    def __init__(self, environment: Environment,
                 autorun=False,
                 verbose=False,
                 plot_reward=False,
                 learning_rate=0.2,
                 discount_rate=0.9):
        self.learning_rate = learning_rate
        self.discount_rate = discount_rate
        self.autorun = autorun
        self.verbose = verbose
        self.plot_reward = plot_reward

        self.environment = environment
        self.episode_rewards = []
        self.average_rewards = []
        self.total_episode = 0

        # create policy table
        self.policy_table = np.zeros((self.environment.grid.shape[0],
                                      self.environment.grid.shape[1],
                                      len(self.environment.get_all_actions())))

        # create action index mapping
        self.action_map = {}
        idx = 0
        for action in self.environment.get_all_actions():
            self.action_map[action] =  idx
            idx += 1

        # init agent location
        self.state = self.environment.get_state()

        if self.plot_reward:
            self.window = Tk()
            self.window.geometry("600x400")
            self.window.title("Average reward vs episode")

    def do_step(self):
        # get possible actions
        possible_actions = self.environment.get_possible_action()

        # find best action
        possible_action_value = []
        for action in possible_actions:
            possible_action_value.append(self.policy_table[(self.state["row"], self.state["col"], self.action_map[action])])
        best_action_indices = np.where(possible_action_value==np.max(possible_action_value))[0]
        best_action = possible_actions[random.choice(best_action_indices)]

        # perform action
        self.environment.perform_action(best_action)

        # get new state
        old_state = self.state
        self.state = self.environment.get_state()

        # update policy table
        reward = self.reward[self.state['tile']]
        look_ahead_value = []
        possible_next_actions = self.environment.get_possible_action()
        for action in possible_next_actions:
            look_ahead_value.append(self.policy_table[(self.state["row"], self.state["col"], self.action_map[action])])
        best_utility = np.max(look_ahead_value)

        self.policy_table[(old_state["row"], old_state["col"],self.action_map[best_action])] += self.learning_rate*(
            reward + self.discount_rate*(best_utility)
        )

        if (self.state["tile"] == "goal") or (self.state["tile"] == "cliff"):
            return reward, True
        else:
            return reward, False


    def do_episode(self):
        episode_reward = 0

        if self.verbose:
            print("------------------------start episode {}----------------------------".format(self.total_episode+1))

        # reset environment
        self.environment.reset_state()
        self.environment.set_experiment_value({
            "episode": self.total_episode+1
        })
        self.state = self.environment.get_state()

        # loop through steps
        is_terminal = False
        step_count = 0
        if self.verbose:
            print("Step {}: Current state {}".format(step_count, self.state))
            self.environment.show_env()
        while not is_terminal:
            step_reward, is_terminal = self.do_step()
            episode_reward +=  step_reward
            step_count += 1
            if self.verbose:
                print("Step {}: Current state {}".format(step_count, self.state))
                self.environment.show_env()

            if not self.autorun:
                # wait for input
                cmd = input("Press ENTER to perform next step or Q to exit: ")
                if (cmd == "q") or (cmd == "Q"):
                    sys.exit(0)
            else:
                if self.verbose:
                    time.sleep(1)

        self.episode_rewards.append(episode_reward)
        self.total_episode += 1
        self.average_rewards.append(np.mean(self.episode_rewards))

        if self.verbose:
            if self.plot_reward:
                for widget in self.window.winfo_children():
                    widget.destroy()
                figure = plt.Figure()
                ax = figure.add_subplot(111)
                chart_type = FigureCanvasTkAgg(figure, self.window)
                chart_type.get_tk_widget().pack()
                ax.plot(range(0,self.total_episode), self.average_rewards)
                ax.set_title("Episode {}".format(self.total_episode))
                ax.set_xlabel("episode")
                ax.set_ylabel("average rewards")

            print("------------------------ episode ended---------------------------")
            print("Episode {}: average reward = {}".format(self.total_episode, self.average_rewards[-1]))
            print("Policy table = ")
            print(self.policy_table)
            print("-----------------------------------------------------------------")

        if not self.autorun:
            # wait for input
            cmd = input("Press ENTER to run next episode or q to stop: ")
            if (cmd=="q") or (cmd=="Q"):
                sys.exit(0)
        else:
            if self.verbose:
                time.sleep(1)

    def training(self, max_episode=1000):
        episode_count = 0
        while episode_count < max_episode:
            self.do_episode()

        print("Average reward: {}".format(self.average_reward))

