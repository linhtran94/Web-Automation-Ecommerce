# Part 1 - Question 2 
> The Web Automation project is built for automating E-commerce websites, that will run results in websites and sort output to CSV file


## Table of Contents
1. [Technical Stack](#technical-stack)
2. [Project Structure](#project-structure)
3. [How to set it up](#how-to-set-it-up)
    1. [Prerequisites](#prerequisites)
    2. [Installation](#installation)
    3. [Running the tests](#running-the-tests)
    4. [Authors](#authors)
    
## Technical Stack
- Python (3)
- Selenium WebDriver
- Pytest

## Project Structure
- Page Object Model

        TestSuites
            --> Test Cases 
                --> Page Objects

        |-- libs (Including library used in the project)
        |-- logs (Logs file)
        |-- utilities (Including common/utilities function used in the project)
        |-- pages (Including base class and page folder)
        |   |   |-- __init__.py
                    |-- base_page.py
        |   |   |--  BasePage.py
        |   |-- pages SortResultPage
        |       |-- __init__.py
        |       |-- SortShopeePage.py
        |       |-- SortTikiPage.py
        |-- tests (Including test case and test folder)
        |   |   |-- __init__.py
        |   |   |-- base_test.py
        |   |   |-- testdemo.py   
        |   |-- tests SortResultTest
        |       |-- __init__.py
        |       |-- SortProduct.py
        |       |-- Test_SortResult.py
        |       |-- TikiReport.csv
        |       |-- TotalReport.csv

## How to set it up
#### Prerequisites    
1. Download the source
2. Use/ Install/ Create ***venv*** (Virtual Environments) (default on Python >3)

#### Installation
- Open terminal, run command 

        pip3 install --upgrade pip -r requirements.txt
        
#### Running the tests
- Run test cases, run command. Run all test cases in project
   
            pytest

### Authors
- Linh Tran: [lynhtran0912@gmail.com](mailto:lynhtran0912@gmail.com)