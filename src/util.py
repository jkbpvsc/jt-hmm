import re

def load_data(path):
    with open(path, 'r') as fp:
        out = []
        for i, line in enumerate(fp):
            split = line.replace('\n', '')
            if re.match('^\S+\s\S+$', split):
                split = split.split(' ')
                a, b = split[0], split[1]
                out.append((a, b))
        return out


def unique(x):
    return list(set(x))

def get_ordered_states(data):
    return unique(list(map(lambda x: x[0], data)))

def get_ordered_emmisions(data):
    return unique(list(map(lambda x: x[1], data)))

def get_elm_post(e, array):
    return array.index(e)