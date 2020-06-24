from src.util import unique, get_ordered_emmisions, get_ordered_states


def get_observables_for_state(state, data):
    emissions = get_ordered_emmisions(data)

    observables_count = [1] * len(emissions)

    filtered_data = list(filter(lambda e: e[0] == state, data))

    for s, e in filtered_data:
        e_pos = emissions.index(e)
        observables_count[e_pos] += 1

    return normalize_observables(observables_count, data)


def normalize_observables(counted_observables, data):
    emissions = get_ordered_emmisions(data)

    total_count = sum(counted_observables)
    normalized_observables = [0] * len(emissions)

    for e in emissions:
        e_pos = emissions.index(e)
        normalized_observables[e_pos] = counted_observables[e_pos] / total_count

    return normalized_observables


def get_emission_matrix(data):
    states = get_ordered_states(data)

    state_count = [None] * len(states)
    for i in range(len(states)):
        state = states[i]
        state_count[i] = get_observables_for_state(state, data)

    return state_count
