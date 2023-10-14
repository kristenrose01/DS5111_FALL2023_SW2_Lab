# DS5111_FALL2023_SW2_Lab

### What did you have to do to get `make` to work?

To get `make` to work, I had to install it using `sudo apt install make`.

### Similarly for `python3 -m venv env`, what did you have to do? (How likely are you to have guessed that without their clear error message?)

The error message provided clear instructions to run the following command to install the python3-venv package: `apt install python3.10-venv`. I also had to include `sudo` at the beginning of the command. This was helpful because it prevented me from having to search through Google/StackExchange to determine how to resolve the error.  

### Both the pip install on the requirements.txt, and the call to run bin/clockdeco\_param.py should be activating the virtual environment first. In other words, there are two bash commands separated by a `;`, the first of which activates. Why can't we just do that on a separate line? In other words, why do we have to do that in one line and separate the commands with a `;`

Each line in a makefile is ran separately. If you do not activate the virtual environment on the same line as these other bash commands, separated by a `;`, these commands will run without going into the virtual environment first.

### As it is, both the `env` and `tests` jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job `run`? What would happen if you accidentally had a file called `run` in your directory? What can we do to fix this?

If there was a file called `run` in the directory, there may be confusion when `make run` is called. Using `.PHONY` makes it clear that the task is not related to a specific file or directory.

### The code provided to you for the test file starts with two lines, seemingly to append something to `sys.path`. What is the purpose of these lines?

The second line appends the current working directory to the end of the `sys.path`. This allows the clockdeco\_param.py file to be imported starting with `bin` as the path, since the directory has already been set.   

## Extra Credit

### Execute sudo apt install tree, and use that application to print out the file and directory structure, just as it is shown in this document at the top.

`tree -a -I 'lib|env|.git|.pytest_cache|__pycache__' /home/ubuntu/DS5111_FALL2023_SW2_Lab` 

### do a pip list or pip freeze and call out versions of the pytest and pylint packages in your requirements.txt.

Added to requirements.txt:
pylint==2.17.5
pytest==7.4.2
