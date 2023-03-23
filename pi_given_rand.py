'''Estimate pi given that Y_AXISou have random (0,1)'''

import random


def estimate_pi(limit):
    '''Run estimate'''
    num_point_circle = 0
    num_point_total = 0
    for _ in range(limit):
        x_axis = random.uniform(0, 1)
        y_axis = random.uniform(0, 1)
        distance = x_axis**2 + y_axis**2
        if distance <= 1:
            num_point_circle += 1
        num_point_total += 1

    return 4 * num_point_circle/num_point_total
