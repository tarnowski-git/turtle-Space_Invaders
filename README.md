# turtle-Space Invaders

A simple Orinted Objected Programming Space Invaders-style game using Python, the Turtle Graphics module.

## Demo

![ScreenCapture_21 01 2020_03 10 44](https://user-images.githubusercontent.com/34337622/72769862-7d683480-3bfc-11ea-894f-03552e2fe301.gif)

## Technologies

-   Python 3.7
-   Turtle

## Prerequisites

-   [Python](https://www.python.org/downloads/)
-   [pip](https://pip.pypa.io/en/stable/installing/)
-   [pipenv](https://pipenv.readthedocs.io/en/latest/install/#make-sure-you-ve-got-python-pip)

## Installation

-   [Clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repo to your local machine using:

```
$ git clone https://github.com/tarnowski-git/turtle-Space_Invaders.git
```

-   Setup your [local environment](https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv):

```
# Spawn a shell with the virtualenv activated
$ pipenv shell

# Install dependencies
$ pipenv install

# Run script into local environment
$ pipenv run python space_invaders.py
```

-   Compile with Pyinstaller to exectutable file:

```
# Windows
pyinstaller --onefile --windowed space_invaders.py
```

## Sources

This game is based on [Christian Thompson](https://www.youtube.com/playlist?list=PLlEgNdBJEO-lqvqL5nNNZC6KoRdSrhQwK) Tutorial.

## License

This project is licensed under the terms of the [**MIT**](https://github.com/tarnowski-git/turtle-Space_Invaders/blob/master/LICENSE) license.
