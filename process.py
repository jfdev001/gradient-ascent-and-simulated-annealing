"""Module for getting number of times sa outperformed or tied greedy."""

import argparse
import os
import pandas as pd
import numpy as np


def cli(description):
    parser = argparse.ArgumentParser(description)

    parser.add_argument(
        'sa_path',
        help='path to simulated annealing data folder.')

    parser.add_argument(
        'greedy_path',
        help='path to greedy data folder')

    parser.add_argument(
        'combos_path',
        help='path to combos.txt')

    parser.add_argument(
        'out_path',
        help='csv file based on pandas dataframe.')

    return parser


def sa_greater_than_greedy(sa_path, greedy_path, combo_line_num):
    """Bool for whether g is greater for sim annealing or greedy.

    Each line in file represents a different combination of inputs.
    If you split a line by spaces, then the second to last ele in the
    list is the g for that run. There are 16 total combinations
    so the combo line number will be between 0 - 15

    :param sa_path: <class 'str'> Path to simulated annealing txt
    :param greedy_path: <class 'str'> Path to greedy txt
    :param combo_line_num: <class 'int'>

    :return: <class 'bool'> True if simulated annealing g >= greedy g,
        False otherwise.
    """

    # Open sim annealing data
    with open(sa_path, 'r') as fobj:
        sa_data = fobj.readlines()

    # Get the g for the sim annealing data desired combo
    sa_g = sa_data[combo_line_num].split(' ')[-2]

    # Open greedy data
    with open(greedy_path, 'r') as fobj:
        greedy_data = fobj.readlines()

    # Get the g for greedy data desired comnbo
    greedy_g = greedy_data[combo_line_num].split(' ')[-2]

    # Compare and return result
    comp = sa_g >= greedy_g
    return comp


def main():

    # CLI
    parser = cli('process optimization data.')
    args = parser.parse_args()

    # Load up combos and strip newline
    combos = []
    with open(args.combos_path, 'r') as fobj:
        for line in fobj:
            combos.append(line.strip('\n'))

    # Must compare the same amount of files
    sa_files = [os.path.join(args.sa_path, f)
                for f in os.listdir(args.sa_path)]
    greedy_files = [os.path.join(args.greedy_path, f)
                    for f in os.listdir(args.greedy_path)]

    num_sa_files = len(sa_files)
    num_greedy_files = len(greedy_files)

    # Determine num files to loop for each combo
    if num_sa_files < num_greedy_files:
        file_num = num_sa_files
    else:
        file_num = num_greedy_files

    # Create dataframe
    df = pd.DataFrame()

    # Loop through combos and files
    print('\nProcess files....')
    for ix, combo in enumerate(combos):

        sa_greater_than_greedy_cnter = 0

        for f_num in range(file_num):

            file_g = sa_greater_than_greedy(
                sa_path=sa_files[f_num],
                greedy_path=greedy_files[f_num],
                combo_line_num=ix)

            if file_g:
                sa_greater_than_greedy_cnter += 1

        df[combo] = [sa_greater_than_greedy_cnter]

    # Write to file
    print('\nWrite df')
    df = df.transpose()
    df.to_csv(args.out_path)


if __name__ == '__main__':
    main()
