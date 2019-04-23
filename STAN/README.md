# PySTAN

PyStan is the Python interface for Stan, a powerful statistical modelling language

You write the model in the Stan language, Stan compiles the model into C, and then you compile and fit the model in Python! Magic!

I recommend reading the [User Guide](https://mc-stan.org/docs/2_19/stan-users-guide/index.html) before trying to create a model, especially Part 2: Programming Techniques, which teaches you how to describe models in the Stan language. Part 1 is useful for understanding different distributions, and Bayesian modelling as a whole.
These models are somewhat difficult to debug, due to the fact that the model is compiled by Stan in C, and the stack traces are sparse. It is vitally important, especially in Stan, to know what you are doing *before* you start coding.

## Installing PyStan
It is recommended that PyStan be installed using conda on Linux or Mac, as Stan only *partially* supports Windows.

1. To install Stan, first [install Anaconda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) (not Miniconda!)
2. Then, create an environment with `conda create -n stan python`
3. Install PyStan with `conda install pystan`
4. If this doesn't work, try reinstalling Cython or Numpy, or resetting your conda env

Alternatively, you can use the Docker container!

## Play with Stan!

Run the notebook in Jupyter! Using the example as a template, generate some data and try to fit some different models.
Change hyperparameters and see the effect.
