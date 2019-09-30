import numpy as np
import itertools
import octave.helper as helper

def analytic(n, k):
    if helper.parity(n) != helper.parity(k):
        print("Analytic probability: 0.0")
    else:
        combinations = list(itertools.combinations(range(n), int((n + k)/2)))
        n_combinations = len(combinations)
        prob = n_combinations/(2**n)
        print("Analytic probability:", prob)

def simulation(n, k, x):
    hits = 0
    for _ in range(x):
        pos = 0
        for _ in range(n):
            pos += np.random.choice([-1, 1])
        if pos == k:
            hits += 1

    print("Simulated probability:", hits/x)

def simulation_vectorial(n, k, x):
    final_positions = np.sum(np.random.choice([-1, 1], (x, n)), axis=1)
    prob = np.sum(final_positions == k)/x

    print("Simulated probability:", prob)


def random_walk(n, k, x):
    analytic(n, k)
    print("começou o calculo com for")
    simulation(n, k, x)
    print("começou o calculo vetorizado com numpy")
    simulation_vectorial(n, k, x)


random_walk(8, 6, 100000)

