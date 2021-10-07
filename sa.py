"""
Author: Jared Frazier
Project: OLA 2
File: sa.py
Class: CSCI 4350
Instructor: Dr. Joshua Phillips
Description: Module for performing simulated annealing.


"""

import numpy as np
from greedy import random_location, cli
from SumofGaussians import SumofGaussians


def annealing_schedule(cur_iter, max_iter):
    """Returns an annealed change.

    https://en.wikipedia.org/wiki/Simulated_annealing
    """

    return (1 - (cur_iter+1)/max_iter)


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
    ascend = True
    while ascend and iteration < iter_threshold:
        pass

        # Calculate step


def main():

    # CLI .. same as pre
    pass


if __name__ == '__main__':
    main()
