# Adres Project 

This project was meant to be used as a technical interview. Uses technologies as Python and Selenium for UI tests and Locust for load testing. 

Please follow the steps to configure the environment to be albe to run this project locally. 

## Installation

This project can run in WIN, LINUX and MAC OS.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the used packages.

Intall Python using 

```bash
pip install python
```

As a recomendation is a good idea to use a virtual environment to avoid having issues with you previous libraries versions installed. 
To configure the virtual env please use: 

## For Windows 
```bash
venv\Scripts\activate
```

## For Mac - install and activate
```bash
python3 -m venv venv
source venv/bin/activate
```
## Install Selenium 
```bash
pip install selenium
```

## PyTests
For this project I'm using Pytests which is one of the most popular libraries to performa and validate tests executions. 
```bash
pip install pytest
```


## WebDrivers
Instead of using downloaded WebDrivers, lets use the default tool that allow us to hadle each webDriver in a cleanest way. 

```bash
pip install webdriver-manager
```


## Example of using WebDirver Manager

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Automatically install and use ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install())
```
## Project Structure
This project has the next scafolding or structure.
```
adres_project/
│── src/                   # Main application code
│   ├── __init__.py        # Marks the folder as a Python
│   ├── pages              # All the Pages according to POM
│── tests/                 # Test cases
│   ├── __init__.py
│   ├── auth_tests.py
│
│── venv/                  # Virtual environment (optional)
│
│── .gitignore             # Ignore unnecessary files in Git
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
│── setup.py               # Setup script for packaging
│── config.yaml            # Configuration file (optional)
│── conftest.py            # Contains the fixtures and web driver config
```


## How to run the tests
Please locate on the folder adres_project and run the command: 

```bash
pytest tests/
```