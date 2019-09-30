import numpy as np
import itertools

# Given a certain number of people, what is the probability that at least two of them
# have birthday on the same day?

# Analytical solution

# Let's compute the probability of all the people having birthday in different days

# The probability of 2 people not having birthday the same day is 364/365
# So to extend this to the rest of the group, we have to keep on multiplying
# 364/365 * 364/365 * 364/365 ... through all the possible combinations

number_of_people = 23

number_of_combinations = len(list(itertools.combinations(range(number_of_people), 2)))

p_not_happen = np.power(364/365, number_of_combinations)

p_happen = 1 - p_not_happen

print("Analytical solution:", p_happen)

# Simulation solution

n_iterations = 1000000
hits = 0
for _ in range(n_iterations):
    birthdays = np.random.uniform(0, 365, number_of_people).astype(int)
    if len(birthdays) != len(np.unique(birthdays)):
        hits += 1

print("Simulation solution:", hits/n_iterations)

# Simulation solution vectorized

def has_dup(x):
    return len(np.unique(x)) != len(x)


birthdays = np.random.uniform(0, 365, (n_iterations, number_of_people)).astype(int)
prob = np.sum(np.apply_along_axis(has_dup, 1, birthdays))/n_iterations


print("Simulation solution:", prob)
