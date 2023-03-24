import click
import os
import git
import isort
import black
#This code sets up a command-line interface with a clean command that takes an optional
#  path argument to specify the path of the repository to clean. The default path
#  is the current directory.


@click.command()
@click.option('--path', default='.', help='Path of the repository to clean')




def clean(path):
    click.echo(f'Cleaning repository at path: {path}')

    repo = git.Repo(path)
    for file_path in repo.git.ls_files().split('\n'):
        file_path = os.path.join(path, file_path)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                code = f.read()
            code = isort.code(code)
            code = black.format_file_contents(
                code,
                fast=True,
                mode=black.FileMode(line_length=88)
            )
            with open(file_path, 'w') as f:
                f.write(code)
