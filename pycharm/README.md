# PyCharm

PyCharm is an integrated development environment (IDE) meant for developing and/or building software in python.
PyCharm is a GUI (unlike other text editors) and here are just a few reasons it's awesome:

- Debugger
- Refactoring made easy
- Project management with interpreter
- Code completion/hints
- Git visualization in editor
- Code coverage


# Getting Started

+ Clone or pull the latest from this repo: `git clone https://github.com/ContextLab/CDL-tutorials.git`

+ Install [PyCharm](https://www.jetbrains.com/pycharm/) professional edition

+ Click `Open` and navigate to this PyCharm tutorial.

# Configure the Python Interpreter

+ Click `Settings / Preferences dialog (⌘,)` and click on `Project Interpreter`

+ To begin, select Python 2.

# Debugging

+ Open `examples/example_debug.py`

+ Go through PEP8 formatting hints and fix

+ Right click and select `Run`

+ Right click and select 'Debug'

+ Edit configurations to appropriate python interpreter

# Profiler

+ Open `examples/example_profile.py`

+ Right click and select `Profile`

# Using Docker as a Remote Interpreter

## Configure and Run Docker Image

+ Follow the instructions in for the Docker tutorial. We will be using the CDL docker as our environment
(note: this feature is only supported in the professional edition of PyCharm, so be sure to download that version).

+ Build the docker image.  Make sure you have docker running, navigate to your
local copy of the Docker repo and execute the line: `docker build -t cdl .`. This will
create a docker image from the instructions specified in Dockerfile.

+ To launch the docker image (for the first time) run the following line:
`docker run -it -p 9999:9999 --name CDL -v <absolute-path-to-your-docker-repo>:/cdl/ cdl`

+ Open the `Settings / Preferences dialog (⌘,)`, click `Build, Execution, Deployment` and then `Docker`.

+ Add a Docker configuration (The Add `+` button) and specify how to connect to the Docker daemon.

+ In the Docker tool window `(View | Tool Windows | Docker)`, select the Docker icon,
and then either click the Connect button or select `Connect` from the context menu.

## Define a Docker-based remote interpreter

+ Open the Settings dialog (press ⌘, or click settings on the main toolbar).

+ Click the Project Interpreter page, on this page click the gear icon next to the Project Interpreter field,
and choose Add from the drop-down list.

+ In the dialog box that opens, select the Docker option, from the drop-down lists select the Docker
server (if the server is missing, click New...) and image name.

+ For more information, check this out: https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html

+ Now you can go ahead and run your script in a docker container!