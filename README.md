# Gradient Ascent and Simulated Annealing for Multivariate Gaussian

Implementation of and comparison for [Hill Climbing (aka Gradient Ascent, aka greedy best first search)](https://en.wikipedia.org/wiki/Hill_climbing) and [Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing) on a known function space modeled by a [multivariate Gaussian distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution).

For a summary of results, see `reoprt/report.pdf`.

# Installation

This repository makes use of Python's scientific computing/data analysis libraries NumPy and Pandas.

`pip install numpy pandas`

# Testing

Both simulated annealing and hill climbing can be tested on the generated multivariate gaussian space. Both algorithms make use of a command line interface which is available as a function named `cli` in `greedy.py`.

The input for both scripts can be shown using `python greedy.py -h` or `python sa.py -h`.

```
positional arguments:
  seed                  random number seed. (default: 0)
  d_dimensions          number of dimensions for exploration space. (default: 3)
  n_gaussians           number of gaussians. (default: 1)

optional arguments:
  -h, --help            show this help message and exit
  --iter_threshold ITER_THRESHOLD
                        max number of iterations before termination. (default: 100000)

logging:
  params for logging outputs.

  --print_last_only {True,False}
                        true to log optimization output at last step and iterations, false to log position only at all steps. (default: False)

greedy:
  params for greedy local search only.

  --step_size STEP_SIZE
                        step size for gradient ascent. (default: 0.01)
```

# Analysis

After running `sa.py` and `greedy.py` with the same arguments related to the Gaussian space (`seed `, `d_dimensions `, `n_gaussians`), the last two arguments being in combos.txt, `process.py` can be run to compare the performance of the algorithms.

# Future Work

Arbitrary function spaces and numerical differentiation might be implemented to avoid strictly traversing the multivariate Gaussian space.
