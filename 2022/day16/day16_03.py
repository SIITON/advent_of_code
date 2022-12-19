import numpy as np
from collections import defaultdict

# Mission: maximize released pressure

# The actor has two choices


# Actions:
# If a valve is closed:
#   open it (takes one minute to open)
#   or
#   move to another (takes one minute)

# States:
# Pressure release per minute
#   or
# Total pressure released
#
# Position
# Valves open known (which to exclude)

# Pre-processing
# There's valves with zero flow rate
# We could exclude these and instead increase the cost to move between connected nodes
# For example in the test data:
#   E is connected to F, F is connected to G, G is connected to H
#   Both F and G has the flow rate of zero.
#   Instead we could connect E directly to H, but increase the cost to move there
#   Since we remove 2 nodes, F and G, the distance from E to H increase to 3.
#                   dict[(str, str)] = 2n - 1
#           cost_to_move((from, to)) = deleted_nodes * 2 - 1
#
#           deleted_nodes = nodes_between('AA', '
#
# AA = 0, II = 0, FF = 0, GG = 0
# Check A
#   AA is connected to ['DD', 'II', 'BB']
# valve = 'AA'
# Check if neighbors are equal to zero
#   for neighbors in connections_to[valve]
#       if neighbor is flow_rate[neighbor] == 0:
#           append neighbor to some list
#       cost_to_move[(valve, neighbor)] =
def dfs(valve, visited, neighbor_of):
    if valve not in visited:
        visited.append(valve)
        for v in neighbor_of[valve]:
            dfs(v, visited, neighbor_of)
    return visited



