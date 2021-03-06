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
        print_last_only=False):
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

    :return: None
    """

    iteration = 0
    while iteration < iter_threshold:

        # Compute temperature
        temp = annealing_schedule(iteration, iter_threshold)

        # Determine candidate move
        # TODO: Should be continuous sampling not random between 2
        # choices!!
        candidate_loc = loc + np.random.choice((-0.05, 0.05))

        # Edge cases -- sets dim with out of bound step to max or min
        # in range
        if np.greater(candidate_loc, 10).any():
            greater_bool_arr = np.greater(candidate_loc, 10)
            greater_ix_arr = np.where(greater_bool_arr)
            candidate_loc[greater_ix_arr] = 10

        elif np.less(candidate_loc, 0).any():
            less_bool_arr = np.less(candidate_loc, 0)
            less_ix_arr = np.where(less_bool_arr)
            candidate_loc[less_ix_arr] = 0

        # Calculate energies of states -- scalars
        candidate_energy = sum_of_gauss.Eval(candidate_loc)
        loc_energy = sum_of_gauss.Eval(loc)

        # Determine update of location
        if candidate_energy > loc_energy:
            loc = candidate_loc

        elif succession_probability(candidate_energy, loc_energy, temp) >= np.random.random():
            loc = candidate_loc

        # Log location and the energy at the state
        if not print_last_only:
            if isinstance(loc, np.ndarray):
                print(*loc, loc_energy)
            else:
                print(loc, loc_energy)

        # Update iterations
        iteration += 1

    # Log location and the energy at the state of last only with iterations
    if print_last_only:
        if isinstance(loc, np.ndarray):
            print(*loc, loc_energy, iteration)
        else:
            print(loc, loc_energy, iteration)


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
        rand_vector, sog, iter_threshold=args.iter_threshold,
        print_last_only=bool(strtobool(args.print_last_only)))


if __name__ == '__main__':
    main()
