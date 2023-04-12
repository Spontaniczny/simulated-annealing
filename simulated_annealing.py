from random import uniform
from math import exp


def simulated_annealing(temps, start_pos, cost_func, pos_func):
    pos = start_pos
    energy1 = cost_func(pos)
    # remember best pos and its energy
    ans = start_pos
    ans_energy = energy1
    for temp in temps:
        for _ in range(10):
            next_pos = pos_func(pos)
            energy2 = cost_func(next_pos)
            delta_energy = energy1 - energy2
            # update best pos if needed
            if energy2 < ans_energy:
                ans = next_pos
                ans_energy = energy2
            if delta_energy > 0 or exp(delta_energy / temp) > uniform(0, 1):
                pos = next_pos
                energy1 = energy2
    return ans, ans_energy
    # return ans


def generate_temp_tab(max_temp, min_temp, temp_func):
    temp = max_temp
    tab = []
    while temp > min_temp:
        tab.append(temp)
        temp = temp_func(temp)
    return tab

