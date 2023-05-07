from random import uniform
from math import exp


def simulated_annealing(temps, start_pos, cost_func, pos_func, inside_loop = 10):
    pos = start_pos
    energy1 = cost_func(pos)
    # remember best pos and its energy
    ans = pos
    ans_energy = energy1
    # energies = []
    for temp in temps:
        # print(f"temp: {temp}")
        for _ in range(inside_loop):
            next_pos = pos_func(pos)
            energy2 = cost_func(next_pos)
            delta_energy = energy2 - energy1
            # print(f"energy1: {energy1}")
            # print(f"energy2: {energy2}")
            # print(f"delta_energy: {delta_energy}")

            # update best pos if needed
            if energy2 < ans_energy:
                # print("Improved!")
                ans = next_pos
                ans_energy = energy2
            if delta_energy < 0 or exp(-delta_energy / temp) > uniform(0, 1):
                # print("Change!")
                pos = next_pos
                energy1 = energy2
    # print("RETURNDED")
    return ans, ans_energy
    # return ans


def generate_temp_tab(max_temp, min_temp, temp_func):
    temp = max_temp
    tab = []
    while temp > min_temp:
        tab.append(temp)
        temp = temp_func(temp)
    return tab