class Env:
    def __init__(self):
        self.e_position = 'AA'
        self.flow_rate = {}
        self.connections = {}
        self.is_open = {}
        self.read_data()
        self.position = 'AA'
        self.visited = []
        self.pressure_released = 0
        self.greedyness = 5
        self.randomness = 50
        self.time = 30

    def read_data(self):
        data = open('input.txt').read().split("\n")
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

    #                   dict[(str, str)] = 2n - 1
    #           cost_to_move((from, to)) = deleted_nodes * 2 - 1
    #
    #           deleted_nodes = nodes_between('AA', '
    #
    # AA = 0, II = 0, FF = 0, GG = 0
    # Check A
    #   AA is connected to ['DD', 'II', 'BB']
    # valve = 'AA'
    # Check if neighbors are equal to zero
    #   for neighbor in connections_to[valve]
    #       if flow_rate[neighbor] == 0:
    #           append neighbor to some list
    #       cost_to_move[(valve, neighbor)] =
    def pre_process_data(self):
        cost_to_move_from_to = defaultdict()
        useless_valves = []
        for valve, fr in self.flow_rate.items():
            if fr == 0 and valve not in useless_valves: # and valve not in useless_valves
                # We can remove this valve as it's useless (we won't ever open)
                # All neighbors will then connect to each other, but at an increased time cost
                neighbors = self.connections[valve]
                for i in range(len(neighbors)): # [0: 'DD', 1: 'II', 2: 'BB']
                    for neighbor in neighbors:
                        if self.flow_rate[neighbor] == 0:
                            useless_valves.append(neighbor)
                        if neighbor != neighbors[i]:
                            cost_to_move_from_to[(neighbors[i], neighbor)] += 1

                useless_valves.append([valve])
                #self.connections.pop(valve)
            else:
                neighbors = self.connections[valve]
                for i in range(len(neighbors)):
                    for neighbor in neighbors:
                        if neighbor != neighbors[i]:
                            cost_to_move_from_to[(neighbors[i], neighbor)] = 1

    def reward(self, s, a):
        #r_s = self.flow_rate[s] * (time - cost_to_open)
        s_next = self.connections[s][a]
        if self.is_open[s_next]:
            return 0
        r_s_next = self.flow_rate[s_next] * (self.time - cost_to_open - cost_to_move)
        r_s_neighbors = 0
        neighbor_count = 1
        for neighbor in self.connections[s_next]:
            if neighbor == s:
                continue
            if not self.is_open[neighbor]:
                r_s_neighbors += self.flow_rate[neighbor] * (self.time - cost_to_open - 2)
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

    def generate_random_actions(self, character='self'):
        self.greedyness = 5
        actions = []
        if character == 'elephant':
            pos = self.e_position
        else:
            pos = self.position
        for depth in range(self.greedyness):
            possible_actions = self.connections[pos]
            actions.append(possible_actions[np.random.randint(len(possible_actions))])
            pos = actions[depth]
        return actions

    def states_given_actions(self, s, actions, character='self'):
        visited_states = []
        if character == 'elephant':
            current_state = self.e_position
        else:
            current_state = self.position
        for action in actions:
            new_state = self.connections[current_state][action]
            visited_states.append(new_state)
            current_state = new_state

    def evaluate_states(self, s: list):
        time_left = self.time
        rewards = 0
        time_taken = 0
        for state in s:
            if self.flow_rate[state] == 0:
                time_left += 1
                continue
            if self.is_open[state]:
                time_left += 1
                continue
            reward_to_open_valve = self.flow_rate[state] * (time_left - time_taken - 1)
            rewards += reward_to_open_valve
            time_taken += 1
        return rewards

    def generate_a_good_sequence(self, character='self'):
        chosen_sequence = []
        reward_of_sequence = 0
        for i in range(self.randomness):
            a = self.generate_random_actions(character=character)
            r = self.evaluate_states(a)
            if r > reward_of_sequence:
                chosen_sequence = a
                reward_of_sequence = r
        return chosen_sequence, reward_of_sequence

    def run(self, verbose=True, greedyness=5, randomness=50):
        self.time = 30
        self.greedyness = greedyness
        self.randomness = randomness
        pressure_release_per_minute = 0
        pressure_released = 0
        sequence = []
        while self.time != 0:
            sequence.append(self.position)
            if verbose:
                print("== Minute", 31-self.time, "==")
                print("Position:", self.position)
                for v, o in self.is_open.items():
                    if o:
                        print(" --- Valve", v, "OPEN ---")
            if self.flow_rate[self.position] != 0 and not self.is_open[self.position]:
                reward_to_open = self.flow_rate[self.position] * (self.time - 1)
            else:
                reward_to_open = 0
            if verbose:
                print("Reward to open valve", self.position, " = ", reward_to_open)
            where_to_move, possible_reward = self.generate_a_good_sequence()
            if len(where_to_move) != 0:
                if verbose:
                    print("We could move to valve", where_to_move[0], "with a possible reward of", possible_reward)
                action = self.connections[self.position].index(where_to_move[0])
                reward_to_move_and_open = self.reward(self.position, action)
            else:
                if verbose:
                    print("Can't move anymore")
                reward_to_move_and_open = 0
            if verbose:
                print("Doing it would release", reward_to_move_and_open, "pressure")
            if reward_to_open > reward_to_move_and_open and not self.is_open[self.position]:
                #print("Reward to open:", reward_to_open, "Reward to move and open:", reward_to_move_and_open)
                if verbose:
                    print("Opening valve", self.position)
                self.time -= 1
                self.is_open[self.position] = True
                pressure_released += pressure_release_per_minute
                pressure_release_per_minute += self.flow_rate[self.position]
            elif len(where_to_move) == 0:
                if verbose:
                    print("Sit tight")
                pressure_released += pressure_release_per_minute
                self.time -= 1
            else:
                # We move
                if verbose:
                    print("Moving to valve", where_to_move[0])
                pressure_released += pressure_release_per_minute
                self.time -= 1
                self.position = where_to_move[0]
            if verbose:
                print("Releasing", pressure_release_per_minute, "each minute")
        if verbose:
            print("Times out, released pressure:", pressure_released)
        return pressure_released, sequence

    def reset(self):
        self.position = 'AA'
        self.e_position = 'AA'
        for v, o in self.is_open.items():
            if o:
                self.is_open[v] = False

    def run_with_elephant(self, verbose=True, greedyness=5, randomness=50):
        self.time = 26
        self.greedyness = greedyness
        self.randomness = randomness
        pressure_release_per_minute = 0
        pressure_released = 0
        sequence = []
        while self.time != 0:
            sequence.append([self.position, self.e_position])
            if verbose:
                print("== Minute", 31-self.time, "==")
                print("Position:", self.position)
                print("Elephant pos:", self.e_position)
                for v, o in self.is_open.items():
                    if o:
                        print(" --- Valve", v, "OPEN ---")
            # PERSON
            if self.flow_rate[self.position] != 0 and not self.is_open[self.position]:
                reward_to_open = self.flow_rate[self.position] * (self.time - 1)
            else:
                reward_to_open = 0
            # ELEPHANT
            if self.flow_rate[self.e_position] != 0 and not self.is_open[self.e_position]:
                e_reward_to_open = self.flow_rate[self.e_position] * (self.time - 1)
            else:
                e_reward_to_open = 0
            # BOTH
            where_to_move, possible_reward = self.generate_a_good_sequence()
            where_to_move_e, possible_reward_e = self.generate_a_good_sequence('elephant')
            # PERSON
            if len(where_to_move) != 0:
                if verbose:
                    print("We could move to valve", where_to_move[0], "with a possible reward of", possible_reward)
                action = self.connections[self.position].index(where_to_move[0])
                reward_to_move_and_open = self.reward(self.position, action)
            else:
                if verbose:
                    print("Can't move anymore")
                reward_to_move_and_open = 0
            # ELEPHANT
            if len(where_to_move_e) != 0:
                action_e = self.connections[self.e_position].index(where_to_move_e[0])
                reward_to_move_and_open_e = self.reward(self.e_position, action_e)
            else:
                reward_to_move_and_open_e = 0
            # PERSON
            pressure_released += pressure_release_per_minute
            if reward_to_open > reward_to_move_and_open and not self.is_open[self.position]:
                self.time -= 0.5
                self.is_open[self.position] = True
                pressure_release_per_minute += self.flow_rate[self.position]
            elif len(where_to_move) == 0:  # Person doesn't move
                self.time -= 0.5
            else:  # Person move
                self.time -= 0.5
                self.position = where_to_move[0]
            # ELEPHANT
            if e_reward_to_open > reward_to_move_and_open_e and not self.is_open[self.e_position]:
                self.time -= 0.5
                self.is_open[self.e_position] = True
                pressure_release_per_minute += self.flow_rate[self.e_position]
            elif len(where_to_move_e) == 0:  # Elephant doesn't move
                self.time -= 0.5
            else:  # ELEPHANT move
                self.time -= 0.5
                self.e_position = where_to_move_e[0]

            if verbose:
                print("Releasing", pressure_release_per_minute, "each minute")
        if verbose:
            print("Times out, released pressure:", pressure_released)
        return pressure_released, sequence


