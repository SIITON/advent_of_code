import numpy as np


class Env:
    def __init__(self):
        self.read_data()
        self.flow_rate = {}
        self.connections = {}
        self.is_open = {}
        self.position = 'AA'
        self.visited = []
        self.pressure_released = 0

    def read_data(self):
        self.flow_rate = {}
        self.connections = {}
        self.is_open = {}
        data = open('test.txt').read().split("\n")
        for line in data:
            words = line.split()
            valve = words[1]
            # The benefit (part of the reward) of opening a valve in the current state
            self.flow_rate[valve] = int(words[4].split(';')[0].split('=')[1])
            # All possible future states from the current state
            self.connections[valve] = line.split('valve')[1].replace('s', '').replace(' ', '').split(',')
            self.is_open[valve] = False

    def depth_first_search(self, valve, visited):
        if valve not in visited:
            visited.append(valve)
            for v in self.connections[valve]:
                self.depth_first_search(v, visited)
        return visited

    def reward(self, s, a):
        #r_s = self.flow_rate[s] * (time - cost_to_open)
        s_next = self.connections[s][a]
        if self.is_open[s_next]:
            return 0
        r_s_next = self.flow_rate[s_next] * (time - cost_to_open - cost_to_move)
        r_s_neighbors = 0
        neighbor_count = 1
        for neighbor in self.connections[s_next]:
            if neighbor == s:
                continue
            if not self.is_open[neighbor]:
                r_s_neighbors += self.flow_rate[neighbor] * (time - cost_to_open - 2)
                neighbor_count += 1

        #return r_s + 0.99 * r_s_next
        return r_s_next + 0.9 * r_s_neighbors/neighbor_count

    def set_position(self, new_position):
        self.position = new_position

    def step(self, a, current_pressure_release):
        if isinstance(a, int):
            s_next = self.connections[self.position][a]
            self.set_position(s_next)
        self.pressure_released += current_pressure_release

    def open_valve(self):
        self.is_open[self.position] = True

    def valve_at_position_is_open(self):
        return self.is_open[self.position]

    def generate_random_actions(self):
        greedyness = 5
        actions = []
        pos = self.position
        for depth in range(greedyness):
            possible_actions = self.connections[pos]
            actions.append(possible_actions[np.random.randint(len(possible_actions))])
            pos = self.connections[pos][actions[depth]]
        return actions

    def states_given_actions(self, s, actions):
        visited_states = []
        current_state = self.position
        for action in actions:
            new_state = self.connections[current_state][action]
            visited_states.append(new_state)
            current_state = new_state

    def evaluate_states(self, s: list):
        time_left = time
        rewards = 0
        time_taken = 0
        for state in s:
            reward_to_open_valve = self.flow_rate[state] * (time_left - time_taken - 1)
            time_taken += 1



env = Env()
env.read_data()
cost_to_open = 1
cost_to_move = 1
time = 30
pressure_release_per_minute = 0
steps_taken = []
while time != 0:
    R = set()
    print("====== Minute", 31 - time, "======")
    print("Current pos:", env.position)
    for state in env.depth_first_search(env.position, []):
        if state is not env.position:
            continue
        for action in range(len(env.connections[state])):
            r = env.reward(state, action)
            move_to = env.connections[state][action]
            R.add((state, action, move_to, r))
            print("State", state, "Action", action, "(move to", move_to, "), R=", r)
    step_reward = 0
    what_to_do = 0
    goal = ''
    for s, a, g, r in R:
        if s == env.position and r > step_reward:
            what_to_do = a
            goal = g
            step_reward = r
    reward_to_open = 0
    if not env.valve_at_position_is_open():
        reward_to_open = env.flow_rate[env.position] * (time - cost_to_open)
        print("Reward to open valve", env.position, "=", reward_to_open)
    if reward_to_open > step_reward and not env.valve_at_position_is_open():
        pressure_release_per_minute += env.flow_rate[env.position]
        env.open_valve()
        env.step(env.position, pressure_release_per_minute)
        print("-- Open valve", env.position, ", releasing", pressure_release_per_minute, "pressure")
    else:
        print("-- We should use action", what_to_do, "and go from", env.position, "to", goal)
        env.step(what_to_do, pressure_release_per_minute)
    time -= 1

print("Part 1:", env.pressure_released)
