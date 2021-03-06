"""
Author: Jared Frazier
Project: OLA 2
File: greedy.py
Class: CSCI 4350
Instructor: Dr. Joshua Phillips
Description: Module for performing gradient ascent.
"""

import argparse
from distutils.util import strtobool
import numpy as np
from SumofGaussians import SumofGaussians


def random_location(seed, d_dimensions, in_range=10):
    """Generate a random location in a D-dimensional cube.

    :param seed: <class 'int'>
    :param d_dimensions: <class 'int'>
    :param n_gaussians: <clas 'int'>
    :param in_range: <class 'int'> Multiplied by random uniform vector
        to get vector in certain range.

    :return: <class 'numpy.ndarray'>
    """

    # Set the seed
    np.random.seed(seed)

    # Vector containing random values in [0, 1]
    rand_uniform_vector = np.random.rand(d_dimensions)

    # Multiply each ele of uniform vector
    rand_vector_in_range = rand_uniform_vector * in_range

    # Return D-dimensional vector in the specified range
    return rand_vector_in_range


def gradient_ascent(
        loc,
        sum_of_gauss,
        iter_threshold=100000, delta_threshold=1e-8, step_size=0.01,
        print_last_only=False):
    """Performs gradient ascent.

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

    ascend = True
    iteration = 0
    while ascend and iteration < iter_threshold:

        # Calculate the change based on step size and derivative
        # of the vector
        delta = step_size * sum_of_gauss.Deriv(loc)

        # Update location
        loc = delta + loc

        # Evaluated center
        eval_ = sum_of_gauss.Eval(loc)

        # Log location
        if not print_last_only:
            if isinstance(loc, np.ndarray):
                print(*loc, eval_)
            else:
                print(loc, eval_)

        # Check to see if the mean absolute change is <= delta threshold...
        # considers all dimensions because the change in all dimensions
        # should be very small to indicate convergence
        if np.mean(np.absolute(delta)) <= delta_threshold:
            ascend = False

        # Update loop counter
        iteration += 1

    # Logging
    if print_last_only:
        if isinstance(loc, np.ndarray):
            print(*loc, eval_, iteration)
        else:
            print(loc, eval_, iteration)


def cli(description):
    """Command line interface for module."""

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        'seed',
        help='random number seed. (default: 0)',
        type=int,
        default=0)

    parser.add_argument(
        'd_dimensions',
        help='number of dimensions for exploration space. (default: 3)',
        type=int,
        default=3)

    parser.add_argument(
        'n_gaussians',
        help='number of gaussians. (default: 1)',
        type=int,
        default=1)

    parser.add_argument(
        '--iter_threshold',
        help='max number of iterations before termination. (default: 100000)',
        type=int,
        default=100000)

    logging = parser.add_argument_group(
        'logging',
        'params for logging outputs.')

    logging.add_argument(
        '--print_last_only',
        choices=['True', 'False'],
        help='true to log optimization output at last step and iterations, \
            false to log position only at all steps. (default: False)',
        type=str,
        default='False')

    greedy = parser.add_argument_group(
        'greedy',
        'params for greedy local search only.')

    greedy.add_argument(
        '--step_size',
        help='step size for gradient ascent. (default: 0.01)',
        type=float,
        default=0.01)

    return parser


def main():

    # CLI
    parser = cli('gradient ascent script')
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
    gradient_ascent(
        rand_vector, sog,
        step_size=args.step_size,
        iter_threshold=args.iter_threshold,
        print_last_only=bool(strtobool(args.print_last_only)))


if __name__ == '__main__':
    main()
