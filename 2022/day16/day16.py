import numpy as np

# All valves begin closed.
# 30 minutes
# total eventual pressure release = time_remaining * valve_flow_rate
# 1 minute to move to a valve, 1 min to open.

# Figure out the network of nodes.
# in test, AA connects to DD, II and BB.
# DD is worth 20, II: 0 and BB: 13.
# Should move to DD
# Travelling salesman
# Need pointers between nodes
# Cost is one
# prioritize close and high flow rate first
# each node has a cost from each node (we should be able to compute it)
# The node with the highest reward should be prioritized
# reward = benefit - cost
#
#     .-->  agent -.
#    / state        \
#   | reward         | action
#    \              /
#     environment <'


#def reward(state):
#    r = []
#    for valves in connections[state]:
#        r.append(flow_rate[valves] * (time - 2))
#    highest_reward_of_connections = max(r)
#    return flow_rate[state] * (time - 1) + 0.9^steps * highest_reward_of_connections


def reward(state, action, steps):
    visited_states.append(state)
    if action == 'open':
        #print("Open valve", state, "releases", flow_rate[state] * (time - steps), "pressure over", time - steps, "minutes")
        if is_open[state]:
            return 0
        return flow_rate[state] * (time - steps - 1)
    r = 0
    steps += 1
    for states in connections[state]:
        if visited_states.__contains__(states):
            continue
        for a in actions:
            if is_open[states] and a == 'open':
                continue
            for s, st, ac, re in R:
                if s == state and st == states and ac == a:
                    return re
            r_of_s = reward(states, a, steps) * (0.9**steps)
            R.add((state, states, a, r_of_s))
            ##print("Move from", state, "to", states, "with ", steps, "steps and then ", a, "releases", r_of_s)
            if r_of_s > r:
                r = r_of_s
    return r



data = open('test.txt').read().split("\n")
flow_rate = {}
connections = {}
is_open = {}
for line in data:
    words = line.split()
    valve = words[1]
    # The benefit (part of the reward) of opening a valve in the current state
    flow_rate[valve] = int(words[4].split(';')[0].split('=')[1])
    # All possible future states from the current state
    connections[valve] = line.split('valve')[1].replace('s', '').replace(' ', '').split(',')
    is_open[valve] = False

# Compute reward for each valve

time = 30
position = 'AA'
t = 0
actions = ['move', 'open']
pressure_released = 0
pressure_released_each_minute = 0
last_visited = 'AA'
while time != 0:
    print("== Minute", 31 - time, "== Position:", position)
    visited_states = []
    R = set()
    step = 0
    reward_open = reward(position, 'open', step)
    move_to = []
    reward_move = reward(position, 'move', step)
    if reward_move > reward_open or is_open[position]:
        max_reward = 0
        for s, st, act, r in R:
            if max_reward < r and position == s and last_visited is not st:
                max_reward = r
                action = act
                to_state = st
                from_state = s
        print("Should move to", to_state, "from", from_state, "and then", action, "potential of releasing", max_reward, "pressure")
        if from_state == position:
            last_visited = position
            position = to_state
            print("Move to valve", position)
    else:
        is_open[position] = True
        #pressure_released += flow_rate[position] * time
        print("We open the valve at", position, "releasing", flow_rate[position], "pressure for a total of", flow_rate[position]*time)
    for v, o in is_open.items():
        if o:
            pressure_released_each_minute += flow_rate[v]
            print("Valve", v, "is open")
    pressure_released += pressure_released_each_minute
    time -= 1
print("Pressure released:", pressure_released)
moves_taken = []
pressure_released = 0
done = False
#while not done: