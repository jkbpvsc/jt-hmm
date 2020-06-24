from src.util import get_ordered_states


def get_transition_matrix(data):
    states = list(map(lambda x: x[0], data))
    t = len(states)

    ordered_states = get_ordered_states(data)

    counted_traversals = [[1] * t] * t

    for i in range(t - 1):
        x1, x2 = ordered_states.index(states[i]), ordered_states.index(states[i + 1])

        counted_traversals[x1][x2] += 1

    return normalise_traversal_count(counted_traversals, data)


def normalise_traversal_count(counted_traversals, data):
    states = get_ordered_states(data)
    t = len(states)

    normalised_traversals = [[0] * t] * t

    for i in range(t):
        total_traversals = sum(counted_traversals[i])
        for j in range(t):
            normalised_traversals[i][j] = counted_traversals[i][j] / total_traversals

    return normalised_traversals
