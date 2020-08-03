from src.observable_prob import *
from src.traversla_prob import *
from src.util import *
from src.viterbi import viterbi

def run(dataset, sequence_len):
    data = load_data(dataset)

    states = get_ordered_states(data)
    emissions = get_ordered_emmisions(data)

    transition_matrix = get_transition_matrix(data)
    emission_matrix = get_emission_matrix(data)

    # first_state = data[0][0]

    starting_probabilities = [1 / len(states)] * len(states)

    observed_sequence = list(map(lambda x: x[1], data[:sequence_len]))
    hidden_sequence = list(map(lambda x: x[0], data[:sequence_len]))

    result = viterbi(
        emissions,
        states,
        starting_probabilities,
        observed_sequence,
        transition_matrix,
        emission_matrix,
    )

    # print(observed_sequence)
    # print(hidden_sequence)
    # print(result)

    # print(list(hidden_sequence[i] == result[i] for i in range(sequence_len)))
    accuracy = sum(hidden_sequence[i] == result[i] for i in range(sequence_len)) / sequence_len * 100

    #print("Dataset: \"{}\"\nSample size: {}\nAccuracy: {}%\n".format(dataset, sequence_len, accuracy))
    print("{},{},{}".format(dataset, sequence_len, accuracy))


if __name__ == '__main__':
    datasets = [
        '../data/robot_no_momemtum.data',
        '../data/robot_with_momemtum.data',
        '../data/typos10.data',
        '../data/typos20.data'
    ]

    sample_sizes = [
        5,
        10,
        25,
        50,
        100,
        250,
        500,
        750,
        1000,
        2500,
        5000,
        10000,
        25000,
    ]

    print('dataset,size,accuracy')

    for dataset in datasets:
        for sample_size in sample_sizes:
            run(dataset, sample_size)

def random_array(set_of_elements, n):
    return [set_of_elements]