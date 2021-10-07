"""
Author: Jared Frazier
Project: OLA 2
File: sa.py
Class: CSCI 4350
Instructor: Dr. Joshua Phillips
Description: Module for performing simulated annealing.
"""

from distutils.util import strtobool

import numpy as np

from greedy import random_location, cli
from SumofGaussians import SumofGaussians


def annealing_schedule(cur_iter, max_iter):
    """Returns an annealed change.

    Linear schedule.

    https://en.wikipedia.org/wiki/Simulated_annealing
    """

    return (1 - (cur_iter+1)/max_iter)


def succession_probability(g_y, g_x, temperature):
    """Return probability of the candidate state being accepted.

    :param g_y: <class 'float'>
    :param g_x: <class 'float'>

    :return: <class 'float'>
    """

    return np.exp((g_y-g_x)/temperature)


def simulated_annealing(
        loc,
        sum_of_gauss,
        iter_threshold=100000, delta_threshold=1e-8,
        print_last_only=False, print_total_iterations=False):
    """Perform simulated annealing.


    :param loc: <class 'numpy.ndarray'> Location of point in
        d-dimensional space.
    :param sum_of_gauss: <class 'SumOfGaussians'> object for
        calculating derivative at a given location.
    :param iter_threshold: <lcass 'int'> Max number of iterations
        before termination of loop.
    :param delta_threshold: <lcass 'float'> Threshold for change to
        current location.
    :param step_size: <class 'float'>
    :param print_last_only: <class 'bool'>
    :param print_total_iterations: <class 'bool'>

    :return: None
    """

    iteration = 0
    while iteration < iter_threshold:

        # Compute temperature
        temp = annealing_schedule(iteration, iter_threshold)

        # Determine candidate move
        candidate_loc = loc + np.random.choice((-0.05, 0.05))

        # Edge cases
        if candidate_loc > 10:
            candidate_loc = 10

        elif candidate_loc < 0:
            candidate_loc = 0

        # Calculate energies of states
        candidate_energy = sum_of_gauss.Eval(candidate_loc)
        loc_energy = sum_of_gauss.Eval(loc)

        # Determine update of location
        if candidate_energy > loc_energy:
            loc = candidate_loc

        elif succession_probability(candidate_energy, loc_energy, temp) >= np.random.random():
            loc = candidate_loc

        # Log location and the energy at the state
        if not print_last_only:
            print(*loc, loc_energy)

        # Update iterations
        iteration += 1

    # Log location and the energy at the state of last only with iterations
    if print_last_only:
        print(*loc, loc_energy, iteration)


def main():

    # CLI
    parser = cli('simulated annealing sciript')
    args = parser.parse_args()

    # Random vector in default range of 10
    rand_vector = random_location(
        seed=args.seed,
        d_dimensions=args.d_dimensions)

    # Init sum of gaussians obj
    sog = SumofGaussians(
        dimensions=args.d_dimensions,
        number_of_centers=args.n_gaussians)

    # Perform gradient ascent
    simulated_annealing(
        rand_vector, sog,
        print_last_only=bool(strtobool(args.print_last_only)),
        print_total_iterations=bool(
            strtobool(args.print_total_iterations))),


if __name__ == '__main__':
    main()