env = Env()
env.read_data()
cost_to_open = 1
cost_to_move = 1

test_goal = 1651
done = False
epochs = 0
best_score = 0
greed = 10
randomness = 5
print("Starting with greed=", greed, "random actions=", randomness)
while not done:
    epochs += 1
    pressure_release, seq = env.run_with_elephant(verbose=False, greedyness=greed, randomness=7)
    if pressure_release > best_score:
        print("Epoch", epochs, "released", pressure_release, "pressure")
        print("By going going:", seq)
        best_score = pressure_release
    if np.mod(epochs, 1000) == 0:
        print("epochs:", epochs, "| Best score:", best_score)
    env.reset()

print("After", epochs, "epochs. Best score released", pressure_release, "pressure")
# Part 1: 1595
# Part 2: 2189
# greed= 10 random actions= 5
#Run 212466 released 2189 pressure
#By going going: [['AA', 'AA'], ['DQ', 'HX'], ['GF', 'BX'], ['GF', 'CD'], ['IH', 'CD'], ['FD', 'DI'], ['EK', 'ZB'], ['EK', 'ZB'], ['MI', 'OY'], ['QB', 'XG'], ['AW', 'XG'], ['AW', 'OY'], ['VK', 'ZB'], ['YQ', 'OI'], ['YQ', 'RG'], ['NK', 'RG'], ['SG', 'SJ'], ['XR', 'EB'], ['XR', 'CE'], ['TP', 'CE'], ['DT', 'LI'], ['DT', 'EZ'], ['TN', 'OU'], ['GU', 'OU'], ['TM', 'TL'], ['TM', 'TL']]