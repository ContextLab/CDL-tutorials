# Tutorials

This is a repo containing useful tutorials on different package and tools the [Contextual Dynamics Lab](http://www.context-lab.com) uses most.  Each tutorial is contained in its own folder.

In general, our tutorials are intended to cultivate and facilitate a "science hacker mindset" and provide some of the tools needed to thrive in an open science hackerspace.  As a place to start, you might be interested in viewing [this video](https://www.youtube.com/watch?v=Gin8_AITmS0), which introduces the science hacker mentality and provides an overview of many of the approaches we use in the lab.

## Using and running stuff
You can try running anything on your own system, but the *supported* method for injesting the tutorials is through our included [Docker](https://www.docker.com/) container. This will allow you to reproduce our computational environment, which is useful for ensuring that things will run the same on any physical system (tested on OSX/MacOS, Windows, Ubuntu, and Debian).  Instruction for setting up and using the Docker container are below (copied and modified from the [MIND](https://github.com/Summer-MIND/mind-tools) repo):

### One time setup
1. Install Docker on your computer using the appropriate guide below:
    - [OSX](https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac)
    - [Windows](https://docs.docker.com/docker-for-windows/install/)
    - [Ubuntu](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/)
    - [Debian](https://docs.docker.com/engine/installation/linux/docker-ce/debian/)
2. Launch Docker and adjust the preferences to allocate sufficient resources (e.g. > 4GB RAM)
3. Build the docker image by opening a terminal in this repo folder and enter `docker build -t cdl .`
4. Use the image to create a new container for the workshop
    - The command below will create a new container that will map your computer's `Desktop` to `/mnt` within the container, so that location is shared between your host OS and the container. Feel free to change `Desktop` to whatever folder you prefer to share instead, but make sure to provide the full path. The command will also share port `9999` with your host computer so any jupyter notebooks launched from *within* the container will be accessible at `localhost:9999` in your web browser
    - `docker run -it -p 9999:9999 --name cdl -v ~/Desktop:/mnt cdl `
    - You should now see the `root@` prefix in your terminal, if so you've successfully created a container and are running a shell from *inside*!
5. To launch any of the notebooks: `jupyter lab --port=9999 --no-browser --ip=0.0.0.0 --allow-root`

### Using the container after setup
1. You can always fire up the container by typing the following into a terminal
    - `docker start cdl && docker attach cdl`
    - When you see the `root@` prefix, letting you know you're inside the container
2. Close a running container with `ctrl + d` from the same terminal you used to launch the container, or `docker stop cdl` from any other terminal

## Getting help

### CDL lab members
If you need help or if something is unclear, join our slack's `computrons` channel [here](https://context-lab.slack.com/messages/C63L5EBKK/).

### Non-CDL lab members
Post a [GitHub issue](https://github.com/ContextLab/CDL-tutorials/issues) or [get in touch](http://www.context-lab.com/contact/)!

## Want to contribute?  Yes please!
Our science is made better through the hard work and dedication of the science community.  We are committed to giving back, and we hope you'll join us in that effort!

### Proposing new tutorial topics or other suggestions
If you have a new tutorial idea or suggestion, please post an [GitHub issue](https://github.com/ContextLab/CDL-tutorials/issues) with your suggested change or addition.  That will give everyone an opportunity to weigh in on and discuss your proposal.  This is especially important prior to putting in efforts to substantially modify existing content (e.g. to avoid wasted effort).  Please check through the existing issues list to make sure that your idea hasn't already been proposed, and to get a sense of which issues are being actively worked on (and who is working on them).  You may also want to add comments to existing issues to help clarify or add to an existing idea.

We track all tutorial ideas through [this project board](https://github.com/ContextLab/CDL-tutorials/projects/1).  To add your issue to the backlog, select the "Tutorials" project from the project dropdown list when you create the issue or edit the issue details.  You can add any additional thoughts, commentary, arguments for prioritizing the given tutorial, offers to work on the given tutorial, etc. via the issue comments.

### Modifying existing content
To contribute by adding, subtracting, or modifying the existing content, please:
- fork this repository
- make your changes to your fork
- submit a pull request (which we'll review and either request changes or merge into the main codebase)

If you are contributing Python code, we prefer Python 3 and try to follow the [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/) when possible.

### Contributing new tutorials
We provide a sample suggested tutorial template [here](https://github.com/ContextLab/CDL-tutorials/tree/master/tutorial_template).  Your tutorial doesn't necessarily have to follow that format, but the example provides a general sense of the sorts of things we hope each tutorial will include.

If you have your own tutorial ideas, feel free to start a new folder, add your stuff (potentially by modifying a copy of the tutorial template), and submit a pull request!

## Questions? Comments? Concerns?
[Let us know](http://www.context-lab.com/contact/)! We love to hear how the community is using our work and how we can make it better! 
