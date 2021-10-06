""" 
Author: Jared Frazier
Project: OLA 2
File: greedy.py
Class: CSCI 4350
Instructor: Dr. Joshua Phillips
Description: Module for performing gradient ascent.
"""

import argparse
import numpy as np
import SumofGaussians


def random_location(seed, d_dimensions, n_gaussians):
    """Generate a random location in a D-dimensional cube.

    :param seed: <class 'int'>
    :param d_dimensions: <class 'int'>
    :param n_gaussians: <clas 'int'>

    :return: <class 'numpy.ndarray'>
    """
    pass


def gradient_ascent(
        loc,
        iter_threshold=100000, delta_threshold=1e-8, step_size=0.01,
        print_last_only=True):
    """Performs gradient ascent.

    :param loc: <class 'numpy.ndarray'> Location of point in 
        d-dimensional space.
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
        delta = step_size * derivative(loc)

        # Update location
        loc = delta + loc

        # Log location
        if not print_last_only:
            print(loc, delta)

        # Check to see if absolute change is <= delta threshold
        if abs(delta) <= delta_threshold:
            ascend = False

        # Update loop counter
        iteration += 1

    # Log last update location
    if print_last_only:
        print(loc, delta)


def main():
    pass


if __name__ == '__main__':
    main()
