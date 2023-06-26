# Telegrammer Project

## Start Project:
### Project Virtual Environment
You need a virtual environment for it. If you are using conda, run bellow command:
```shell
conda create -n telegrammer python=3.10
conda env list # To check if it is installed correctly
conda activate telegrammer
```
Use it also as the environment for you Pycharm
1. Go to `settings` -> `Project: <project_name>` -> `Python Interpretter`
2. Add a new local conda environment. Conda Executable is at `/home/mahdi/anaconda3/bin/conda`. choose your new environment (telegrammer)

Install you the project's requirements:
```shell
pip install -r requirements.txt
```

### Pycharm Use Tabs
Make sure your Pycharm uses tabs for indention:
`settings` -> `Editor` -> `Code Style` -> `Python` -> `Tabs and Indents` -> Set `Use tab character`