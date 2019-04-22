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

### Alternatively, you can use the Docker container

1. Install Docker on your computer using the appropriate guide below:
    - [OSX](https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac)
    - [Windows](https://docs.docker.com/docker-for-windows/install/)
    - [Ubuntu](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/)
    - [Debian](https://docs.docker.com/engine/installation/linux/docker-ce/debian/)
2. Launch Docker and adjust the preferences to allocate sufficient resources (e.g. > 4GB RAM)
3. Build the docker image by opening a terminal in the desired folder and enter `docker build -t stan .`  
4. Use the image to create a new container for the workshop
    - The command below will create a new container that will map your computer's `Desktop` to `/mnt` within the container, so that location is shared between your host OS and the container. Feel free to change `Desktop` to whatever folder you prefer to share instead, but make sure to provide the full path. The command will also share port `8888` with your host computer so any jupyter notebooks launched from *within* the container will be accessible at `localhost:8888` in your web browser (or `192.168.99.100:8888` if using Docker Toolbox)
    - `docker run -it -p 8888:8888 --name stan -v ~/Desktop:/mnt contextualdynamicslab/supereeg `
    - You should now see the `root@` prefix in your terminal, if so you've successfully created a container and are running a shell from *inside*!
5. To launch Jupyter: `jupyter notebook --no-browser --ip=0.0.0.0 --allow-root`
6. (Optional) Connect Docker to [PyCharm](https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html) or another IDE


## Play with Stan!

Run the notebook in Jupyter! Using the example as a template, generate some data and try to fit some different models.
Change hyperparameters and see the effect.
