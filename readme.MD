# Alien Invasion Game

Alien Invasion is a Python-based game built using the Pygame library, following the *Python Crash Course* book project. In this game, players control a spaceship and must defend against waves of aliens descending from above. This project demonstrates essential programming concepts and game development techniques using Python and Pygame.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Control a spaceship to shoot down aliens.
- Alien waves that progressively increase in difficulty.
- Score tracking for players.
- Game over condition when aliens reach the bottom of the screen or the player loses all lives.
- Modular, easily extendable code for adding new features or game mechanics.

## Installation

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/alien-invasion.git
cd alien-invasion
```

## Environment Setup

This project uses Conda to manage the environment, ensuring all dependencies are consistent and reproducible.

### Step 1: Create the Conda Environment

The environment is defined in environment.yml. Run the following command to create it:

```bash
conda env create -f environment.yml
```

This will install the required dependencies, including Pygame and ipykernel for Jupyter notebook compatibility.

### Step 2: Activate the Environment

Activate the newly created environment with:

```bash
conda activate alien_invasion
```

### Register the Jupyter Kernel

To set this environment as the default Jupyter kernel for notebooks in this project, register it as a kernel:

```bash
python -m ipykernel install --user --name=alien_invasion --display-name "Alien Invasion Env"
```

### Step 4: Configure Default Kernel for VS Code (Optional)

If you’re using Visual Studio Code, you can set this environment as the default kernel for all notebooks by adding a .vscode/settings.json file in the project folder:

```json
{
    "jupyter.notebook.defaultKernel": "alien_invasion",
    "jupyter.jupyterServer.kernelSpec": {
        "display_name": "Alien Invasion Env",
        "name": "alien_invasion"
    }
}
```

## Usage

This command launches the game window. Use the following controls to play:

    Arrow Keys: Move the spaceship left or right.
    Spacebar: Fire bullets at incoming aliens.

### Running Notebooks

For any .ipynb notebooks in this repository, make sure they use the Alien Invasion Env kernel. This kernel should be the default in VS Code, but you can select it manually if needed.

## Project Structure

Here’s an overview of the project files:

- alien_invasion.py: Main script to run the game.
- settings.py: Contains configuration settings for game elements.
- game_functions.py: Handles game mechanics, such as player movement, shooting, and alien movement.
- README.md: Documentation for the project.
- environment.yml: Defines the Conda environment setup for the project.
- .vscode/settings.json: Optional settings file to set default Jupyter kernel in VS Code.

## Contributing

Contributions are welcome! Here’s how to get started:

    Fork the repository.
    Create a new branch with your feature or bug fix.
    Make your changes and commit them with clear commit messages.
    Push to your branch and submit a pull request.

Please ensure your code follows the style of the existing codebase and is well-documented.

## License

This project is open-source and available under the MIT License. See the [LICENSE.txt](https://github.com/christopheragonzales/alien_invasion/blob/main/license.txt) file for more details.
