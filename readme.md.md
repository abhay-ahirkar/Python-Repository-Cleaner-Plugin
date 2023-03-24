# Python Repository Cleaner Plugin

The Python Repository Cleaner Plugin is a command-line tool that helps keep your Python repositories clean and organized. It removes commented-out code, unused imports, and trailing whitespace from all files in a repository.

## Installation

1.  Clone the repository containing the `cleaner.py` file.
    
2.  Install the required Python packages using `pip`. Open a terminal or command prompt and run the following command:
    
    arduinoCopy code
    
    `pip install click isort black gitpython` 
    
3.  Navigate to the directory containing the `cleaner.py` file.
    

## Usage

To use the plugin, run the `clean` command with the desired options. Here are some examples:

-   To clean the repository in the current directory:
    
    Copy code
    
    `python cleaner.py clean` 
    
-   To clean a repository in a specific directory:
    
    cssCopy code
    
    `python cleaner.py clean --path /path/to/repository` 
    
-   To see help information about the command:
    
    bashCopy code
    
    `python cleaner.py clean --help` 
    

The plugin will remove commented-out code, unused imports, and trailing whitespace from all files in the specified repository.

## Contributing

We welcome contributions to this project! If you have any bug reports, feature requests, or pull requests, please submit them to our [GitHub repository](https://github.com/your-repository-url).

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
