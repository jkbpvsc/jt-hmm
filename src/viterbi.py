import numpy as np

def viterbi(
        observations,
        states,
        starting_probabilities,
        sequence_of_observations,
        transition_matrix,
        emission_matrix,
):
    t = len(sequence_of_observations) - 1

    z = [0] * (t + 1)
    x = [0] * (t + 1)

    t1 = [[0] * len(sequence_of_observations) for _ in range(len(states))]
    t2 = [[0] * len(sequence_of_observations) for _ in range(len(states))]

    index_of_first_obs = observations.index(sequence_of_observations[0])
    for i in range(len(states)):
        t1[i][0] = starting_probabilities[i] * emission_matrix[i][index_of_first_obs]
        t2[i][0] = 0

    for j in range(1, len(sequence_of_observations)):
        pos_of_observation = observations.index(sequence_of_observations[j])
        for i in range(len(states)):
            prob_of_seeing_emission = emission_matrix[i][pos_of_observation]
            max_value = max([t1[k][j - 1] * transition_matrix[k][i] * prob_of_seeing_emission for k in range(len(states))])
            t1[i][j] = max_value

            calculations = [(k, t1[k][j - 1] * transition_matrix[k][i] * prob_of_seeing_emission) for k in range(len(states))]

            arg_max, _ = max(calculations, key=lambda x: x[1])
            t2[i][j] = arg_max

    calculations = [ (k, t1[k][t]) for k in range(len(states)) ]
    arg_max, asda = max(calculations, key=lambda x: x[1])
    z[t] = arg_max
    x[t] = states[z[t]]

    for j in range(t, 0, -1):
        z[j - 1] = t2[z[j]][j]
        x[j - 1] = states[z[j - 1]]

    return list(x)






