
def loadFromFilePath(file):
    f = open(file, "r")

    state_list = []
    for line in f:
        state_list.append(line.strip())
    str = ' '.join(state_list)
    state_list = str.split()
    state_list[state_list.index('*')] = '0'

    dim = int(state_list[0])

    if (len(state_list) - 1 != dim**2):
        return False
    for x in state_list:
        if(x.isdigit() == False):
            return False


    state_list = [int(x) for x in state_list]
    return(state_list)

def computeNeighbors(state):
    state = list(state)

    base_state = state[1:]

    if(type(base_state[0]) == tuple):
        base_state = list(base_state[0])
    neighbors = []

    blank_index = base_state.index(0)

    if(blank_index >= dimension):
        up_copy = base_state.copy()
        to_swap = base_state[blank_index - dimension]
        up_copy[blank_index],up_copy[blank_index - dimension] = up_copy[blank_index - dimension], up_copy[blank_index]
        neighbors.append((to_swap,tuple(up_copy)))
    if (blank_index < len(base_state)-dimension):
        down_copy = base_state.copy()
        to_swap = base_state[blank_index + dimension]
        down_copy[blank_index], down_copy[blank_index + dimension] = down_copy[blank_index + dimension], down_copy[blank_index]
        neighbors.append((to_swap, tuple(down_copy)))
    if((blank_index + 1) % dimension != 0):
        right_copy = base_state.copy()
        to_swap = base_state[blank_index + 1]
        right_copy[blank_index], right_copy[blank_index + 1] = right_copy[blank_index + 1], right_copy[blank_index]
        neighbors.append((to_swap,tuple(right_copy)))
    if((blank_index) % dimension != 0):
        left_copy = base_state.copy()
        to_swap = base_state[blank_index - 1]
        left_copy[blank_index],left_copy[blank_index - 1] = left_copy[blank_index - 1], left_copy[blank_index]
        neighbors.append((to_swap, tuple(left_copy)))
    return neighbors
def isGoal(state):
    state = list(state)
    goal = [x for x in range(dimension**2)]
    goal = goal[1:]
    goal.append(0)
    print("state 1 " + str(state[1:]))
    return state[1:] == goal
def bfs(state):
    state = tuple(state)
    frontier = [state]
    discovered = set(state)
    parents = {state: None}

    while len(frontier) != 0:
        current_state = frontier.pop(0)
        discovered.add(current_state)
        if isGoal(current_state):
            return traceParents(parents, current_state)
        for neighbor in computeNeighbors(current_state):
            if neighbor[1] not in discovered:
                frontier.append(neighbor)
                discovered.add(neighbor)
                parents[neighbor[1]] = (neighbor[0], current_state[1])

def dfs(state):
    state = tuple(state)
    frontier = [state]
    discovered = set(state)
    parents = {state: None}
    while len(frontier) != 0:
        current_state = frontier.pop(-1)
        discovered.add(current_state)
        if isGoal(current_state):
            return traceParents(parents, current_state)
        for neighbor in computeNeighbors(current_state):
            if neighbor[1] not in discovered:
                frontier.append(neighbor)
                discovered.add(neighbor)
                parents[neighbor[1]] = (neighbor[0], current_state)
def bds(state):
    goal = [x for x in range(dimension ** 2)]
    goal.append(0)
    goal = tuple(goal)

    state = tuple(state)
    frontier = [state]
    frontier_back = [goal]

    discovered = set(state)
    discovered_back = set(goal)

    parents = {state: None}
    parents_back = {goal: None}

    while len(frontier) != 0 or len(back_frontier) != 0:
        current_state = frontier.pop(0)
        discovered.add(current_state)
        if current_state in discovered_back:
            return traceParents(parents, current_state) + traceParents(parents_back,current_state)[::-1]
        for neighbor in computeNeighbors(current_state):
            if neighbor[1] not in discovered:
                frontier.append(neighbor)
                discovered.add(neighbor)
                parents[neighbor[1]] = (neighbor[0], current_state)

        current_state = frontier_back.pop(0)
        discovered_back.add(current_state)
        if current_state in discovered:
            return traceParents(parents, current_state) + traceParents(parents_back,current_state)[::-1]
        for neighbor in computeNeighbors(current_state):
            if neighbor[1] not in discovered_back:
                frontier_back.append(neighbor)
                discovered_back.add(neighbor)
                parents_back[neighbor[1]] = (neighbor[0], current_state)

def traceParents(parents, current_state):
    trace_list = []
    while parents[current_state]:
        trace_list = [parents[current_state][0]] + trace_list
        current_state = parents[current_state]
    return trace_list


state_list = loadFromFilePath("input.TXT")

if(state_list != False):
    dimension = state_list[0]

    # print(bfs(state_list))
    # print(dfs(state_list))
    # print(bds(state_list))
else:
    print('something is wrong with the input file')
