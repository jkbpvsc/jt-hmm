from src.observable_prob import *
from src.traversla_prob import *
from src.util import *
from src.viterbi import viterbi
from random import *


if __name__ == '__main__':
    data = load_data('../data/robot_with_momemtum.data')

    states = get_ordered_states(data)
    emissions = get_ordered_emmisions(data)

    transition_matrix = get_transition_matrix(data)
    emission_matrix = get_emission_matrix(data)

    first_state = data[0][0]

    starting_probabilities = [1 / len(states)] * len(states)

    observed_sequence = list(map(lambda x: x[1], data[:200]))

    result = viterbi(
        emissions,
        states,
        starting_probabilities,
        observed_sequence,
        transition_matrix,
        emission_matrix,
    )

    print(observed_sequence)
    print(result)


def random_array(set_of_elements, n):
    return [set_of_elements]