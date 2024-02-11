# Household Budget Management

## Description

This is an application designed for managing a household budget. It provides functionalities for adding expenses and income, deleting entries, and displaying statistics. The application is built using Python 3.8+ and SQLite3.

The application uses the argparse module for parsing command-line arguments. This allows the user to interact with the application easily using various commands. The arguments are defined in the Parser class and are used to determine what action should be performed when the script is run. Each action requires different arguments, which are also defined in the Parser class.

## Requirements

- Python 3.8 or newer
- SQLite3

## Installation

1. Clone the repository to your local machine using `git clone`.
2. Install the required dependencies using `pip install -r requirements.txt`.

## Usage

Execute the main script using `python main.py`. You can utilize various command-line arguments such as:

- `--add-expense`: Add an expense. This requires additional arguments: `--name`, `--category`, `--date`, `--value`.
- `--add-income`: Add income. This requires additional arguments: `--name`, `--category`, `--date`, `--value`.
- `--delete`: Delete an entry. This requires an additional argument: `--id`.
- `--stats`: Display statistics.
- `--list`: Display entries.

## License

This project is licensed under the terms of the MIT License.
